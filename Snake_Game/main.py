import tkinter as tk
import random


def update_score(snake, score):
    score["text"] = f"Skor: {len(snake) - 1}"


def control_collision(canvas, snake):
    if len(snake) > 2:
        for body_part in range(len(snake) - 1):
            if canvas.coords(snake[body_part]) == canvas.coords(snake[len(snake) - 1]):
                game_over = tk.Label(root, text="GAME OVER", width=21, height=12, bg="black", fg="red", font=("Arial, 40"))
                game_over.place(x=0, y=0)
                end_score = tk.Label(root, text=f"Skor: {len(snake) - 1}", width=5, height=1, bg="black", fg="red", font=("Arial, 20"))
                end_score.place(x=285, y=280)
    
    coords = canvas.coords(snake[len(snake) - 1])
    if coords[0] >= 630 or coords[0] < 0 or coords[1] >= 630 or coords[1] < 0:
        game_over = tk.Label(root, text="GAME OVER", width=21, height=12, bg="black", fg="red", font=("Arial, 40"))
        game_over.place(x=0, y=0)
        end_score = tk.Label(root, text=f"Skor: {len(snake) - 1}", width=5, height=1, bg="black", fg="red", font=("Arial, 20"))
        end_score.place(x=285, y=280)


def create_food(canvas, snake, food):
    while True:
        x = random.randint(0, 20)
        y = random.randint(0, 20)

        new_food = canvas.create_oval(0 + (x * 30), 0 + (y * 30), 30 + (x * 30), 30 + (y * 30), fill="red", outline="gray")

        same_coordinates = False
        for body_part in snake:
            if canvas.coords(body_part) == canvas.coords(new_food):
                same_coordinates = True
        
        if same_coordinates == False:
            break

    food.append(new_food)


def eat_food(canvas, snake, food):
    canvas.delete(food[0])
    food.clear()

    coords = canvas.coords(snake[0])
    new_body_part = canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill="lightgreen", outline="gray")

    snake.insert(0, new_body_part)
    create_food(canvas, snake, food)


def movement(canvas, snake, food, score, direction):
    global after_id
    try:
        canvas.after_cancel(after_id)
    except NameError:
        pass

    if direction == "Up":
        move_snake_up(canvas, snake, food, score)
    if direction == "Down":
        move_snake_down(canvas, snake, food, score)
    if direction == "Left":
        move_snake_left(canvas, snake, food, score)
    if direction == "Right":
        move_snake_right(canvas, snake, food, score)


def move_snake_up(canvas, snake, food, score):
    global after_id

    for body_part in range(1, len(snake)):
        canvas.coords(snake[body_part - 1], canvas.coords(snake[body_part]))
    canvas.move(snake[len(snake) - 1], 0, -30)

    if canvas.coords(snake[len(snake) - 1]) == canvas.coords(food[0]):
        eat_food(canvas, snake, food)

    control_collision(canvas, snake)
    update_score(snake, score)

    after_id = canvas.after(100, lambda: move_snake_up(canvas, snake, food, score))


def move_snake_down(canvas, snake, food, score):
    global after_id

    for body_part in range(1, len(snake)):
        canvas.coords(snake[body_part - 1], canvas.coords(snake[body_part]))
    canvas.move(snake[len(snake) - 1], 0, 30)

    if canvas.coords(snake[len(snake) - 1]) == canvas.coords(food[0]):
        eat_food(canvas, snake, food)

    control_collision(canvas, snake)
    update_score(snake, score)

    after_id = canvas.after(100, lambda: move_snake_down(canvas, snake, food, score))


def move_snake_left(canvas, snake, food, score):
    global after_id

    for body_part in range(1, len(snake)):
        canvas.coords(snake[body_part - 1], canvas.coords(snake[body_part]))
    canvas.move(snake[len(snake) - 1], -30, 0)

    if canvas.coords(snake[len(snake) - 1]) == canvas.coords(food[0]):
        eat_food(canvas, snake, food)

    control_collision(canvas, snake)
    update_score(snake, score)

    after_id = canvas.after(100, lambda: move_snake_left(canvas, snake, food, score))


def move_snake_right(canvas, snake, food, score):
    global after_id

    for body_part in range(1, len(snake)):
        canvas.coords(snake[body_part - 1], canvas.coords(snake[body_part]))
    canvas.move(snake[len(snake) - 1], 30, 0)

    if canvas.coords(snake[len(snake) - 1]) == canvas.coords(food[0]):
        eat_food(canvas, snake, food)

    control_collision(canvas, snake)
    update_score(snake, score)
        
    after_id = canvas.after(100, lambda: move_snake_right(canvas, snake, food, score))


def create_canvas(root):
    canvas = tk.Canvas(root, width=630, height=630, bg="black")

    line_count = 0
    while(line_count < 21):
        column_count = 0
        while(column_count < 21):
            canvas.create_rectangle(0 + (column_count * 30), 0 + (line_count * 30), 30 + (column_count * 30), 30 + (line_count * 30), outline="black")
            
            column_count += 1
        line_count += 1

    return canvas


def snake_game():
    global root
    root = tk.Tk()
    root.geometry("630x700")
    root.title("Snake Game")

    score = tk.Label(root, text="Skor: 0", width=22, height=1, font=("Arial, 35"))
    score.place(x=10, y=640)
    canvas = create_canvas(root)
    snake = [canvas.create_rectangle(300, 300, 330, 330, fill="lightgreen", outline="gray")]
    food = []
    create_food(canvas, snake, food)
    canvas.bind("<Up>", lambda event: movement(canvas, snake, food, score, "Up"))
    canvas.bind("<Down>", lambda event: movement(canvas, snake, food, score, "Down"))
    canvas.bind("<Left>", lambda event: movement(canvas, snake, food, score, "Left"))
    canvas.bind("<Right>", lambda event: movement(canvas, snake, food, score, "Right"))

    canvas.pack()
    canvas.focus_set()
    root.mainloop()


snake_game()
