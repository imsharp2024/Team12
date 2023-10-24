import pygame

class PlayerEntryScreen:
    def __init__(self, screen):
        self.screen = screen
        self.red_players = [{"name": "", "id": ""} for _ in range(15)]
        self.green_players = [{"name": "", "id": ""} for _ in range(15)]
        self.current_team = "RED"
        self.current_entry_index = 0
        self.current_entry_type = "name"

    def draw_screen(self):
        self.screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 36)
        label_text = font.render("Photon Laser Tag: Player Entry", True, (0, 0, 255))
        label_rect = label_text.get_rect(center=(self.screen.get_width() // 2, 30))
        self.screen.blit(label_text, label_rect)

        timer_text = font.render("Game Timer", True, (255, 255, 255))
        timer_rect = timer_text.get_rect(midtop=(self.screen.get_width() // 2, 60))
        self.screen.blit(timer_text, timer_rect)

        score_text = font.render("Score: 100", True, (255, 255, 255))
        score_rect_red = score_text.get_rect(midtop=(self.screen.get_width() // 4, 90))
        score_rect_green = score_text.get_rect(midtop=(3 * self.screen.get_width() // 4, 90))
        self.screen.blit(score_text, score_rect_red)
        self.screen.blit(score_text, score_rect_green)

        entry_font = pygame.font.Font(None, 28)
        entry_box_size = (120, 30)

        for i in range(15):
            # Red Team
            pygame.draw.rect(self.screen, (255, 0, 0), (20, 130 + i * 40, entry_box_size[0], entry_box_size[1]), 2)
            entry_text = entry_font.render(self.red_players[i]["name"], True, (255, 0, 0))
            entry_rect = entry_text.get_rect(topleft=(30, 130 + i * 40))
            self.screen.blit(entry_text, entry_rect)

            pygame.draw.rect(self.screen, (255, 0, 0), (20 + entry_box_size[0], 130 + i * 40, entry_box_size[0], entry_box_size[1]), 2)
            entry_text = entry_font.render(self.red_players[i]["id"], True, (255, 0, 0))
            entry_rect = entry_text.get_rect(topleft=(30 + entry_box_size[0], 130 + i * 40))
            self.screen.blit(entry_text, entry_rect)

            # Green Team
            pygame.draw.rect(self.screen, (0, 255, 0), (self.screen.get_width() // 2 + 10, 130 + i * 40, entry_box_size[0], entry_box_size[1]), 2)
            entry_text = entry_font.render(self.green_players[i]["name"], True, (0, 255, 0))
            entry_rect = entry_text.get_rect(topleft=(self.screen.get_width() // 2 + 20, 130 + i * 40))
            self.screen.blit(entry_text, entry_rect)

            pygame.draw.rect(self.screen, (0, 255, 0), (self.screen.get_width() // 2 + 10 + entry_box_size[0], 130 + i * 40, entry_box_size[0], entry_box_size[1]), 2)
            entry_text = entry_font.render(self.green_players[i]["id"], True, (0, 255, 0))
            entry_rect = entry_text.get_rect(topleft=(self.screen.get_width() // 2 + 20 + entry_box_size[0], 130 + i * 40))
            self.screen.blit(entry_text, entry_rect)

        controls_text = font.render("Tab = Next Entry | Enter = Switch Team | F5 = Start Game | F12 = Clear All Entries",
                                    True, (255, 255, 255))
        controls_rect = controls_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() - 20))
        self.screen.blit(controls_text, controls_rect)

    def move_to_next_entry(self):
        if self.current_entry_type == "name":
            self.current_entry_type = "id"
        else:
            self.current_entry_index = (self.current_entry_index + 1) % 15
            self.current_entry_type = "name"

    def switch_team(self):
        self.current_team = "GREEN" if self.current_team == "RED" else "RED"

    def start_game(self):
        pass

    def clear_all_entries(self):
        self.red_players = [{"name": "", "id": ""} for _ in range(15)]
        self.green_players = [{"name": "", "id": ""} for _ in range(15)]

    def handle_key_event(self, event):
        if event.key == pygame.K_TAB:
            self.move_to_next_entry()
        elif event.key == pygame.K_RETURN:
            self.switch_team()
        elif event.key == pygame.K_F5:
            self.start_game()
        elif event.key == pygame.K_F12:
            self.clear_all_entries()
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isprintable() and self.current_entry_index < 15:
                if self.current_team == "RED":
                    if event.key == pygame.K_BACKSPACE:
                        if self.current_entry_type == "name":
                            self.red_players[self.current_entry_index]["name"] = self.red_players[self.current_entry_index]["name"][:-1]
                        else:
                            self.red_players[self.current_entry_index]["id"] = self.red_players[self.current_entry_index]["id"][:-1]
                    else:
                        if self.current_entry_type == "name":
                            self.red_players[self.current_entry_index]["name"] += event.unicode
                        else:
                            self.red_players[self.current_entry_index]["id"] += event.unicode
                else:
                    if event.key == pygame.K_BACKSPACE:
                        if self.current_entry_type == "name":
                            self.green_players[self.current_entry_index]["name"] = self.green_players[self.current_entry_index]["name"][:-1]
                        else:
                            self.green_players[self.current_entry_index]["id"] = self.green_players[self.current_entry_index]["id"][:-1]
                    else:
                        if self.current_entry_type == "name":
                            self.green_players[self.current_entry_index]["name"] += event.unicode
                        else:
                            self.green_players[self.current_entry_index]["id"] += event.unicode

# Main entry point for testing
if __name__ == "__main__":
    pygame.init()

    size = (1000, 700)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Photon Laser Tag: Player Entry')

    entry_screen = PlayerEntryScreen(screen)

    running = True
    while running:
        entry_screen.draw_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                entry_screen.handle_key_event(event)

        pygame.display.flip()

    pygame.quit()
