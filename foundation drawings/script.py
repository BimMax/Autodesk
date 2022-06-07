#Change sheets number
# -*- coding: UTF-8 -*-
import os, sys
import Autodesk
import re
from Autodesk.Revit.DB import *
import sys
from System.Collections.Generic import List
import Autodesk.Revit.DB.Transaction
import clr
clr.AddReference("RevitAPI")
clr.AddReference("ProtoGeometry")
pg = clr.AddReference("ProtoGeometry")
# Import ToProtoType, ToRevitType geometry conversion extension methods
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

from dimension import found_dim
doc =  DocumentManager.Instance.CurrentDBDocument

#print(dir(Revit.GeometryConversion.GeometryObjectConverter.Convert))
import math
UNIT_CONVERT = 304.8005
uidoc = __revit__.ActiveUIDocument
curview = uidoc.ActiveGraphicalView
__doc__ = 'hole'
__author__ = 'Herashchanka Max'

from Autodesk.Revit.Creation import *

from form import *

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

__doc__ = 'Renumber sheets in selected part'
__author__ = 'Herashchanka Max'


#style = Autodesk.Revit.UI.Selection.PickBoxStyle.Directional
#style = 'Directional'
#object_type = Autodesk.Revit.UI.Selection.ObjectType.Element
#element = uidoc.Selection.PickObject(object_type)


#select activ, view
active_view = __revit__.ActiveUIDocument.Document.ActiveView

#select all object in category
all_foundation =list(FilteredElementCollector(doc). \
    OfCategory(BuiltInCategory.OST_StructuralFoundation). \
    WhereElementIsNotElementType().ToElements())

all_view_type = list(FilteredElementCollector(doc). \
    OfClass(ViewFamilyType). \
    ToElements())

all_title_blocks = FilteredElementCollector(doc). \
    OfCategory(BuiltInCategory.OST_TitleBlocks). \
    WhereElementIsElementType().ToElements()

all_templates = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Views)
all_schedules_type = list(FilteredElementCollector(doc). \
    OfClass(ViewSchedule). \
    ToElements())

#print((list(all_schedules_type)[0].GetFilters()))
all_schedules = list(FilteredElementCollector(doc). \
    OfCategory(BuiltInCategory.OST_Schedules).\
    GetEnumerator())

tempDict = {}
for tp in all_templates:
    if tp.IsTemplate and "КЖ" in tp.Name:
        tempDict[tp.Name] = tp.Id

view_type_dict = {}
for view in all_view_type:
    aa = view.get_Parameter(BuiltInParameter.SYMBOL_FAMILY_AND_TYPE_NAMES_PARAM).AsString()
    if 'Разрез' in aa or 'Section' in aa:
        view_type_dict[aa] = view.Id

#a = view_type_dict['Разрез']#.GetSimilarTypes()[0]

#print(a)
#print(dir(a))
family_section = {}
schedule_parameters = []

for parameter in list(all_schedules[0].Parameters.GetEnumerator()):
    schedule_parameters.append(parameter.Definition.Name)
sheet_params = []

all_sheets = FilteredElementCollector(doc). \
    OfCategory(BuiltInCategory.OST_Sheets).ToElements()

for parameter in list(all_sheets[0].Parameters.GetEnumerator()):
    sheet_params.append(parameter.Definition.Name)

title_dict = {}
title_blocks_name = []

for title in all_title_blocks:
    for param in list(title.Parameters.GetEnumerator()):
        #print((title.FamilyName))
        if param.Definition.Name.ToString() =='Имя типа':
            title_string = title.FamilyName + " " + param.AsString()
            title_dict[title_string] = [title.FamilyName, param.AsString(), title.Id, title]
            title_blocks_name.append(title_string)


def create_next_note(view, textbox):
    textNoteOptions = TextNoteOptions()
    defaultTypeId = doc.GetDefaultElementTypeId(ElementTypeGroup.TextNoteType)
    opts = TextNoteOptions(defaultTypeId)
    width = 190 / UNIT_CONVERT
    y = 60 + 6 * len(list(textbox.split('\n')))
    text = TextNote.Create(doc, view.Id, XYZ(-width, y / UNIT_CONVERT, 0), width, textbox, opts)
    return text
# select schedules example
for schedule in all_schedules:
    if schedule.Name == '___Ведомость материалов':
        material_schedule_example = schedule
    elif schedule.Name == '___Спецификация арматуры':
        rebar_schedule_example = schedule
    elif schedule.Name == '___ВРС(арматура)':
        all_rebar_example = schedule
    elif schedule.Name == '___Ведомость деталей (арматура)':
        rebar_shape_example = schedule
    elif schedule.Name == '___Спецификация сборочных единиц':
        part_example = schedule

