import pygame

pygame.mixer.init()
pygame.mixer.music.load("welcome.mp3")
pygame.mixer.music.play()
pygame.init()

white = (255, 255, 255)
red = (250,0,0)
yellow = ("#FFFF00")
q = (198, 75, 58)

screen_length = 900
screen_width = 500

gameWindow = pygame.display.set_mode((screen_length,screen_width))
pygame.display.set_caption("Snake game")
pygame.display.update()  

exit_game = False
game_over = False
fps = 30
clock = pygame.time.Clock()
font = pygame.font.SysFont("Chiller", 100,bold=20,italic=20)
font2 = pygame.font.SysFont("Chiller", 30, bold=20, italic=20)

def text_screen(text, color, x, y):
    text_welcome = font.render(text ,True, color)
    gameWindow.blit(text_welcome, (x,y))

def lower_text(text, color, x, y):
    text_welcome = font2.render(text ,True, color)
    gameWindow.blit(text_welcome, (x,y))

wel_img = pygame.image.load("pic1.jpg")
wel_img = pygame.transform.scale(wel_img, (900,500)).convert_alpha()

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pygame.mixer.music.stop()
                import main_game

    gameWindow.fill(q)
    gameWindow.blit(wel_img,(0,0))
    lower_text("Press Enter to start the game", yellow, 290, 250)
    text_screen("Welcome", yellow, 300, 150)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()