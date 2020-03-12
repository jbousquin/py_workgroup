Last week we saw how you create a list of all the files in a folder, limit that list to certain file types using conditionals, and rename subsets of that list.
This week we'll get more advance with how we rename them, getting the new name from a list of new names with the same order as our old names.

### List iterators
An iterator can be used to keep track of how many items we've gone through (iterated) over a for loop:
```python
lst1 = ["a", "b", "c", "d"]
i = 0
for item in lst1:
     print(item + " is in the {} place".format(i))
     i += 1
```

Following that example, i could then be used to index a second list with our new name at the same location.  
```python
lst1 = ["a", "b", "c", "d"]
lst2 = ["a1", "b1", "c1", "d1"]
i = 0
for item in lst1:
     print(item + " will become " + lst2[i]) 
     i += 1
```

If you remember index() that might seem like another way to get an item at the same index in another list:
```python
lst1 = ["a", "b", "c", "d"]
lst2 = ["a1", "b1", "c1", "d1"]

for item in lst1:
     item2 = lst1.index(item)
     print('{}, position {}'.format(lst2[item2], item2))
```

However, if the list contains multiple instances of the same value this will  
be a problem, as it returns the index of the first occurence:
```python
lst1 = ["a", "a", "c", "d"]
lst2 = ["a1", "b1", "c1", "d1"]

for item in lst1:
     item2 = lst1.index(item)
     print(item2)
```

Another way to generate an iterator is using the built in method enumerate:
```python
lst1 = ["a", "a", "c", "d"]
lst2 = ["a1", "b1", "c1", "d1"]

for i, item in enumerate(lst1):
     print(item + " will become " + lst2[i])
```

## Applying it to 99_files

```python
# Comments
# Author

import os


path = r'~py_workgroup\practice\data\99_files'
file_list = os.listdir(path)

pdf_list = []

for item in file_list:
     if item.endswith('.pdf'):
          pdf_list.append(os.path.join(path, item))

#for item in pdf_list:
#     new_name = os.path.join(path, #name?)
#     os.rename(item, new_name)
```

Now lets say we have an excel sheet with all our old names and we went through it and lined each one up to create our new names, then read those new names into a python list:
```python
new_names = ['Andreasen-etal-2001.pdf', 'Arrow-etal-1993.pdf', 'Aubry-etal-2006.pdf', 'Banzhaf-etal-2005.pdf', 'Banzhaf-etal-2012.pdf', 'Beaumont-etal-2007.pdf', 'Beys-da-Silva-etal-2014.pdf', 'Bhuta-etal-2014.pdf', 'Bishoi-etal-2009.pdf', 'Blomqvist-etal-2013.pdf', 'Borja-etal-2008.pdf', 'Borja-etal-2005.pdf', 'Brown-etal-2015.pdf', 'Brudvig-etal-2014.pdf', 'Bruno-etal-2002.pdf', 'Butchart-etal-2010.pdf', 'Clifton-etal-2011.pdf', 'Collen-etal-2008.pdf', 'Crossman-etal-2013.pdf', 'Cutter-etal-2003.pdf', 'Cutter-etal-2006.pdf', 'Cutter-etal-2008.pdf', 'Davies-etal-2006.pdf', 'DeFries-etal-2005.pdf', 'Deliege-etal-2015.pdf', 'Diaz-etal-2006.pdf', 'Djalante-etal-2012.pdf', 'Dobbie-etal-2013.pdf', 'Eakin-etal-2009.pdf', 'Eigenbrod-etal-2010.pdf', 'Elliot-2002.pdf', 'Evans-etal-2014.pdf', 'Faber-etal-2012.pdf', 'Fasola-etal-2010.pdf', 'Fromm-2000.pdf', 'Greaver-etal-2012.pdf', 'Haines-Young-etal-2009.pdf', 'Hak-etal-2015.pdf', 'Hallett-2014.pdf', 'Helfenstein-etal-2014.pdf', 'Hermoso-etal-2013.pdf', 'Herrick-2000.pdf', 'Herrick-etal-2010.pdf', 'Holling-1973.pdf', 'Jorgenson-etal-2015.pdf', 'Karnauskas-etal-2014.pdf', 'Katsanevakis-etal-2014.pdf', 'Kerr-etal-2003.pdf', 'Kronenberg-2014.pdf', 'Kumar-etal-2008.pdf', 'Lackey-1998.pdf', 'Laugen-etal-2014.pdf', 'Le Pape-etal-2014.pdf', 'Loh-etal-2005.pdf', 'Loomis-etal-2014.pdf', 'Lowe-etal-2009.pdf', 'Mace-etal-2012.pdf', 'Marine Trophic Index-ND.pdf', 'Martin-2014.pdf', 'Mawdsley-etal-2009.pdf', 'McCauley-2006.pdf', 'McCrea-etal-2015.pdf', 'Muller-2005.pdf', 'Muller-etal-2012.pdf', 'Muller-etal-2016.pdf', 'Muller-etal-2000.pdf', 'Murphy-etal-2013.pdf', 'Muscolo-etal-2014.pdf', 'Naeem-1998.pdf', 'Noss-2001.pdf', 'Orfanidis-etal-2003.pdf', 'Ostendorf-2011.pdf', 'Paulraj-etal-2015.pdf', 'Peck-etal-2009.pdf', 'Perrings-etal-2011.pdf', 'Pettorelli-etal-2005.pdf', 'Poikane-etal-2014.pdf', 'Pulselli-etal-2011.pdf', 'Rapport-etal-2013.pdf', 'Seppelt-etal-2011.pdf', 'Smeets-etal-1999.pdf', 'Smith-etal-2013.pdf', 'Smith-etal-B.pdf', 'Spooner-etal-2006.pdf', 'Stapanian-etal-2013.pdf', 'Sterk-etal-2013.pdf', 'Stinchcombe-etal-2007.pdf', 'Timko-etal-2009.pdf', 'Tompkins-etal-2004.pdf', 'Tsai-etal-2009.pdf', 'Turner-etal-1998.pdf', 'Verissimo-etal-2013.pdf', 'Villafan-etal-2001.pdf', 'Walker-etal-2002.pdf', 'Wolter-etal-2003.pdf', 'Wong-etal-2015.pdf']
```
First we'll test that the two have the same number of names
```python
len(pdf_list) == len(new_names)
```
Then we can update our loop over the pdf_list to change all the names:
```python
for i, item in enumerate(pdf_list):
     new_name = os.path.join(path, new_names[i])
     os.rename(item, new_name)
```

Now of course in the real application you'd want to probably read in the old name from that excel file too rather than trusting os.listdir() to go in the expected order.
