The utils.field_to_list() function you've been using uses a [data access cursor object](http://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-classes/cursor.htm).

```python
def field_to_list(table, field):
    """Read Field in Table to List
    Notes: field as string, 1 field at a time
    Example: lst = field_to_lst("table.shp", "fieldName")
    """
    lst = []
    # Check that field exists in table
    if field_exists(table, field) is True:
        # Use cursor to iterate through table
        with arcpy.da.SearchCursor(table, [field]) as cursor:
            for row in cursor:
                lst.append(row[0])
                #may be a faster implemenetation w/ lst += [row[0]]
        return lst
    else:
        message("{} could not be found in {}".format(field, table))
        message("Empty values will be returned.")
```

Here we just use a search cursor to read values from a field.
We could instead use an update cursor to add values to a field from a list:

```python
def list_to_field(table, field, lst)
  i = 0
  with arcpy.da.UpdateCursor(table, [field]) as cusor:
    for row in cusor:
      row[0] = lst[i]
      i += 1
      cusor.updateRow(row)
```

Notice the update cursor used a .updateRow() method.

We could also use a cursor to read other attributes, like the [geometry object](http://pro.arcgis.com/en/pro-app/arcpy/get-started/reading-geometries.htm) of the cursor (SHAPE@)
Or if we are using it in a web service query, we can get the geometry directly as a JSON string (SHAPE@JSON).
You can also change the cursor [spatial reference](http://pro.arcgis.com/en/pro-app/arcpy/get-started/setting-a-cursor-s-spatial-reference.htm) without re-projecting the feature.
