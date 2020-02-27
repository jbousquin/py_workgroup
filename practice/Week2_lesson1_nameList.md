Often data will requiring some 'cleaning' before it can be used in analysis. This lesson will implement some of the python basics learned so far to prepare a mock dataset for further analysis.

#Script layout

All python scripts follow the same general structure when read from top to bottom (with space in between each section):
  1. Documentation (commented text) describing what the script does who authored it
  2. import any required modules
  3. Define any functions that will be used in the script
  4. Define input variables (although this is not strict it helps to see everything at once up front)

Create a python script and add some descriptive text about what the file does using comments:

    # This file takes a string of station names and creates a noramlized list of those names for further analysis
    # Author <your name>

Next, import any modules you plan to use, we don't actually need any for this excersise, but for practice try:

    import os

We won't use any functions yet, so the next step is to define input variables. Define the string variable you'll be working with:

    names = "Fifth Ave (boat launch)\n Little Sandy Pond\n skinequit pond\n Bearses Pond\n Picture Lake (Flax Pond)\n Sand Pond,\n WHITE POND\n Dennis Pond\n Buck's Pond\n Hinkley's Pond\n Flax Pond (Yarmouth/Dennis)\n Long Pond-Long Pond Drive\n Long Pond-Cahoon St.\n Long Pond\n Upper Mill Pon\n Queen Sewell Pond\n Gull Pond - Gull Pond Landing\n Gull Pond (2) - Steele Rd.\n Tides Hotel\n Long Pond - Indian\n PARKERS RIVER SPORTFISHING PIER\n BASS RIVER(UNC.  FREEMAN'S LANDING)\n BAKER'S POND\n WEQUASSETT INN\n"
    
Now we can experiment with some of the string methods available for use on the variable names because it is string datatype. If you aren't sure what the dot notatoin methods are you can either google the documentation or, depending on your IDE it may make suggestions just after typing:

    names.

First let's address the '\n' between every beach name. Often this will come up when a text file is read in as it denotes a new line for each item. In this case it suggests each name had it's own line in the original file. We could use the .strip() method to remove all occurances of '\n':

    names.strip('\n')

It doesn't actually change our variable in-place though, if we print names it still has the '\n':

    print(names)

To change the variable using this string method it must be set to the result (this is just for demonstration, don't do it):

    names = names.strip('\n')

As an alternatvie to .strip() we could also use the .replace() method to remove occurances of '\n' and replace them with an empty string:

    names.replace('\n', '')

Why are there two methods to do the same thing? Well now without '\n' we can't tell which name is which. Instead of seperating entries so that each has it's own line, a common way to seperate entries is using a comma. You may be familiar with Comma Seperated Values (CSV) as a file type. To do this:

    names.replace('\n', ',')

Play around with some of the other string methods available using the dot notation. For example see if you can find one to make all the names lower case.

You may notice there is now a ',' at the end of the string. One easy way to remove characters from the beginning or end of a string is to use the index, i.e. the place in string where the characters we want are. We could count the number of characters in the string, or with python determine the length in number of characters using len():

    len(names)
 
Now we know we just want the first 480 characters, to not include that last ','. To do this we get every character up to 480 using the index:

    names[:480]

Again you'll noticed we waited to set the variable to the result so that we can experiement with the index some more. For example, what happens if we do:

    names[480]
    names[-1]

Can you think of a way to get the same result as names[:480] without knowing the length of the string?
