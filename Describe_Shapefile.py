import arcpy
fc = r'C:\Python27\ArcGIS10.8\SHAPE FILE\trees.shp'
desc = arcpy.Describe (fc)

print (desc.shapetype)

