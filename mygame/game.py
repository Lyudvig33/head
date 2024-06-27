"""
This idle game is implemented using the pygame module,
here the player can jump, shooting enemies..
the author of the game Lyudvig Asoyan.
Date 31.05.2024
"""
import pygame

def init_game_and_create_window():
    """
    function for create game window
    """
    pygame.init()
    screen = pygame.display.set_mode((618, 359))
    pygame.display.set_caption("First Game")
    # the method clock for setting the game speed
    clock = pygame.time.Clock()
    return screen, clock

def load_images():
    """
    function for loading images in game
    """

# Alpha code conversion method for more,
# efficient display of transparent parts of images

    #backgroung image for game
    back_gr = pygame.image.load('back_gr.png').convert_alpha()
    # character walk right images
    walk_right = [pygame.image.load('player_move/right1.png').convert_alpha(),
                  pygame.image.load('player_move/right2.png').convert_alpha(),
                  pygame.image.load('player_move/right3.png').convert_alpha(),
                  pygame.image.load('player_move/right4.png').convert_alpha()]
    # character  walk left images
    walk_left = [pygame.image.load('player_move/left4.png').convert_alpha(),
                 pygame.image.load('player_move/left3.png').convert_alpha(),
                 pygame.image.load('player_move/left2.png').convert_alpha(),
                 pygame.image.load('player_move/left1.png').convert_alpha()]
    # enemy image
    enemy = pygame.image.load('roomba.png').convert_alpha()
    # bullet image
    bullet = pygame.image.load('bullet.png').convert_alpha()

    return back_gr, walk_right, walk_left, enemy, bullet

def game_configs():
    """
    function for configurations character and enemy, lose window and sound game
    """

    # List to hold Roomba objects in the game
    roomba_list_in_game = []

    # Counter for player animation frames
    player_anim_count = 0

    player_speed = 5

    # the coordinates of the character
    player_x = 100
    player_y = 250

    #the background
    back_x = 0

    # Flag indicating whether the player is jumping
    is_jump = False

    # jump height
    jump_count = 10
    enemy_count = 0
    enemy_speed = 30
    # bullets count
    bullets_left = 5
    bullets_count = []

    # The enemy appears every 3 seconds
    roomba_timer = 32866 # Userevent
    pygame.time.set_timer(roomba_timer,2000)

    # Set up font and labels for game messages
    # Font for game labels
    label = pygame.font.Font('leter.ttf', 45)
    lose_label = label.render("You Lose! ", True, ('white'))
    restart_label = label.render("Restart ", True, ('green'))
    rest_label = restart_label.get_rect(topleft=(210, 200))

    game_sound = pygame.mixer.Sound('mario.mp3')
    game_sound.play()
    # Set up flags for game state
    # Flag indicating whether the game is in progress
    gameplay = True
    # Flag indicating whether the game is running
    running = True
    # Return all game configurations
    return roomba_list_in_game, player_anim_count,\
            player_speed, player_x, player_y,\
            back_x, is_jump, jump_count, \
           enemy_count, enemy_speed, bullets_left,\
           bullets_count, roomba_timer, label,\
           lose_label, restart_label, rest_label, \
           game_sound, gameplay, running

