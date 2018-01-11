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

