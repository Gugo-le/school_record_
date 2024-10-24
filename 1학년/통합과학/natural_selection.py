import pygame
import random
import math

# 초기화
pygame.init()

# 화면 크기 설정
W, H = 800, 600
screen = pygame.display.set_mode((W, H))

# 셀과 음식 클래스 정의
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20
        self.color = (255, 255, 0)
        self.velocity_x = random.uniform(-1, 1)  # 초기 속도 설정
        self.velocity_y = random.uniform(-1, 1)

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.color = (0, 240, 100)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# 충돌 감지 함수
def check_collision(cell, food):
    distance = math.sqrt((cell.x - food.x) ** 2 + (cell.y - food.y) ** 2)
    return distance < (cell.radius + food.radius)

# 공간 분할 기법 구현
def spatial_partition(cells, foods, cell_size):
    grid = {}
    for cell in cells:
        grid_key = (int(cell.x // cell_size), int(cell.y // cell_size))
        if grid_key not in grid:
            grid[grid_key] = []
        grid[grid_key].append(cell)

    for food in foods:
        grid_key = (int(food.x // cell_size), int(food.y // cell_size))
        if grid_key not in grid:
            grid[grid_key] = []
        grid[grid_key].append(food)

    return grid

# 셀과 음식 생성
cells = [Cell(random.randint(100, W-100), random.randint(100, H-100)) for _ in range(5)]
foods = [Food(random.randint(100, W-100), random.randint(100, H-100)) for _ in range(5)]

# 메인 루프
running = True
cell_size = 50  # 공간 분할을 위한 그리드 크기

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((127, 127, 127))

    # 이동
    for cell in cells:
        cell.move()
        cell.draw(screen)

    # 공간 분할
    grid = spatial_partition(cells, foods, cell_size)

    # 충돌 체크
    for grid_key in grid:
        objects = grid[grid_key]
        for i in range(len(objects)):
            for j in range(i + 1, len(objects)):
                if isinstance(objects[i], Cell) and isinstance(objects[j], Food):
                    if check_collision(objects[i], objects[j]):
                        print(f"Collision detected between Cell at ({objects[i].x}, {objects[i].y}) and Food at ({objects[j].x}, {objects[j].y})")
                        # 음식의 상태 업데이트 예시
                        foods.remove(objects[j])  # 음식 삭제 (이벤트 발생)

    # 음식 그리기
    for food in foods:
        food.draw(screen)

    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()