def play():
    """
    Main function to run the game loop, handle user input,
    update game state, and render graphics.
    This function controls the flow of the game,
    including handling user input, updating the game state,
    rendering graphics, and managing game
    events such as enemy spawning and bullet firing.
    """

    screen, clock = init_game_and_create_window()
    back_gr, walk_right, walk_left, enemy, bullet = load_images()
    roomba_list_in_game, player_anim_count,\
    player_speed, player_x, player_y, back_x,\
    is_jump, jump_count, \
    enemy_count, enemy_speed, bullets_left,\
    bullets, roomba_timer, label, lose_label,\
    restart_label, rest_label, \
    game_sound, gameplay, running = game_configs()

    while running:
        # character speed
        clock.tick(enemy_speed)

        # put 2 images on the background
        screen.blit(back_gr, (back_x, 0))
        screen.blit(back_gr, (back_x + 618, 0))

        if gameplay:
            #draw a pixels around the character
            player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

            # adding enemies to the game
            if roomba_list_in_game:
                for i, el in enumerate(roomba_list_in_game):
                    screen.blit(enemy, el)
                    el.x -= 10

                    # when the enemies have gone beyond the screen, remove them
                    if el.x < -10:
                        roomba_list_in_game.pop(i)

                    # as soon as  we manage to outrun two enemies we add their speed by 5
                        enemy_count += 1
                        if enemy_count % 2 == 0:
                            enemy_speed += 5

                    # when character touch enemy the game ends
                    if player_rect.colliderect(el):
                        gameplay = False

            # the function is to move the chracter to the left or the right
            keys = pygame.key.get_pressed()
            # left key
            if keys[1073741904] and player_x > 25:
                player_x -= player_speed
            # right key
            elif keys[1073741903] and player_x < 359:
                player_x += player_speed

            # check if the player is not  currently jumping
            if not is_jump:

                if keys[32]:# Check if the spacebar is pressed to initiate a jump
                    is_jump = True # Set the flag to indicate that the player is now jumping
                    game_sound = pygame.mixer.Sound('jump.mp3')
                    game_sound.play()

            else:  # If the player is currently jumping
                if jump_count >= -10:
                    if jump_count > 0:

                        #raise to a power so that the jumps are smoother
                        player_y -= (jump_count ** 2) / 2
                    else:
                        player_y += (jump_count ** 2) / 2
                    jump_count -= 1

                #Half after the jump we update the configurations
                else:
                    is_jump = False
                    jump_count = 10

            # as we click on the left or right arrow, a picture of personage ir drawn
            if keys[1073741904]:
                screen.blit(walk_left[int(player_anim_count)], (player_x, player_y))
            else:
                screen.blit(walk_right[int(player_anim_count)], (player_x, player_y))

            # change the pictures of the character to get an animation
            if player_anim_count >= 3:
                player_anim_count = 0
            else:
                player_anim_count += 0.25

            # conditions for change the background image to create an animation effect
            back_x -= 2
            if back_x == -618:
                back_x = 0

            # draw bullets in the game
            if bullets:
                for (i, bul) in enumerate(bullets):
                    screen.blit(bullet, (bul.x, bul.y))
                    bul.x += 4
                    # if the bullets are out the screen, delete them
                    if bul.x > 630:
                        bullets.pop(i)
                    # we check the if enemies in the game,if bulltes touched the enemies,
                    # we remove the enemies and bullets
                    if roomba_list_in_game:
                        for (index, devils) in enumerate(roomba_list_in_game):
                            if bul.colliderect(devils):
                                roomba_list_in_game.pop(index)
                                bullets.pop(i)
        else:
            # lose window color
            screen.fill(('black'))
            # lose window titles place
            screen.blit(lose_label, (199, 140))
            # restart game button
            screen.blit(restart_label, rest_label)

            # the mouse function is to close and restart game with mouse
            mouse = pygame.mouse.get_pos()

            # the game starts over as soon as we click the label Restart!
            if rest_label.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplay = True
                player_x = 120
                roomba_list_in_game.clear()
                bullets_left = 5
        pygame.display.update()

        # get a list of all possible events
        for event in pygame.event.get():

            # activate to buttons for quit game
            if event.type == 256:

                running = False
                pygame.quit()

            #add enemies to the gmae when the condition is satisfied
            if event.type == roomba_timer:
                roomba_list_in_game.append(enemy.get_rect(topleft=(620, 250)))

            # the condition checks the number of bullets and,
            # does not allow multiple bullets to be fired at once
            if gameplay and event.type == 769 and \
                event.key == 1073742049 and bullets_left > 0:

                bullets.append(bullet.get_rect(topleft=(player_x + 30, player_y + 10)))
                bullets_left -= 1
play()
