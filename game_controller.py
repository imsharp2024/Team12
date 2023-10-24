import pygame

class GameController:
    def __init__(self, player_entry_screen):
        self.player_entry_screen = player_entry_screen

    def handle_key_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                self.player_entry_screen.move_to_next_entry()
            elif event.key == pygame.K_RETURN:
                self.player_entry_screen.switch_team()
            elif event.key == pygame.K_F5:
                self.player_entry_screen.start_game()
            elif event.key == pygame.K_F12:
                self.player_entry_screen.clear_all_entries()
            elif event.key == pygame.K_BACKSPACE:
                self.player_entry_screen.handle_backspace()
            elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                self.player_entry_screen.handle_enter()
            elif event.key == pygame.K_ESCAPE:
                self.player_entry_screen.handle_escape()
            elif event.key == pygame.K_DELETE:
                self.player_entry_screen.handle_delete()
            elif event.key == pygame.K_UP:
                self.player_entry_screen.move_cursor_up()
            elif event.key == pygame.K_DOWN:
                self.player_entry_screen.move_cursor_down()
            elif event.key == pygame.K_LEFT:
                self.player_entry_screen.move_cursor_left()
            elif event.key == pygame.K_RIGHT:
                self.player_entry_screen.move_cursor_right()
            elif event.key == pygame.K_KP0 or (event.key >= pygame.K_1 and event.key <= pygame.K_9):
                self.player_entry_screen.handle_keypress(event)

    def handle_typing(self, event):
        if event.type == pygame.KEYDOWN and event.key != pygame.K_RETURN:
            self.player_entry_screen.handle_typing(event.unicode)
