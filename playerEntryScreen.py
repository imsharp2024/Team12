import supabase
import os
import pygame
import sys
import time
import UDP
from play_action_display import PlayActionDisplay

pygame.init()
API_URL = 'https://igvofczanemojilwsmaw.supabase.co'
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imlndm9mY3phbmVtb2ppbHdzbWF3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTUxNTEzNzksImV4cCI6MjAxMDcyNzM3OX0.n8jZGrDv0A4cxA2BIZrtV2jIXVqIdCEpjLE2PFg1YWQ'
supabase_client = supabase.Client(API_URL, API_KEY)

table_name = 'DatabaseTable'
columns_to_select = ['name']
' '.join(map(str, columns_to_select))

class playerEntryScreen:
    def __init__(self, screen):
        # query to retrieve data from database
        query = supabase_client.from_(table_name).select('*').order('id')
        response = query.execute()
        self.data = response.data
        self.screen = screen
        self.redPlayers = [{"name": "", "id": ""} for i in range(20)]
        self.greenPlayers = [{"name": "", "id": ""} for i in range(20)]
        self.current_team = "RED"
        self.current_entry_index = 0
        self.current_entry_type = "name"

    # retrieves username from database if it exists based on id
    def findOrCreateUser(self):
        found = False
        if self.current_team == "RED":
            name = self.redPlayers[self.current_entry_index]["name"]
            id = self.redPlayers[self.current_entry_index]["id"]
            print(name, id)
        elif self.current_team == "GREEN":
            name = self.greenPlayers[self.current_entry_index]["name"]
            id = self.greenPlayers[self.current_entry_index]["id"]

        try:
            for row in self.data:
               response = row.get("id")
               if response == int(id):
                  name = row.get("name")
                  print("Welcome back " + name + "!")
                  found = True
                  break
            if found != True:
                  print("Welcome new player!")
                  supabase_client.table('DatabaseTable').insert({"id": id, "name": name}).execute()
        except:
            print("Invalid ID number")

    # udp broadcasts player entered equipment id
    def udpBroadcast(self, id):
        udpObject = UDP.UDP()
        udpObject.client()


   # Delete all players
    def deleteAllPlayers(self):
      self.redPlayers = [{"name": "", "id": ""} for i in range(20)]
      self.greenPlayers = [{"name": "", "id": ""} for i in range(20)]

    def move_to_next_entry(self):
        if self.current_entry_type == "name":
            self.current_entry_type = "id"
        else:
            self.current_entry_index = (self.current_entry_index + 1) % 20
            self.current_entry_type = "name"

    def start_game(self):
        print("start game")
        self.play_action_display = PlayActionDisplay(self.screen, self.redPlayers, self.greenPlayers, 0, 0)
        running = True
        while running:
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                  running = False
               elif event.type == pygame.KEYDOWN:
                  running = False
            self.play_action_display.render()
            pygame.display.flip()

   # Handle key events
    def keyEvents(self, event):
      if event.key == pygame.K_TAB:
         if self.current_entry_type == "id":
            self.findOrCreateUser()
         self.move_to_next_entry()
         #print(self.current_entry_index, " ", self.current_team)
      elif event.key == pygame.K_RETURN:
         self.current_entry_index = 0
         self.current_entry_type = "name"
         if self.current_team == "RED":
            self.current_team = "GREEN" 
         else:
            self.current_team = "RED"
         #print(self.current_entry_index, " ", self.current_team)
      elif event.key == pygame.K_F5:
         self.start_game()
      elif event.key == pygame.K_F12:
         self.deleteAllPlayers()
      elif event.type == pygame.KEYDOWN:
         if event.unicode.isprintable() and self.current_entry_index < 16:
            if self.current_team == "RED":
               if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                  #print("DELETE")
                  if self.current_entry_type == "name":
                     self.redPlayers[self.current_entry_index]["name"] = self.redPlayers[self.current_entry_index]["name"][:-1]
                  else:
                     self.redPlayers[self.current_entry_index]["id"] = self.redPlayers[self.current_entry_index]["id"][:-1]
               else:
                  if self.current_entry_type == "name":
                     self.redPlayers[self.current_entry_index]["name"] += event.unicode
                  else:
                     self.redPlayers[self.current_entry_index]["id"] += event.unicode
            else:
               if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                  if self.current_entry_type == "name":
                     self.greenPlayers[self.current_entry_index]["name"] = self.greenPlayers[self.current_entry_index]["name"][:-1]
                  else:
                     self.greenPlayers[self.current_entry_index]["id"] = self.greenPlayers[self.current_entry_index]["id"][:-1]
               else:
                  if self.current_entry_type == "name":
                     self.greenPlayers[self.current_entry_index]["name"] += event.unicode
                  else:
                     self.greenPlayers[self.current_entry_index]["id"] += event.unicode

    # Draw elements to screen
    def drawScreen(self):
      self.screen.fill((0, 0, 0))
      # Draw rectangles
      pygame.draw.rect(self.screen, (45,1,0), (200, 50, 300, 510))
      pygame.draw.rect(self.screen, (1,33,00), (500, 50, 300, 510))
      pygame.draw.rect(self.screen, (217, 217, 217), (250, 100, 250, 460))
      pygame.draw.rect(self.screen, (217, 217, 217), (550, 100, 250, 460))
      pygame.draw.rect(self.screen, (100, 100, 100), (380, 560, 250, 25))

      # Draw horizontal lines
      for i in range(1, 20):
         pygame.draw.line(self.screen, (45,1,0), (250, i * 23 + 100), (500, i * 23 + 100), 2)
      for i in range(1, 20):
         pygame.draw.line(self.screen, (1,33,00), (550, i * 23 + 100), (800, i * 23 + 100), 2)
      
      # Draw vertical line
      pygame.draw.line(self.screen, (45,1,0), (350, 100), (350, 560), 2)
      pygame.draw.line(self.screen, (1,33,00), (650, 100), (650, 560), 2)

      # Draw words and check boxes
      font = pygame.font.Font('freesansbold.ttf', 32)
      text = font.render('Edit Current Screen', True, (119, 119, 254))
      self.screen.blit(text, (350, 10))

      font = pygame.font.Font(None, 32)
      text = font.render('»', True, (217, 217, 217))
      self.screen.blit(text, (210, 99))

      font = pygame.font.Font(None, 25)
      text = font.render('RED TEAM', True, (217, 217, 217))
      self.screen.blit(text, (300, 70))
      pygame.draw.rect(self.screen, (217, 217, 217), pygame.Rect(295, 60, 150, 35), 1)

      text = font.render('GREEN TEAM', True, (217, 217, 217))
      self.screen.blit(text, (600, 70))
      pygame.draw.rect(self.screen, (217, 217, 217), pygame.Rect(595, 60, 150, 35), 1)

      font = pygame.font.Font(None, 20)
      text = font.render('Game Mode: Standard public mode', True, (217, 217, 217))
      self.screen.blit(text, (390, 565))

      font = pygame.font.Font(None, 15)
      for i in range(0,20):
         # Red Team
         text = font.render(str(i), True, (217, 217, 217))
         pygame.draw.rect(self.screen, (217, 217, 217), pygame.Rect(223, i * 23 + 105, 12, 12), 1)
         entry_text = font.render(self.redPlayers[i]["name"], True, (0, 0, 0))
         entry_rect = entry_text.get_rect(topleft=(255, i * 23 + 105))
         self.screen.blit(entry_text, entry_rect)
         self.screen.blit(text, (237, i * 23 + 107))

         entry_text = font.render(self.redPlayers[i]["id"], True, (0, 0, 0))
         entry_rect = entry_text.get_rect(topleft=(355, i * 23 + 105))
         self.screen.blit(entry_text, entry_rect)

         # Green Team
         pygame.draw.rect(self.screen, (217, 217, 217), pygame.Rect(523, i * 23 + 105, 12, 12), 1)
         entry_text = font.render(self.greenPlayers[i]["name"], True, (0, 0, 0))
         entry_rect = entry_text.get_rect(topleft=(555, i * 23 + 105))
         self.screen.blit(entry_text, entry_rect)
         self.screen.blit(text, (537, i * 23 + 107))

         entry_text = font.render(self.greenPlayers[i]["id"], True, (0, 0, 0))
         entry_rect = entry_text.get_rect(topleft=((655, i * 23 + 105)))
         self.screen.blit(entry_text, entry_rect)

      # Draw F key boxes
      font = pygame.font.Font(None, 25)
      for i in range(0,12):
         if i not in [3,5,8,10]:
            text = font.render('F'+str(i+1), True, (48, 245, 49))
            self.screen.blit(text, (i*83+30, 620))
            pygame.draw.rect(self.screen, (217, 217, 217), pygame.Rect(i*83, 590, 83, 110), 1)
            if i == 11:
               text = font.render("Clear", True, (48, 245, 49))
               self.screen.blit(text, (i*83+20, 645))
               text = font.render("Game", True, (48, 245, 49))
               self.screen.blit(text, (i*83+20, 660))
            elif i == 4:
               text = font.render("Start", True, (48, 245, 49))
               self.screen.blit(text, (i*83+20, 645))
               text = font.render("Game", True, (48, 245, 49))
               self.screen.blit(text, (i*83+20, 660))

