We used the urllib module to download zip files from the web in earlier. In this excercise we'll build on that, showing how more complex url strings can be used to query an API and then we'll transition to requesting these instead through the requests module.

## Constructing a url to query an API
For this excercise we'll use the census data API available through census.gov. They have a lot of different datasets so it's always a good idea to start at their [developer website](https://www.census.gov/developers/).

Many APIs will require you to use some type of key or other authentication. This allows them to track who is using the API and block anyone with malicious intent (i.e. repeatedly querying the API just to overlaod it). When writing your code it is usually a good idea to read this type of information from a separate file that doesn't get shared with the code. This is particurly true for API services that charge you based on use! Many APIs will encourage but not require a key, Census is one of those, you can use the API without including a key but it may limit how big the response can be or the response rate. To sign-up for an key:
https://api.census.gov/data/key_signup.html

We will start with the [2010 Decennial](https://www.census.gov/data/developers/data-sets/decennial-census.html) census. The census API is great in that each has:

* API Call: https://api.census.gov/data/2010/dec/sf1?

Which is like what we were using as our base_url in past examples

* Example calls: https://api.census.gov/data/2010/dec/sf1?get=H001001,NAME&for=state:*

Which are working examples of how to request specific information

* API Variables: [html](https://api.census.gov/data/2010/dec/sf1/variables.html) [xml](https://api.census.gov/data/2010/dec/sf1/variables.xml) [json](https://api.census.gov/data/2010/dec/sf1/variables.json)

Which are very long lists of all the variables/parameters you can restrict your request with, and they're available in variety of formats.

Start by looking at the example url. First if you navigate to that url you'll notice you get the results right in your browser. Looking more closely at the url, the first part - everything before the '?' is what we've been calling our base_url. The first bit is a list of the fields we want 'H001001' and 'NAME'. Ampersands, '&' are used to add more parameters to the string, in this case to specify 'for' where we want that information. In this case that is by state and the '*' is a wild card meaning any value of state (i.e. all states).

When we look at the result we have a list of lists, where each nested list represents a row of results for one of the geographies (states) where the columns are 'H001001', 'NAME' and 'state.' Looking at the results you can tell right away 'NAME' is the name of each state. Based on what we've done with census in the past you may recognize results in the 'state' column are the census FIPS code for that state. We'll come back to the unknown field 'H001001'. First what happens if we change our wild card to one of the FIPS, e.g. Florida:

https://api.census.gov/data/2010/dec/sf1?get=H001001,NAME&for=state:12

Now you just got results for Florida! Now lets figure out what these H001001 results mean, go to the [html](https://api.census.gov/data/2010/dec/sf1/variables.html) variable list because that is most human readbale (also the slowest to load). Right at the top you may see the 'for' clause we were using in the example, and it says it's the FIPS 'for clause. There are also other sub-divisions of state geographies for reference (e.g. COUNTY (FIPS)). Before we get too distracted ctrl-f to find 'H001001. You'll see this is Total housing units. If we wanted a subset of those housing units considered 'rural; we could use 'H002005'. Let's do that for Florida and Alabama:

https://api.census.gov/data/2010/dec/sf1?get=H002005,NAME&for=state:12,01

If we wanted to do that API request for any state in python:
```python
from urllib import urlretrieve  #py2.x
from urllib.request import urlretrieve  #py3.x

base_url = 'https://api.census.gov/data/2010/dec/sf1'

# In this case urllib knows to insert the '?get='
base_query = 'H002005,NAME&for=state:'
state = '12'

url = base_url
query = base_query + state

response = urlretrieve(url, query)
```
## webservice queries
Continuing with census, we'll take a look at the [TIGERweb geoservices Rest API](https://www.census.gov/data/developers/data-sets/TIGERweb-map-service.html). Within that folder of services lets start with [tigerWMS_Current](https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Current/MapServer). Within that map service there are a bunch of layers, lets look at [Counties](https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Current/MapServer/86) (ID 86).



requests module

query to census API

query to website using spatial info from lesson 2 (e.g. census FIPS)

query to OCS
query to arcGIS hosted feature services
