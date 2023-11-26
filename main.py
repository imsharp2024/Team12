import pygame
import supabase
import time
import pygame.mixer
from PlayActionDisplay import PlayActionDisplay
from playerEntryScreen import playerEntryScreen
from UDP import UDP

API_URL = 'https://igvofczanemojilwsmaw.supabase.co'
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imlndm9mY3phbmVtb2ppbHdzbWF3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTUxNTEzNzksImV4cCI6MjAxMDcyNzM3OX0.n8jZGrDv0A4cxA2BIZrtV2jIXVqIdCEpjLE2PFg1YWQ'
supabase_client = supabase.Client(API_URL, API_KEY)

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Set up screen dimensions
size = (1000, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Entry Terminal')

# Create an instance of PlayActionDisplay
play_action_display = PlayActionDisplay(screen, 0, 0, 0, 0)

# Initialize UDP object
udp = UDP()

# load music tracks
music_tracks = ["Track01.mp3", "Track02.mp3", "Track03.mp3", 
                "Track04.mp3", "Track05.mp3", "Track06.mp3", 
                "Track07.mp3", "Track08.mp3"]
# play music
for track in music_tracks:
    pygame.mixer.init()
    pygame.mixer.music.load(track)
    pygame.mixer.music.play(999)
    
# -----------------------------------------------------------------------------------------
# Display splash screen for 3 seconds
# -----------------------------------------------------------------------------------------

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
# -----------------------------------------------------------------------------------------

# Create an instance of PlayerEntryScreen
entryScreen = playerEntryScreen(screen)

# -----------------------------------------------------------------------------------------
# Main game loop
# -----------------------------------------------------------------------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            entryScreen.keyEvents(event)

    entryScreen.drawScreen()
    pygame.display.flip()
    pygame.time.delay(10)  # Add a small delay to reduce CPU usage


    entryScreen.drawScreen()
    pygame.display.flip()

# Close supabase client at the end of code
pygame.quit()
