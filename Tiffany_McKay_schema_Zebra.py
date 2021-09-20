#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:43:51 2021

@author: Tiffany McKay
"""

    
#Import packages
import pandas as pd
import numpy as np


# Read data 
auto_ins = pd.read_csv('Homework_-_Auto_Insurance.csv')
home_ins = pd.read_csv('Homework_-_Home_Insurance.csv')


#Preview data
print(auto_ins.head(10))
print("\n")
print(home_ins.head(10))

#Stacking data together
output1 = pd.DataFrame()
output1 = pd.concat([home_ins, auto_ins], axis=0, sort=False)

#Fixing indices after stacking
output1 = output1.reset_index(drop=True)

#Keeping a untouched copy for testing 
output_not_cleaned = output1

#Check data
print(output1)


#Define functions to clean data 

def drop_column(dataframe, column_to_drop):
    """ Target schema drops the columns TestColumn and AccountId, so this is a function to drop columns that are not in the target  schema."""
    dataframe=dataframe.drop(column_to_drop, axis=1)
    return dataframe


def string_columns(dataframe):
    """ After merging data some columns maintained a float data type, to have a clean format, this function changes every column to a string datatype, to have a consistent data type across all columns, and we will make changes to datatypes that will not be strings later"""
    for column_name in dataframe.columns:
        try:
            dataframe[column_name] = dataframe[column_name].astype(str)
        except:
            pass
    return dataframe


def replace_quotes(dataframe):
    """ Function used to replace any quotation marks found in the data received, that should be a string """
    for column_name in dataframe.columns:
        try:
            dataframe[column_name] = dataframe[column_name].str.replace('"',"")
        except:
            pass
    return dataframe
 
    

def column_to_float(dataframe, column_name):
    """There are some columns that have to be floats, denoted by the target schema, this is a function to convert these columns from strings to float data types."""
    dataframe[column_name]=output1[column_name].astype(float)
    return dataframe
    
    

def string_zerofloat_format(dataframe):
    """ For columns such as Phone Number that were imported as a float, when this column gets converted to a string, it maintains the .0 at the end of the string, this function removes the .0 found at the end of the phone numbers, or any other column that may experience this."""
    for column_name in dataframe.columns:
        try:
            dataframe[column_name] = dataframe[column_name].str.replace("\.0","")
        except:
            pass
    return dataframe

def drop_nulls(dataframe):
    """This function drops any rows in the columns that have a null or nan value other than Phone Number, which is a column allowed to have null values."""
#Creating an empty list to collect the items that should be dropped 
    drop_lst =[]
    for i, row in dataframe.iterrows():
        if sum(row.drop('Phone Number').isnull()) or sum(row.drop('Phone Number')=='nan') > 0:
            drop_lst.append(i)
            print('PLEASE NOTE: index ', i, ':', row.values, 'has been dropped')
    dataframe = dataframe.drop(drop_lst)
    dataframe = dataframe.reset_index(drop=True)
    return dataframe
 
          


#Calling Functions 
output1 = drop_column(output1,'TestColumn')
output1 = drop_column(output1,'AccountId')

output1 = string_columns(output1)
output1 = replace_quotes(output1)

output1 = column_to_float(output1, 'Cost Per Ad Click')
output1 = string_zerofloat_format(output1)
output1 = drop_nulls(output1)


#Check data
print(output1)


#Target Schema DataFrame        
target_schema = output1
target_schema = target_schema.reset_index(drop=True)


#write the taregt schema to local file
target_schema.to_csv('target_schema.csv')


# ------------------- test ------------------------

#Make sure  DO_TEST is True if you want to run tests
DO_TEST = True
if DO_TEST:
    def test_drop_column():
        """This tests to see if the function to drop columns sucessfully dropped the columns that were not in the target schema"""
        df_result_testcolumn = output_not_cleaned
        df_result_accountid = output_not_cleaned
        # call drop_columns
        df_result_testcolumn = drop_column(output_not_cleaned, 'TestColumn')
        df_result_accountid = drop_column(output_not_cleaned, 'AccountId')
        assert 'TestColumn'  not in df_result_testcolumn.columns
        assert 'AccountId' not in df_result_accountid.columns
        print('TEST PASSED, for drop_column')
    
    
    def test_string_columns():
        """This tests to see if the functon to convert the data to stiings successfully converted."""
        df_result_strings= output_not_cleaned
        df_result_strings = string_columns(output_not_cleaned)
        for column_name in df_result_strings.columns:
            assert isinstance(df_result_strings.loc[0, column_name], str)
        print('TEST PASSED, for string_columns')

    
    
    def test_replace_quotes():
        """This tests to see if the function that removed quotes worked and that there are no remaining quotations in the data """
        df_result_quotes = replace_quotes(output_not_cleaned)
        assert '"'  not in df_result_quotes.values
        print('TEST PASSED, for replace_quotes')

     
    
    def test_column_to_float():
        """This tests to see if the column that should be a float is actually a float"""
        df_result_float= output_not_cleaned
        df_result_float = column_to_float(df_result_float, 'Cost Per Ad Click')
        assert isinstance(df_result_float.loc[0, 'Cost Per Ad Click'], float)
        print('TEST PASSED, for column_to_float')
        
        
    
    def test_string_zerofloat_format():
        """This test is to make sure strings that were previously imported as floats do not keep the .0 at the end of the string, this .0 gets added when data types are floats"""
        df_result_zero = output_not_cleaned
        df_result_zero = string_zerofloat_format(output_not_cleaned)
        assert '\.0'  not in df_result_zero.values
        print('TEST PASSED, for string_zerofloat_format')
        
        
    def test_drop_nulls():
        """This tests to see if the the non-nullable columns have their null values dropped. Converting the data to strings changed the null values to "nan" hence the refrences to nan below."""
        df_result_nulls = output1
       #dropping the null values 
        df_result_nulls = drop_nulls(output1)    
        assert "nan" not in df_result_nulls[["Provider Name", "CampaignID", "Cost Per Ad Click", "Redirect Link", "Address", "Zipcode"]].values
        print('TEST PASSED, for drop_nulls')

        
        
#TESTS
    test_drop_column()
    test_string_columns()
    test_replace_quotes()
    test_column_to_float()
    test_string_zerofloat_format()
    test_drop_nulls()
        
else:
    print('No test were ran, file in local drive. If you want to run tests, please change DO_TEST to true!')
        
        