import pygame
import time

class PlayActionDisplay:
    def __init__(self, screen, red_team_players, green_team_players, red_team_score, green_team_score):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.red_team_players = red_team_players
        self.green_team_players = green_team_players
        self.red_team_score = red_team_score
        self.green_team_score = green_team_score
        
        # Countdown timer settings
        self.reset_timers()

    def update_display(self, red_team_players, green_team_players, red_team_score, green_team_score):
        # Update player and team information
        self.red_team_players = red_team_players
        self.green_team_players = green_team_players

        # Ensure 'score' key is present and initialize to 0
        for player in self.red_team_players:
            player.setdefault('score', 0)

        for player in self.green_team_players:
            player.setdefault('score', 0)

        self.red_team_score = red_team_score
        self.green_team_score = green_team_score

    def reset_timers(self):
        self.start_time = time.time()
        self.timer_duration_short = 30  # 30 seconds
        self.timer_duration_long = 6 * 60  # 6 minutes
        self.is_initial_countdown = True

    def update_timer(self):
        elapsed_time = time.time() - self.start_time

        if self.is_initial_countdown:
            remaining_time = max(0, self.timer_duration_short - elapsed_time)
        else:
            remaining_time = max(0, self.timer_duration_long - elapsed_time)

        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)

        time_string = f"{minutes:02}:{seconds:02}"

        if remaining_time == 0 and self.is_initial_countdown:
            # Initial countdown has ended, switch to the long countdown
            self.is_initial_countdown = False
            self.start_time = time.time()  # Reset start time for the long countdown

        return time_string

    def render(self):
        self.screen.fill((0, 0, 0))  # Clear the screen

        # Display team labels
        red_team_label = self.font.render("Red Team", True, (255, 0, 0))
        red_team_rect = red_team_label.get_rect(topleft=(10, 10))
        self.screen.blit(red_team_label, red_team_rect)

        green_team_label = self.font.render("Green Team", True, (0, 255, 0))
        green_team_rect = green_team_label.get_rect(topleft=(self.screen.get_width() // 2 + 10, 10))
        self.screen.blit(green_team_label, green_team_rect)

        # Display top three players and scores for Red Team
        for i in range(min(3, len(self.red_team_players))):
            if 'score' in self.red_team_players[i]:
                player_info = f"{self.red_team_players[i]['name']} - Score: {self.red_team_players[i]['score']}"
            else:
                player_info = f"{self.red_team_players[i]['name']} - Score: N/A"
            text = self.font.render(player_info, True, (255, 0, 0))
            text_rect = text.get_rect(topleft=(10, 50 + i * 40))
            self.screen.blit(text, text_rect)

        # Display top three players and scores for Green Team
        for i in range(min(3, len(self.green_team_players))):
            if 'score' in self.green_team_players[i]:
                player_info = f"{self.green_team_players[i]['name']} - Score: {self.green_team_players[i]['score']}"
            else:
                player_info = f"{self.green_team_players[i]['name']} - Score: N/A"
            text = self.font.render(player_info, True, (0, 255, 0))
            text_rect = text.get_rect(topleft=(self.screen.get_width() // 2 + 10, 50 + i * 40))
            self.screen.blit(text, text_rect)

        # Display cumulative team scores
        red_team_score_info = f"Team Score: {self.red_team_score}"
        text = self.font.render(red_team_score_info, True, (255, 0, 0))
        text_rect = text.get_rect(topleft=(10, 220))
        self.screen.blit(text, text_rect)

        green_team_score_info = f"Team Score: {self.green_team_score}"
        text = self.font.render(green_team_score_info, True, (0, 255, 0))
        text_rect = text.get_rect(topleft=(self.screen.get_width() // 2 + 10, 220))
        self.screen.blit(text, text_rect)

        # Add "No Events Yet" text under team scores as a placeholder
        smaller_font = pygame.font.Font(None, 24)
        events_text = smaller_font.render("No Events Yet", True, (255, 255, 255))
        events_rect = events_text.get_rect(topleft=(10, 260))
        self.screen.blit(events_text, events_rect)
        
        events_text = smaller_font.render("No Events Yet", True, (255, 255, 255))
        events_rect = events_text.get_rect(topleft=(510, 260))
        self.screen.blit(events_text, events_rect)

        # Display the countdown timer in the top right corner
        if self.is_initial_countdown:
            timer_label_text = self.font.render("Warning! Starting in:", True, (255, 255, 255))
        else:
            timer_label_text = self.font.render("Timer:", True, (255, 255, 255))
        timer_label_rect = timer_label_text.get_rect(topright=(self.screen.get_width() - 90, 10))
        self.screen.blit(timer_label_text, timer_label_rect)

        timer_text = self.font.render(self.update_timer(), True, (255, 255, 255))
        timer_rect = timer_text.get_rect(topright=(self.screen.get_width() - 10, 10))
        self.screen.blit(timer_text, timer_rect)
