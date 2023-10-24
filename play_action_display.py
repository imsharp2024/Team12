import pygame
import supabase

class PlayActionDisplay:
    def __init__(self, screen, player_name, player_health, player_ammo, game_time, player_team):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.player_name = player_name
        self.player_health = player_health
        self.player_ammo = player_ammo
        self.game_time = game_time
        self.player_team = player_team

    def update_display(self, player_name, player_health, player_ammo, game_time, player_team):
        # Update player information
        self.player_name = player_name
        self.player_health = player_health
        self.player_ammo = player_ammo
        self.game_time = game_time
        self.player_team = player_team

    def render(self):
        self.screen.fill((0, 0, 0))  # Clear the screen

        # Display player information
        player_info = f"Name: {self.player_name} | Health: {self.player_health} | Ammo: {self.player_ammo}"
        team_info = f"Team: {self.player_team}"
        game_time_info = f"Game Time: {self.game_time}"

        text = self.font.render(player_info, True, (255, 255, 255))
        text_rect = text.get_rect(topleft=(10, 10))
        self.screen.blit(text, text_rect)

        text = self.font.render(team_info, True, (255, 255, 255))
        text_rect = text.get_rect(topleft=(10, 50))
        self.screen.blit(text, text_rect)

        text = self.font.render(game_time_info, True, (255, 255, 255))
        text_rect = text.get_rect(topleft=(10, 90))
        self.screen.blit(text, text_rect)
