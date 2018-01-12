This week we talked about lists. Lists are one of the main ways groups of data can be managed.
Feature attribute tables have data in fields, although these entire tables can be handled as multi-dimensional arrays in numpy, we're going to play with them as lists.

Pulling feature attributes to a list is a bit beyond what we've done so far, but I've provided a field_to_list() function in the utils.py module

## QC data in field
I want to compare data over time for a given point. Normally I might create a third field and then use field calculator to fill it in.
But lets do it using lists in python:

```python
# Comments
# Author

from utils import field_to_list

field1 = "B01003_1E"
field2 = "HD01_VD01"
# Note you'll need to specify your copy of the repo instead of ~
# If in arc you can drag and drop the layer (careful of selections)
shp = r"~\py_workgroup\practice\data\QC_data.shp"

list_1 = field_to_list(shp, field1)
list_2 = field_to_list(shp, field2)
```

Now I could loop through and do math to find only points that are different:

```python
# make list to hold differences
diff_list = []
#make iterator
i = 0
for val in list_1:
  if val != list_2[i]:
    diff_list.append(float(val) - float(list_2[i]))
  i = i + 1
```

These fields are text fields, so we get an error the first time one of them is non-numeric:

```python
Runtime error 
Traceback (most recent call last):
  File "<string>", line 3, in <module>
ValueError: could not convert string to float: 
```

We dig can dig in to find that this string value is null u' '. There are a few ways we could handle this, but let's try just catching those nulls and saving them to the list as such:

```python
diff_list = []
i = 0
for val in list_1:
  if val != list_2[i]:
    if val == " ":
      diff_list.append("<null>")
    else:
      diff_list.append(float(val) - float(list_2[i]))
  i = i + 1
```
Well now we have a list of 314 instances where the columns don't match. How many of those are because of the null?

```python
not_null_list = []
for x in diff_list:
  if x != "<null>":
    not_null_list.append(x)
```

Alright, so the differences all have null for the first column. If we want to explore them more or fix it we really need to know the feature ID:

```python
field3 = "FID"
list_3 = field_to_list(shp, field3)

diff_list = []
ID_list = [] # List to hold ID
i = 0
for val in list_1:
  if val != list_2[i]:
    ID_list.append(list_3[i])
    if val == " ":
      diff_list.append("<null>")
    else:
      diff_list.append(val - list_2[i])
  i = i + 1
```

Now we have a list we can use to further explore those errors and try to find out why they might have happend.

## Make layer selection using list
We have a ID_list with all features that don't equal. We could go through one by one, but let's say we want to explore it with a selection in arcmap.

First we have to make sure we have a layer, as selections are temporary and can only be made on a layer not a shapefile:

```python
arcpy.MakeFeatureLayer_management(shp, "temp_layer")
```

Next we'll construct a where_clause concatenating each ID in our list just like the one you use in select by attribute:

```python
where_clause = '' # empty string
for ID in ID_list:
  query = field3 + ' = ' + str(ID) + " OR "
  where_clause = where_clause + query
```

Sometimes query strings can be tricky, so I'd encourage you to test it in select by attribute for the first ID:

```python
ID = ID_list[0]
query = field3 + ' = ' + str(ID) + " OR "
print query
```

Using that we see we'll need to remove the last " OR ", but otherwise it seems to work. We'll add that and then use it to make the selection:

```
where_clause = where_clause[:-4]
arcpy.SelectLayerByAttribute_management("temp_layer", "NEW_SELECTION", where_clause)
```

## Delete multiple fields
Ever have a huge table and you only care about a couple fields, but all the extras make it hard to work with? Clicking each one and deleting is a pain. Well we can make a list of the fields, subset it with the names we want to keep and then loop over the ones we want to delete.

First we need our list of fields to delete. arpyc.ListFields() returns a list of field "objects" where each object have attributes accessed using dot notation. We're interested in .name

```python
# Create a list for field names
fields_list = [x.name for x in arcpy.ListFields(lyr)]

# Long version
fields_list = []
for x in arcpy.ListFields(lyr):
  fields_list.append(x.name)
```

Now we want to make a list of the fields to keep, and for any field in fields_list not in our keep_list we'll add it to a delete_list

```python
keep_list = ['FID', 'Shape', 'GEOID10', 'B01003_1E', 'B01003_1M', 'HD01_VD01', 'HD02_VD01']
delete_list = [field for field in fields_list if field not in keep_list]
# Long version
delete_list = []
for field in fields_list:
  if field not in keep_list:
    delete_list.append(field)
```

And now we loop over our delete_list, deleting each field

```python
for field in delete_list:
  arcpy.DeleteField_management(lyr, field)
```
