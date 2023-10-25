import pygame
from play_action_display import PlayActionDisplay

class PlayerEntryScreen:
    def __init__(self, screen):
        self.screen = screen
        self.red_players = [{"name": "", "id": ""} for _ in range(15)]
        self.green_players = [{"name": "", "id": ""} for _ in range(15)]
        self.current_team = "RED"
        self.current_entry_index = 0
        self.current_entry_type = "name"
        self.play_action_display = None

    def draw_screen(self):
        if self.play_action_display is None:
            self.screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 36)
            label_text = font.render("Photon Laser Tag", True, (0, 0, 255))
            label_rect = label_text.get_rect(center=(self.screen.get_width() // 2, 30))
            self.screen.blit(label_text, label_rect)

            entry_font = pygame.font.Font(None, 28)
            entry_box_size = (120, 30)
            team_column_width = entry_box_size[0] * 2 + 10
            team_column_height = 15 * 40

            # Red Team Label
            red_team_label = entry_font.render("Red Team", True, (255, 0, 0))
            red_team_rect = red_team_label.get_rect(center=(self.screen.get_width() // 4, 40))
            self.screen.blit(red_team_label, red_team_rect)

            # Green Team Label
            green_team_label = entry_font.render("Green Team", True, (0, 255, 0))
            green_team_rect = green_team_label.get_rect(center=(3 * self.screen.get_width() // 4, 40))
            self.screen.blit(green_team_label, green_team_rect)

            # Drawing red and green teams
            red_team_x = (self.screen.get_width() // 4) - (team_column_width // 2)
            red_team_y = 70
            for i in range(15):
                pygame.draw.rect(self.screen, (255, 0, 0), (red_team_x, red_team_y + i * 40, entry_box_size[0], entry_box_size[1]), 2)
                entry_text = entry_font.render(self.red_players[i]["name"], True, (255, 0, 0))
                entry_rect = entry_text.get_rect(topleft=(red_team_x + 10, red_team_y + i * 40))
                self.screen.blit(entry_text, entry_rect)

                pygame.draw.rect(self.screen, (255, 0, 0), (red_team_x + entry_box_size[0], red_team_y + i * 40, entry_box_size[0], entry_box_size[1]), 2)
                entry_text = entry_font.render(self.red_players[i]["id"], True, (255, 0, 0))
                entry_rect = entry_text.get_rect(topleft=(red_team_x + 20 + entry_box_size[0], red_team_y + i * 40))
                self.screen.blit(entry_text, entry_rect)

            green_team_x = (3 * self.screen.get_width() // 4) - (team_column_width // 2)
            green_team_y = 70
            for i in range(15):
                pygame.draw.rect(self.screen, (0, 255, 0), (green_team_x, green_team_y + i * 40, entry_box_size[0], entry_box_size[1]), 2)
                entry_text = entry_font.render(self.green_players[i]["name"], True, (0, 255, 0))
                entry_rect = entry_text.get_rect(topleft=(green_team_x + 10, green_team_y + i * 40))
                self.screen.blit(entry_text, entry_rect)

                pygame.draw.rect(self.screen, (0, 255, 0), (green_team_x + entry_box_size[0], green_team_y + i * 40, entry_box_size[0], entry_box_size[1]), 2)
                entry_text = entry_font.render(self.green_players[i]["id"], True, (0, 255, 0))
                entry_rect = entry_text.get_rect(topleft=(green_team_x + 20 + entry_box_size[0], green_team_y + i * 40))
                self.screen.blit(entry_text, entry_rect)

            controls_text = font.render("Tab = Next Entry | Enter = Switch Team | F5 = Start Game | F12 = Clear All Entries",
                                        True, (255, 255, 255))
            controls_rect = controls_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() - 20))
            self.screen.blit(controls_text, controls_rect)
        else:
            self.play_action_display.render()

    def move_to_next_entry(self):
        if self.current_entry_type == "name":
            self.current_entry_type = "id"
        else:
            self.current_entry_index = (self.current_entry_index + 1) % 15
            self.current_entry_type = "name"

    def switch_team(self):
        if self.current_team == "RED":
            for i in range(15):
                if not self.green_players[i]["name"] and not self.green_players[i]["id"]:
                    self.current_team = "GREEN"
                    self.current_entry_index = i
                    return
        elif self.current_team == "GREEN":
            for i in range(15):
                if not self.red_players[i]["name"] and not self.red_players[i]["id"]:
                    self.current_team = "RED"
                    self.current_entry_index = i
                    return

    def start_game(self):
        self.play_action_display = PlayActionDisplay(self.screen, self.red_players, self.green_players, 0, 0)

    def handle_key_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                # Gather player info based on the current team
                if self.current_team == "RED":
                    player_info = {
                        "name": self.red_players[self.current_entry_index]["name"],
                        "id": self.red_players[self.current_entry_index]["id"]
                    }
                else:
                    player_info = {
                        "name": self.green_players[self.current_entry_index]["name"],
                        "id": self.green_players[self.current_entry_index]["id"]
                    }

                # Call the add_player method to add the player
                self.add_player(player_info)

                # Move to the next entry
                self.move_to_next_entry()
                
            elif event.key == pygame.K_RETURN:
                self.switch_team()
            elif event.key == pygame.K_F5:
                self.start_game()
            elif event.key == pygame.K_F12:
                self.clear_all_entries()
            elif event.key == pygame.K_BACKSPACE:
                if self.current_team == "RED":
                    if self.current_entry_type == "name":
                        self.red_players[self.current_entry_index]["name"] = self.red_players[self.current_entry_index]["name"][:-1]
                    else:
                        self.red_players[self.current_entry_index]["id"] = self.red_players[self.current_entry_index]["id"][:-1]
                else:
                    if self.current_entry_type == "name":
                        self.green_players[self.current_entry_index]["name"] = self.green_players[self.current_entry_index]["name"][:-1]
                    else:
                        self.green_players[self.current_entry_index]["id"] = self.green_players[self.current_entry_index]["id"][:-1]
            elif event.unicode.isprintable() and self.current_entry_index < 15:
                if self.current_team == "RED":
                    if self.current_entry_type == "name":
                        self.red_players[self.current_entry_index]["name"] += event.unicode
                    else:
                        self.red_players[self.current_entry_index]["id"] += event.unicode
                else:
                    if self.current_entry_type == "name":
                        self.green_players[self.current_entry_index]["name"] += event.unicode
                    else:
                        self.green_players[self.current_entry_index]["id"] += event.unicode
                            
    def add_player(self, player_info):
        player_info['score'] = 0

        # player_info contains "name" and "id"
        if self.current_team == "RED":
            if self.current_entry_type == "name":
                self.red_players[self.current_entry_index]["name"] = player_info["name"]
            else:
                self.red_players[self.current_entry_index]["id"] = player_info["id"]
            
            # Initialize the score to 0
            self.red_players[self.current_entry_index].setdefault('score', 0)
        else:
            if self.current_entry_type == "name":
                self.green_players[self.current_entry_index]["name"] = player_info["name"]
            else:
                self.green_players[self.current_entry_index]["id"] = player_info["id"]

            # Initialize the score to 0
            self.green_players[self.current_entry_index].setdefault('score', 0)

# Main entry point for testing
if __name__ == "__main__":
    pygame.init()

    size = (1000, 700)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Photon Laser Tag: Player Entry')

    entry_screen = PlayerEntryScreen(screen)

    while entry_screen.running:
        entry_screen.draw_screen()

        pygame.display.flip()

    pygame.quit()
