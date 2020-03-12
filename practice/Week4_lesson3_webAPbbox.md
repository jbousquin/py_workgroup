We used the urllib module to download zip files from the web in earlier. In this excercise we'll build on that, showing how more complex url strings can be used to query an API and then we'll transition to requesting these instead through the requests module.

## Constructing a url to query an API
For this excercise we'll use the census data API available through census.gov. They have a lot of different datasets so it's always a good idea to start at their [developer website](https://www.census.gov/developers/).

Many APIs will require you to use some type of key or other authentication. This allows them to track who is using the API and block anyone with malicious intent (i.e. repeatedly querying the API just to overlaod it). When writing your code it is usually a good idea to read this type of information from a separate file that doesn't get shared with the code. This is particurly true for API services that charge you based on use! Many APIs will encourage but not require a key, Census is one of those, you can use the API without including a key but it may limit how big the response can be or the response rate. To sign-up for an key:
https://api.census.gov/data/key_signup.html

We will start with the [2010 Decennial](https://www.census.gov/data/developers/data-sets/decennial-census.html) census. The census API is great in that each has:

* API Call: api.census.gov/data/2010/dec/sf1?
Which is like what we were using as our base_url in past examples

* Example calls: https://api.census.gov/data/2010/dec/sf1?get=H001001,NAME&for=state:*
Which are working examples of how to request specific information

* API Variables: [html](https://api.census.gov/data/2010/dec/sf1/variables.html)[xml] (https://api.census.gov/data/2010/dec/sf1/variables.xml) [json](https://api.census.gov/data/2010/dec/sf1/variables.json)

## webservice queries
Continuing with census, we'll take a look at the [TIGERweb geoservices Rest API](https://www.census.gov/data/developers/data-sets/TIGERweb-map-service.html). Within that folder of services lets start with [tigerWMS_Current](https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Current/MapServer). Within that map service there are a bunch of layers, lets look at [Counties](https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Current/MapServer/86) (ID 86).



requests module

query to census API

query to website using spatial info from lesson 2 (e.g. census FIPS)

query to OCS
query to arcGIS hosted feature services
