If you're able to download something using the web, you should be able to do it with python.

# Create url to retrive

Let's say we wanted to get a shapefile for Santa Rosa county. 
  1. Google "santa rosa county census shapefile" and follow the first [hit](https://catalog.data.gov/dataset/tiger-line-shapefile-2019-county-santa-rosa-county-fl-address-range-feature-county-based)
  2. Scroll down on the site to find the first download button and copy it's link address. It should be:
  http://www2.census.gov/geo/tiger/TIGER2012/ADDRFEAT/tl_2012_12113_addrfeat.zip

Now open your python shell. First, add some descriptive text about what the file does using comments:

    # This file downloads a shapefile for Santa Rosa County
    # Author <your name>

Next, we need to declare a variable for the link:

    url = "http://www2.census.gov/geo/tiger/TIGER2012/ADDRFEAT/tl_2012_12113_addrfeat.zip"
  
Typing a variable (e.g. url) into the shell will print the evaluation of that variable.

    url
> 'http://www2.census.gov/geo/tiger/TIGER2012/ADDRFEAT/tl_2012_12113_addrfeat.zip'

The quotation marks, `''` or `""` on either side denote that it is a string type variable.
The name of the variable, `url` doesn't matter, as long as it is referenced consistently.

# Create variable to save download as
Next we need to have a variable to tell python where to put our download, both the directory and the filename.

    filepath = "C:\Users\<user name>\Desktop"
  
Typing this variable into shell prints the `\` as `\\` because backslashes are escape characters. How python interprets backslashes can get complex and depends on the character after the backslash and even your operating system ([details](https://pythonconquerstheuniverse.wordpress.com/2008/06/04/gotcha-%E2%80%94-backslashes-are-escape-characters/)).
One way to avoid confusion is to denote the string as raw:

    filePath = r"C:\Users\<user name>\Desktop"

Note that setting a variable a second time replaces the original value of that variable.

Next, create your desired filename as a new variable:

    fileName = "SantaRosaCounty.zip"

String variables can be added on to the end of other string variables using `+` . Set the full file name including the directory:
    
    fullFileName = filePath + fileName
    
When you print the value of the new variable we can see we left out backslash separators. We know from above that windows uses `\\`:

    fullFileName = filePath + "\\" + fileName

# Download file
Python uses modules to add functionality that other people have written code for.
Each module is basically a script with functions inside that take specified variables to do something. We will revisit functions and modules in more detail later.
A module can be imported using import <module name>:

```python
    import this
    import os
    import arcpy
    import urllib
```

The os module gives us operating system based functions. When we were declaring our fullFileName, if we didn't know the expected seperators were `"\\"` we could have used the sep function in the os module:

    fullFileName = filePath + os.sep + fileName
  
The arcpy module allows us to use arcGIS functionality outside of arcGIS desktop. In the python window of arcMap this module is already imported.

The urllib module is one of the packages for using urls. There are several that can be used depending on your specific needs and instal.
Once urllib is imported the functions inside can be accessed using the module they are in and dot notation:

```python
    import urllib
    urllib.urlretrieve()
```

The function urlretrieve() performs some function on the variables we put in (). When a function isn't given the variables (aka arguments) that it expects you should get an error. The urlretrieve() function expects at least 1 argument and so you get an error:

>```python
>Traceback (most recent call last):
>  File "<pyshell#37>", line 1, in <module>
>    urllib.urlretrieve()
>TypeError: urlretrieve() takes at least 1 argument (0 given)
>```

How do we know what argument the function wants? Google the module.function to find the documentation that will tell what the variables should be (The first [hit](https://docs.python.org/2/library/urllib.html) should the documentation for the python standard library).
The python documentation can be jargony, scroll down to urllib.**urlretrieve**(url[, filename[, reporthook[,data]]]) and we see the first argument is the url. We know from the error we got that the function only requires 1 argument, and now we see it is the url. In the documentation we see it will also take additional arguments such as filename:

> The second argument, if present, specifies the file location to copy to (if absent, the location will be a tempfile with a generated name).

It looks like it wants (url, filename) as the variables:

    urllib.urlretrieve(url, fullFileName)

Go see if it worked!

# Additional things to try
In the example above the name of the function within the urllib module and what arguments it expected had to be known. Depending on the IDE you are using there may be helpful resources for this. 
Try importing urllib from the python window in arcMap:

```python
    import urllib
```

As you type the interface will try to autocomplete for you. If you type urllib. it will start suggesting functions within that library.

    urlib.u

> urllib.urlretrieve

Likewise, once you out the function the IDE may be able to show you the expected syntax:

> urllib.urlretrieve(url, filename=None, reporthook=None, data=None)

It takes time for python to import an entire library, so if we are only using a couple known functions we can choose to only import those:
```python
    from urllib import urlretrieve
```

Now the function is accessible outside of the module:

    urlretrieve(url, fullFileName)


  
