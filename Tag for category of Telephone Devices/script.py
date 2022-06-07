#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

from Autodesk.Revit.DB import *
import sys
from System.Collections.Generic import List
import Autodesk.Revit.DB.Transaction
import clr


uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

# Select telephone devices
te = Autodesk.Revit.DB.FilteredElementCollector(doc).OfCategory(
    BuiltInCategory.OST_TelephoneDevices).WhereElementIsNotElementType().ToElements()

rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType().ToElements()

all_levels = list(FilteredElementCollector(doc). \
    OfCategory(BuiltInCategory.OST_Levels). \
    WhereElementIsNotElementType().ToElements())

clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

params_dict = {}
for a in list(te[0].Parameters.GetEnumerator()):
    params_dict[a.Definition.Name] = [a]

import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *


class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()

    def InitializeComponent(self):
        self._dgv = System.Windows.Forms.DataGridView()
        self._parametersbox = System.Windows.Forms.ComboBox()
        self._Параметр = System.Windows.Forms.GroupBox()
        self._Number = System.Windows.Forms.DataGridViewTextBoxColumn()
        self._Level = System.Windows.Forms.DataGridViewComboBoxColumn()
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._Cancel_button = System.Windows.Forms.Button()
        self._accept_button = System.Windows.Forms.Button()
        self._grdBox = System.Windows.Forms.GroupBox()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._dgv.BeginInit()
        self._Параметр.SuspendLayout()
        self._groupBox1.SuspendLayout()
        self._grdBox.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self.SuspendLayout()
        #
        # dgv
        #
        self._dgv.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        self._dgv.Columns.AddRange(System.Array[System.Windows.Forms.DataGridViewColumn](
            [self._Number,
             self._Level]))
        self._dgv.GridColor = System.Drawing.SystemColors.ActiveCaption
        self._dgv.Location = System.Drawing.Point(6, 21)
        self._dgv.Name = "dgv"
        self._dgv.RowTemplate.Height = 24
        self._dgv.Size = System.Drawing.Size(391, 135)
        self._dgv.TabIndex = 0
        #
        # parametersbox
        #
        self._parametersbox.FormattingEnabled = True
        self._parametersbox.Location = System.Drawing.Point(6, 21)
        self._parametersbox.Name = "parametersbox"
        self._parametersbox.Size = System.Drawing.Size(397, 24)
        self._parametersbox.TabIndex = 0
        #
        # Параметр
        #
        self._Параметр.Controls.Add(self._parametersbox)
        self._Параметр.Location = System.Drawing.Point(1, 178)
        self._Параметр.Name = "Параметр"
        self._Параметр.Size = System.Drawing.Size(403, 52)
        self._Параметр.TabIndex = 2
        self._Параметр.TabStop = False
        self._Параметр.Text = "Примечание из параметра:"
        #
        # Number
        #
        self._Number.HeaderText = "No"
        self._Number.Name = "Number"
        self._Number.Width = 50
        #
        # Level
        #
        self._Level.FillWeight = 300
        self._Level.HeaderText = "Revit Level"
        self._Level.Name = "Level"
        self._Level.Resizable = System.Windows.Forms.DataGridViewTriState.True
        self._Level.SortMode = System.Windows.Forms.DataGridViewColumnSortMode.Automatic
        self._Level.Width = 300
        #
        # groupBox1
        #
        self._groupBox1.Controls.Add(self._label1)
        self._groupBox1.Location = System.Drawing.Point(1, 236)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(133, 103)
        self._groupBox1.TabIndex = 3
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Пример марки:"
        #
        # label1
        #
        self._label1.Location = System.Drawing.Point(11, 27)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(127, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "РК1.101.[1,2...n]"
        #
        # label2
        #
        self._label2.Location = System.Drawing.Point(6, 18)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(144, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "РК - СС_Тип _сети"
        #
        # label3
        #
        self._label3.Location = System.Drawing.Point(8, 37)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(177, 23)
        self._label3.TabIndex = 1
        self._label3.Text = "1-порядковый №этажа"
        #
        # label4
        #
        self._label4.Location = System.Drawing.Point(8, 77)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(177, 23)
        self._label4.TabIndex = 1
        self._label4.Text = "101 - номер помещения"
        #
        # label5
        #
        self._label5.Location = System.Drawing.Point(6, 56)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(258, 20)
        self._label5.TabIndex = 1
        self._label5.Text = "[1,2..n]- номер в границах помещения"
        self._label5.Click += self.Label5Click
        #
        # Cancel_button
        #
        self._Cancel_button.Location = System.Drawing.Point(309, 342)
        self._Cancel_button.Name = "Cancel_button"
        self._Cancel_button.Size = System.Drawing.Size(75, 23)
        self._Cancel_button.TabIndex = 4
        self._Cancel_button.Text = "Cancel"
        self._Cancel_button.UseVisualStyleBackColor = True
        self._Cancel_button.MouseClick += self.Cancel_buttonClick
        #
        # accept_button
        #
        self._accept_button.Location = System.Drawing.Point(216, 342)
        self._accept_button.Name = "accept_button"
        self._accept_button.Size = System.Drawing.Size(75, 23)
        self._accept_button.TabIndex = 6
        self._accept_button.Text = "OK"
        self._accept_button.UseVisualStyleBackColor = True
        self._accept_button.MouseClick += self.Button2Click
        #
        # grdBox
        #
        self._grdBox.Controls.Add(self._dgv)
        self._grdBox.Location = System.Drawing.Point(1, 2)
        self._grdBox.Name = "grdBox"
        self._grdBox.Size = System.Drawing.Size(403, 170)
        self._grdBox.TabIndex = 8
        self._grdBox.TabStop = False
        self._grdBox.Text = "Соотвествие уровня номеру этажа:"
        #
        # groupBox2
        #
        self._groupBox2.Controls.Add(self._label4)
        self._groupBox2.Controls.Add(self._label5)
        self._groupBox2.Controls.Add(self._label2)
        self._groupBox2.Controls.Add(self._label3)
        self._groupBox2.Location = System.Drawing.Point(134, 236)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(270, 103)
        self._groupBox2.TabIndex = 2
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Параметры"
        #
        # MainForm
        #
        self.ClientSize = System.Drawing.Size(406, 377)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._grdBox)
        self.Controls.Add(self._accept_button)
        self.Controls.Add(self._Cancel_button)
        self.Controls.Add(self._groupBox1)
        self.Controls.Add(self._Параметр)
        self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle
        self.Name = "MainForm"
        self.Text = "МаркаСС"
        self.Load += self.MainFormLoad
        self._dgv.EndInit()
        self._Параметр.ResumeLayout(False)
        self._groupBox1.ResumeLayout(False)
        self._grdBox.ResumeLayout(False)
        self._groupBox2.ResumeLayout(False)
        self.ResumeLayout(False)

        for x in params_dict.keys():
            self._parametersbox.Items.Add(x)
        for level in all_levels:
            self._Level.Items.Add(level.Name)

    def Label1Click(self, sender, e):
        pass

    def MainFormLoad(self, sender, e):
        pass

    def SplitContainer6SplitterMoved(self, sender, e):
        pass

    def Label5Click(self, sender, e):
        pass

    def Cancel_buttonClick(self, sender, e):
        self.condition = False
        self.Close()

    def Button2Click(self, sender, e):
        self.condition = True
        self.levels = {}
        rows = self._dgv.Rows
        i = 0
        # -1 потому что добавляется пустая строка
        while i < len(rows)-1:

            self.levels[rows[i].Cells[1].Value] = rows[i].Cells[0].Value
            i += 1

        self.Close()


form = MainForm()
Application.Run(form)
Application.EnableVisualStyles()

levels = form.levels
extra_param = form._parametersbox.Text




if form.condition:
    counter1 = 0
    room_list = []
    work_dict = {}
    number = 1

    i = 0

    t = Transaction(doc, "Set Mark for all telephone devices")

    t.Start()
    while i < len(te):

        sf = te[i].Location.Point
        inroom = False
        k = 0

        while inroom == False and k < len(rooms):

            if rooms[k].IsPointInRoom(sf):

                inroom = True
                try:
                    if rooms[k].get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString() not in work_dict.keys():
                        level_number = levels[rooms[k].get_Parameter(BuiltInParameter.ROOM_LEVEL_ID).AsValueString()] # set number of level
                        sType = te[i].LookupParameter("СС.Тип сети").AsString()
                        tempL = [sType]

                        tempL.append(level_number)  # add number of level

                        # get room number and add to dict
                        room_number = rooms[k].get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()

                        tempL.append(room_number)

                        tempL.append(0)  # add number pf telephone devices in room

                        # conver list to string parameter

                        count = int(te[i].Symbol.LookupParameter("СС.Количество портов").AsValueString())
                        c = 0
                        ss = ""
                        while c < count:
                            tempL.append(int(tempL.pop(-1)) + 1)  # new value
                            work_dict[rooms[k].get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()] = tempL

                            ii = 0

                            while ii < len(tempL):
                                ss = ss + str(tempL[ii])
                                if ii != len(tempL) - 1 and ii != 0:
                                    ss = ss + "."
                                elif ii == 0:

                                    pass
                                else:
                                    ss = ss + "\n"

                                ii += 1

                            c += 1
                        if len(te[i].LookupParameter("ADSK_Примечание").AsString()) > 0:
                            ss = ss + "*"
                        te[i].LookupParameter("Марка").Set(str(ss))

                        # add pairs room_number:list_of_the_parameter to dictionary
                        work_dict[rooms[k].get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()] = tempL


                    else:
                        # get list of parametr value
                        tempL = work_dict[rooms[k].get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()]

                        sType = te[i].LookupParameter("СС.Тип сети").AsString()
                        tempL.pop(0)
                        tempL.insert(0, sType)

                        count = int(te[i].Symbol.LookupParameter("СС.Количество портов").AsValueString())

                        c = 0
                        ss = ""
                        while c < count:
                            tempL.append(int(tempL.pop(-1)) + 1)  # new value
                            work_dict[rooms[k].get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()] = tempL

                            ii = 0

                            while ii < len(tempL):
                                ss = ss + str(tempL[ii])
                                if ii != len(tempL) - 1 and ii != 0:
                                    ss = ss + "."
                                elif ii == 0:

                                    pass
                                else:
                                    ss = ss + "\n"

                                ii += 1

                            c += 1
                        #print((te[i].LookupParameter(extra_param)))
                        try:
                            if len(te[i].LookupParameter(extra_param).AsString()) > 0:
                                ss = ss + "*"
                                te[i].LookupParameter("Марка").Set(str(ss))
                        except:
                            te[i].LookupParameter("Марка").Set(str(ss))
                            pass
                except:
                    continue
            k += 1

        i += 1
    t.Commit()

