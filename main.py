import pygame
from assets import Food, Snake, Direction, Field
from addition import Direction, GameStatus, Point

pygame.init()


class SnakeGame:
    def __init__(self) -> None:
        # Setting up game screen and frame rate
        self.screen = pygame.display.set_mode([420, 420])
        self.clock = pygame.time.Clock()

        # Initializing game character's instances

        full_cell_size = 20
        self.field = Field(int(self.screen.get_width() / full_cell_size))
        self.border = 4
        self.cell_size = full_cell_size - self.border
        self.snake = Snake(self.field.side)
        self.food = Food()

        # Setting random coordinates for food instance
        self.food.apply_random_coordinates(self.field.side)

        # Setting up game status
        self.status = GameStatus.STOP

    def start(self):

        # Updating game status
        self.status = GameStatus.RUN

        # Main loop
        while self.status == GameStatus.RUN:

            # Looping through in-game events
            for event in pygame.event.get():

                # Exiting if appropriate key has been pressed
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key in (pygame.K_q, pygame.K_ESCAPE):
                    self.status = GameStatus.STOP

                elif event.type == pygame.KEYDOWN:
                    # Setting up new direction depending on pressed key
                    match event.key:
                        case pygame.K_w:
                            if self.snake.direction != Direction.DOWN:
                                self.snake.direction = Direction.UP
                        case pygame.K_s:
                            if self.snake.direction != Direction.UP:
                                self.snake.direction = Direction.DOWN
                        case pygame.K_a:
                            if self.snake.direction != Direction.RIGHT:
                                self.snake.direction = Direction.LEFT
                        case pygame.K_d:
                            if self.snake.direction != Direction.LEFT:
                                self.snake.direction = Direction.RIGHT

            # Move snake according to its direction
            if self.snake.direction:
                self.snake.move(self.field.side)

            # Filling screen with black color to draw new frame
            self.screen.fill((0,0,0))

            for y in range(self.field.side):
                for x in range(self.field.side):

                    # Calculating position of each cell
                    top = y * self.border + y * self.cell_size
                    left = x * self.border + x * self.cell_size

                    # If snake ate food then create new tail part
                    if self.snake.tail[0] == self.food.position:
                        self.snake.grow(self.food.position)
                        self.food.apply_random_coordinates(self.field.side)

                    # Set base color as black
                    color = (0, 0, 0)

                    # Depending on coordinates chage color of cell if there's any instance here
                    if Point(x, y) in self.snake.tail:
                        color = self.snake.color
                    elif Point(x, y) == self.food.position:
                        color = self.food.color

                    # Draw rectangle with known parameters
                    pygame.draw.rect(self.screen, color, pygame.Rect(left, top, self.cell_size, self.cell_size))

            pygame.display.flip()
            self.clock.tick(4)

pygame.quit()


if __name__ == "__main__":
    g = SnakeGame()
    g.start()
