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
For a broader list of the dataset properties see the (documentation)[https://pro.arcgis.com/en/pro-app/arcpy/functions/dataset-properties.htm].

## Get extent from shapefile

## Reading fields from a shp (Delete multiple fields)
Ever have a huge table and you only care about a couple fields, but all the extras make it hard to work with? Clicking each one and deleting is a pain.
Well we can make a list of the fields, subset it with the names we want to keep and then loop over the ones we want to delete.

First we need our list of fields to delete. arpyc.ListFields() returns a list of field "objects," we'll revisit what this means next time, but for now just know that object.name will give us the name of the field.

```python
# Long version
fields_list = []
for x in arcpy.ListFields(lyr):
  fields_list.append(x.name)
  
# Create a list for field names using list comprehension
fields_list = [x.name for x in arcpy.ListFields(lyr)]  
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
  arcpy.DeleteField_management(lyr, field)
```

Our final code would look something like this:

```python
fields_list = [x.name for x in arcpy.ListFields(lyr)]
keep_list = ['FID', 'Shape', 'GEOID10', 'B01003_1E', 'HD01_VD01']
delete_list = [field for field in fields_list if field not in keep_list]

for field in delete_list:
  arcpy.DeleteField_management(lyr, field)
``

## Reading features in a gdb
