import supabase
import pygame

API_URL = 'https://igvofczanemojilwsmaw.supabase.co'
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imlndm9mY3phbmVtb2ppbHdzbWF3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTUxNTEzNzksImV4cCI6MjAxMDcyNzM3OX0.n8jZGrDv0A4cxA2BIZrtV2jIXVqIdCEpjLE2PFg1YWQ'
supabase_client = supabase.Client(API_URL, API_KEY)

# retrieving data from this table in supabase
table_name = 'DatabaseTable'

# columns to recieve data from
columns_to_select = ['id', 'name']

# query to retrieve data from the table
query = supabase_client.from_(table_name).select(columns_to_select).order('id', ascending=False)

# execute query and retrieve the data
response = query.execute()

# check if query was successful
if response.status_code == 20:
    data = response.content['data']

    if data:
        for row in data:
            print(row)
    else:
        print("No data found in the table.")
else:
    print(f"Error: {response.status_code}, {response.error}")



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