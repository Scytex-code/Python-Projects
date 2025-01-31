import numpy as np
import pygame  


def create_board():
    global matrix, screen
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 700, 100), 0)

    for row in range(6):
        for column in range(7):
            if matrix[row][column] == 0:
                pygame.draw.circle(screen, (0, 0, 0), (50 + (column * 100), 150 + (row * 100)), 45, 0)
            elif matrix[row][column] == 1:
                pygame.draw.circle(screen, (255, 0, 0), (50 + (column * 100), 150 + (row * 100)), 45, 0)
            else:
                pygame.draw.circle(screen, (255, 255, 0), (50 + (column * 100), 150 + (row * 100)), 45, 0)


def place_circle(red_turn, mouse_x, colour_code):
    global matrix, screen

    if red_turn:
        colour = (255, 0, 0)
    else:
        colour = (255, 255, 0)

    for row in range(7):
        if matrix[5 - row][int(mouse_x / 100)] == 0:
            matrix[5 - row][int(mouse_x / 100)] = colour_code
            pygame.draw.circle(screen, colour, (50 + (int(mouse_x / 100) * 100), 650 - (row * 100)), 45, 0)
            return True

    return False


def check_win(colour_code):
    global matrix

    for row in range(6):
        for column in range(7):
            if matrix[row][column] == colour_code:
                if column <= 3:
                    if matrix[row][column + 1] == colour_code and matrix[row][column + 2] == colour_code and matrix[row][column + 3] == colour_code:
                        return f"Player {colour_code}", True
                if row <= 2:
                    if matrix[row + 1][column] == colour_code and matrix[row + 2][column] == colour_code and matrix[row + 3][column] == colour_code:
                        return f"Player {colour_code}", True
                if row <= 2 and column <= 3:
                    if matrix[row + 1][column + 1] == colour_code and matrix[row + 2][column + 2] == colour_code and matrix[row + 3][column + 3] == colour_code:
                        return f"Player {colour_code}", True
                if row <= 2 and column >= 3:
                    if matrix[row + 1][column - 1] == colour_code and matrix[row + 2][column - 2] == colour_code and matrix[row + 3][column - 3] == colour_code:
                        return f"Player {colour_code}", True

    return "Nobody", False


def end_game(winner):
    global screen

    if winner == "Player 1":
        colour = (255, 0, 0)
    else:
        colour = (255, 255, 0)

    font = pygame.font.Font(None, 100)
    text = font.render(f"{winner} Won!", True, colour)
    screen.blit(text, (125, 20))


def Connect_4():
    global matrix, screen
    pygame.init()  

    matrix = np.array((
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                    ))
    screen = pygame.display.set_mode((700, 700))

    running = True
    red_turn = True
    game_is_won = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.dict.get('button') == 1:
                    mouse_x, _ = event.dict.get('pos')

                    if red_turn == True:
                        column_is_full = place_circle(red_turn, mouse_x, 1)
                        winner, game_is_won = check_win(1)

                        if column_is_full == True:
                            red_turn = False
                    else:
                        column_is_full = place_circle(red_turn, mouse_x, 2)
                        winner, game_is_won = check_win(2)

                        if column_is_full == True:
                            red_turn = True

        screen.fill((0, 0, 255))
        create_board()

        if game_is_won == True:
            end_game(winner)
            break

        mouse_x, _ = pygame.mouse.get_pos()
        if red_turn == True:
            pygame.draw.circle(screen, (255, 0, 0), (mouse_x, 50), 45, 0)
        else:
            pygame.draw.circle(screen, (255, 255, 0), (mouse_x, 50), 45, 0)

        pygame.display.update()

    end_loop(running)


def end_loop(running):
    pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


Connect_4()
