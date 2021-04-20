# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 11:05:48 2021

@author: jbousqui
"""

import arcpy


# Set your file names
shp = r'L:\Public\jbousqui\Code\GitHub\H2O_BEST\greenspace_access\package\tests\parcels.shp'
out_shp = r'L:\Public\jbousqui\Code\GitHub\H2O_BEST\greenspace_access\package\tests\parcels2.shp'

field = 'parcels1_5'  # The field you want to select on

# Retrieve all values from field in attribute table to list
field_values = [row[0] for row in arcpy.da.SearchCursor(shp, [field])]
# Long form this looks like
#field_values = []
#with arcpy.da.SearchCursor(shp, [field]) as cursor:
#    for row in cursor:
#        field_values.append(row[0])

# Coerce that list to a set (all unique) then back to a list (order changes)
unique_values = list(set(field_values))

# Generate selection layer from attribute query to copy
# First make the shp a layer
lyr = "parcels_lyr"
arcpy.MakeFeatureLayer_management(shp, lyr)
# Now make the sql query string, there are many ways to do this
drop_values = ['COUNTIES (OTHER THAN PUBLIC SCHOOLS, COLLEGES, HOSPITALS) INCLUDING NON-MUNICIPAL GOVERNMENT',
               'FEDERAL, OTHER THAN MILITARY, FORESTS, PARKS, RECREATIONAL AREAS, HOSPITALS, COLLEGES',
               'MILITARY',
               'PARCELS WITH NO VALUES',
               'PUBLIC COUNTY SCHOOLS - INCLUDING ALL PROPERTY OF BOARD OF PUBLIC INSTRUCTION',
               'RIVERS AND LAKES, SUBMERGED LANDS',
               'STATE, OTHER THAN MILITARY, FORESTS, PARKS, RECREATIONAL AREAS, COLLEGES, HOSPITALS',
               'UTILITY, GAS AND ELECTRICITY, TELEPHONE AND TELEGRAPH, LOCALLY ASSESSED RAILROADS, WATER AND SEWER SERVICE, PIPELINES, CANALS, RADIO/TELEVISION COMMUNICATION',
               'RIGHT-OF-WAY, STREETS, ROADS, IRRIGATION CHANNEL, DITCH, ETC.',
               'MUNICIPAL, OTHER THAN PARKS, RECREATIONAL AREAS, COLLEGES, HOSPITALS',
               'AIRPORTS (PRIVATE OR COMMERCIAL), BUS TERMINALS, MARINE TERMINALS, PIERS, MARINAS',
               'SEWAGE DISPOSAL, SOLID WASTE, BORROW PITS, DRAINAGE RESERVOIRS, WASTE LAND, MARSH, SAND DUNES, SWAMPS',]
#where_qry = ["{} = '{}' OR ".format(field, val) for val in drop_values][:-4]
where_qry = "{} = '".format(field) + "' OR {} = '".format(field).join(drop_values) + "'"
# Long form
#where_qry = ''
#for val in select_values:
#    where_qry += "{} = '{}' OR ".format(field, val)
#where_qry = where_qry[:-4]  # Drops last 4 characters from string
# New Selection of parcels that do not (INVERT) have the string criteria
arcpy.management.SelectLayerByAttribute(lyr, 'NEW_SELECTION', where_qry, 'INVERT')
# Save the selection as new shp (layers are cleared at end of session unless saved in mxd)
arcpy.CopyFeatures_management(lyr, out_shp)
