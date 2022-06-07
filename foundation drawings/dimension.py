
#Change sheets number
# -*- coding: UTF-8 -*-
import os, sys
import Autodesk
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
from Autodesk.Revit.DB.HostObjectUtils import *
from Autodesk.Revit.DB.ExtensibleStorage import *
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc =  DocumentManager.Instance.CurrentDBDocument
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
from Autodesk.Revit.UI import Selection
doc =  __revit__.ActiveUIDocument.Document #DocumentManager.Instance.CurrentDBDocument
app =  doc.Application
options = app.Create.NewGeometryOptions()
options.ComputeReferences = True

#options.DetailLevel = ViewDetailLevel.Fine

#print(dir(Revit.GeometryConversion.GeometryObjectConverter.Convert))
import math
UNIT_CONVERT = 304.8005
uidoc = __revit__.ActiveUIDocument
curview = uidoc.ActiveGraphicalView
av = uidoc.ActiveView
__doc__ = 'hole'
__author__ = 'Herashchanka Max'

#lineid = uidoc.Selection.PickObjects(Selection.ObjectType.Element)[0].ElementId
#line = doc.GetElement(lineid).Location.Curve
#print(line)
#print(dir(line))
#RightDirection
from Autodesk.Revit.Creation import *

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument


all_foundation =list(FilteredElementCollector(doc). \
    OfCategory(BuiltInCategory.OST_StructuralFoundation). \
    WhereElementIsNotElementType().ToElements())

#print(dir(av))
avr = av.RightDirection
avd = av.ViewDirection


#print(dir(all_foundation[0].Location))
face_dict = {}


points = []


def get_face_for_4XY(view_name, vert, vert_other):

    a = vert.Item[2]
    a1 = vert.Item[3]
    vert.Clear()
    vert.Append(a)
    vert.Append(a1)

    a = vert_other.Item[2]
    a1 = vert_other.Item[3]
    vert_other.Clear()
    vert_other.Append(a)
    vert_other.Append(a1)

    return vert, vert_other


def get_faces_for_dim(element, type, view_name, view):

    vert = ReferenceArray()
    vert_other = ReferenceArray()
    hor = ReferenceArray()
    vert_list = []
    hor_list = []
    counter = -1
    options.IncludeNonVisibleObjects = False
    #options.View = view

    faces = list(list(element.get_Geometry(Options(options)).GetEnumerator())[0]. \
                 Faces.GetEnumerator())
    if len(faces) == 0:
        faces = list(list(element.get_Geometry(Options(options)).GetEnumerator())[2]. \
                     Faces.GetEnumerator())
    print(len(faces))
    for face in faces:
        if view_name=='2XZ_face' or view_name=='1YZ_face' :
            if face.FaceNormal.ToVector().IsParallel(avd.ToVector()):
                hor.Append(face.Reference)
                hor_list.append(face)

            if view_name=='2XZ_face':
                if face.FaceNormal.ToVector().IsParallel(avr.ToVector()):
                    vert.Append(face.Reference)
                    vert_list.append(face)
            elif view_name=='1YZ_face':
                if face.FaceNormal.ToVector().IsParallel(avd.CrossProduct(avr).ToVector()):
                    vert.Append(face.Reference)
                    vert_list.append(face)
        else:
            if face.FaceNormal.ToVector().IsParallel(avr.ToVector()):
                vert.Append(face.Reference)
                vert_list.append(face)
            elif face.FaceNormal.ToVector().IsParallel(avd.CrossProduct(avr).ToVector()):
                vert_other.Append(face.Reference)
    print('vert', vert, vert_other)
    if  type =='outer':

        if '3XY' in view_name or '5XY' in view_name:

            a = vert.Item[0]
            a1 = vert.Item[1]
            vert.Clear()
            vert.Append(a)
            vert.Append(a1)


            a = vert_other.Item[0]
            a1 = vert_other.Item[1]
            vert_other.Clear()
            vert_other.Append(a)
            vert_other.Append(a1)


        elif '4XY' in view_name:
            vert, vert_other = get_face_for_4XY('4XY', vert, vert_other)


        elif view_name == '2XZ_face' or view_name == '1YZ_face':

            a = vert.Item[0]
            a1 = vert.Item[1]
            vert.Clear()
            vert.Append(a)
            vert.Append(a1)
            a = hor.Item[1]
            a1 = hor.Item[len(list(hor))-1]
            hor.Clear()
            hor.Append(a)
            hor.Append(a1)

       # print(len(list(vert)))
    elif type =='inner':
        if '4XY' in view_name:
            vert, vert_other = get_face_for_4XY('4XY', vert, vert_other)

    return hor,vert, hor_list,vert_list, vert_other
