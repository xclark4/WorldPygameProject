import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 700, 600
PLAYER_SIZE = 50
PLAYER_COLOR = (255, 0, 0)  # Red color for the player
BACKGROUND_COLOR = (0, 0, 0)  # Black background
GOAL_COLOR = (0, 255, 0)  # Green color for the goal
WHITE = (255, 255, 255)  # White color for borders
LEVEL_COLOR = (255, 255, 255)  # White color for level text

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("World's Hardest Game")
DRAGONFLY_IMAGE = pygame.image.load("images/dragonfly.png").convert_alpha()
img = pygame.image.load('images/butterfly.png').convert_alpha()
img = pygame.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE))

#Sounds
level_create_sound = pygame.mixer.Sound("sounds/Voicy_Level 3.mp3")
death_sound = pygame.mixer.Sound("sounds/Voicy_Game Over.mp3")

# Define Player class
class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - PLAYER_SIZE
        self.speed = 5

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

        # Boundary checks (within the white borders)
        self.x = max(50, min(WIDTH - 50 - PLAYER_SIZE, self.x))
        self.y = max(50, min(HEIGHT - 50 - PLAYER_SIZE, self.y))

    def draw(self):
        screen.blit(img, (self.x, self.y))

# Define Goal class
class Goal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, GOAL_COLOR, (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE))

# Define Obstacle class (with movement and image)
class Obstacle:
    def __init__(self, x, y, speed, direction='horizontal'):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.width = 50
        self.height = 50

    def move(self):
        if self.direction == 'horizontal':
            self.x += self.speed
            if self.x < 50 or self.x + self.width > WIDTH - 50:
                self.speed = -self.speed
        else:
            self.y += self.speed
            if self.y < 50 or self.y + self.height > HEIGHT - 50:
                self.speed = -self.speed

    def draw(self):
        screen.blit(DRAGONFLY_IMAGE, (self.x, self.y))

# Function to detect collision
def check_collision(player, obstacles):
    for obstacle in obstacles:
        if player.x < obstacle.x + obstacle.width and player.x + PLAYER_SIZE > obstacle.x and player.y < obstacle.y + obstacle.height and player.y + PLAYER_SIZE > obstacle.y:
            return True
    return False

# Function to draw the border (green side display)
def draw_borders():
    pygame.draw.rect(screen, WHITE, (50, 50, WIDTH - 100, HEIGHT - 100), 5)  # White border for the level

# Function to display the level
def display_level(level):
    font = pygame.font.SysFont("Arial", 36)
    text = font.render(f"Level {level}", True, LEVEL_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 20))

# Game loop
def game_loop(level=2):
    player = Player()
    goal = Goal(WIDTH // 2 - PLAYER_SIZE // 2, 50)
    obstacles = [Obstacle(100, 150, 3), Obstacle(300, 250, 2, 'vertical'), Obstacle(500, 350, 4)]
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get user input for movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: #Left
            player.move(-player.speed, 0)
        if keys[pygame.K_d]: #Right
            player.move(player.speed, 0)
        if keys[pygame.K_w]: #Up
            player.move(0, -player.speed)
        if keys[pygame.K_s]: #Down
            player.move(0, player.speed)

        # Move obstacles
        for obstacle in obstacles:
            obstacle.move()

        # Check for collisions with obstacles
        if check_collision(player, obstacles):
            print("Game Over! You hit an obstacle.")
            pygame.time.delay(1000)  # Pause for a second
            break

        # Check if the player reached the goal
        if player.x < goal.x + PLAYER_SIZE and player.x + PLAYER_SIZE > goal.x and player.y < goal.y + PLAYER_SIZE and player.y + PLAYER_SIZE > goal.y:
            print(f"You won! You reached the goal in Level {level}.")
            pygame.time.delay(1000)  # Pause for a second
            break

        # Fill the screen with the background color
        screen.fill(BACKGROUND_COLOR)

        # Draw the borders around the game area
        draw_borders()

        # Display the level
        display_level(level)

        # Draw the player, goal, and obstacles
        player.draw()
        goal.draw()
        for obstacle in obstacles:
            obstacle.draw()

        # Update the display
        pygame.display.update()

        # Cap the frame rate to 60 FPS
        clock.tick(60)
    #Dragonfly Collision
    for dragonfly in dragonfly:
        dragonfly.move()
        dragonfly.draw()

        if butterfly_rect.colliderect(dragonfly.rect):
            death_sound.play()
            pygame.time.delay(1400)
            print ("You Lost!")
            pygame.quit()
            exit()

    #Goal Collision
    if butterfly_rect.colliderect(goal_rect):
        print("You Win!")
        pygame.quit()

# Start the game with level 2
game_loop(level=2)
       
      
  
       
  
  
