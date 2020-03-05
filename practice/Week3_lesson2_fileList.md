Ever have a folder full of files, like jpegs from your camera, that you want to rename consistently? In this excercise we'll write a function to do just that. 

## List files in folder 

For this excercise you will need the contents of the folder 99_files in ~py_workgroup\practice\data\99_files.zip
where ~ is your local folder containing the github repo. Alternatively you can use my copy on the L or any folder containing multiple pdf files and other types of files (just make a copy of it because the contents will be altered irrepably).

Set up your script with the variable path set to the 99_files folder

```python
# Comments
# Author

import os


path = r'~py_workgroup\practice\data\99_files'

```

We can use the function listdir() from the os module to list all the contents of a given directory:

```python
file_list = os.listdir(path)
```

You can test the length of the list to see that everything is there and use the index to check the name of the first file in the list:

```python
len(file_list)
file_list[0]
```

## Use conditionals to limit list to one just pdfs
There are multiple types of files in the folder, what if you want a list of just the pdfs?
Start by figuring out how to test if a file is a pdf

```python
first_file = file_list[0]
if first_file.endswith('.pdf'):
	print("It's a PDF!")
else:
	print('It is not a pdf')
```
Now do this while looping over all the files in the list:
```python
for single_file in file_list:
	if single_file.endswith('.pdf'):
		print('It's a PDF!')
	else:
		print('It is not a pdf')
```

That's great, but a lot of printed info, instead let's add it item by item to a new list just for pdfs:

```python
pdf_list = []
for single_file in file_list:
	if single_file.endswith('.pdf'):
		pdf_list.append(single_file)
```

All we have to do to change the file type is change the '.pdf' condition

For this excercise we're going to rename the files so it is handy to have a list in python, but in the future we'll learn how to write this list to a text file that can easily be imported into excel or some other type of software to track all your files. You could also use other conditionals (e.g. parts of the file name) to identify specific files within a list by file type to do something to. For example I use a script to periodically clean my desktop and file away any notes I saved as textfiles.

## Rename files in a list
WARNING anytime you delete or otherwise alter files using python you need to be extremely careful, it is easy to get disoriented on what directory you're working in and files deleted this way can't be retreived from the recycle bin.

For this we'll use the os.rename() function:
```python
os.rename(old, new)
```
where 'old' is the current file path/name and 'new' is the updated path/name

For first_file:
```python
first_file = file_list[0]

old = os.path.join(path, first_file)
new = os.path.join(path, 'new_name'+ first_file)

os.rename(old, new)
```

Now that you have tested it out try it within a for loop

## Other file name tricks
Keep in mind this approach can also be used to put the same file in a different folder/directory, change the filetype or to do various other things. It also becomes more handy as you have more information about the file being renamed.

To split the filename from the extension you can use the os.path.splitext() function, which returns a list with the filename and the extension:
```python
first_file = file_list[0]
newName = os.path.splitext(first_file)[0] + 'prj' +  os.path.splitext(first_file)[1]
new = os.path.join(path, newName)
```
This has the advantage over .split('.') because it distinguishes between the extension and any leading '.' in the path/file name.
