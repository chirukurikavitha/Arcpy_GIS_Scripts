# ArcPy - Find Shapefile Geometry Type

This is a simple ArcPy script to find the geometry type (like Point, Line, or Polygon) of any Shapefile.

## Description
The script uses the `arcpy.Describe()` function to read the properties of a shapefile. Then, it prints whether the shapefile contains points, lines, or polygons using the `shapeType` property.

## How it Works (Code)
```python
import arcpy

# Set the path to the shapefile
fc = r'C:\Python27\ArcGIS10.8\SHAPE FILE\trees.shp'

# Get shapefile properties
desc = arcpy.Describe(fc)

# Print the geometry type
print(desc.shapeType)
