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

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc =  DocumentManager.Instance.CurrentDBDocument

#print(dir(Revit.GeometryConversion.GeometryObjectConverter.Convert))
import math
UNIT_CONVERT = 304.8005
uidoc = __revit__.ActiveUIDocument
curview = uidoc.ActiveGraphicalView
__doc__ = 'hole'
__author__ = 'Herashchanka Max'

from Autodesk.Revit.Creation import *

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
av= doc.ActiveView
__doc__ = 'Renumber sheets in selected part'
__author__ = 'Herashchanka Max'



style = Autodesk.Revit.UI.Selection.PickBoxStyle.Directional

aa = uidoc.Selection.PickBox(style)
Min = aa.Min
Max = aa.Max
min = [Min.ToPoint().X,Min.ToPoint().Y,Min.ToPoint().Z]
max = [Max.ToPoint().X,Max.ToPoint().Y,Max.ToPoint().Z]
i = 0
for x in min:

    if round(min[2],2)==round(max[2],2):

        if aa.Max.ToPoint().Y > aa.Min.ToPoint().Y:

            if aa.Max.ToPoint().X > aa.Min.ToPoint().X:

                reverseY = 1
                reverseX = 1
            else:

                reverseY = 1
                reverseX = -1
        else:
            if aa.Max.ToPoint().X > aa.Min.ToPoint().X:

                reverseY = -1
                reverseX = 1
            else:

                reverseY = -1
                reverseX = -1

        p1 = XYZ(aa.Max.ToPoint().X, aa.Max.ToPoint().Y, aa.Max.ToPoint().Z).ToPoint()
        p2 = XYZ(aa.Min.ToPoint().X, aa.Max.ToPoint().Y, aa.Max.ToPoint().Z).ToPoint()
        dx = Line.ByStartPointEndPoint(p1, p2).Length / UNIT_CONVERT  # abs(aa.Max.ToPoint().X)-abs(aa.Min.ToPoint().X)

        p1 = XYZ(aa.Max.ToPoint().X, aa.Max.ToPoint().Y, aa.Max.ToPoint().Z).ToPoint()
        p2 = XYZ(aa.Max.ToPoint().X, aa.Min.ToPoint().Y, aa.Max.ToPoint().Z).ToPoint()
        dy = Line.ByStartPointEndPoint(p1, p2).Length / UNIT_CONVERT  # abs(aa.Max.ToPoint().Y)-abs(aa.Min.ToPoint().Y)
        # print(dx, dy)

        xx = [aa.Min.ToPoint().X/UNIT_CONVERT, aa.Min.ToPoint().X/UNIT_CONVERT,\
              (aa.Min.ToPoint().X+dx*reverseX)/UNIT_CONVERT, (aa.Min.ToPoint().X+dx*reverseX)/UNIT_CONVERT]
        yy = [aa.Min.ToPoint().Y/UNIT_CONVERT, (aa.Min.ToPoint().Y+dy*reverseY)/UNIT_CONVERT,\
              (aa.Min.ToPoint().Y+dy*reverseY)/UNIT_CONVERT, aa.Min.ToPoint().Y/UNIT_CONVERT]
        t = 0
    elif round(min[1],2) == round(max[1],2):
        if aa.Max.ToPoint().Z > aa.Min.ToPoint().Z:


            if aa.Max.ToPoint().X > aa.Min.ToPoint().X:

                reverseY = 1
                reverseX = 1
            else:

                reverseY = 1
                reverseX = -1
        else:
            if aa.Max.ToPoint().X > aa.Min.ToPoint().X:

                reverseY = -1
                reverseX = 1
            else:

                reverseY = -1
                reverseX = -1


        p1 = XYZ(aa.Max.ToPoint().X, aa.Max.ToPoint().Y, aa.Max.ToPoint().Z).ToPoint()
        p2 = XYZ(aa.Min.ToPoint().X, aa.Max.ToPoint().Y, aa.Max.ToPoint().Z).ToPoint()
        dx = Line.ByStartPointEndPoint(p1, p2).Length/UNIT_CONVERT  # abs(aa.Max.ToPoint().X)-abs(aa.Min.ToPoint().X)

        p1 = XYZ(aa.Max.ToPoint().X, aa.Max.ToPoint().Y, aa.Max.ToPoint().Z).ToPoint()
        p2 = XYZ(aa.Max.ToPoint().X, aa.Max.ToPoint().Y, aa.Min.ToPoint().Z).ToPoint()
        dy = Line.ByStartPointEndPoint(p1, p2).Length/UNIT_CONVERT  # abs(aa.Max.ToPoint().Y)-abs(aa.Min.ToPoint().Y)
        #print(dx, dy)

        xx = [aa.Min.ToPoint().X/UNIT_CONVERT, aa.Min.ToPoint().X/UNIT_CONVERT,\
              (aa.Min.ToPoint().X+dx*reverseX)/UNIT_CONVERT, (aa.Min.ToPoint().X+dx*reverseX)/UNIT_CONVERT]
        yy = [aa.Min.ToPoint().Z/UNIT_CONVERT, (aa.Min.ToPoint().Z+dy*reverseY)/UNIT_CONVERT,\
              (aa.Min.ToPoint().Z+dy*reverseY)/UNIT_CONVERT, aa.Min.ToPoint().Z/UNIT_CONVERT]
        t = 1
    elif int(min[0])==int(max[0]):

        if aa.Max.ToPoint().Z > aa.Min.ToPoint().Z:


            if aa.Max.ToPoint().Y > aa.Min.ToPoint().Y:

                reverseY = 1
                reverseX = 1
            else:

                reverseY = -1
                reverseX = 1
        else:

            if aa.Max.ToPoint().Y > aa.Min.ToPoint().Y:

                reverseY = 1
                reverseX = -1
            else:

                reverseY = -1
                reverseX = -1

        p1 = XYZ(aa.Max.ToPoint().X, aa.Max.ToPoint().Y, aa.Max.ToPoint().Z).ToPoint()
        p2 = XYZ(aa.Max.ToPoint().X, aa.Min.ToPoint().Y, aa.Max.ToPoint().Z).ToPoint()
        dy = Line.ByStartPointEndPoint(p1, p2).Length / UNIT_CONVERT  # abs(aa.Max.ToPoint().X)-abs(aa.Min.ToPoint().X)

        p1 = XYZ(aa.Max.ToPoint().X, aa.Max.ToPoint().Y, aa.Max.ToPoint().Z).ToPoint()
        p2 = XYZ(aa.Max.ToPoint().X, aa.Max.ToPoint().Y, aa.Min.ToPoint().Z).ToPoint()
        dx = Line.ByStartPointEndPoint(p1, p2).Length / UNIT_CONVERT  # abs(aa.Max.ToPoint().Y)-abs(aa.Min.ToPoint().Y)

        xx = [aa.Min.ToPoint().Z / UNIT_CONVERT, aa.Min.ToPoint().Z / UNIT_CONVERT,\
              (aa.Min.ToPoint().Z + dx*reverseX) / UNIT_CONVERT, (aa.Min.ToPoint().Z + dx*reverseX) / UNIT_CONVERT]
        yy = [aa.Min.ToPoint().Y / UNIT_CONVERT, (aa.Min.ToPoint().Y + dy*reverseY) / UNIT_CONVERT,\
              (aa.Min.ToPoint().Y + dy*reverseY) / UNIT_CONVERT, aa.Min.ToPoint().Y / UNIT_CONVERT]
        t=2

