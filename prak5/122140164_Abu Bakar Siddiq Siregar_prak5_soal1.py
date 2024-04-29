import pygame
import random

RED = (255, 0, 0)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
FPS = 10

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        pass

    def move(self):
        pass

class Snake(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.length = 1
        self.direction = 'RIGHT'
        self.body = [(x, y)]

    def draw(self, surface):
        for block in self.body:
            pygame.draw.rect(surface, 'blue', (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

    def move(self):
        if self.direction == 'UP':
            self.y -= BLOCK_SIZE
        elif self.direction == 'DOWN':
            self.y += BLOCK_SIZE
        elif self.direction == 'LEFT':
            self.x -= BLOCK_SIZE
        elif self.direction == 'RIGHT':
            self.x += BLOCK_SIZE

        self.body.insert(0, (self.x, self.y))
        if len(self.body) > self.length:
            self.body.pop()

    def grow(self):
        self.length += 1

class Food(GameObject):
    def __init__(self):
        x = random.randrange(0, SCREEN_WIDTH, BLOCK_SIZE)
        y = random.randrange(0, SCREEN_HEIGHT, BLOCK_SIZE)
        super().__init__(x, y)

    def draw(self, surface):
        pygame.draw.rect(surface, 'red', (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.snake = Snake(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.food = Food()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_UP or event.key == pygame.K_w) and self.snake.direction != 'DOWN':
                        self.snake.direction = 'UP'
                    elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.snake.direction != 'UP':
                        self.snake.direction = 'DOWN'
                    elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.snake.direction != 'RIGHT':
                        self.snake.direction = 'LEFT'
                    elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.snake.direction != 'LEFT':
                        self.snake.direction = 'RIGHT'

            self.snake.move()
            self.check_collision()

            self.screen.fill('black')
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()

    def check_collision(self):
        if self.snake.x == self.food.x and self.snake.y == self.food.y:
            self.snake.grow()
            self.food = Food()  

        for block in self.snake.body[1:]:
            if self.snake.x == block[0] and self.snake.y == block[1]:
                self.game_over()

        if self.snake.x < 0 or self.snake.x >= SCREEN_WIDTH or self.snake.y < 0 or self.snake.y >= SCREEN_HEIGHT:
            self.game_over()

    def game_over(self):
        print("Game Over!")
        pygame.quit()
        quit()

if __name__ == "__main__":
    game = Game()
    game.run()
