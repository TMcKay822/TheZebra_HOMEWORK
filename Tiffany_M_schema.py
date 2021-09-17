#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:43:51 2021

@author: tiffany
"""

#Import packages
import pandas as pd
import pandera
import numpy as np
import os
import datetime
from csv import reader

# Read data 
auto_ins = pd.read_csv('Homework_-_Auto_Insurance.csv')
home_ins = pd.read_csv('Homework_-_Home_Insurance.csv')


#preview data
print(auto_ins.head(10))
print("\n")
print(home_ins.head(10))


output1 = pd.DataFrame()
output1 = pd.concat([home_ins, auto_ins], axis=0, sort=False)
#stacking data together


print(output1)

output1 = output1.reset_index(drop=True)
output1=output1.drop('TestColumn', axis=1)

output1=output1.drop('AccountId', axis=1)

print(output1)

output1['Cost Per Ad Click']=output1['Cost Per Ad Click'].astype(str)
output1['Zipcode'] = output1['Zipcode'].str.replace('"',"")
output1['Cost Per Ad Click'] = output1['Cost Per Ad Click'].str.replace('"',"")
output1['Cost Per Ad Click']=output1['Cost Per Ad Click'].astype(float)



output1['Phone Number']=output1['Phone Number'].astype(str)
output1['Phone Number'] = output1['Phone Number'].str.replace("\.0","")


drop_lst =[]


for i, row in output1.iterrows():
    if sum(row.drop('Phone Number').isnull()) > 0:
        drop_lst.append(i)
        print(i, ':', row.values, 'has been dropped')
        
target_schema = output1.drop(drop_lst)


import pandera as pa

# Defining the schema
schema = pa.DataFrameSchema({
    "Provider Name" : pa.Column(pa.String, nullable=False),
    "CampaignID" : pa.Column(pa.String, nullable=False),
    "Cost Per Ad Click" : pa.Column(pa.Float, nullable=False),
    "Redirect Link" : pa.Column(pa.String, nullable=False),
    "Phone Number" : pa.Column(pa.String, nullable=True),
    "Address" : pa.Column(pa.String, nullable=False),
    "Zipcode" : pa.Column(pa.String, nullable=False),
})


#Testing the validation of the schema
schema.validate(target_schema)

#write the taregt schema to local file
target_schema.to_csv('target_schema.csv')
