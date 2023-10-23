import supabase
import os
import pygame
import sys
import time
import UDP

pygame.init()
API_URL = 'https://igvofczanemojilwsmaw.supabase.co'
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imlndm9mY3phbmVtb2ppbHdzbWF3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTUxNTEzNzksImV4cCI6MjAxMDcyNzM3OX0.n8jZGrDv0A4cxA2BIZrtV2jIXVqIdCEpjLE2PFg1YWQ'
supabase_client = supabase.Client(API_URL, API_KEY)

table_name = 'DatabaseTable'
columns_to_select = ['name']
' '.join(map(str, columns_to_select))

# ------------------------------------------------------------------------------------------------
# Enter player info
# ------------------------------------------------------------------------------------------------
class playerEntry:
    def __init__(self):
        # query to retrieve data from database
        query = supabase_client.from_(table_name).select('*').order('id')
        response = query.execute()
        self.data = response.data

    # retrieves username from database if it exists based on id
    def findOrCreateUser(self, id):
        playerID = id
        found = False

        for row in self.data:
            response = row.get("id")
            if response == int(playerID):
                playerName = row.get("name")
                print("Welcome back " + playerName + "!")
                found = True
                return playerName
                break
        # asks user for new username and adds user to databaseq
        if found != True:
            newUserName = input("Welcome new user! Please enter a username: ")
            supabase_client.table('DatabaseTable').insert({"id": playerID, "name": newUserName}).execute()
            return newUserName

    # udp broadcasts player entered equipment id
    def udpBroadcast(self):
        equipmentID = input("Please enter your equipment ID number: ")
        udpObject = UDP.UDP()
        udpObject.client()

# ------------------------------------------------------------------------------------------------
# Draw elements to screen
# ------------------------------------------------------------------------------------------------
class drawPlayerEntryScreen:
   def __init__(self,screen):
      self.redPlayers = []
      self.greenPlayers = []

      # Draw rectangles
      pygame.draw.rect(screen, (45,1,0), (200, 50, 300, 510))
      pygame.draw.rect(screen, (1,33,00), (500, 50, 300, 510))
      pygame.draw.rect(screen, (217, 217, 217), (250, 100, 250, 460))
      pygame.draw.rect(screen, (217, 217, 217), (550, 100, 250, 460))
      pygame.draw.rect(screen, (100, 100, 100), (380, 560, 250, 25))

      # Draw horizontal lines
      for i in range(1, 20):
         pygame.draw.line(screen, (45,1,0), (250, i * 23 + 100), (500, i * 23 + 100), 2)
      for i in range(1, 20):
         pygame.draw.line(screen, (1,33,00), (550, i * 23 + 100), (800, i * 23 + 100), 2)
      
      # Draw vertical line
      pygame.draw.line(screen, (45,1,0), (350, 100), (350, 560), 2)
      pygame.draw.line(screen, (1,33,00), (650, 100), (650, 560), 2)

      # Draw words and check boxes
      font = pygame.font.Font('freesansbold.ttf', 32)
      text = font.render('Edit Current Screen', True, (119, 119, 254))
      screen.blit(text, (350, 10))

      font = pygame.font.Font(None, 32)
      text = font.render('»', True, (217, 217, 217))
      screen.blit(text, (210, 99))

      font = pygame.font.Font(None, 25)
      text = font.render('RED TEAM', True, (217, 217, 217))
      screen.blit(text, (300, 70))
      pygame.draw.rect(screen, (217, 217, 217), pygame.Rect(295, 60, 150, 35), 1)

      text = font.render('GREEN TEAM', True, (217, 217, 217))
      screen.blit(text, (600, 70))
      pygame.draw.rect(screen, (217, 217, 217), pygame.Rect(595, 60, 150, 35), 1)

      font = pygame.font.Font(None, 20)
      text = font.render('Game Mode: Standard public mode', True, (217, 217, 217))
      screen.blit(text, (390, 565))

      font = pygame.font.Font(None, 15)
      for i in range(0,20):
         text = font.render(str(i), True, (217, 217, 217))
         pygame.draw.rect(screen, (217, 217, 217), pygame.Rect(223, i * 23 + 105, 12, 12), 1)
         screen.blit(text, (237, i * 23 + 107))
         pygame.draw.rect(screen, (217, 217, 217), pygame.Rect(523, i * 23 + 105, 12, 12), 1)
         screen.blit(text, (537, i * 23 + 107))

      # Draw F key boxes
      font = pygame.font.Font(None, 25)
      for i in range(0,12):
         if i not in [3,5,8,10]:
            text = font.render('F'+str(i), True, (48, 245, 49))
            screen.blit(text, (i*83+30, 620))
            pygame.draw.rect(screen, (217, 217, 217), pygame.Rect(i*83, 590, 83, 110), 1)

      # Write RED player names on screen 
      for i in range(len(self.redPlayers)):
         text = font.render(self.redPlayers[i], True, (119, 119, 254))
         screen.blit(text, (237, i * 23 + 107))

      # Write GREEN player names on screen
      for i in range(len(self.greenPlayers)):
         text = font.render(self.redPlayers[i], True, (119, 119, 254))
         screen.blit(text, (537, i * 23 + 107))

   # Add player to a list
   def addPlayer(self, name, color):
      if color.upper == "RED":
         self.redPlayers.append(name)
      else:
         self.greenPlayers.append(name)
      
   # Delete a player from a list
   def deletePlayer(self, name, color):
      if color.upper == 'RED':
         for i in self.redPlayers:
            if self.redPlayers[i] == name:
               self.redPlayers.remove(i)
      else:
         for i in self.greenPlayers:
            if self.greenPlayers[i] == name:
               self.greenPlayers.remove(i)

   # Delete all players from list both lists
   def deleteAllPlayers(self):
      self.redPlayers.clear()
      self.greenPlayers.clear()


