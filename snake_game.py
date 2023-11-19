import pygame
import random

# Khởi tạo màn hình
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Màu sắc
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)

# Thông số rắn
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = "RIGHT"
change_to = direction

# Thông số thức ăn
food_pos = [random.randrange(1, width//10) * 10, random.randrange(1, height//10) * 10]
food_spawn = True

# Thông số game
score = 0

# Thông số đồ họa
fps_controller = pygame.time.Clock()

# Hàm vẽ rắn và thức ăn
def draw_snake():
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

def draw_food():
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

# Hàm chạy trò chơi
def run_game():
    global direction, change_to, snake_pos, snake_body, food_pos, food_spawn, score

    # Kiểm tra xem rắn có ăn thức ăn không
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Tạo thức ăn mới
    if not food_spawn:
        food_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
    food_spawn = True

    # Kiểm tra và thay đổi hướng di chuyển
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # Di chuyển rắn
    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "RIGHT":
        snake_pos[0] += 10

    # Cập nhật thân rắn
    snake_body.insert(0, list(snake_pos))

    # Kiểm tra va chạm với tường hoặc chính mình
    if snake_pos[0] < 0 or snake_pos[0] > width-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > height-10:
        game_over()
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    # Vẽ đồ họa
    screen.fill(black)
    draw_snake()
    draw_food()
    pygame.display.flip()

    # Đồ họa chuyển động
    fps_controller.tick(20)

# Hàm kết thúc game
def game_over():
    pygame.quit()
    quit()

# Vòng lặp chính
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    run_game()
