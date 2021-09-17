# TheZebra_HOMEWORK

- Created by: Tiffany McKay

- Purpose:
  To help merge two csvs that I received together (auto insurance and home insurance). Once merged, I want to clean the data to have the data types for each column match the target schema I was given.  

# Description
- Import python packages such as pandas to help read the csvs 
- Use concat to help merge the two csvs (home and auto insurance) 
- Once data was merged the indices were no longer accurate so, I reset the indices, this completed merged file was saved to output1 dataframe. 
- Save the csvs given into the working directory you have your python set to.

- The dataframe then had few items that needed a previous pass through for cleaning in terms of data, for instance Zipcodes had "" in the string, and Cost Per Ad Click, and Phone NUmber as well needed reformatting in terms of data. Once the data was cleaned by replacing strings or setting some strings to floats etc. it was easy to establish the data types that should be associated with these columns. 

After merging the data, the Cost Per Ad Click column had two data types in output1, float from the home table and str from the auto table, so first changed all of the data to strings to then convert them to float data type to match the target schema.

Finally, I wanted to establish which columns could be nullable, so used a for loop to iterrate through the columns that could be nullable (which was just one in this target schema, and that was the Phone Number column). I then saved the rows that included a null value into a drop_lst list as well as dropped these rows. 


I also included the schema definition as a part of the pandera package to validate the target_schema structure matches the data types and the nullable values. 

# Dependencies
- A python IDE, either Spyder or Visual Studio Code
- A new package that may not have been installed, pandera
-   If using Anaconda, please use the following:
-     conda install -c conda-forge pandera
-     conda install -c conda-forge/label/cf202003 pandera


What I would have liked to do next time: 
- Validation tests for the future: 
-     Maybe adding a summary of the data, count of columns, count of rows, average or sum of the float values (Cost Per Clicks) before and after transformation
-     Come up with a set of rules of what errors we receive in the past when we get these files, for instance, are there specific campaign IDs to look for and expect each time? Should there be a set number of characters for each columnn, as in a max number of characters a column can contain? For instance phone number should be 7 digits. 

