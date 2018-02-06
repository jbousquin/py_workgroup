Object Oriented Programing can get complex, but at the basis the idea is you should reuse the same structures and modules. 
You interact with obecjts (instances) of classes of information with set structures, meaning an object will have set attributes and it's own functions, or methods, that can be used on it.

## Creating a new object

```python
class NewClass(object):
  def __init__(self, var1):
    self.var1 = var1
```

Test it out:

```python
something = NewClass("a")
something
something.var1
```

Add a method to the new class:

```python
class NewClass(object):
  def __init__(self, var1):
    self.var1 = var1
  def special_method(self, char):
    self.special = char + self.var1 + char
```

Test it out:

```python
something = NewClass("a")
something.special
something.special_method("_")
something.special
```

## File Objects and input/output
Commonly you'll have to read a input or write an output to a .txt file or .csv
These files are treated as objects.

First set the file and file path to a variable:

```python
import os

filepath = r"L:\Public\jbousqui\Code\GitHub\py_workgroup\practice\data"
completeFile = filepath + os.sep + "TestTextFile.txt"
```

Next open that file as a file object:

```python
file_object = open(completeFile, "r")
file_object.close()
```

The second arguement in open(), "r" in this case, is used to determine what will be done with the file. "r" for read, "a" for append, "w" for write and "r+" for both. Also note that we close() the file when we are done with it. Before performing other functions on a file object it must be closed and re-opened. To test if a file has been closed you can use .closed

Better yet, you can use the with as syntax to automatically close the file:

```python
with open(completeFile, "r") as file_obj:
  print file_obj.read()

file_obj.closed
```

Once a file is open .read() and .write() methods can be used. To read a multi-line file one line at a time .readline() is used. When writing to a file, "\n" is used to denote the start of a new line.

```python
with open(completeFile, "r") as file_obj:
  print file_obj.readlines()
```  

```python
with open(completeFile, "r+") as file_obj:
  file_obj.write("new line")
```
Notice where the new line of text was added. Let's fix line one and this time append it to the end:

```python
with open(completeFile, "a") as file_obj:
  file_obj.write("\nnew line")
```
Another way around this is to read the file to a variable and then re-write the file:

```python
with open(completeFile, "r+") as file_obj:
  lines = file_obj.read() + "\nNewest line"
  file_obj.seek(0)
  file_obj.write(lines)
```

Think of .seek() as finding a character place within the text, starting at 0.
If looking to change a certain setting in a file it is often useful to .readlines() until the item meets a condition and then updating that line according to the new setting.
