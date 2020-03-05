Last week we saw how you create a list of all the files in a folder, limit that list to certain file types using conditionals, and rename subsets of that list.
This week we'll get more advance with how we rename them, getting the new name from a list of new names with the same order as our old names.

### List iterators
An iterator can be used to keep track of how many items we've gone through (iterated) over a for loop:
```python
lst1 = ["a", "b", "c", "d"]
i = 0
for item in lst1:
     print(item + " is in the " + i + " place")
     i += 1
```

Following that example, i could then be used to index a second list with our new name at the same location.  
```python
lst1 = ["a", "b", "c", "d"]
lst2 = ["a1", "b1", "c1", "d1"]
i = 0
for item in lst1:
     print(item + " will become " + lst2[i]) 
     i += 1
```

If you remember index() that might seem like another way to get an item at the same index in another list:
```python
lst1 = ["a", "b", "c", "d"]
lst2 = ["a1", "b1", "c1", "d1"]

for item in lst1:
     item2 = lst1.index(item)
     print(item2)
```

However, if the list contains multiple instances of the same value this will  
be a problem, as it returns the index of the first occurence:
```python
lst1 = ["a", "a", "c", "d"]
lst2 = ["a1", "b1", "c1", "d1"]

for item in lst1:
     item2 = lst1.index(item)
     print(item2)
```

Another way to generate an iterator is using the built in method enumerate:
```python
lst1 = ["a", "a", "c", "d"]
lst2 = ["a1", "b1", "c1", "d1"]

for i, item in enumerate(lst1):
     print(item + " will become " + lst2[i])
```

## Applying it to 99_files

```python
# Comments
# Author

import os


path = r'~py_workgroup\practice\data\99_files'
file_list = os.listdir(path)

pdf_list = []

for item in file_list:
     if item.endswith('.pdf'):
          pdf_list.append(os.path.join(path, item))

#for item in pdf_list:
#     new_name = os.path.join(path, #name?)
#     os.rename(item, new_name)
```
