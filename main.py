import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((580, 290))
pygame.display.set_caption("Pygame itProger Game")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)



bg = pygame.image.load('images/bg.png')
walk_left = [
    pygame.image.load('images/player_left/1.png'),
    pygame.image.load('images/player_left/2.png'),
    pygame.image.load('images/player_left/3.png'),
    pygame.image.load('images/player_left/4.png')
]
walk_right = [
    pygame.image.load('images/player_right/1.png'),
    pygame.image.load('images/player_right/2.png'),
    pygame.image.load('images/player_right/3.png'),
    pygame.image.load('images/player_right/4.png')
]

player_anim_count = 0
bg_x = 0

player_speed = 5
player_x = 150
player_y = 190

is_jump = False
jump_count = 7

bg_sound = pygame.mixer.Sound('sounds/bg.mp3')
bg_sound.play()

running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 580, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))

    if keys[pygame.K_LEFT] and player_x > 50:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 200:
        player_x += player_speed

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -7:
            if jump_count > 0:
                player_y -= (jump_count**2) / 2
            else:
                player_y += (jump_count**2) / 2
            jump_count-=1
        else:
            jump_count = 7
            is_jump = False

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    bg_x -= 2
    if bg_x == -580:
        bg_x = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_a:
                screen.fill((19, 105, 2))

    clock.tick(10)

