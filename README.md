# TheZebra_HOMEWORK

- Created by: Tiffany McKay

- Purpose:
  To help merge two csvs that I received together (auto insurance and home insurance). Once merged, I want to clean the data to have the data types for each column match the target schema I was given.  

# Description
- Import python packages such as pandas to help read the csvs 
- Used concat to help merge the two csvs (home and auto insurance) 
- Once data was merged the indices were no longer accurate so, I reset the indices, this completed merged file was saved to output1 dataframe. 
- Save the csvs given into the working directory you have your python set to.

- The dataframe then had few items that needed cleaning in terms of data, for instance Zipcodes had "" in the string, and Cost Per Ad Click, and Phone Number as well needed reformatting in terms of data formatting. 

- I created functions to clean the data, such as dropping columns that were not in the target schema, converting all of teh columns to strings and then changing the columns that were not strings into floats. I also created functions to replace the quotations with empty spaces, as well as a function to replace the .0 found in phone number. Phone number was imported as a float so when converted to a string it contained a ".0" at the end of each phone number, so had to clean that as well. Cost Per Ad Click was the only column in the target schema meant to be a float, so created a function that converted this column from a string to a column. Additionally, created a function that dropped any rows that contained "nan" with the exception of Phone Number as this column was nullable. I wanted to establish which columns could be nullable, so used a for loop to iterrate through the columns that could be nullable(Phone Number column). I then saved the rows that included a null value into a drop_lst list as well as dropped these rows. 


- Once all of my functions were created and decalred, I created a new data frame called target_schema that gets written locally into the current working directory and is saved as a csv.

- Below this is my test section that can be turned on or off, by changing DO_TEST from True to False. Currently set to True. 
- All of the functions created above are tested to confirm they successfully ran, if there is a failure we shall receive an AssertionError message. 



# Dependencies
- A python IDE, for instancee, Spyder in Anaconda, or Visual Studio Code



## Validation tests for the future: 
- We could consider adding a summary of the data, count of columns, count of rows, average or sum of the float values (Cost Per Clicks) before and after transformation
- We could come up with a set of rules of what errors we have received in the past when we get these files. 
For instance, are there specific campaign IDs to look for and expect each time? 
-  Should there be a set number of characters for each columnn, as in a max number of characters a column can contain? For instance phone number should be 7 digits. 

