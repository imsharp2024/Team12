import pygame
import supabase
import time
from play_action_display import PlayActionDisplay
from player_entry_screen import PlayerEntryScreen
from UDP import UDP

API_URL = 'https://igvofczanemojilwsmaw.supabase.co'
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imlndm9mY3phbmVtb2ppbHdzbWF3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTUxNTEzNzksImV4cCI6MjAxMDcyNzM3OX0.n8jZGrDv0A4cxA2BIZrtV2jIXVqIdCEpjLE2PFg1YWQ'
supabase_client = supabase.Client(API_URL, API_KEY)

# Initialize Pygame
pygame.init()

# Set up screen dimensions
screen_size = (1000, 700)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Laser Tag Game')

# Create an instance of PlayActionDisplay
play_action_display = PlayActionDisplay(screen, 0, 0, 0, 0)

# Initialize UDP object
udp = UDP()

# Display splash screen for 3 seconds
splash_image = pygame.image.load("images/splashscreen_large.jpg")
splash_image = pygame.transform.scale(splash_image, screen_size)
screen.blit(splash_image, (0, 0))
pygame.display.flip()
time.sleep(3)

# Create an instance of PlayerEntryScreen
entry_screen = PlayerEntryScreen(screen)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            entry_screen.handle_key_event(event)

    entry_screen.draw_screen()
    pygame.display.flip()
    pygame.time.delay(10)  # Add a small delay to reduce CPU usage


    entry_screen.draw_screen()
    pygame.display.flip()

# Close supabase client at the end of code
pygame.quit()
