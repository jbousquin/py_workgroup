We've seen some of the ways to read things on your system to a list (e.g. reading file names within a folder), but it is often useful to do the same type of thing in arc.

## Background
We're working with arcpy, so if you're working outside of arcPro/ArcMap your script would start like:

```python
# Comments
# Author

import os
import arcpy

path = r'~py_workgroup\practice\data\QC_data'
shp = os.path.join(path, 'QC_data.shp')
```

We've talked a little bit about 'objects' as being special types of variables you can create, get properties from and interact otherwise with. Many times you'll run a arcpy function and it will return one of these objects with information about the inputs. We'll start by looking at the arcpy.Describe() function:

```python
desc = arcpy.Describe(shp)
print(desc)
```
We've created a variable called desc which is a 'geoprocessing describe data object.' We  can use this to find out different information about this shapefile and otherwise interact with it:

```python
desc.dataType
```
For a broader list of the dataset properties see the [documentation](https://pro.arcgis.com/en/pro-app/arcpy/functions/dataset-properties.htm).

## Get extent from shapefile
Some of the properties from the describe object return another object. Two that are particurly useful are the [spatialReference](https://pro.arcgis.com/en/pro-app/arcpy/classes/spatialreference.htm) and the [extent](https://pro.arcgis.com/en/pro-app/arcpy/classes/extent.htm):

```python
desc.spatialReference
desc.spatialReference.factoryCode  # EPSG
desc.spatialReference.name
desc.spatialReference.exportToString()

desc.extent
desc.extent.XMax
desc.extent.JSON
```

## Reading fields from a shp (Delete multiple fields)
Ever have a huge table and you only care about a couple fields, but all the extras make it hard to work with? Clicking each one and deleting is a pain.
Well we can make a list of the fields, subset it with the names we want to keep and then loop over the ones we want to delete.

First we need our list of fields to delete. arpyc.ListFields() returns a list of field "objects," we'll revisit what this means next time, but for now just know that object.name will give us the name of the field.

```python
# Long version
fields_list = []
for x in arcpy.ListFields(shp):
  fields_list.append(x.name)
  
# Create a list for field names using list comprehension
fields_list = [x.name for x in arcpy.ListFields(shp)]  
```

Now we want to make a list of the fields to keep, and for any field in fields_list not  
in our keep_list we'll add it to a delete_list.

```python
# Long version
delete_list = []
for field in fields_list:
  if field not in keep_list:
    delete_list.append(field)

# List comprehension version
keep_list = ['FID', 'Shape', 'GEOID10', 'B01003_1E', 'B01003_1M', 'HD01_VD01', 'HD02_VD01']
delete_list = [field for field in fields_list if field not in keep_list]
```

And now we loop over our delete_list, deleting each field

```python
for field in delete_list:
  arcpy.DeleteField_management(shp, field)
```

Our final code would look something like this:

```python
fields_list = [x.name for x in arcpy.ListFields(shp)]
keep_list = ['FID', 'Shape', 'GEOID10', 'B01003_1E', 'HD01_VD01']
delete_list = [field for field in fields_list if field not in keep_list]

for field in delete_list:
  arcpy.DeleteField_management(shp, field)
```

## List of shapefiles or feature classes
You can also read files to a list using arcpy, start off the same way but instead of setting a variable (e.g. shp) set it to your folder/geodatabase and set the current workspace to that using env
```python
import os
import arcpy

path = r''  # folder containting shapefiles
gdb = r'.gdb'  # Alternatively you can set the workspace to a geodatabase

# Set the workspace to path
arcpy.env.workspace = path

# Now list all the shapefiles in that folder
featureClass_list = arcpy.ListFeatureClasses()
```

One time this might be useful is if combining it with functions from early excercises where we copied a shapefile or when re-projecting several files and copying them into a geodatabase:

```python
# Copy shapefiles in list to a file geodatabase
for fc in featureClass_list:
    arcpy.CopyFeatures_management(fc, os.path.join(gdb, os.path.splitext(fc)[0]))
```