# print(dx, dy)
# print(aa.Max.ToPoint())
# print(aa.Min.ToPoint())
i = 0
curves= CurveLoop()
#lines = []
while i< len(xx):
    if t == 0:
        if i!=len(xx)-1:
            p1 = XYZ(xx[i],yy[i],0)
            p2 = XYZ(xx[i+1],yy[i+1],0)
        else:
            p1 = XYZ(xx[i], yy[i], 0)
            p2 = XYZ(xx[0], yy[0], 0)


    elif t ==1 :
        if i!=len(xx)-1:
            p1 = XYZ(xx[i],0,yy[i])
            p2 = XYZ(xx[i+1],0,yy[i+1])
        else:
            p1 = XYZ(xx[i],0, yy[i])
            p2 = XYZ(xx[0], 0, yy[0])


    elif t==2:
        if i!=len(xx)-1:
            p1 = XYZ(0, yy[i],xx[i])
            p2 = XYZ(0, yy[i+1],xx[i+1])
        else:
            p1 = XYZ(0, yy[i], xx[i])
            p2 = XYZ(0, yy[0], xx[0])
    l = Line.ByStartPointEndPoint(p1.ToPoint(), p2.ToPoint())


    curves.Append(l.ToRevitType())
    i+=1

t = Transaction(doc, "Set crop")

t.Start()
av.CropBoxVisible = True
vcrShapeMgr = av.GetCropRegionShapeManager()
vcrShapeMgr.SetCropShape(curves)
av.CropBoxActive = True
av.CropBoxVisible = False

t.Commit()
