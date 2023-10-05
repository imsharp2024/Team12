import supabase
import os
import pygame

API_URL = 'https://igvofczanemojilwsmaw.supabase.co'
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imlndm9mY3phbmVtb2ppbHdzbWF3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTUxNTEzNzksImV4cCI6MjAxMDcyNzM3OX0.n8jZGrDv0A4cxA2BIZrtV2jIXVqIdCEpjLE2PFg1YWQ'
supabase_client = supabase.Client(API_URL, API_KEY)

# retrieving data from this table in supabase
table_name = 'DatabaseTable'

# columns to recieve data from
columns_to_select = ['name']

' '.join(map(str, columns_to_select))

# query to retrieve data from the table
query = supabase_client.from_(table_name).select('*').order('id')

# execute query and retrieve the data
data, count = supabase_client.table('DatabaseTable').insert({"id": 3, "name": "Joe"}).execute()
data, count = supabase_client.table('DatabaseTable').insert({"id": 5, "name": "Mary"}).execute()
  
response = query.execute()
data = response.data
if data:
    for row in data:
        print(row)
else:
    print("No data found in the table.")



# --- TO IMPLEMENT ---
# class Model():
#     def __init__(self):

# class View():
#     def __init__(self, model):

# class Controller():
#     def __init__(self, model, view):

pygame.init()
# m = Model()
# v = View(m)
# c = Controller(m,v)

# close supabase client at end of code
#supabase_client.close()