def get_all_view_crop(element):

    crop = {}
    aa = element.get_BoundingBox(active_view).ToProtoType()
    print(dir(aa))#.ToPolySurface()#.ToProtoType()
    faces = list(element.get_BoundingBox(active_view).ToProtoType().ToPolySurface().Faces)
    for face in faces:
        # print(face.SurfaceGeometry().NormalAtParameter())
        if abs(face.SurfaceGeometry().NormalAtParameter().X) == 1:
            YZ_face = face.SurfaceGeometry()
        elif abs(face.SurfaceGeometry().NormalAtParameter().Y) == 1:
            XZ_face = face.SurfaceGeometry()
        elif abs(face.SurfaceGeometry().NormalAtParameter().Z) == 1:
            XY_face = face.SurfaceGeometry()
    names = ['1YZ_face', '2XZ_face', '3XY_face', '4XY_face', '5XY_face']
    i = 0
    for face in [YZ_face, XZ_face, XY_face, XY_face, XY_face]:
        # print(i)
        curves = CurveLoop()
        edges = list(face.Edges)
        # print((face.PerimeterCurves()))
        for curve in face.PerimeterCurves():
            curves.Append(curve.ToRevitType())
        # zprint(dir(curves.Transform(Autodesk.Revit.DB.Transform)))
        crop[names[i]] = curves
        i += 1

    return crop


def create_views(element, cr):

    views = []
    new_box = elements[element][1]
    elem = elements[element][0]
    counter = 1
    for view in sorted(cr.keys()):
        p = elem.Location.Point
        transform = Transform.Identity
        if view == '1YZ_face':
            pp = XYZ(p.X, p.Y, -p.Y + (elements[element][1].Max.Z - elements[element][1].Min.Z) / 2)
            viewdir = p.BasisX  # .Normalize()
            # print(viewdir)
            up = p.BasisZ
            right = up.CrossProduct(viewdir)

        elif view == '2XZ_face':
            pp = XYZ(p.X, p.Y, -p.Y + (elements[element][1].Max.Z - elements[element][1].Min.Z) / 2)
            viewdir = p.BasisY  # .Normalize()
            up = p.BasisZ
            right = up.CrossProduct(viewdir)
        else:

            if counter == 1:
                Z = elements[element][1].Min.Z + 150 / UNIT_CONVERT
            elif counter == 2:
                Z = (elements[element][1].Max.Z - elements[element][1].Min.Z) / 2
            else:
                Z = (elements[element][1].Max.Z) - 150 / UNIT_CONVERT

            pp = XYZ(p.X, p.Y, Z)
            viewdir = -pp.BasisZ  # .Normalize()
            if viewdir.Z == 1:
                viewdir = -viewdir  # .ToVector().Reverse().ToRevitType()
                # print(dir(viewdir))
            up = pp.BasisY
            right = up.CrossProduct(viewdir)
            counter += 1
        # print(viewdir,up,right,pp,pp.Normalize())
        transform.Origin = pp
        # print(viewdir)
        sectionBox = BoundingBoxXYZ()
        transform.BasisX = right
        transform.BasisY = up
        transform.BasisZ = viewdir
        sectionBox.Transform = transform
        sectionBox.Min = XYZ(0, 1, new_box.Min.Z)
        if view == '5XY_face':
            sectionBox.Max = XYZ(1, 2, new_box.Max.Z)
        else:
            sectionBox.Max = XYZ(1, 2, 1.64)

        vs = ViewSection.CreateSection(doc, viewTypeId, sectionBox)  # family_section.keys()[10]

        try:
            vs.ViewTemplateId = tempDict[templates[sorted(cr.keys()).index(view)]]
        except:
            pass
        if view == '5XY_face':
            vs.Name = 'Фундамент монолитный ' + element
        else:
            pass
        vcrShapeMgr = vs.GetCropRegionShapeManager()
        vcrShapeMgr.SetCropShape(cr[view])
        vs.CropBoxActive = True
        vs.CropBoxVisible = False
        views.append(vs)
        if view == '1YZ_face' or view == '2XZ_face':
            view_dim = found_dim(elem, vs, cr[view], view)
        else:
            view_dim = found_dim(elem, vs, cr[view], view)
            # pass
    return views


