#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import clr
from Autodesk.Revit.DB import *
clr.AddReference("RevitServices")

import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager


clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')


import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

clr.AddReference("RevitAPI")

pg = clr.AddReference("ProtoGeometry")

from Autodesk.DesignScript.Geometry import *

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document




def mysort(l):
    # for e in l:
    ss = ""
    for ee in l:
        if ee.isdigit():
            ss = ss + ee
    return int(ss)


def mysortA(l):
    ss = ""
    for ee in l:
        if ee.isdigit() == False and ee != "'" and ee != "\"":
            ss = ss + ee
    return ss


def boundB(elements, view):
    minXList = []
    minYList = []
    minZList = []
    maxXList = []
    maxYList = []
    maxZList = []

    for x in elements:
        maxXList.append(x.get_BoundingBox(view).Max.X)
        maxYList.append(x.get_BoundingBox(view).Max.Y)
        maxZList.append(x.get_BoundingBox(view).Max.Z)
        minXList.append(x.get_BoundingBox(view).Min.X)
        minYList.append(x.get_BoundingBox(view).Min.Y)
        minZList.append(x.get_BoundingBox(view).Min.Z)
        bb = BoundingBoxXYZ()
        bb.Min = XYZ(min(minXList), min(minYList), min(minZList))
        bb.Max = XYZ(max(maxXList), max(maxYList), max(maxZList))
    return bb


filterDict = {}
tempDict = {}

filters = FilteredElementCollector(doc).OfClass(ParameterFilterElement).ToElements()
templates = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Views)

###### Выбор существующих шаблонов и добавление в словарь

for tp in templates:
    if tp.IsTemplate and "Вентиляция_Схема" in tp.Name:
        tempDict[tp.Name] = tp.Id

ducts = FilteredElementCollector(doc).OfCategory(
    BuiltInCategory.OST_DuctCurves).WhereElementIsNotElementType().ToElements()
Name = []

##### Выбор типоразмеров листов которые есть
title_blocks = FilteredElementCollector(doc).OfCategory(
    BuiltInCategory.OST_TitleBlocks).WhereElementIsElementType().ToElements()
for tt in title_blocks:

    if tt.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString() == "A2A" or tt.get_Parameter(
            BuiltInParameter.SYMBOL_NAME_PARAM).AsString() == "А2А":
        tb = tt
l1 = []

all_sheets = FilteredElementCollector(doc). \
    OfCategory(BuiltInCategory.OST_Sheets).ToElements()
sheet_params = []
for a in list(all_sheets[0].Parameters.GetEnumerator()):
    sheet_params.append(a.Definition.Name)

ductDict = {}
for d in ducts:
    # dName.append(d.get_Parameter(BuiltInParameter.RBS_SYSTEM_NAME_PARAM).AsString())
    a = d.get_Parameter(BuiltInParameter.RBS_SYSTEM_NAME_PARAM).AsString()

    db = d.get_BoundingBox(doc.ActiveView)
    if a not in l1 and a.startswith("В") or a not in l1 and a.startswith("П"):
        l1.append(a)
        tl = [d]
        ductDict[a] = tl
    elif a in ductDict.keys():
        # print(ductDict[a])
        ductDict[a].append(d)

    #  ductDict[a] = sa

l12 = sorted(l1, key=mysort)
l2 = sorted(l12, key=mysortA)

av = doc.ActiveView
v = ViewDuplicateOption.Duplicate



#print('l2',l1)

import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *


