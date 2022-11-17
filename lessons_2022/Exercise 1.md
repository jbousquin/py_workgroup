## Goals

In this exercise we will make a file accessible to our jupyter notebook, read that file into a dataframe and then manipulate the data in the dataframe.

    Step 1: Create a new notebook and save it as 'Exercise_1' 
    Step 2: Get a local copy of surveys.csv and add it to the notebook
    Step 3: Make your first block markdown and add a title
    Step 4: In the next code block import the pandas library
    Step 5: In the next code block add a comment describing where the file came from and set a new variable to the csv file location
    Step 6: read the csv file to a dataframe

### Questions (Create a metadown header cell for each and add code to solve)

1) What are the column names?
2) What data type does the '' col contain?
3) Create a new column with the same data as '' but where the data type is string
4) What is the value for the new column at the 6 index?
5) What are the unique values for '' col?
6) Create a dictionary where the key is the unique values for '' col and the value is the count of instances of that value
7) Add a new '' key to the dictionary and give it a vlue of 0
8) Create a new dataframe without the '' col
9) Aggregate rows based on the '' col
10) Create a new dataframe without any values of '' in the '' col (filter)
