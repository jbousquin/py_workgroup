Now we'll do a similar excerise as with arcpy, but instead of deleting a list of fields  
from a attribute table we will delete a list of files from a system directory.

# Warning be careful with this, it is way too easy to delete something unintentionally.

First we'll list everything in a given folder using [os.listdir()](https://www.tutorialspoint.com/python/os_listdir.htm)

```python
my_path = r"C:\Users\<username>\Desktop\test_folder"
contents_list = os.listdir(my_path)
```

On inspection we see this lists everything in the folder, files and sub-folders.

Next we will filter out just the files using [os.path.isfile](https://docs.python.org/2/library/os.path.html) and [os.path.join](https://docs.python.org/2/library/os.path.html).
os.path.join is being used to get the full filename and path to pass to os.path.isfile to test:

```python
# Long way
file_list = []
for f in contents_list:
  if f os.path.isfile(os.path.join(my_path, f):
    file_list.append(f)

# List comprehension
file_list = [f for f in contents_list if os.path.isfile(os.path.join(my_path, f))]
```

Last we delete the files:

```python
for f in file_list:
  os.remove(f)
```

Putting it all together (and putting os.listdir() in the list comprehension too):

```python
my_path = r"C:\Users\<username>\Desktop\test_folder"
file_list = [f for f in os.listdir(my_path) if os.path.isfile(os.path.join(my_path, f))]

for f in file_list:
  os.remove(f)
```

Additional conditional statements makes this type of thing more useful. For example,  
when going through a folder of downloaded zip files you may want to delete ones that  
downloaded incorrectly or you've already unzipped the needed files from. In a simliar  
way a list of files could be used to rename all the photos in a folder to follow some  
desired convention.
