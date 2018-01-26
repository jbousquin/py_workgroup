This file is what I'll walk through to review the code topics on the agenda

### List iterators
Last time we looked at using an iterator to keep track of how many items  
we've gone through (iterated) over a for loop:

```python
lst1 = ["a", "b", "c", "d"]
i = 0
for item in lst1:
  print item + " is in the " + i + " place" 
  i += 1
```

Last time we used i to index a second list at the same location.  
If you remember index() that might seem like another way to get  
an item at the same index in another list:

```python
lst1 = ["a", "b", "c", "d"]
lst2 = range(10, 14)

for item in lst1:
  item2 = lst1.index(item)
  print item2
```

However, if the list contains multiple instances of the same value this will  
be a problem, as it returns the index of the first occurence:

```python
lst1 = ["a", "a", "c", "d"]
lst2 = range(10, 14)

for item in lst1:
  item2 = lst1.index(item)
  print item2
```

Another way to generate an iterator is using the built in method enumerate:

```python
lst1 = ["a", "a", "c", "d"]

for i, item in enumerate(lst1):
  print item + " is in " + str(i) + " place"
```


### Dictionary iterators
When using dictionaries remember elements are store by key not by position,  
meaning their order is ignored and they can't be indexed like lists.  
When looping over a dictionary it will give keys:

```python
dict1 = {"word1": 1, "word2": ["Short", "Sentence"]}

for item in dict1:
  print item
```

Keys must be unique and can be used like iterators to return the 
values of each key:

```python
for item in dict1:
  print dict1[item]
```

Dictionaries also have a built in .items() method to return both the key  
and its value:

```python
for item in dict1.items():
  print item
```

Alternatively, we can get a list of keys and iterate over that if we wanted:

```python
for key in dict1.keys():
  print dict1[key]
  print "Position : " + str(dict1.keys().index(key))
```

And, as you might have suspected, you can get a list of the key values using  
.values():

```python
for item in dict1.values():
  print item
```

Note- when I say list I mean it very literaly:

```python
dict1.values()
type(dict1.values())
```

### New data types set() and tuple()
If you look at each item in a dict.items() list, you may notice an unfamiliar data type  
(a, b). These are [tuples](https://www.tutorialspoint.com/python/python_tuples.htm). Tuples are like lists except they are immutable,   
meaning you can't update the value of elements in place like with a list:

```python
var = "a", "b"
var[0]
var[1]
var[1] = "new value"
```

A set is an unordered collection of unique elements.

```python
lst1 = ['a', 'a', 'c', 'd']
print set(lst1)
```

I wouldn't consider either of these data types my "go to," but they're both useful.

### Matrix math with lists, tuples, and zip()

The zip() function will take items in two lists and combine them (using element position)  
into a list of tuples:

```python
lst1 = range(1, 9)
lst2 = range(11, 19)
lst3 = zip(lst1, lst2)
print lst3
```

Now we could loop over that list and do a math function:

```python
lst4 = []
for i in lst3:
  lst4.append(sum(i))
```

If it was a more complex, custom math function:

```python
lst4 = []
for a, b in lst3:
  lst4.append(a + b)
```

This may not seem all that much better, but next we will add list comprehension...

### List Comprehension
Sometimes you have a simple conditional that you want to use to remove a subset of values:

```python
lst1 = ["NA", 1, 2, 4, 8]
lst2 = []
for item in lst1:
  #if type(item) == type([]):
  if isinstance(item, int):
    lst2.append(item)
```

But that is a lot of lines of code just to remove NA.  
List comprehension allows you to do this pythonically, as one line:

```python
lst3 = [item for item in lst1 if isinstance(item, int)]
```

This also lets you do things to item, like math, before adding it to the new list:

```python
lst4 = [item + 1 for item in lst1 if isinstance(item, int)]
```

Now let's take it back to tuples, we had those two lists we wanted to add together.  
zip let us make one list with each tuple in it. Now we can use list comprehension  
to do math using each tuple:

```python
lst1 = range(1, 9)
lst2 = range(11, 19)

lst3 = [a + b for a, b in zip(lst1, lst2)]
```

All in one line, we could even add in removal of NA again.

```python
lst1 = range(1, 9)
lst2 = ["NA"] + range(12, 19)

lst3 = [a + b for a, b in zip(lst1, lst2) if a != "NA" and b != "NA"]
```