# ------------------------------------------------------------------------------------------------
# Load splash screen
# ------------------------------------------------------------------------------------------------

# Screen dimensions
size = (1000, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Entry Terminal')

# Upload image
try:
    image = pygame.image.load("splashscreen Large.jpg")
    image = pygame.transform.scale(image, size)
except pygame.error as e:
    print("Error loading image:", e)
    sys.exit()

# Set the start time
start_time = time.time()

# Show screen for 3 seconds
running = True
while running:
   # Handle events
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False

   # Calculate the elapsed time
   elapsed_time = time.time() - start_time

   # Display the image for DISPLAY_TIME seconds
   if elapsed_time < 3:
        screen.blit(image, (0, 0))
   else:
        running = False
   pygame.display.flip()

# ------------------------------------------------------------------------------------------------
# Main loop
# ------------------------------------------------------------------------------------------------
numRedPlayers = 0
numGreenPlayers = 0

running = True
while running:
   screen.fill((0, 0, 0))

   # draw player entry screen
   entryScreen = drawPlayerEntryScreen(screen)

   # Handle events
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      # Check for the F12 key press
      if event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
         entryScreen.deleteAllPlayers()

   pygame.display.flip()

   teamColor = input("Would you like to enter players for the RED team or GREEN team (or enter 'exit' to quit)? ")

   # Enter RED players
   if teamColor.upper() == 'RED':
      while True:
         if numRedPlayers < 21:
            player = playerEntry()
            id = input("Enter player ID for RED team (or 'exit' to quit): ")
            if id.lower() == 'exit':
               break
            else:
               playerName = player.findOrCreateUser(id)
               player.udpBroadcast()
               numRedPlayers += 1
               entryScreen.addPlayer(playerName, teamColor)

   # Enter GREEN players
   elif teamColor.upper() == 'GREEN':
      while True:
         if numGreenPlayers < 21:
            player = playerEntry()
            id = input("Enter player ID for GREEN team (or 'exit' to quit): ")
            if id.lower() == 'exit':
               break
            else:
               playerName = player.findOrCreateUser(id)
               player.udpBroadcast()
               numGreenPlayers += 1
               entryScreen.addPlayer(playerName, teamColor)
   else:
      break

pygame.quit()
