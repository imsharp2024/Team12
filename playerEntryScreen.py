# NOT FINISHED - handing off final visual components to Kierson

import supabase
import os
import pygame
import UDP

pygame.init()
API_URL = 'https://igvofczanemojilwsmaw.supabase.co'
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imlndm9mY3phbmVtb2ppbHdzbWF3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTUxNTEzNzksImV4cCI6MjAxMDcyNzM3OX0.n8jZGrDv0A4cxA2BIZrtV2jIXVqIdCEpjLE2PFg1YWQ'
supabase_client = supabase.Client(API_URL, API_KEY)

table_name = 'DatabaseTable'
columns_to_select = ['name']
' '.join(map(str, columns_to_select))

class playerEntry:
    def __init__(self):
        # query to retrieve data from database
        query = supabase_client.from_(table_name).select('*').order('id')
        response = query.execute()
        self.data = response.data
        found = False

    def findOrCreateUser(self, id):
        # retrieves username from database if it exists based on id
        playerID = id

        for row in self.data:
            response = row.get("id")
            if response == int(playerID):
                playerName = row.get("name")
                print("Welcome back " + playerName + "!")
                self.found = True
                break

        # asks user for new username and adds user to databaseq
        if self.found != True:
            newUserName = input("Welcome new user! Please enter a username: ")
            supabase_client.table('DatabaseTable').insert({"id": playerID, "name": newUserName}).execute()


    def udpBroadcast(self):
        # udp broadcasts player entered equipment id
        equipmentID = input("Please enter your equipment ID number: ")
        udpObject = UDP.UDP()
        udpObject.client()



size = (1000, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Entry Terminal')
numPlayers = 0

running = True
while running:

   # Handle events
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False

   # Draw shapes
   pygame.draw.rect(screen, (45,1,0), (200, 50, 300, 510))
   pygame.draw.rect(screen, (1,33,00), (500, 50, 300, 510))
   pygame.draw.rect(screen, (217, 217, 217), (250, 100, 250, 460))
   pygame.draw.rect(screen, (217, 217, 217), (550, 100, 250, 460))

    # Draw horizontal lines
   for i in range(1, 20):
       pygame.draw.line(screen, (45,1,0), (250, i * 23 + 100), (500, i * 23 + 100), 2)
   for i in range(1, 20):
          pygame.draw.line(screen, (1,33,00), (550, i * 23 + 100), (800, i * 23 + 100), 2)
   # Draw vertical line
   pygame.draw.line(screen, (45,1,0), (350, 100), (350, 560), 2)
   pygame.draw.line(screen, (1,33,00), (650, 100), (650, 560), 2)

   pygame.display.flip()

   if numPlayers < 21:
        player = playerEntry()
        id = input("Enter player ID (or 'exit' to quit): ")
        if id.lower() == 'exit':
            break
        else:
            player.findOrCreateUser(id)
            player.udpBroadcast()
            numPlayers += 1

pygame.quit()
