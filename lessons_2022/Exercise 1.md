## Goals

In this exercise we will make a file accessible to our jupyter notebook, read that file into a dataframe and then manipulate the data in the dataframe.

    Step 1: Create a new notebook and save it as 'Exercise_1'
    Step 2: Get a local copy of surveys.csv and add it to the notebook files
    Step 3: Make your first block markdown and add a title
    Step 4: In the next code block import the pandas library
    Step 5: In the next code block add a comment describing where the file came from and set a new variable to the csv file location
    Step 6: read the csv file to a dataframe

### Questions (Create a metadown header cell for each and add code to solve)

1) Choose a method to view a sample of the dataframe (e.g., first 5 fows, etc.)
2) Create a list for the column names
3) What data type does the 'plot_id' col contain?
4) What is the value of the 'plot_id' col in the first row? The value of 'species_id' in the same same?
5) What are the unique values for 'plot_id' col?
6) Create a new column with the same data as 'plot_id' and 'species_id' combined and seperated by '_'
7) What is the value for the new column at the 6 index?
10) Create a new dataframe without the 'record_id' col
11) Create a new dataframe without any values of 'F' in the 'sex' col (using conditionals)
12) Aggregate rows based on the 'year' col

Assignment to work on:
* Create a dictionary where the key is the unique values for 'plot_id' col and the value is the count of instances of that value
* Add a new key to the dictionary (make it sequential) and give it a value of 0