class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()

    def InitializeComponent(self):
        self._dataGridView1 = System.Windows.Forms.DataGridView()
        self._SheetNumber = System.Windows.Forms.DataGridViewTextBoxColumn()
        self._SheetName = System.Windows.Forms.DataGridViewTextBoxColumn()
        self._SystemName = System.Windows.Forms.DataGridViewComboBoxColumn()
        self._Template = System.Windows.Forms.DataGridViewComboBoxColumn()
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._accept_button = System.Windows.Forms.Button()
        self._Cancel_button = System.Windows.Forms.Button()
        self._groupParameter1 = System.Windows.Forms.GroupBox()
        self._par1ComboBox = System.Windows.Forms.ComboBox()
        self._par1Value = System.Windows.Forms.TextBox()
        self._groupParameter2 = System.Windows.Forms.GroupBox()
        self._par1Value2 = System.Windows.Forms.TextBox()
        self._par2ComboBox = System.Windows.Forms.ComboBox()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._par4Value = System.Windows.Forms.TextBox()
        self._par4ComboBox = System.Windows.Forms.ComboBox()
        self._groupBox3 = System.Windows.Forms.GroupBox()
        self._par3Value = System.Windows.Forms.TextBox()
        self._par3ComboBox = System.Windows.Forms.ComboBox()
        self._dataGridView1.BeginInit()
        self._groupBox1.SuspendLayout()
        self._groupParameter1.SuspendLayout()
        self._groupParameter2.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self._groupBox3.SuspendLayout()
        self.SuspendLayout()
        #
        # dataGridView1
        #
        self._dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        self._dataGridView1.Columns.AddRange(System.Array[System.Windows.Forms.DataGridViewColumn](
            [self._SheetNumber,
             self._SheetName,
             self._SystemName,
             self._Template]))
        self._dataGridView1.Location = System.Drawing.Point(9, 21)
        self._dataGridView1.Name = "dataGridView1"
        self._dataGridView1.RowTemplate.Height = 24
        self._dataGridView1.Size = System.Drawing.Size(693, 206)
        self._dataGridView1.TabIndex = 0
        #
        # SheetNumber
        #
        self._SheetNumber.HeaderText = "SheetNumber"
        self._SheetNumber.Name = "SheetNumber"
        #
        # SheetName
        #
        self._SheetName.HeaderText = "SheetName"
        self._SheetName.Name = "SheetName"
        #
        # SystemName
        #
        self._SystemName.HeaderText = "SystemName"
        self._SystemName.Name = "SystemName"
        self._SystemName.Width = 150
        #
        # Template
        #
        self._Template.HeaderText = "Template"
        self._Template.Name = "Template"
        self._Template.Width = 300
        #
        # groupBox1
        #
        self._groupBox1.Controls.Add(self._dataGridView1)
        self._groupBox1.Location = System.Drawing.Point(12, 1)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(714, 247)
        self._groupBox1.TabIndex = 1
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Создать лісты"
        #
        # accept_button
        #
        self._accept_button.Location = System.Drawing.Point(528, 434)
        self._accept_button.Name = "accept_button"
        self._accept_button.Size = System.Drawing.Size(90, 30)
        self._accept_button.TabIndex = 2
        self._accept_button.Text = "OK"
        self._accept_button.UseVisualStyleBackColor = True
        self._accept_button.Click += self.Accept_buttonClick
       #self._accept_button.MouseClick += self.Accept_buttonClick
        #
        # Cancel_button
        #
        self._Cancel_button.Location = System.Drawing.Point(624, 434 )
        self._Cancel_button.Name = "Cancel_button"
        self._Cancel_button.Size = System.Drawing.Size(90, 30)
        self._Cancel_button.TabIndex = 3
        self._Cancel_button.Text = "Cancel"
        self._Cancel_button.UseVisualStyleBackColor = True
        self._Cancel_button.Click += self.Cancel_buttonClick
        #self._Cancel_button.MouseClick += self.Cancel_buttonClick
        #
        # groupParameter1
        #
        self._groupParameter1.AccessibleDescription = ""
        self._groupParameter1.AccessibleName = ""
        self._groupParameter1.Controls.Add(self._par1Value)
        self._groupParameter1.Controls.Add(self._par1ComboBox)
        self._groupParameter1.Location = System.Drawing.Point(12, 270)
        self._groupParameter1.Name = "groupParameter1"
        self._groupParameter1.Size = System.Drawing.Size(341, 74)
        self._groupParameter1.TabIndex = 4
        self._groupParameter1.TabStop = False
        self._groupParameter1.Text = "Sheet parameter 1:"
        self._groupParameter1.Enter += self.GroupBox2Enter
        #
        # par1ComboBox
        #
        self._par1ComboBox.AccessibleDescription = ""
        self._par1ComboBox.AccessibleName = ""
        self._par1ComboBox.FormattingEnabled = True
        self._par1ComboBox.Location = System.Drawing.Point(6, 33)
        self._par1ComboBox.Name = "par1ComboBox"
        self._par1ComboBox.Size = System.Drawing.Size(160, 24)
        self._par1ComboBox.TabIndex = 0
        self._par1ComboBox.Text = "<Choose parameter>"
        #
        # par1Value
        #
        self._par1Value.Location = System.Drawing.Point(172, 35)
        self._par1Value.Name = "par1Value"
        self._par1Value.Size = System.Drawing.Size(163, 22)
        self._par1Value.TabIndex = 1
        self._par1Value.Text = "   <Set value>"
        #
        # groupParameter2
        #
        self._groupParameter2.AccessibleDescription = ""
        self._groupParameter2.AccessibleName = ""
        self._groupParameter2.Controls.Add(self._par1Value2)
        self._groupParameter2.Controls.Add(self._par2ComboBox)
        self._groupParameter2.Location = System.Drawing.Point(375, 270)
        self._groupParameter2.Name = "groupParameter2"
        self._groupParameter2.Size = System.Drawing.Size(340, 74)
        self._groupParameter2.TabIndex = 5
        self._groupParameter2.TabStop = False
        self._groupParameter2.Text = "Sheet parameter 2:"
        #
        # par1Value2
        #
        self._par1Value2.Location = System.Drawing.Point(172, 35)
        self._par1Value2.Name = "par1Value2"
        self._par1Value2.Size = System.Drawing.Size(162, 22)
        self._par1Value2.TabIndex = 1
        self._par1Value2.Text = "   <Set value>"
        #
        # par2ComboBox
        #
        self._par2ComboBox.AccessibleDescription = ""
        self._par2ComboBox.AccessibleName = ""
        self._par2ComboBox.FormattingEnabled = True
        self._par2ComboBox.Location = System.Drawing.Point(6, 33)
        self._par2ComboBox.Name = "par2ComboBox"
        self._par2ComboBox.Size = System.Drawing.Size(160, 24)
        self._par2ComboBox.TabIndex = 0
        self._par2ComboBox.Text = "<Choose parameter>"
        #
        # groupBox2
        #
        self._groupBox2.AccessibleDescription = ""
        self._groupBox2.AccessibleName = ""
        self._groupBox2.Controls.Add(self._par4Value)
        self._groupBox2.Controls.Add(self._par4ComboBox)
        self._groupBox2.Location = System.Drawing.Point(375, 354)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(340, 74)
        self._groupBox2.TabIndex = 7
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Sheet parameter 4:"
        #
        # par4Value
        #
        self._par4Value.Location = System.Drawing.Point(172, 35)
        self._par4Value.Name = "par4Value"
        self._par4Value.Size = System.Drawing.Size(162, 22)
        self._par4Value.TabIndex = 1
        self._par4Value.Text = "   <Set value>"
        #
        # par4ComboBox
        #
        self._par4ComboBox.AccessibleDescription = ""
        self._par4ComboBox.AccessibleName = ""
        self._par4ComboBox.FormattingEnabled = True
        self._par4ComboBox.Location = System.Drawing.Point(6, 33)
        self._par4ComboBox.Name = "par4ComboBox"
        self._par4ComboBox.Size = System.Drawing.Size(160, 24)
        self._par4ComboBox.TabIndex = 0
        self._par4ComboBox.Text = "<Choose parameter>"
        #
        # groupBox3
        #
        self._groupBox3.AccessibleDescription = ""
        self._groupBox3.AccessibleName = ""
        self._groupBox3.Controls.Add(self._par3Value)
        self._groupBox3.Controls.Add(self._par3ComboBox)
        self._groupBox3.Location = System.Drawing.Point(12, 354)
        self._groupBox3.Name = "groupBox3"
        self._groupBox3.Size = System.Drawing.Size(341, 74)
        self._groupBox3.TabIndex = 6
        self._groupBox3.TabStop = False
        self._groupBox3.Text = "Sheet parameter 3:"
        self._groupBox3.Enter += self.GroupBox3Enter
        #
        # par3Value
        #
        self._par3Value.Location = System.Drawing.Point(172, 35)
        self._par3Value.Name = "par3Value"
        self._par3Value.Size = System.Drawing.Size(163, 22)
        self._par3Value.TabIndex = 1
        self._par3Value.Text = "   <Set value>"
        #
        # par3ComboBox
        #
        self._par3ComboBox.AccessibleDescription = ""
        self._par3ComboBox.AccessibleName = ""
        self._par3ComboBox.FormattingEnabled = True
        self._par3ComboBox.Location = System.Drawing.Point(6, 33)
        self._par3ComboBox.Name = "par3ComboBox"
        self._par3ComboBox.Size = System.Drawing.Size(160, 24)
        self._par3ComboBox.TabIndex = 0
        self._par3ComboBox.Text = "<Choose parameter>"
        #
        # MainForm
        #
        self.ClientSize = System.Drawing.Size(727, 471)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupParameter2)
        self.Controls.Add(self._groupBox3)
        self.Controls.Add(self._groupParameter1)
        self.Controls.Add(self._Cancel_button)
        self.Controls.Add(self._accept_button)
        self.Controls.Add(self._groupBox1)
        self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle
        self.Name = "MainForm"
        self.Text = "Ов Системы"
        self.Load += self.MainFormLoad
        self._dataGridView1.EndInit()
        self._groupBox1.ResumeLayout(False)
        self._groupParameter1.ResumeLayout(False)
        self._groupParameter1.PerformLayout()
        self._groupParameter2.ResumeLayout(False)
        self._groupParameter2.PerformLayout()
        self._groupBox2.ResumeLayout(False)
        self._groupBox2.PerformLayout()
        self._groupBox3.ResumeLayout(False)
        self._groupBox3.PerformLayout()
        self.ResumeLayout(False)

        for sys in l2:
            self._SystemName.Items.Add(sys)
        for template in tempDict.keys():
            self._Template.Items.Add(template)

        for parameter in sheet_params:
            self._par1ComboBox.Items.Add(parameter)
            self._par2ComboBox.Items.Add(parameter)
            self._par3ComboBox.Items.Add(parameter)
            self._par4ComboBox.Items.Add(parameter)

    def MainFormLoad(self, sender, e):
        pass


    def Accept_buttonClick(self, sender, e):
        self.sheet_params_dict = {}
        self.sheet_params_dict[self._par1ComboBox.Text] = self._par1Value.Text
        self.sheet_params_dict[self._par2ComboBox.Text] = self._par1Value2.Text
        self.sheet_params_dict[self._par3ComboBox.Text] = self._par3Value.Text
        self.sheet_params_dict[self._par4ComboBox.Text] = self._par4Value.Text
        self.create_sheets = []
        for row in list(self._dataGridView1.Rows):
            self.create_sheets.append([row.Cells[0].Value,row.Cells[1].Value,row.Cells[2].Value,row.Cells[3].Value])
        self.Close()
    def Cancel_buttonClick(self, sender, e):
        self.create_sheets = []
        self.Close()
    def GroupBox2Enter(self, sender, e):
        pass

    def GroupBox3Enter(self, sender, e):
        pass




