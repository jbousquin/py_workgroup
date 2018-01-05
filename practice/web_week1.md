If you're able to download something using the web, odds are you could do it with python.

# Create url to retrive

Let's say we wanted to get a shapefile for Santa Rosa county. 
  (1) Google "santa rosa county shapefile" and the first hit should be:
  https://catalog.data.gov/dataset/tiger-line-shapefile-2012-county-santa-rosa-county-fl-address-range-feature-county-based
  (2) Scroll down on the site to find a download button and copy the link addres, it should be:
  http://www2.census.gov/geo/tiger/TIGER2012/ADDRFEAT/tl_2012_12113_addrfeat.zip

Now open your python shell. First, add some descriptive text about what the file does using comments:
  # This file downloads a shapefile for Santa Rosa County
  # Author Name

Next, we need to declare a variable for the link:

  url = "http://www2.census.gov/geo/tiger/TIGER2012/ADDRFEAT/tl_2012_12113_addrfeat.zip"
  
Typing a variable (e.g. url) into the shell will print the evaluation of that variable.
  
The quotation marks on either side denote that it is a string type variable. The name of the variable doesn't matter, as long as it is referenced consistently.

# Create variable to save download as
Next we need to have a variable to tell python where to put our download, both the directory and the filename.
  filepath = "C:\Users\jbousqui\Desktop"
  
Typing this variable into shell prints the "\" as "\\" because of how the operating system treats directories.
One way to avoid any confusion this might cause is to denote the string as raw:
  filePath = r"C:\Users\jbousquin\Desktop"
Notice that setting a variable a second time replaces the original value of that variable.

String variables can be added on to the end of other string variables. Add your desired filename as a new variable:
  fileName = "SantaRosaCounty.zip"
Then set the full file name including the directory:
  fullFileName = filePath + fileName
When you print the value of the new variable we can see we left out separators. We know from above that windows uses "\\":
  fullFileName = filePath + "\\" + fileName

# Download file
Python uses modules to add functionality that other people have written code for.
Each module has functions inside that take specified variables to do something.
A module can be imported using import <module name>:
  import this
  import os
  import urllib
  import arcpy
  
The os module gives us operating system based functions. When we were declaring our fullFileName, if we didn't know the windows seperators were "\\" we could have used the sep function in the os module:
  os.sep
  fullFileName = filePath + os.sep + fileName
  
Note: When using arcGIS functionality outside of arcGIS desktop we must access the arcpy functions using import arcpy.

Now we'll focus on urllib. This is one of the libraries for using urls. There are several that can be used depending on your specific needs.
Once we've imported urllib we can use functions based on the library they are in:
  import urllib
  urllib.urlretrieve()

It takes time for python to import an entire library, so if we are only using a couple known functions we can choose to only import those:
  from urllib import urlretrieve

Now using urlretrieve() performs that function on the variables we put in ().
Google the module.function to find the documentation that will tell what the variables should be.
  https://docs.python.org/2/library/urllib.html
There is a bunch of jargon here, lets find our function (ctrl-F "urlretrieve(").
It looks like it wants (url, filename) as the variables:
  urlretrieve(url, fullFileName)
  
Go see if it worked

Try importing urllib from the python window in arcMap:
  import urllib
As you type the interface will try to autocomplete for you. If you typr urllib. it will start suggesting functions within that library.
When you type out the funciton it will show you the syntax:
  urlib.urlretrieve(
urllib.urlretrieve(url, filename=None, reporthook=None, data=None)


  