def found_dim(element, av, crop, view_name):
    '''
    Hfpvths lk zdthnbrfkmys[ hfphtpjd
    Cjplftncz wtgjxrf hfpvthjd lkz rf;ljq jgjhyjq kbybb bp reference lines.
    Uhfyb gj rjnjhsv cnfdbncz hfpvth jghtltkz.ncz dyenhb wbrkf lkz rf;ljq jgjhyjq kbybb
    '''
    reference_lines = list(crop.GetEnumerator())
    reversing = -1 if view_name == '1YZ_face' else 1
    #list(list(av.GetCropRegionShapeManager().GetCropShape().ToArray())[0].GetEnumerator())
    reference_lines.remove(reference_lines[2])
    reference_lines.remove(reference_lines[1])
    reference_lines+= reference_lines
    avr = av.RightDirection
    avd = av.ViewDirection
    i= 0
    hor, vert, hor_list, vert_list,vert_other = get_faces_for_dim(element, 'outer', view_name, av)
    
    #print(len(list(vert)))
    hor_inner, vert_inner, hor_list_inner, vert_list_inner,vert_other_inner = get_faces_for_dim(element, 'inner', view_name,av)
    while i < 4:

        if view_name == '2XZ_face' or view_name == '1YZ_face':
            if i > 1:  # Dytiyzz uf,fhbnyfz wtgjxrf hfpvthjd
                if i == 2:
                    line = reference_lines[0].CreateOffset(24 * 20 / UNIT_CONVERT, avd * reversing)
                elif i == 3:
                    line = reference_lines[1].CreateOffset(24 * 20 / UNIT_CONVERT, avd * reversing)

                # print(len(vert_list))
                # pass
            else:  # dyenhtyyzz wtgjxrf hfpvthjd
                if i == 0:
                    line = reference_lines[0].CreateOffset(16 * 20 / UNIT_CONVERT, avd * reversing)
                elif i == 1:
                    line = reference_lines[1].CreateOffset(16 * 20 / UNIT_CONVERT, avd * reversing)
                # print(element)
            if   i ==1 or i ==3 :
                if i==1:
                    dimen = doc.Create.NewDimension(av, line, hor_inner)
                #pass
                else:
                    dimen = doc.Create.NewDimension(av, line, hor)

            elif i==0 or i ==2:
                if i==0:
                    dimen = doc.Create.NewDimension(av, line, vert_inner)
                   # print(len(list(vert_inner)))
                else:
                    dimen = doc.Create.NewDimension(av, line, vert)
                #dimen = doc.Create.NewDimension(doc.ActiveView, line, vert)
        elif view_name == '4XY_face':
            if i == 0:
                line = reference_lines[0]#.CreateOffset(16 * 20 / UNIT_CONVERT, avd)
            elif i == 1:
                line = reference_lines[1]#.CreateOffset(16 * 20 / UNIT_CONVERT, avd)

                # print(len(vert_list))
                # pass

            if i == 0:
                dimen = doc.Create.NewDimension(av, line, vert_inner)
                line = reference_lines[0].CreateOffset(8 * 20 / UNIT_CONVERT, avd)
                dimen = doc.Create.NewDimension(av, line, vert)
            elif i == 1:
                dimen = doc.Create.NewDimension(av, line, vert_other_inner)
                line = reference_lines[1].CreateOffset(8 * 20 / UNIT_CONVERT, avd)
                dimen = doc.Create.NewDimension(av, line, vert_other)
        else:

            if i == 0:
                line = reference_lines[0].CreateOffset(16 * 20 / UNIT_CONVERT, avd )
            elif i == 1:
                line = reference_lines[1].CreateOffset(16 * 20 / UNIT_CONVERT, avd )

            # print(len(vert_list))
            # pass

            if i == 0:
                dimen = doc.Create.NewDimension(av, line, vert_inner)
                line = reference_lines[0].CreateOffset(24 * 20 / UNIT_CONVERT, avd )
                dimen = doc.Create.NewDimension(av, line, vert)
            elif i==1:
                dimen = doc.Create.NewDimension(av, line, vert_other_inner)
                line = reference_lines[1].CreateOffset(24 * 20 / UNIT_CONVERT, avd )
                dimen = doc.Create.NewDimension(av, line, vert_other)
        i+=1
        #print(len(hor_list))
        '''for face in hor_list[1:]:
            print(face.Area)
            #print(11111)
            #print(dir(hor[hor_list.index(face)]))
            origin  = face.Origin
            aa = face.Origin
            print(aa)
            print(dir(aa))
            bend = XYZ(0,0,0)
            end = XYZ(0,0,0)
            #print(dir(origin))
            doc.Create.NewSpotElevation(av, face.Reference, origin, bend, end, origin, True)'''
    return dimen

'''t = Transaction(doc, "test dimesion")
t.Start()



dimension = found_dim(all_foundation[0], av)

t.Commit()
'''