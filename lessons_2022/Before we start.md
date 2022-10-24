# Before we start

## What is Programming and Coding?

Programming is the process of writing _"programs"_ that a computer can execute and produce some
(useful) output.
Programming is a multi-step process that involves the following steps:

1. Identifying the aspects of the real-world problem that can be solved computationally
2. Identifying (the best) computational solution
3. Implementing the solution in a specific computer language
4. Testing, validating, and adjusting implemented solution.

While _"Programming"_ refers to all of the above steps,
_"Coding"_ refers to step 3 only: _"Implementing the solution in a specific computer language"_. It's
important to note that _"the best"_ computational solution must consider factors beyond the computer.
Who is using the program, what resources/funds does your team have for this project, and the available
timeline all shape and mold what "best" may be.

## Why py?
* Efficient (loop friendly)
* Versatile (C, but can integrate C#, .net, JS, ObjectiveC etc.)
* Libraries/packages by domain experts (e.g. scipy)
* Readable 
* Fun Monty python references

## R vs python
* coursera [Python or R for Data Analysis: Which Should I Learn?](https://www.coursera.org/articles/python-or-r-for-data-analysis)
* datacamp [Choosing Python or R for Data Analysis? An Infographic](https://www.datacamp.com/community/tutorials/r-or-python-for-data-analysis)
* rstudio [R vs. Python: What’s the best language for Data Science?](https://blog.rstudio.com/2019/12/17/r-vs-python-what-s-the-best-for-language-for-data-science/)
* Running python in [Rstudio](https://www.rstudio.com/solutions/r-and-python/) (R notebooks, Quarto, reticulate)
* Run either in jupyter with the proper kernal

## [Zen of Python](https://peps.python.org/pep-0020/#the-zen-of-python)

## Tools
Text editor – where your script is written
* IDLE (in python install)
* Notepad
* Notepad++

Console - where code is run

* IDLE Shell
* Command line

Integrated Development Environment (IDE) – combines these plus more

* Visual Studio (multi-language)
* Rstudio (R, some Python)
* [Spyder](https://www.spyder-ide.org) (similar to R studio/matlab)
* PyCharm (good for web dev, Git, support for JS, HTML/CSS etc.)
* Jupyter notebooks (cloud-based, great for instruction and web)

For further info - see reccent lightning talks on IDEs (EPA Internal)

## environments
![xkcd](https://imgs.xkcd.com/comics/python_environment.png)

Great in concept - allow you to switch between versions and packages
* [Anaconda distribution](https://www.anaconda.com/products/distribution) (comes with many scientific packages)
* Conda environment management (part of anaconda & ArcGIS Pro)
* Virtual environments (usually set up through pip install from [PyPI](https://pypi.org/))

## How to learn more after the workshop?

The material we cover during this workshop will give you an initial taste of how you can use Python
to analyze data for your own research. However, you will need to learn more to do advanced
operations such as cleaning your dataset, using statistical methods, or creating beautiful graphics.
The best way to become proficient and efficient at python, as with any other tool, is to use it to
address your actual research questions. As a beginner, it can feel daunting to have to write a
script from scratch, and given that many people make their code available online, modifying existing
code to suit your purpose might make it easier for you to get started.

## Seeking help

* check under the _Help_ menu
* type `help()`
* type `?object` or `help(object)` to get information about an object
* [Python documentation][python-docs]
* [Pandas documentation][pandas-docs]

Finally, a generic Google or internet search "Python task" will often either send you to the
appropriate module documentation or a helpful forum where someone else has already asked your
question.

I am stuck... I get an error message that I don’t understand.
Start by googling the error message. However, this doesn’t always work very well, because often,
package developers rely on the error catching provided by Python. You end up with general error
messages that might not be very helpful to diagnose a problem (e.g. "subscript out of bounds"). If
the message is very generic, you might also include the name of the function or package you’re using
in your query.

However, you should check Stack Overflow. Search using the `[python]` tag. Most questions have already
been answered, but the challenge is to use the right words in the search to find the answers:
<https://stackoverflow.com/questions/tagged/python?tab=Votes>

### Asking for help

The key to receiving help from someone is for them to rapidly grasp your problem. You should make it
as easy as possible to pinpoint where the issue might be.

Try to use the correct words to describe your problem. For instance, a package is not the same thing
as a library. Most people will understand what you meant, but others have really strong feelings
about the difference in meaning. The key point is that it can make things confusing for people
trying to help you. Be as precise as possible when describing your problem.

If possible, try to reduce what doesn’t work to a simple reproducible example. If you can reproduce
the problem using a very small data frame instead of your 50,000 rows and 10,000 columns one,
provide the small one with the description of your problem. When appropriate, try to generalize what
you are doing so even people who are not in your field can understand the question. For instance,
instead of using a subset of your real dataset, create a small (3 columns, 5 rows) generic one.

### Where to ask for help?

* The person sitting next to you during the workshop. Don’t hesitate to talk to your neighbor during
the workshop, compare your answers, and ask for help. You might also be interested in organizing
regular meetings following the workshop to keep learning from each other.
* Your friendly colleagues: if you know someone with more experience than you, they might be able and
willing to help you.
* [Stack Overflow][so-python]: if your question hasn’t been answered before and is well crafted,
chances are you will get an answer in less than 5 min. Remember to follow their guidelines on how to
ask a good question.
* [Python mailing lists][python-mailing-lists]

## More resources

- [PyPI - the Python Package Index][pypi]

- [The Hitchhiker's Guide to Python][python-guide]

- [Dive into Python 3][dive-into-python3]


[anaconda]: https://www.anaconda.com
[anaconda-community]: https://www.anaconda.com/community
[dive-into-python3]: https://finderiko.com/python-book
[pandas-docs]: https://pandas.pydata.org/pandas-docs/stable/
[pypi]: https://pypi.org/
[python-docs]: https://www.python.org/doc
[python-guide]: https://docs.python-guide.org
[python-mailing-lists]: https://www.python.org/community/lists
[stack-overflow]: https://stackoverflow.com
[so-python]: https://stackoverflow.com/questions/tagged/python?tab=Votes

