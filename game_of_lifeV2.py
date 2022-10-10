import random, pygame

WIDTH, HEIGHT = 100, 100
grid = []
multiplier = 6
FPS = 15

color_grid = []
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255, 255, 255)
ORANGE = (199, 93, 32)
PINK = (200, 12, 242)
colors = [BLUE,RED, GREEN, WHITE]
for x in range(HEIGHT):
    row = []
    for y in range(WIDTH):
        row.append(random.choice(colors))
    color_grid.append(row)


for x in range(HEIGHT):
    row = []
    for y in range(WIDTH):
        row.append(" ")
    grid.append(row)

for x in range(random.randint(0, WIDTH * HEIGHT/5)):
    grid[random.randint(0, HEIGHT-1)][random.randint(0, WIDTH-1)] = "1"


adds = [-1, 0, 1]
def checker(x, y):
    validity = 0
    for add in adds:
        for add1 in adds:
            try:
                abort = [add, add1]
                if grid[x+add][y+add1] == "1" and abort != [0, 0]:
                    validity += 1
            except Exception as e:
                pass
    return validity

pygame.init()

WIN = pygame.display.set_mode((WIDTH*multiplier+20, HEIGHT*multiplier+20), pygame.RESIZABLE)
pygame.display.set_caption("Game of Life")
# color = (0, 255, 0)

radius = multiplier
def draw(x, y, color, win):
    pygame.draw.rect(win, color, (x,y,multiplier,multiplier))


def main():
    global grid

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        WIN.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        for x in range(HEIGHT):
            for y in range(WIDTH):
                if grid[x][y] == "1":
                    draw(x*multiplier+10, y*multiplier+10,color_grid[x][y], WIN)

        dummy_grid =[]
        for x in range(HEIGHT):
            row = []
            for y in range(WIDTH):
                row.append(" ")
            dummy_grid.append(row)

        for x in range(HEIGHT):
            for y in range(WIDTH):
                if grid[x][y] == "1":
                    if 2 <= checker(x, y) < 4:
                        dummy_grid[x][y] = "1"
                    else:
                        dummy_grid[x][y] = " "
                elif grid[x][y] == " ":
                    if checker(x, y) == 3:
                        dummy_grid[x][y] = "1"
                    else:
                        dummy_grid[x][y] = " "
        grid = dummy_grid

        pygame.display.update()
                
    pygame.quit()

main()