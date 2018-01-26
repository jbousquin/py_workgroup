### Federal GIS Servers (rather incomplete):
https://mappingsupport.com/p/surf_gis/list-federal-GIS-servers.pdf
### State GIS resources
https://mappingsupport.com/p/surf_gis/list-state-GIS-servers.pdf


### How to find IDLE on your machine:
IDLE comes with the standard install of python. Depending on where python is installed on your machine the shortcut to it may be in different places. Mine was installed with arc 10.3 so it was:
C:\Python27\ArcGIS10.3\Lib\idlelib\idle.pyw

If I want to run python from command line instead of IDLE:
C:\Python27\ArcGIS10.3\python.exe

If you don’t know where it is you can create a python file by changing the extension on a text file (.txt) to .py then right click and “Edit with IDLE”


### Forward slash vs backslash:
I briefly addressed file paths yesterday and since had a great question about using forward slashes “/” instead of the backslash “\” (I’d never tried).

https://imgs.xkcd.com/comics/backslashes.png

Unix uses forward slashes, and although Windows uses mainly backslashes it will usually accept either (Stack explanation of why). The catch is that not all software written for windows will always accept / (arc & QGIS seem to). Using os.sep from the os module is the safest solution. If you’re using “/” but concerned, os.path.normpath() can be used to normalize the pathname by collapsing redundant separators or on windows converting / to \. Using a raw string is my go to since that lets me copy it directly (apparently common). As to the “There should be one-- and preferably only one --obvious way to do it.” – don’t hardcode paths, make your user supply it or derive it using the os module.



### Resources for learning python
Collection of Python books and documents contributed by EPA Python users:  https://usepa.sharepoint.com/sites/oei_Work/edapservicecenter/Shared%20Documents/PythonBooks?csf=1

Python courses on EPA's Skillport site:  https://epa.skillport.com/skillportfe/main.action#browse/c739e936-2e2d-47c2-b5c8-c4a3e6e635fb 

"Learn Python The Hard Way" https://learnpythonthehardway.org/

Learn Python: https://www.learnpython.org/

Hackerrank Python Tutorials: https://www.hackerrank.com/python-tutorial

Code Academy Intro to Python Course:  https://www.codecademy.com/learn/learn-python

### Learning Python for Data Science

Python for Data Science on EPA's Skillport site:  https://epa.skillport.com/skillportfe/main.action#browse/ee90310a-0f07-4274-95e5-5c1f5f30e4a2 

DataCamp Python for Data Science course: https://www.datacamp.com/courses/intro-to-python-for-data-science

### Local Arcpy resources
L:\Public\jbousqui\GIS_Resources

### Pep8 style guide:
https://www.python.org/dev/peps/pep-0008/

### Why is something un-pythonic?
https://docs.quantifiedcode.com/python-anti-patterns/index.html


### R or python
My opinion is each has it's use cases where it is better suited. I've been acusing of always answering with "it depends," so a little more - R was writen by statisticians as a user-friendly way to do data analysis, stats and graphical models; python is written by programers as a efficient and readable programing language and has had stats capabilities added to it. So python is more efficient and generally plays more nicely with other code/programs, but R has more statistics and visualization capacity and many of those are more user friendly. Both have extensive user communities, so if "there is a library/package for that" isn't true of either yet, just give it time (year old e.g. [here](https://elitedatascience.com/r-vs-python-for-data-science)). Here is what other people say:

https://www.datacamp.com/community/tutorials/r-or-python-for-data-analysis

https://www.kdnuggets.com/2015/05/r-vs-python-data-science.html

https://www.datascience.com/blog/r-vs-python-for-data-models-data-science
