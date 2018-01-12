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

field1 = ""
field2 = ""
layer = ""

list_1 = field_to_list(layer, field1)
list_2 = field_to_list(layer, field2)
```

Now I could loop through and do math to find only points that are different:

```python
# make list to hold differences
diff_list = []
#make iterator
i = 0
for val in list_1:
  if val != list_2[i]:
    diff_list.append(val - list_2[i])
  i = i + 1
```

Though that difference doesn't mean much without the ID of the feature:

```python
field3 = "FID"
list_3 = field_to_list(layer, field3)

# make list to hold differences
diff_list = []
ID_list = [] # List to hold ID
i = 0
for val in list_1:
  if val != list_2[i]:
    diff_list.append(val - list_2[i])
    ID_list.append(list_3[i])
  i + 1
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
