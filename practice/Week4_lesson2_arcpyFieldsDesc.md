We've seen some of the ways to read things on your system to a list (e.g. reading file names within a folder), but it is often useful to do the same type of thing in arc.

## Reading features in a gdb
We're working with arcpy, so if you're working outside of arcPro/ArcMap your script would start like:

```python
# Comments
# Author

import arcpy


gdb = r'~py_workgroup\practice\data\99_files'
```

## Reading fields from a shp (Delete multiple fields)
Ever have a huge table and you only care about a couple fields, but all the extras make it  
hard to work with? Clicking each one and deleting is a pain.
Well we can make a list of the fields, subset it with the names we want to keep and then  
loop over the ones we want to delete.

First we need our list of fields to delete. arpyc.ListFields() returns a list of
field "objects," we'll revisit what this means next time, but for now just know that object.name 
will give us the name of the field.

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
## Get extent from shapefile
