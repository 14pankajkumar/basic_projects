import pygame
import random
import os

pygame.mixer.init()
pygame.init()

# Colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
yellow = ("#FFFF00")

screen_length = 900
screen_width = 500
# Creating Window
gameWindow = pygame.display.set_mode((screen_length,screen_width))
pygame.display.set_caption("Snake game")
pygame.display.update()  

# Background image
bgimg = pygame.image.load("bg_img.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_length, screen_width)).convert_alpha()

over_img = pygame.image.load("pic2.jpg")
over_img = pygame.transform.scale(over_img, (screen_length, screen_width)).convert_alpha()

clock = pygame.time.Clock()
font = pygame.font.SysFont("Chiller", 55, bold=20, italic=20)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text,(x,y))

def plot_snake(gameWindow,color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])

# Creating a game loop
def game_loop():
    # Game soecification variabes
    snk_list = []
    snk_lenght = 1
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10
    fps = 30
    vilocity_x = 0
    vilocity_y = 0
    food_x = random.randint(20, 880)
    food_y = random.randint(20, 480)
    score = 0
    # check if hiscore file exists-
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open("Hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.blit(over_img, (0,0))
            text_screen("Game over!!! Press enter to continue", yellow, 80, 180)
            text_screen("Press M to main menu",yellow,210,280)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

                    if event.key == pygame.K_m:
                        import start_screen
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vilocity_x = 6
                        vilocity_y = 0

                    if event.key == pygame.K_LEFT:
                        vilocity_x = -6
                        vilocity_y = 0

                    if event.key == pygame.K_UP:
                        vilocity_y = -6
                        vilocity_x = 0

                    if event.key == pygame.K_DOWN:
                        vilocity_y = 6
                        vilocity_x = 0

                    if event.key == pygame.K_q:
                        score +=5
            # score = score+1
            # print("Score= ",score)
            snake_x = snake_x + vilocity_x
            snake_y = snake_y + vilocity_y
            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score = score+10
                # print("Score= ", score)
                pygame.mixer.music.load("beep.mp3")
                pygame.mixer.music.play()
                food_x = random.randint(20, 880)
                food_y = random.randint(20,480)
                snk_lenght +=5
                if score>int(hiscore):
                    hiscore = score
                

            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0,0))
            text_screen("score "+str(score) + "  HighScore : "+str(hiscore), yellow, 5,5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if len(snk_list)>snk_lenght:
                del snk_list[0]
            
            if snake_x<0 or snake_x>screen_length or snake_y<0 or snake_y>screen_width:
                game_over = True
                pygame.mixer.music.load("gameover.wav")
                pygame.mixer.music.play()

            
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("gameover.wav")
                pygame.mixer.music.play()

            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
game_loop()