form = MainForm()
Application.Run(form)
Application.EnableVisualStyles()



if len(form.create_sheets)>0:
    t = Transaction(doc, "Create view")
    t.Start()

    for row in list(form.create_sheets)[:-1]:#-1 dropes empty row
        avdId = av.Duplicate(v)
        avd = doc.GetElement(avdId)
        newsheet = ViewSheet.Create(doc, tb.Id)
        if row[3]:
            avd.ViewTemplateId = tempDict[row[3]]

        else:
            try:
                tempName = "Вентиляция_Схема " + row[2]
                avd.ViewTemplateId = tempDict[tempName]
            except:
                print("Не найдено шаблона с именем '{0}'. Запустите программу повторно и выберите шаблон для вида".format(tempName))

        newsheet.Name = row[1]
        newsheet.SheetNumber = row[0]
        for param in form.sheet_params_dict.keys():
            try:
                newsheet.LookupParameter(param).Set(form.sheet_params_dict[param])
            except:
                pass
        vp1 = Viewport.Create(doc, newsheet.Id, avd.Id, XYZ(0, 1, 0))
    t.Commit()

"""
t = Transaction(doc, "Create view")
t.Start()
n = 1

for k in l2[:5]:
    avdId = av.Duplicate(v)
    avd = doc.GetElement(avdId)

    tempName = "Вентиляция_Схема " + k
    print(tempName)

    try:
        avd.ViewTemplateId = tempDict[tempName]

        name = "Система" + " " + k
        avd.Name = name

        # avd.CropBox  = boundB(ductDict[k], av)
        avd.SetSectionBox(boundB(ductDict[k], avd))
        ######Создание листа и размещение вида на нем
        newsheet = ViewSheet.Create(doc, tb.Id)
        newsheet.Name = name
        newsheet.SheetNumber = "OV" + str(n)
        n += 1
        vp1 = Viewport.Create(doc, newsheet.Id, avd.Id, XYZ(1, 1, 0))
    except:
        pass
t.Commit()


###### Выбор существующих фильтров и добавление в словарь

for f in filters:
    if "ОВ_Системы" in f.Name :

        ss = f.Name[11:]

        ss2 = ""
        if "("in ss and ")" in ss:
            ss = ss.replace( "(" , "")
            ss = ss.replace( ")" ,  "")
            ss = ss.replace(" ", "")
        l1 = [ss]
        l1.append(f)
        filterDict[ss]=l1
    elif  "ОВ_Другие дисциплины" in f.Name or "ОВ_Оборудование_Приток" in f.Name or "ОВ_Оборудование_Не определено" in f.Name or "ОВ_Оборудование_Соединительная муфта" in f.Name or "ОВ_Оборудование_Вытяжка" in f.Name:
        l = [f.Name]
        l.append(f)
        filterDict[f.Name] = l





####### Выборка возуховодов в моедли и получение параметра имя ситемы


#######Копирование видов дл якаждой марки на основе активного вида и применение фильтров




    for ff in filterDict.values():
        f = ff
        if k.startswith("В"):#Для вытяжных устновок, чьи иимена ситсем начинаются , В
            if  f[0].startswith("В") and "Вытяжка" not in f[0]  and "Воздухозабор" not in f[0] and "ВЕ2-6" not in f[0]:
                avd.AddFilter(f[1].Id)
                avd.SetFilterVisibility(f[1].Id, False) if f[0] != k else avd.SetFilterVisibility(f[1].Id, True)
            elif "Приток"  in f[0] and "Воздухозабор" not in f[0]:
                avd.AddFilter(f[1].Id)
                avd.SetFilterVisibility(f[1].Id, False)
            elif f[0] == "ОВ_Другие дисциплины" or f[0] == "Вытяжка_Не сортировано" or "Оборудование" in f[0]:
                avd.AddFilter(f[1].Id)
                if "Вытяжка" in f[0] and "Оборудование" in f[0]:
                    avd.SetFilterVisibility(f[1].Id, True)
                else:
                    avd.SetFilterVisibility(f[1].Id, False)

        elif k.startswith("П"):#Для вытяжных устновок, чьи иимена ситсем начинаются , В
            if  f[0].startswith("П") and "Приток" not in f[0]  and "Воздухозабор" not in f[0] and "ВЕ2-6" not in f[0]:
                avd.AddFilter(f[1].Id)
                avd.SetFilterVisibility(f[1].Id, False) if f[0] != k else avd.SetFilterVisibility(f[1].Id, True)
            elif "Вытяжка"  in f[0] and "Воздухозабор" not in f[0]:
                avd.AddFilter(f[1].Id)
                avd.SetFilterVisibility(f[1].Id, False) if f[0] != k else avd.SetFilterVisibility(f[1].Id, True)
            elif f[0] == "ОВ_Другие дисциплины" or f[0] == "Приток_Не сортировано" or "Оборудование" in f[0]:
                avd.AddFilter(f[1].Id)
                if "Приток" in f[0]:
                    avd.SetFilterVisibility(f[1].Id, True)
                else:
                    avd.SetFilterVisibility(f[1].Id, False)







t.Commit()
"""
