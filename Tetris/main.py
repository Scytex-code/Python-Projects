import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
BOARD_WIDTH = 300
BOARD_HEIGHT = 600
BLOCK_SIZE = 30
TOP_LEFT_X = (SCREEN_WIDTH - BOARD_WIDTH) // 2
TOP_LEFT_Y = SCREEN_HEIGHT - BOARD_HEIGHT
NEXT_SHAPE_X = 660
NEXT_SHAPE_Y = 300


def draw_board():
    for row in range(1, BOARD_HEIGHT // BLOCK_SIZE):
        pygame.draw.line(screen, (100, 100, 100), (TOP_LEFT_X, TOP_LEFT_Y + (row * BLOCK_SIZE)), (TOP_LEFT_X + BOARD_WIDTH, TOP_LEFT_Y + (row * BLOCK_SIZE)))

    for column in range(1, BOARD_WIDTH // BLOCK_SIZE):
        pygame.draw.line(screen, (100, 100, 100), (TOP_LEFT_X + (column * BLOCK_SIZE), TOP_LEFT_Y), (TOP_LEFT_X + (column * BLOCK_SIZE), TOP_LEFT_Y + BOARD_HEIGHT))

    pygame.draw.rect(screen, (255, 0, 0), (TOP_LEFT_X, TOP_LEFT_Y, BOARD_WIDTH + 1, BOARD_HEIGHT), 4)
    
    tetris_font = pygame.font.Font(None, 100)
    text = tetris_font.render("TETRIS", True, (255, 255, 255))
    screen.blit(text, (270, 20))

    side_text_font = pygame.font.Font(None, 50)
    text = side_text_font.render("Next Shape", True, (255, 255, 255))
    screen.blit(text, (580, 250))

    text = side_text_font.render("Total Score", True, (255, 255, 255))
    screen.blit(text, (30, 250))

    text = side_text_font.render(f": {score}", True, (255, 255, 255))
    screen.blit(text, (50, 310))


def create_current_block(all_blocks, block_queue):
    global screen, running

    current_block = []

    if block_queue[0] == "S":
        current_block.append(pygame.draw.rect(screen, (0, 255, 0), (TOP_LEFT_X + (BOARD_WIDTH // 2) - 30, TOP_LEFT_Y + 30, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (0, 255, 0), (TOP_LEFT_X + (BOARD_WIDTH // 2), TOP_LEFT_Y + 30, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (0, 255, 0), (TOP_LEFT_X + (BOARD_WIDTH // 2), TOP_LEFT_Y, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (0, 255, 0), (TOP_LEFT_X + (BOARD_WIDTH // 2) + 30, TOP_LEFT_Y, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append("S")
    elif block_queue[0] == "Z":
        current_block.append(pygame.draw.rect(screen, (255, 0, 0), (TOP_LEFT_X + (BOARD_WIDTH // 2) - 30, TOP_LEFT_Y, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (255, 0, 0), (TOP_LEFT_X + (BOARD_WIDTH // 2), TOP_LEFT_Y, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (255, 0, 0), (TOP_LEFT_X + (BOARD_WIDTH // 2), TOP_LEFT_Y + 30, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (255, 0, 0), (TOP_LEFT_X + (BOARD_WIDTH // 2) + 30, TOP_LEFT_Y + 30, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append("Z")
    elif block_queue[0] == "I":
        current_block.append(pygame.draw.rect(screen, (0, 255, 255), (TOP_LEFT_X + (BOARD_WIDTH // 2), TOP_LEFT_Y, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (0, 255, 255), (TOP_LEFT_X + (BOARD_WIDTH // 2), TOP_LEFT_Y + 30, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (0, 255, 255), (TOP_LEFT_X + (BOARD_WIDTH // 2), TOP_LEFT_Y + 60, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (0, 255, 255), (TOP_LEFT_X + (BOARD_WIDTH // 2), TOP_LEFT_Y + 90, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append("I")
    elif block_queue[0] == "O":
        current_block.append(pygame.draw.rect(screen, (255, 255, 0), (TOP_LEFT_X + (BOARD_WIDTH // 2) - 30, TOP_LEFT_Y, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (255, 255, 0), (TOP_LEFT_X + (BOARD_WIDTH // 2), TOP_LEFT_Y, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (255, 255, 0), (TOP_LEFT_X + (BOARD_WIDTH // 2) - 30, TOP_LEFT_Y + 30, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (255, 255, 0), (TOP_LEFT_X + (BOARD_WIDTH // 2), TOP_LEFT_Y + 30, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append("O")
    elif block_queue[0] == "J":
        current_block.append(pygame.draw.rect(screen, (255, 165, 0), (TOP_LEFT_X + (BOARD_WIDTH // 2) - 30, TOP_LEFT_Y, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (255, 165, 0), (TOP_LEFT_X + (BOARD_WIDTH // 2) - 30, TOP_LEFT_Y + 30, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (255, 165, 0), (TOP_LEFT_X + (BOARD_WIDTH // 2), TOP_LEFT_Y + 30, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (255, 165, 0), (TOP_LEFT_X + (BOARD_WIDTH // 2) + 30, TOP_LEFT_Y + 30, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append("J")
    elif block_queue[0] == "L":
        current_block.append(pygame.draw.rect(screen, (0, 0, 255), (TOP_LEFT_X + (BOARD_WIDTH // 2) - 30, TOP_LEFT_Y + 30, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (0, 0, 255), (TOP_LEFT_X + (BOARD_WIDTH // 2), TOP_LEFT_Y + 30, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (0, 0, 255), (TOP_LEFT_X + (BOARD_WIDTH // 2) + 30, TOP_LEFT_Y + 30, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (0, 0, 255), (TOP_LEFT_X + (BOARD_WIDTH // 2) + 30, TOP_LEFT_Y, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append("L")
    elif block_queue[0] == "T":
        current_block.append(pygame.draw.rect(screen, (128, 0, 128), (TOP_LEFT_X + (BOARD_WIDTH // 2), TOP_LEFT_Y, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (128, 0, 128), (TOP_LEFT_X + (BOARD_WIDTH // 2) - 30, TOP_LEFT_Y + 30, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (128, 0, 128), (TOP_LEFT_X + (BOARD_WIDTH // 2), TOP_LEFT_Y + 30, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append(pygame.draw.rect(screen, (128, 0, 128), (TOP_LEFT_X + (BOARD_WIDTH // 2) + 30, TOP_LEFT_Y + 30, BLOCK_SIZE, BLOCK_SIZE)))
        current_block.append("T")

    is_colliding = False
    for block_index in range(len(all_blocks)):
        for square_index in range(len(all_blocks[block_index]) - 1):
            for current_square_index in range(len(current_block) - 1):
                if current_block[current_square_index].x == all_blocks[block_index][square_index].x and current_block[current_square_index].y == all_blocks[block_index][square_index].y:
                    is_colliding = True

    if is_colliding:
        running = False

    return current_block


def draw_next_block(block_queue):
    global screen

    if block_queue[1] == "S":
        pygame.draw.rect(screen, (0, 255, 0), (NEXT_SHAPE_X - 30, NEXT_SHAPE_Y + 30, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (0, 255, 0), (NEXT_SHAPE_X, NEXT_SHAPE_Y + 30, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (0, 255, 0), (NEXT_SHAPE_X, NEXT_SHAPE_Y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (0, 255, 0), (NEXT_SHAPE_X + 30, NEXT_SHAPE_Y, BLOCK_SIZE, BLOCK_SIZE))
    elif block_queue[1] == "Z":
        pygame.draw.rect(screen, (255, 0, 0), (NEXT_SHAPE_X - 30, NEXT_SHAPE_Y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (255, 0, 0), (NEXT_SHAPE_X, NEXT_SHAPE_Y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (255, 0, 0), (NEXT_SHAPE_X, NEXT_SHAPE_Y + 30, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (255, 0, 0), (NEXT_SHAPE_X + 30, NEXT_SHAPE_Y + 30, BLOCK_SIZE, BLOCK_SIZE))
    elif block_queue[1] == "I":
        pygame.draw.rect(screen, (0, 255, 255), (NEXT_SHAPE_X, NEXT_SHAPE_Y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (0, 255, 255), (NEXT_SHAPE_X, NEXT_SHAPE_Y + 30, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (0, 255, 255), (NEXT_SHAPE_X, NEXT_SHAPE_Y + 60, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (0, 255, 255), (NEXT_SHAPE_X, NEXT_SHAPE_Y + 90, BLOCK_SIZE, BLOCK_SIZE))
    elif block_queue[1] == "O":
        pygame.draw.rect(screen, (255, 255, 0), (NEXT_SHAPE_X - 30 + 15, NEXT_SHAPE_Y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (255, 255, 0), (NEXT_SHAPE_X + 15, NEXT_SHAPE_Y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (255, 255, 0), (NEXT_SHAPE_X - 30 + 15, NEXT_SHAPE_Y + 30, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (255, 255, 0), (NEXT_SHAPE_X + 15, NEXT_SHAPE_Y + 30, BLOCK_SIZE, BLOCK_SIZE))
    elif block_queue[1] == "J":
        pygame.draw.rect(screen, (255, 165, 0), (NEXT_SHAPE_X - 30, NEXT_SHAPE_Y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (255, 165, 0), (NEXT_SHAPE_X - 30, NEXT_SHAPE_Y + 30, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (255, 165, 0), (NEXT_SHAPE_X, NEXT_SHAPE_Y + 30, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (255, 165, 0), (NEXT_SHAPE_X + 30, NEXT_SHAPE_Y + 30, BLOCK_SIZE, BLOCK_SIZE))
    elif block_queue[1] == "L":
        pygame.draw.rect(screen, (0, 0, 255), (NEXT_SHAPE_X - 30, NEXT_SHAPE_Y + 30, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (0, 0, 255), (NEXT_SHAPE_X, NEXT_SHAPE_Y + 30, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (0, 0, 255), (NEXT_SHAPE_X + 30, NEXT_SHAPE_Y + 30, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (0, 0, 255), (NEXT_SHAPE_X + 30, NEXT_SHAPE_Y, BLOCK_SIZE, BLOCK_SIZE))
    elif block_queue[1] == "T":
        pygame.draw.rect(screen, (128, 0, 128), (NEXT_SHAPE_X, NEXT_SHAPE_Y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (128, 0, 128), (NEXT_SHAPE_X - 30, NEXT_SHAPE_Y + 30, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (128, 0, 128), (NEXT_SHAPE_X, NEXT_SHAPE_Y + 30, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (128, 0, 128), (NEXT_SHAPE_X + 30, NEXT_SHAPE_Y + 30, BLOCK_SIZE, BLOCK_SIZE))


def draw_all_blocks(all_blocks):
    global screen

    for block in all_blocks:
        if block[len(block) - 1] == "S":
            colour = (0, 255, 0)
        elif block[len(block) - 1] == "Z":
            colour = (255, 0, 0)
        elif block[len(block) - 1] == "I":
            colour = (0, 255, 255)
        elif block[len(block) - 1] == "O":
            colour = (255, 255, 0)
        elif block[len(block) - 1] == "J":
            colour = (255, 165, 0)
        elif block[len(block) - 1] == "L":
            colour = (0, 0, 255)
        elif block[len(block) - 1] == "T":
            colour = (128, 0, 128)
        else:
            colour = (0, 0, 0)
        
        for square_index in range(len(block) - 1):
            pygame.draw.rect(screen, colour, (block[square_index].x, block[square_index].y, BLOCK_SIZE, BLOCK_SIZE))


def move_current_block(all_blocks, current_block, direction):
    for square_index in range(len(current_block) - 1):
        if direction == "Down":
            current_block[square_index].y += BLOCK_SIZE
        elif direction == "Left":
            current_block[square_index].x -= BLOCK_SIZE
        elif direction == "Right":
            current_block[square_index].x += BLOCK_SIZE

    is_colliding = False
    for block_index in range(len(all_blocks) - 1):
        for square_index in range(len(all_blocks[block_index]) - 1):
            for current_square_index in range(len(current_block) - 1):
                if current_block[current_square_index].x == all_blocks[block_index][square_index].x and current_block[current_square_index].y == all_blocks[block_index][square_index].y:
                    is_colliding = True
    for current_square_index in range(len(current_block) - 1):
        if current_block[current_square_index].y == 700 or current_block[current_square_index].x < 250 or current_block[current_square_index].x > 549:
            is_colliding = True

    is_placed = False
    if is_colliding:
        for square_index in range(len(current_block) - 1):
            if direction == "Down":
                current_block[square_index].y -= BLOCK_SIZE
                is_placed = True
            elif direction == "Left":
                current_block[square_index].x += BLOCK_SIZE
            elif direction == "Right":
                current_block[square_index].x -= BLOCK_SIZE
    
    return is_placed


def rotate_current_block(all_blocks, block_queue, current_block):
    if block_queue[0] == "S":
        if current_block[1].x == current_block[2].x:
            current_block[0].x += BLOCK_SIZE * 2
            current_block[1].x += BLOCK_SIZE
            current_block[1].y -= BLOCK_SIZE
            current_block[3].x -= BLOCK_SIZE
            current_block[3].y -= BLOCK_SIZE
        else:
            current_block[0].x -= BLOCK_SIZE * 2
            current_block[1].x -= BLOCK_SIZE
            current_block[1].y += BLOCK_SIZE
            current_block[3].x += BLOCK_SIZE
            current_block[3].y += BLOCK_SIZE
    elif block_queue[0] == "Z":
        if current_block[1].x == current_block[2].x:
            current_block[0].x += BLOCK_SIZE * 2
            current_block[0].y -= BLOCK_SIZE
            current_block[1].x += BLOCK_SIZE
            current_block[2].y -= BLOCK_SIZE
            current_block[3].x -= BLOCK_SIZE
        else:
            current_block[0].x -= BLOCK_SIZE * 2
            current_block[0].y += BLOCK_SIZE
            current_block[1].x -= BLOCK_SIZE
            current_block[2].y += BLOCK_SIZE
            current_block[3].x += BLOCK_SIZE
    elif block_queue[0] == "I":
        if current_block[0].x == current_block[1].x:
            current_block[0].x -= BLOCK_SIZE * 2
            current_block[0].y += BLOCK_SIZE * 2
            current_block[1].x -= BLOCK_SIZE
            current_block[1].y += BLOCK_SIZE
            current_block[3].x += BLOCK_SIZE
            current_block[3].y -= BLOCK_SIZE
        else:
            current_block[0].x += BLOCK_SIZE * 2
            current_block[0].y -= BLOCK_SIZE * 2
            current_block[1].x += BLOCK_SIZE
            current_block[1].y -= BLOCK_SIZE
            current_block[3].x -= BLOCK_SIZE
            current_block[3].y += BLOCK_SIZE
    elif block_queue[0] == "J":
        if current_block[0].x == current_block[1].x:
            if current_block[0].x < current_block[2].x:
                current_block[0].x += BLOCK_SIZE * 2
                current_block[1].x += BLOCK_SIZE
                current_block[1].y -= BLOCK_SIZE
                current_block[3].x -= BLOCK_SIZE
                current_block[3].y += BLOCK_SIZE
            else:
                current_block[0].x -= BLOCK_SIZE * 2
                current_block[1].x -= BLOCK_SIZE
                current_block[1].y += BLOCK_SIZE
                current_block[3].x += BLOCK_SIZE
                current_block[3].y -= BLOCK_SIZE
        else:
            if current_block[0].x < current_block[2].x:
                current_block[0].y -= BLOCK_SIZE * 2
                current_block[1].x -= BLOCK_SIZE
                current_block[1].y -= BLOCK_SIZE
                current_block[3].x += BLOCK_SIZE
                current_block[3].y += BLOCK_SIZE
            else:
                current_block[0].y += BLOCK_SIZE * 2
                current_block[1].x += BLOCK_SIZE
                current_block[1].y += BLOCK_SIZE
                current_block[3].x -= BLOCK_SIZE
                current_block[3].y -= BLOCK_SIZE
    elif block_queue[0] == "L":
        if current_block[2].x == current_block[3].x:
            if current_block[0].x < current_block[3].x:
                current_block[0].x += BLOCK_SIZE
                current_block[0].y -= BLOCK_SIZE
                current_block[2].x -= BLOCK_SIZE
                current_block[2].y += BLOCK_SIZE
                current_block[3].y += BLOCK_SIZE * 2
            else:
                current_block[0].x -= BLOCK_SIZE
                current_block[0].y += BLOCK_SIZE
                current_block[2].x += BLOCK_SIZE
                current_block[2].y -= BLOCK_SIZE
                current_block[3].y -= BLOCK_SIZE * 2
        else:
            if current_block[0].x < current_block[3].x:
                current_block[0].x += BLOCK_SIZE
                current_block[0].y += BLOCK_SIZE
                current_block[2].x -= BLOCK_SIZE
                current_block[2].y -= BLOCK_SIZE
                current_block[3].x -= BLOCK_SIZE * 2
            else:
                current_block[0].x -= BLOCK_SIZE
                current_block[0].y -= BLOCK_SIZE
                current_block[2].x += BLOCK_SIZE
                current_block[2].y += BLOCK_SIZE
                current_block[3].x += BLOCK_SIZE * 2
    elif block_queue[0] == "T":
        if current_block[0].x == current_block[2].x:
            if current_block[0].x > current_block[1].x:
                current_block[0].x += BLOCK_SIZE
                current_block[0].y += BLOCK_SIZE
                current_block[1].x += BLOCK_SIZE
                current_block[1].y -= BLOCK_SIZE
                current_block[3].x -= BLOCK_SIZE
                current_block[3].y += BLOCK_SIZE
            else:
                current_block[0].x -= BLOCK_SIZE
                current_block[0].y -= BLOCK_SIZE
                current_block[1].x -= BLOCK_SIZE
                current_block[1].y += BLOCK_SIZE
                current_block[3].x += BLOCK_SIZE
                current_block[3].y -= BLOCK_SIZE
        else:
            if current_block[0].x > current_block[1].x:
                current_block[0].x -= BLOCK_SIZE
                current_block[0].y += BLOCK_SIZE
                current_block[1].x += BLOCK_SIZE
                current_block[1].y += BLOCK_SIZE
                current_block[3].x -= BLOCK_SIZE
                current_block[3].y -= BLOCK_SIZE
            else:
                current_block[0].x += BLOCK_SIZE
                current_block[0].y -= BLOCK_SIZE
                current_block[1].x -= BLOCK_SIZE
                current_block[1].y -= BLOCK_SIZE
                current_block[3].x += BLOCK_SIZE
                current_block[3].y += BLOCK_SIZE

    is_colliding = False
    for block_index in range(len(all_blocks) - 1):
        for square_index in range(len(all_blocks[block_index]) - 1):
            for current_square_index in range(len(current_block) - 1):
                if current_block[current_square_index].x == all_blocks[block_index][square_index].x and current_block[current_square_index].y == all_blocks[block_index][square_index].y:
                    is_colliding = True
    for current_square_index in range(len(current_block) - 1):
        if current_block[current_square_index].y == 700 or current_block[current_square_index].x < 250 or current_block[current_square_index].x > 549:
            is_colliding = True

    if is_colliding:
        if block_queue[0] == "S":
            if current_block[1].x == current_block[2].x:
                current_block[0].x += BLOCK_SIZE * 2
                current_block[1].x += BLOCK_SIZE
                current_block[1].y -= BLOCK_SIZE
                current_block[3].x -= BLOCK_SIZE
                current_block[3].y -= BLOCK_SIZE
            else:
                current_block[0].x -= BLOCK_SIZE * 2
                current_block[1].x -= BLOCK_SIZE
                current_block[1].y += BLOCK_SIZE
                current_block[3].x += BLOCK_SIZE
                current_block[3].y += BLOCK_SIZE
        elif block_queue[0] == "Z":
            if current_block[1].x == current_block[2].x:
                current_block[0].x += BLOCK_SIZE * 2
                current_block[0].y -= BLOCK_SIZE
                current_block[1].x += BLOCK_SIZE
                current_block[2].y -= BLOCK_SIZE
                current_block[3].x -= BLOCK_SIZE
            else:
                current_block[0].x -= BLOCK_SIZE * 2
                current_block[0].y += BLOCK_SIZE
                current_block[1].x -= BLOCK_SIZE
                current_block[2].y += BLOCK_SIZE
                current_block[3].x += BLOCK_SIZE
        elif block_queue[0] == "I":
            if current_block[0].x == current_block[1].x:
                current_block[0].x -= BLOCK_SIZE * 2
                current_block[0].y += BLOCK_SIZE * 2
                current_block[1].x -= BLOCK_SIZE
                current_block[1].y += BLOCK_SIZE
                current_block[3].x += BLOCK_SIZE
                current_block[3].y -= BLOCK_SIZE
            else:
                current_block[0].x += BLOCK_SIZE * 2
                current_block[0].y -= BLOCK_SIZE * 2
                current_block[1].x += BLOCK_SIZE
                current_block[1].y -= BLOCK_SIZE
                current_block[3].x -= BLOCK_SIZE
                current_block[3].y += BLOCK_SIZE
        elif block_queue[0] == "J":
            if current_block[0].x == current_block[1].x:
                if current_block[0].x < current_block[2].x:
                    current_block[0].y += BLOCK_SIZE * 2
                    current_block[1].x += BLOCK_SIZE
                    current_block[1].y += BLOCK_SIZE
                    current_block[3].x -= BLOCK_SIZE
                    current_block[3].y -= BLOCK_SIZE
                else:
                    current_block[0].y -= BLOCK_SIZE * 2
                    current_block[1].x -= BLOCK_SIZE
                    current_block[1].y -= BLOCK_SIZE
                    current_block[3].x += BLOCK_SIZE
                    current_block[3].y += BLOCK_SIZE
            else:
                if current_block[0].x < current_block[2].x:
                    current_block[0].x += BLOCK_SIZE * 2
                    current_block[1].x += BLOCK_SIZE
                    current_block[1].y -= BLOCK_SIZE
                    current_block[3].x -= BLOCK_SIZE
                    current_block[3].y += BLOCK_SIZE
                else:
                    current_block[0].x -= BLOCK_SIZE * 2
                    current_block[1].x -= BLOCK_SIZE
                    current_block[1].y += BLOCK_SIZE
                    current_block[3].x += BLOCK_SIZE
                    current_block[3].y -= BLOCK_SIZE
        elif block_queue[0] == "L":
            if current_block[2].x == current_block[3].x:
                if current_block[0].x < current_block[3].x:
                    current_block[0].x += BLOCK_SIZE
                    current_block[0].y += BLOCK_SIZE
                    current_block[2].x -= BLOCK_SIZE
                    current_block[2].y -= BLOCK_SIZE
                    current_block[3].x -= BLOCK_SIZE * 2
                else:
                    current_block[0].x -= BLOCK_SIZE
                    current_block[0].y -= BLOCK_SIZE
                    current_block[2].x += BLOCK_SIZE
                    current_block[2].y += BLOCK_SIZE
                    current_block[3].x += BLOCK_SIZE * 2
            else:
                if current_block[0].x < current_block[3].x:
                    current_block[0].x -= BLOCK_SIZE
                    current_block[0].y += BLOCK_SIZE
                    current_block[2].x += BLOCK_SIZE
                    current_block[2].y -= BLOCK_SIZE
                    current_block[3].y -= BLOCK_SIZE * 2
                else:
                    current_block[0].x += BLOCK_SIZE
                    current_block[0].y -= BLOCK_SIZE
                    current_block[2].x -= BLOCK_SIZE
                    current_block[2].y += BLOCK_SIZE
                    current_block[3].y += BLOCK_SIZE * 2
        elif block_queue[0] == "T":
            if current_block[0].x == current_block[2].x:
                if current_block[0].x > current_block[1].x:
                    current_block[0].x -= BLOCK_SIZE
                    current_block[0].y += BLOCK_SIZE
                    current_block[1].x += BLOCK_SIZE
                    current_block[1].y += BLOCK_SIZE
                    current_block[3].x -= BLOCK_SIZE
                    current_block[3].y -= BLOCK_SIZE
                else:
                    current_block[0].x += BLOCK_SIZE
                    current_block[0].y -= BLOCK_SIZE
                    current_block[1].x -= BLOCK_SIZE
                    current_block[1].y -= BLOCK_SIZE
                    current_block[3].x += BLOCK_SIZE
                    current_block[3].y += BLOCK_SIZE
            else:
                if current_block[0].x > current_block[1].x:
                    current_block[0].x -= BLOCK_SIZE
                    current_block[0].y -= BLOCK_SIZE
                    current_block[1].x -= BLOCK_SIZE
                    current_block[1].y += BLOCK_SIZE
                    current_block[3].x += BLOCK_SIZE
                    current_block[3].y -= BLOCK_SIZE                   
                else:
                    current_block[0].x += BLOCK_SIZE
                    current_block[0].y += BLOCK_SIZE
                    current_block[1].x += BLOCK_SIZE
                    current_block[1].y -= BLOCK_SIZE
                    current_block[3].x -= BLOCK_SIZE
                    current_block[3].y += BLOCK_SIZE


def check_full_row(all_blocks, row_dictionary):
    global score

    for y in row_dictionary:
        row_dictionary[y] = 0

    for block in all_blocks:
        for square_index in range(len(block) - 1):
            row_dictionary[block[square_index].y] += 1
        
    for y in row_dictionary:
        if row_dictionary[y] == 10:
            for block in all_blocks:
                setback = 0
                for square_index in range(len(block) - 1):
                    if block[square_index - setback].y == y:
                        block.pop(square_index - setback)
                        setback += 1
            
            for block in all_blocks:
                for square_index in range(len(block) - 1):
                    if block[square_index].y < y:
                        block[square_index].y += BLOCK_SIZE
            
            score += 100


def start_loop():
    global screen

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                running = False

        screen.fill((0, 0, 0))

        start_loop_font = pygame.font.Font(None, 100)
        text = start_loop_font.render("Press any key to begin", True, (255, 255, 255))
        screen.blit(text, (30, 290))

        pygame.display.update()


def tetris():
    global screen, running, score

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    start_loop()

    TIMER_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(TIMER_EVENT, 1000)

    blocks = ["S", "Z", "I", "O", "J", "L", "T"]
    block_queue = [random.choice(blocks), random.choice(blocks)]
    all_blocks = []
    current_block = create_current_block(all_blocks, block_queue)
    all_blocks.append(current_block)

    row_dictionary = {}
    for y in range(100, 700, 30):
        row_dictionary[y] = 0

    score = 0
    running = True
    while running:
        is_placed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == TIMER_EVENT:
                is_placed = move_current_block(all_blocks, current_block, "Down")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    rotate_current_block(all_blocks, block_queue, current_block)
                elif event.key == pygame.K_DOWN:
                    is_placed = move_current_block(all_blocks, current_block, "Down")
                elif event.key == pygame.K_LEFT:
                    is_placed = move_current_block(all_blocks, current_block, "Left")
                elif event.key == pygame.K_RIGHT:
                    is_placed = move_current_block(all_blocks, current_block, "Right")

        if is_placed == True:
            check_full_row(all_blocks, row_dictionary)
            block_queue.pop(0)
            block_queue.append(random.choice(blocks))
            current_block = create_current_block(all_blocks, block_queue)
            all_blocks.append(current_block)

        screen.fill((0, 0, 0))
        draw_all_blocks(all_blocks)
        draw_next_block(block_queue)
        draw_board()

        pygame.display.update()
    
    end_loop()


def end_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.draw.rect(screen, (0, 0, 0), (275, 225, 250, 251), 0)
        pygame.draw.rect(screen, (255, 255, 255), (275, 225, 250, 251), 1)

        end_loop_font = pygame.font.Font(None, 100)
        text = end_loop_font.render("Game", True, (255, 0, 0))
        screen.blit(text, (300, 260))

        text = end_loop_font.render("Over", True, (255, 0, 0))
        screen.blit(text, (317, 370))
        
        pygame.display.update()

    pygame.quit()


tetris()
