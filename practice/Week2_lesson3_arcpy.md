ArcGIS Desktop tasks and processing are able to be automated through python. Python scripts are also able to handle certain data more directly (efficiently) and provide added functions based on outside python libraries.

In the excercise we will take a simple task in arcMap and perform it using python instead of through the Graphic User Interface (GUI).

## Data to use for this excercise
In the Week2_lesson2_web exercise we downloaded a shapefile of Santa Rosa County to the desktop. Start by unzipping that file to a folder on the desktop and add it as a layer in arcMap. If that data is not accessible the zip file `tl_2019_12113_addrfeat.zip` can be downloaded from [GitHub](https://github.com/jbousquin/py_workgroup/tree/master/practice/data/tl_2019_12113_addrfeat.zip)

1. Right click the zip file, go to WinZip > Extract to folder `C:\Users\<user name>\Desktop\tl_2012_12113_addrfeat`

## Using the python window
1. Open ArcMap
2. Open the python window within arcMap.

This window has two panes, on the left is like shell, what you type gets executed. Type:

```python
print("Hello World")
```

On the right documentation that should help you write your script. If you just type the function it will show expected arguments etc.:

```python
print
```

You can set variables just like before. The shapefile can be declared as a variable:

    shapefile = r"C:\Users\<user name>\Desktop\tl_2019_12113_addrfeat\tl_2019_12113_addrfeat.shp"

## First create a copy of a shapefile
1. In ArcMap go to Add Data (The plus sign on the yellow box in the toolbar).
3. Navigate to the new folder and Add the new shapefile `tl_2019_12113_addrfeat.shp` as a layer on your map.
4. Copy the shapefile using the `Copy Features` tool under Data Management Tools > Features in ArcToolbox.
For Input Features just drag and drop the layer from your table of contents. For the Output Features we're going to save it to the desktop as `newShapefile.shp`

## Layers vs shapefiles
In arcToolbox there are differences between when you drag and drop a layer and when you navigate to or type in the shapefile. The same differences carry over to the python window. We can set variables based on layers already in our map without knowing the shapefile location.

    lyr = 'tl_2019_12113_addrfeat'
    
The value for lyr can either be typed out or dragged and dropped. Just remember these two are not equivalent, one is a layer on the map and the other is a specific shapefile.

At this point, python only evaluates the shapefiles as a string and doesn't treat it in any special way. It doesn't matter if the value of the `shapefile` variable is actually a shapefile, or even if it doesn't exist. Create a variable for the file we want to create:

    outShapefile = r"C:\Users\<user name>\Desktop\newShapefile2.shp"

## Functions in arcpy
The arcpy module is already imported into arcMap. Just like when we used functions from urllib, we can use arcpy functions using arcpy.function()

arcpy functions are named to resemble the tools in arcToolbox. Try:

    arcpy.CopyFeatures
    
Note that it should autocomplete as `arcpy.CopyFeatures_management` since this function is in the Data Management tools. In the right panel look at the documentation for this function. Try the function using our variables:

    arcpy.CopyFeatures_management(shapefile, outShapefile)

Notice that just like when we used the tool to copy the file manually, python added the result as a layer on the map by default.

arcpy is well documented and the html lookups include code examples. [Google arcpy Copy Features](http://pro.arcgis.com/en/pro-app/tool-reference/data-management/copy-features.htm) and scroll down to look at the code samples there.

In the code samples you may notice there is both an example for the python window and for stand-alone scripts. The standalone script is how you will want to store your scripts and python can run them without opening arcMap. However, to run arcpy functions you must have the arcpy library installed, and it requires arcGIS.

## Moving a manual process to python
The copy we made using python was fairly straightforward to figure out and the documentation gives good examples but here is another alternative to copying manual processes into python scripts. 

Each time a task is performed in arcMap a record of it appears in results. Open the results window to examine when we manually copied the shapefile.

1. Open results window
2. Click Current Session
3. Expand the first instance of Copy Features (the second is the one we just did using the python window)
4. Right click and select Copy as Python Snipet
5. Open a new python script (IDLE or even notepad)
6. paste the contents of your clipboard to this script

In the first line is a comment about replacing the layer `"tl_2012_12113_addrfeat"` the second line is the function we previously typed out with some additions:

    arcpy.CopyFeatures_management(in_features="tl_2019_12113_addrfeat", out_feature_class="C:/Users/<user name>/Desktop/newShapefile.shp", config_keyword="", spatial_grid_1="0", spatial_grid_2="0", spatial_grid_3="0")
    
The layer must be replaced because outside of the python window in arcMap it doesn't mean anything to python. The other additions are defaults that we didn't set. Copying the result as a python snipet is not foolproof, but it can get you started.

Although this task seemed simple, once you start combining it with other python functions you'll see where it can be powerful. For example, the example in CopyFeatures_mangement documentation shows how to create a list of all the shapefiles in a folder and copy each of them to a new location. We'll learn about loops in week 3.

Try experimenting with other processes and see if you can perform those with python.
