Last week we experimented with downloads using a url, but what if we want to download a bunch of files from a site or the file we want to download depends on some user provided variable or area of interest?

One way to get multiple downloads if to loop over a list.
One way to test if a user provided variable meets certain criteria is using conditional if statements.

## Set up script
We'll start off setting up our script just like last time

```python
# Author name
# other comments with relevant metadata
from urllib import urlretrieve
import os
   
filepath = r"C:\Users\<user name>\Desktop"
fullFileName = filepath + os.sep + "SantaRosaCounty.zip"
```

if py 3.x
```python
from urllib.request import urlretrieve
```
## Downloading multiple county shapefiles

Last week we downloaded a shapefile for Santa Rosa County using:
```python
url = 'https://www2.census.gov/geo/tiger/TIGER2019/ADDRFEAT/tl_2019_12113_addrfeat.zip'
urlretrieve(url, fullFileName)
```
This time, instead navigate to the page where the zip file is located: https://www2.census.gov/geo/tiger/TIGER2019/ADDRFEAT

All the files hosted here are for different counties in the United States as of 2019. You might notice they all start with 'tl_2019_' and end with '_addrfeat.zip' The 5 digits that change are called FIPS or GEOIDs and each equates to a different county (see [nrcs link](https://www.nrcs.usda.gov/wps/portal/nrcs/detail/fl/about/?cid=nrcs143_013697)). The first 2 digits identify the state, e.g. 12 = Florida, then the last 3 digits are for the county, e.g.  113. 

Let's start by getting the files for both Santa Rosa and Escambia County (FL). We know the FIPS codes for those so let's start by creating a list of the codes:
```python
fips_list = [12113, 12033]
```
We know we'll need to construct 2 things for each:
     (1) the url to get the link from 
     (2) a unique file name, since fullFileName = filepath + os.sep + "SantaRosaCounty.zip" won't work for Escambia County

For the link we'll use the host page as a starting point for constructing our url:

    base_url = 'https://www2.census.gov/geo/tiger/TIGER2019/ADDRFEAT/'

We could construct each link using the list and index:

```python
url_SantaRosa = base_url + 'tl_2019_' + str(fips_list[0]) + '_addrfeat.zip'
url_Escambia = base_url + 'tl_2019_' + str(fips_list[1]) + '_addrfeat.zip'
```

You'll notice we had to coerce both fips to string using str() because they were both int() datatype. There are several ways to format strings to combine several pieces of information from variables, one of these is the string .format method:

```python
   url_SantaRosa = '{}tl_2019_{}_addrfeat.zip'.format(base_url, fips_list[0])
   url_Escambia = '{}tl_2019_{}_addrfeat.zip'.format(base_url, fips_list[1])
```

The string is everything between ' and ', anywhere there is a {} a piece of information is inserted into the string. The two results are about the same length, but it is easier to read and the variables are automatically coerced to string.

Next we need to set unique fullFileName variables. Again we could do that by indexing our list:

```python
   fileName_SantaRosa = os.path.join(filepath, 'county_{}.zip'.format(fips_list[0])
   fileName_Escambia = os.path.join(filepath, 'county_{}.zip'.format(fips_list[1])
```

Those variables will work and will allow you to download the files using urlliretrieve again:

```python
    urlretrieve(url_SantaRosa, fileName_SantaRosa)
    urlretrieve(url_Escambia, fileName_Escambia)
```
## Downloading using for loop over list
But that's like 8 lines of code, is that really any better than just clicking the two links and changing the file names? Now let's instead do the same thing within a for loop where we will loop over our list, downloading files as we go:

```python
for fip in fips_list:
   url = '{}tl_2019_{}_addrfeat.zip'.format(base_url, fip)
   fileName = os.path.join(filepath, 'county_{}.zip'.format(fip)
   urlretrieve(url, fileName)
```
## Downloading using a function
Taking it a step furth we could create a function to download the file to the destination given any FIP:

```python
def downloadCounty(fip, filepath):
   base_url = 'https://www2.census.gov/geo/tiger/TIGER2019/ADDRFEAT/'
   url = '{}tl_2019_{}_addrfeat.zip'.format(base_url, fip)
   fileName = os.path.join(filepath, 'county_{}.zip'.format(fip)
   urlretrieve(url, fileName)
```

Then we run it with:

```python
for fip in fips_list:
   downloadCounty(fip, filepath)
```

You may notice we had to define base_url within our funtion. Variables are typically declared 'locally', this means if base_url is defined in the script it will not be available within a function unless declared gloablly or passed as a parameter to the function (i.e. like fip. Once in the function the variable name for the parameter will be used not the original variable in the script, e.g. this works the same as the above:

```python
def downloadCounty(crazyFIPname, crazy_filepath):
   base_url = 'https://www2.census.gov/geo/tiger/TIGER2019/ADDRFEAT/'
   base_url = '{}tl_2019_{}_addrfeat.zip'.format(base_url, crazyFIPname)
   fileName = os.path.join(crazy_filepath, 'county_{}.zip'.format(crazyFIPname)
   urlretrieve(base_url, fileName)
```

This also means any changes made within the function (e.g. to base_url) don't alter the variables in the main script. Of course any changes made to disk, e.g. like downloading the file, will be made and available for interaction in the main script. To get altered variables you use return:

```python
def downloadCounty(crazyFIPname, crazy_filepath):
   base_url = 'https://www2.census.gov/geo/tiger/TIGER2019/ADDRFEAT/'
   base_url = '{}tl_2019_{}_addrfeat.zip'.format(base_url, crazyFIPname)
   fileName = os.path.join(crazy_filepath, 'county_{}.zip'.format(crazyFIPname)
   urlretrieve(base_url, fileName)
   return base_url
```

And set either the original variable or a new variable to the result:

```python
for fip in fips_list:
   base_url2 = downloadCounty(fip, filepath)
```
## Downloading a subset for a longer list using conditional
You are probably not impressed with the for loop or function as it only reduced your code by two lines, but now it doesn't matter how long your list is you could download all the counties in FL if you wanted. For instance lets say you have a complete list of all the FIPS scraped from a website (to keep it short this is just FL and AL):

```python
fips_list = ['01067', '01073', '01117', '01095', '01123', '01107', '01039', '01015', '01043', '01115', '01083', '01053', '01055', '01081', '01003', '01097', '01007', '01071', '01109', '01021', '01131', '01127', '01019', '01121', '01005', '01045', '01103', '01091', '01069', '01031', '01035', '01057', '01077', '01049', '01061', '01065', '01013', '01093', '01133', '01029', '01089', '01025', '01017', '01027', '01119', '01041', '01105', '01001', '01051', '01099', '01101', '01079', '01033', '01125', '01009', '01113', '01059', '01111', '01047', '01075', '01087', '01011', '01023', '01037', '01063', '01085', '01129', '12001', '12117', '12081', '12037', '12095', '12027', '12031', '12099', '12105', '12086', '12055', '12103', '12083', '12013', '12059', '12071', '12049', '12077', '12053', '12035', '12119', '12005', '12009', '12075', '12039', '12133', '12069', '12051', '12011', '12107', '12091', '12017', '12101', '12127', '12131', '12021', '12041', '12061', '12089', '12111', '12063', '12019', '12113', '12007', '12047', '12087', '12097', '12125', '12023', '12121', '12003', '12079', '12065', '12043', '12115', '12093', '12033', '12123', '12057', '12045', '12015', '12129', '12109', '12085', '12073', '12029', '12067']
```

We would use a conditional within our for loop to determine if it would be downloaded or not:

```python
for fip in fips_list:
   if fip.startswith('12'):
      downloadCounty(fip, filepath)
```

We can get more sophisticated and catch any non-Alabama as well:

```python
for fip in fips_list:
   if fip.startswith('12'):
      downloadCounty(fip, filepath)
    elif fip.startswith('01'):
      print('AL, skipped')
    else:
      print('Weird, {} is neither in AL or FL?'.format(fip))
```

These are the basics, but this same structure can be used for queries to some APIs and are very powerful.
