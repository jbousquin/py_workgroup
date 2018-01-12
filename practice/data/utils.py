# Utility functions
# Author: Justin Bousquin
# Email: bousquin.justin@epa.gov

import arcpy

def message(s):
    print(s)

    
def field_exists(table, field):
    """Check if field exists in table
    Notes: return true/false
    """
    fieldList = [f.name for f in arcpy.ListFields(table)]
    return True if field in fieldList else False


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
