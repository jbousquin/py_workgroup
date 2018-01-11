Last week we experimented with downloads using a url, but what if the file we want to download depends on some user provided variable or area of interest?

One way to test if a user provided variable meets certain criteria is using conditional if statements.

## Set up script
We'll start off setting up our script just like last time

```python
# Author name
# other comments with relevant metadata
from urllib import urlretrieve
import os
   
filepath = r"C:\Users\<user name>\Desktop"
fullFileName = filepath + os.sep + "NLCD_raster"
```

## Downloading NLCD data
In the past, the [Multi-Resolution Land Characteristics Consortium (MRLC)](https://www.mrlc.gov/) was one of the few comprehensize sources for downloading national scale land use rasters. USGS has recently started providing smaller sections of this data on [AWS](https://www.sciencebase.gov/catalog/item/513624bae4b03b8ec4025c4d) as well. We're going to write a script that will download the latest state NLCD data based on it's abbreviation.

First let's focus on FL. Just like we had the Santa Rosa County roads [url](http://www2.census.gov/geo/tiger/TIGER2012/ADDRFEAT/tl_2012_12113_addrfeat.zip), we'll start off with the url for FL:

https://s3-us-west-2.amazonaws.com/prd-tnm/StagedProducts/NLCD/data/2011/landcover/states/NLCD2011_LC_Florida.zip

And compare that link to another state (Alabama) to see what parts we expect to change:

https://s3-us-west-2.amazonaws.com/prd-tnm/StagedProducts/NLCD/data/2011/landcover/states/NLCD2011_LC_Alabama.zip

At this point it looks like just the state name changes, so we'll build the url string with a variable for state_name:

    state_name = "Florida"
    url = "https://s3-us-west-2.amazonaws.com/prd-tnm/StagedProducts/NLCD/data/2011/landcover/states/NLCD2011_LC_" + state_name + ".zip"

Next we know we need to download it using urlretrieve:

    urlretrieve(url, fullFileName)
    
Now as long as state_name is correct it should work for any state. But we want it to work for an abbreviation, e.g. "FL". We can create a dictionary of all abbreviations and what their full name is in the aws:

```python
state_names = {'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona',
               'AR': 'Arkansas', 'CA': 'California', 'CO': 'Colorado',
               'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida',
               'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho',
               'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
               'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana',
               'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts',
               'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi',
               'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska',
               'NV': 'Nevada', 'NH': 'New_Hampshire', 'NJ': 'New_Jersey',
               'NM': 'New_Mexico', 'NY': 'New_York',
               'NC': 'North_Carolina', 'ND': 'North_Dakota', 'OH': 'Ohio',
               'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania',
               'RI': 'Rhode_Island', 'SC': 'South_Carolina',
               'SD': 'South_Dakota', 'TN': 'Tennessee', 'TX': 'Texas',
               'UT': 'Utah', 'VT': 'Vermont', 'VA': 'Virginia',
               'WA': 'Washington', 'WV': 'West_Virginia',
               'WI': 'Wisconsin', 'WY': 'Wyoming'}
 ```
 
 Note- Be sure to declare our dictionary before we reference it.
 
 Now we can use the abbreviation to find the full name in the state_names dictionary (based on the key).
 
```python
 user_input = "FL"
 state_name = state_names[user_input]
```

But what if our user put the territory "PR" instead, which isn't in our list? Let's use a conditional to catch it and report back a message:

```python
if user_input in state_names:
  state_name = state_names[user_input]
else:
  print "%s not in list of states where NLCD data is available."
```

Let's say we want to test our script to make sure everything works. We can loop over a list of the states:

```python
 list_of_states = ['WA', 'WI', 'WV', 'FL', 'WY', 'NH', 'NJ', 'NM', 'NC', 'ND', 'NE', 'NY', 'RI', 'NV', 'CO', 'CA', 'GA', 'CT', 'OK', 'OH', 'KS', 'SC', 'KY', 'OR', 'SD', 'DE', 'HI', 'TX', 'LA', 'TN', 'PA', 'VA', 'AK', 'AL', 'AR', 'VT', 'IL', 'IN', 'IA', 'AZ', 'ID', 'ME', 'MD', 'MA', 'UT', 'MO', 'MN', 'MI', 'MT', 'MS']

For user_input in list_of_states:
  state_name = state_names[user_input]
  url = "https://s3-us-west-2.amazonaws.com/prd-tnm/StagedProducts/NLCD/data/2011/landcover/states/NLCD2011_LC_" + state_name + ".zip"
  urlretrieve(url, fullFileName)
``` 
  
Even better we could make everything in the for loop into a function:

```python
def download_nlcd(state_name, filepath):
  url = "https://s3-us-west-2.amazonaws.com/prd-tnm/StagedProducts/NLCD/data/2011/landcover/states/NLCD2011_LC_" + state_name + ".zip"
  fullFileName = filepath + os.sep + "NLCD_" + state_name + ".zip"
  urlretrieve(url, fullFileName)
```

When we test it we realize HI doesn't work even though it is in our list. We have a couple options, we could just remove it and it will get caught in our conditional, or we can add another conditional to download HI from NLCD 2001 instead:

https://s3-us-west-2.amazonaws.com/prd-tnm/StagedProducts/NLCD/data/2001/landcover/states/NLCD2001_LC_Hawaii.zip

The only variable we need to add is for year:

```python
if state_name == "Hawaii":
  year = "2001"
else:
  year = "2011"
```

And we re-write our function with the added variable year:

```python
def download_nlcd(state_name, year, filepath):
  url = "https://s3-us-west-2.amazonaws.com/prd-tnm/StagedProducts/NLCD/data/" + year + "/landcover/states/NLCD2011_LC_" + state_name + ".zip"
  fullFileName = filepath + os.sep + "NLCD_" + state_name + ".zip"
  urlretrieve(url, fullFileName)
```

And while we're at it lets add "PR" too:
```python
if state_name == "Hawaii" OR state_name == "Puerto_Rico"
  year = "2001"
else:
  year = "2011"
```