def create_sheet(title_block_id, element, sheet_params=None, prefix='Фундамент монолитный'):

    newsheet = ViewSheet.Create(doc, title_block_id)
    newsheet.Name = prefix + ' ' + element
    return newsheet


def add_views_to_sheet(sheet, views_list):
    x = [-500, -350, -350, -150, -500]
    y = [120, 120, 320, 150, 320]
    vp_id = ElementId(551910)
    vp_list = []
    for i, view in enumerate(views_list):
        point = XYZ(x[i] / UNIT_CONVERT, y[i] / UNIT_CONVERT, 0)
        vp = Viewport.Create(doc, sheet.Id, view.Id, point)
        # print(dir(vp))
        vp.ChangeTypeId(vp_id)
        # print((vp.GetValidTypes()[1]))
        vp_list.append(vp)
        # x+=150/UNIT_CONVERT

    return vp_list


def create_schedule(element_mark, example, schedule_sort):
    duplicate_option = ViewDuplicateOption.Duplicate
    schId = example.Duplicate(duplicate_option)
    sch = doc.GetElement(schId)

    filter = sch.Definition.GetFilter(2)
    filter.SetValue(element_mark)
    sch.Definition.SetFilter(2, filter)
    try:
        sch.LookupParameter(schedule_sort).Set(element_mark)
    except:
        pass
    if example.Name == '___Ведомость материалов':
        sch.Name = 'КЖ.{name}.Ведомость материалов'.format(name=element_mark)
    elif example.Name == '___Спецификация арматуры':
        sch.Name = 'КЖ.{name}.Спецификация арматуры'.format(name=element_mark)
    elif example.Name == '___Спецификация сборочных единиц':
        sch.Name = 'КЖ.{name}.___Спецификация сборочных единиц'.format(name=element_mark)
    return sch
tempDict = {}
for tp in all_templates:
    if tp.IsTemplate and "КЖ" in tp.Name:
        tempDict[tp.Name] = tp.Id


userform = MainForm(tempDict.keys(),schedule_parameters,sheet_params, title_blocks_name, view_type_dict.keys())
#userform.InitializeComponent(userform, all_templates)
Application.Run(userform)
Application.EnableVisualStyles()

if userform.start==1:
    templates = userform.temp_dict

    schedule_group_parameter = userform.schedule_group_parameter
    sheet_parameters_dict = userform.sheet_parameters_dict
    start_sheet_number = userform.SheetNumber
    textbox = userform.TextNote
    viewTypeId = view_type_dict[userform.view_type]
    titleblokId = title_dict[userform.title_block][2]



    elements = {}
    for foundation in all_foundation:
        if 'ундамент монолитный' in foundation.Symbol.LookupParameter("О_Наименование").AsString():
            elements[foundation.LookupParameter("Марка").AsString()] = [foundation,foundation.get_BoundingBox(active_view)]



    t = Transaction(doc, "Create foundation sheets")
    t.Start()

    popravka = 2.1/ UNIT_CONVERT
    #schedule_group_parameter = 'Орг.КомплектЧертежей'

    for el in sorted(elements.keys(), key = lambda x: int(re.compile('\d+').findall(x)[0])):
        element = elements[el][0]
        sheet_title_block = all_title_blocks[5]
        #print(element)
        crop_view = get_all_view_crop(element)
        views = create_views(el, crop_view)
        sheet = create_sheet(titleblokId, el)
        notes = create_next_note(sheet, textbox)
        try:
            for key in sheet_parameters_dict.keys():
                sheet.LookupParameter(key).Set(sheet_parameters_dict[key])
        except:
            pass
        try:
            if el == sorted(elements.keys())[0]:
                sheet.SheetNumber = start_sheet_number
        except:
            pass
        add = add_views_to_sheet(sheet, views)
        schedule_point = XYZ(-190/UNIT_CONVERT,400/UNIT_CONVERT,0)
        counter = 1
        for schedule in [part_example, rebar_schedule_example, material_schedule_example,all_rebar_example,rebar_shape_example]:
            schedule_instance = create_schedule(el, schedule,schedule_group_parameter)
            sheet_schedule = ScheduleSheetInstance.Create(doc, sheet.Id, schedule_instance.Id, schedule_point)
            #aa = schedule_instance.ViewCropRegionShapeManager().GetCropShape()
            delta = abs(sheet_schedule.get_BoundingBox(sheet).Max.Y-sheet_schedule.get_BoundingBox(sheet).Min.Y)
            y = schedule_point.Y + counter*popravka - delta
            schedule_point = XYZ(-190 / UNIT_CONVERT, y, 0)
            counter +=1
    t.Commit()
