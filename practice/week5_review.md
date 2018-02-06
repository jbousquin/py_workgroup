Object Oriented Programing can get complex, but at the basis the idea is you should reuse the same structures and modules. 
You interact with obecjts (instances) of classes of information with set structures, meaning an object will have set attributes and it's own functions, or methods, that can be used on it.

## Creating a new object

```python
class NewClass(object):
  def __init__(self, var1):
    self.var1 = var1
```

Test it out:

```python
something = NewClass("a")
something
something.var1
```

Add a method to the new class:

```python
class NewClass(object):
  def __init__(self, var1):
    self.var1 = var1
  def special_method(self, char):
    self.special = char + self.var1 + char
```

Test it out:

```python
something = NewClass("a")
something.special
something.special_method("_")
something.special
```

## File Objects and input/output
