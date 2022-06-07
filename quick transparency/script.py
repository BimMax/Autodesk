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

uidoc = __revit__.ActiveUIDocument
curview = uidoc.ActiveGraphicalView
__doc__ = '100% transparancy'
__author__ = 'Herashchanka Max'

from Autodesk.Revit.Creation import *

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
active_view = doc.ActiveView


object_type = Autodesk.Revit.UI.Selection.ObjectType.Element
element = uidoc.Selection.PickObject(object_type)

t = Transaction(doc, "Set crop")
t.Start()
over = OverrideGraphicSettings().SetSurfaceTransparency(100)
curview.SetElementOverrides(element.ElementId, over)

t.Commit()
