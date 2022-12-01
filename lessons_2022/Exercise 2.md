# Concatenating DataFrames

    Step 1: Create subset for rows 4-9 lines of surveys table
    Step 2: Grab the second to last rows
    Step 3: Reset the index values so the second dataframe appends properly
    Note: drop=True arg avoids adding new index column with old index values
    Step 4: Stack the DataFrames on top of each other

    Step 1: Create a subset for rows and columns
    Step 2: Create a subset for the same rows and different columns
    Step 3: Place the DataFrames side by side

# Save dataframe as csv and download to local machine


# Joining DataFrames

    Step 1: Read in first 10 lines of surveys table
    Step 2: Import a small subset of the species data (speciesSubset.csv) designed for this part of the lesson.
    Note: In this example, species_sub is the lookup table containing genus, species, and taxa names that we want to join with the data in survey_sub to produce a new DataFrame that contains all of the columns from both species_df and survey_df.
    Step 3: Identify join keys
    
    Step 4: attempt left join
    Step 5: pick another join type
    
# Inner Join .merge()
