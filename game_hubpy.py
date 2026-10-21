from tkinter import *
from tkinter import messagebox
import random
import threading
import turtle
import time


def add_starry_background(window, bg_color="#ffe6f0", star_color="yellow"):
    canvas = Canvas(window, bg=bg_color, width=400, height=300, highlightthickness=0)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)
    for _ in range(80):
        x, y = random.randint(0, 400), random.randint(0, 300)
        r = random.randint(1, 3)
        canvas.create_oval(x, y, x + r, y + r, fill=star_color, outline="")

# ========== Guess the Number ==========
def play_guess():
    window = Toplevel()
    window.title("Guess the Number")
    window.geometry("400x300")
    add_starry_background(window)

    secret = random.randint(1, 100)
    attempts = IntVar(value=0)

    def check_guess():
        try:
            guess = int(entry.get())
            attempts.set(attempts.get() + 1)
            if guess < secret:
                result.config(text="Too low! Try higher.", fg="#cc6600")
            elif guess > secret:
                result.config(text="Too high! Try lower.", fg="#9933ff")
            else:
                result.config(text=f"Correct! It took you {attempts.get()} tries!", fg="#00cc66")
        except ValueError:
            result.config(text="Please enter a number!", fg="red")

    Label(window, text="Guess the number between 1-100", font=("Comic Sans MS", 14), bg="#ffe6f0").pack(pady=10)
    entry = Entry(window, font=("Comic Sans MS", 14), justify='center')
    entry.pack()
    Button(window, text="Check", font=("Arial", 12), command=check_guess, bg="#ff6699", fg="white").pack(pady=10)
    result = Label(window, text="", font=("Arial", 12), bg="#ffe6f0")
    result.pack()

# ========== Rock Paper Scissors ==========
def play_rps():
    window = Toplevel()
    window.title("Rock Paper Scissors")
    window.geometry("400x400")
    window.configure(bg="#ffe6f0")
    add_starry_background(window)

    player_score = IntVar(value=0)
    computer_score = IntVar(value=0)
    result_text = StringVar()

    choices = {"✊": "Rock", "✋": "Paper", "✌️": "Scissors"}
    def play(user_emoji):
        user_choice = choices[user_emoji]
        comp_emoji, comp_choice = random.choice(list(choices.items()))
        result_line = f"You: {user_emoji} ({user_choice})\nComputer: {comp_emoji} ({comp_choice})\n"
        if user_choice == comp_choice:
            result_text.set(result_line + "It's a Tie!")
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Scissors" and comp_choice == "Paper") or \
             (user_choice == "Paper" and comp_choice == "Rock"):
            player_score.set(player_score.get() + 1)
            result_text.set(result_line + "You Win!")
        else:
            computer_score.set(computer_score.get() + 1)
            result_text.set(result_line + "Computer Wins!")

        if player_score.get() == 5:
            messagebox.showinfo("Game Over", "You won the match!")
            reset_game()
        elif computer_score.get() == 5:
            messagebox.showinfo("Game Over", "Computer won the match!")
            reset_game()

    def reset_game():
        player_score.set(0)
        computer_score.set(0)
        result_text.set("")

    Label(window, text="Rock Paper Scissors", font=("Comic Sans MS", 16, "bold"), bg="#ffe6f0", fg="#cc0066").pack(pady=10)
    Label(window, text="First to 5 wins!", font=("Arial", 10), bg="#ffe6f0", fg="gray").pack()

    score_frame = Frame(window, bg="#ffe6f0")
    score_frame.pack(pady=10)
    Label(score_frame, text="You:", bg="#ffe6f0", fg="black").grid(row=0, column=0)
    Label(score_frame, textvariable=player_score, bg="#ffe6f0", fg="green").grid(row=0, column=1)
    Label(score_frame, text="Computer:", bg="#ffe6f0", fg="black").grid(row=0, column=2)
    Label(score_frame, textvariable=computer_score, bg="#ffe6f0", fg="red").grid(row=0, column=3)

    for emoji in choices.keys():
        Button(window, text=emoji, font=("Arial", 20), width=4,
               command=lambda e=emoji: play(e), bg="#ff99cc", fg="white").pack(pady=5)

    Label(window, textvariable=result_text, bg="#ffe6f0", fg="#9933ff", wraplength=350, font=("Arial", 12)).pack(pady=20)
    Button(window, text="Reset Game", command=reset_game, bg="#cc0066", fg="white").pack()

# ========== Hangman ==========
def play_hangman():
    window = Toplevel()
    window.title("Hangman")
    window.geometry("400x300")
    add_starry_background(window)

    words = ["python", "hangman", "game", "student", "project"]
    word = random.choice(words)
    hidden = ["_" for _ in word]

    def guess():
        letter = entry.get().lower()
        entry.delete(0, END)
        if letter in word:
            for i, l in enumerate(word):
                if l == letter:
                    hidden[i] = letter
        word_label.config(text=" ".join(hidden))
        if "_" not in hidden:
            messagebox.showinfo("Hangman", "You Win!")
            window.destroy()

    word_label = Label(window, text=" ".join(hidden), bg="#ffe6f0", fg="black", font=("Courier", 20, "bold"))
    word_label.pack(pady=10)
    entry = Entry(window, font=("Arial", 14), justify='center')
    entry.pack()
    Button(window, text="Guess", command=guess, bg="#ff6699", fg="white").pack(pady=10)

# ========== Snake ==========
def play_snake():
    def run_snake():
        wn = turtle.Screen()
        wn.title("Snake Game")
        wn.bgcolor("#ffe6f0")
        wn.setup(width=600, height=600)
        wn.tracer(0)

        head = turtle.Turtle()
        head.shape("turtle")
        head.color("green")
        head.penup()
        head.goto(0, 0)
        head.direction = "stop"

        segments = []

        food = turtle.Turtle()
        food.shape("circle")
        food.color("red")
        food.penup()
        food.goto(0, 100)
        def go_up():
            if head.direction != "down":
                head.direction = "up"

        def go_down(): 
            if head.direction != "up":
                head.direction = "down"

        def go_left():
            if head.direction != "right":
                head.direction = "left"

        def go_right():
            if head.direction != "left":
                head.direction = "right"

        def move():
            if head.direction == "up":
                head.sety(head.ycor() + 20)
            if head.direction == "down":
                head.sety(head.ycor() - 20)
            if head.direction == "left":
                head.setx(head.xcor() - 20)
            if head.direction == "right":
                head.setx(head.xcor() + 20)

           
            if head.xcor() > 290:
                head.setx(-290)
            elif head.xcor() < -290:
                head.setx(290)
            if head.ycor() > 290:
                head.sety(-290)
            elif head.ycor() < -290:
                head.sety(290) 
        wn.listen()
        wn.onkeypress(go_up, "Up")
        wn.onkeypress(go_down, "Down")
        wn.onkeypress(go_left, "Left")
        wn.onkeypress(go_right, "Right")

        while True:
            wn.update()
            if head.distance(food) < 20:
                x = random.randint(-280, 280)
                y = random.randint(-280, 280)
                food.goto(x, y)

                segment = turtle.Turtle()
                segment.shape("square")
                segment.color("lightgreen")
                segment.penup()
                segments.append(segment)

            for i in range(len(segments)-1, 0, -1):
                x = segments[i-1].xcor()
                y = segments[i-1].ycor()
                segments[i].goto(x, y)

            if segments:
                segments[0].goto(head.xcor(), head.ycor())

            move()
            time.sleep(0.1)

    threading.Thread(target=run_snake).start()

# ========== Main Menu ==========
def main_menu():
    root = Tk()
    root.title("Student Game Hub")
    root.geometry("400x500")
    root.configure(bg="#ffe6f0")
    add_starry_background(root)

    Label(root, text="Welcome to Student Game Hub!", font=("Comic Sans MS", 16, "bold"), fg="#cc0066", bg="#ffe6f0").pack(pady=20)
    Label(root, text="Choose a game to play:", font=("Arial", 12), fg="black", bg="#ffe6f0").pack(pady=5)

    Button(root, text="Guess the Number", width=30, bg="#ff99cc", fg="white", command=play_guess).pack(pady=8)
    Button(root, text="Rock Paper Scissors", width=30, bg="#ff66b2", fg="white", command=play_rps).pack(pady=8)
    Button(root, text="Hangman", width=30, bg="#ff6699", fg="white", command=play_hangman).pack(pady=8)
    Button(root, text="Snake Game", width=30, bg="#ff3399", fg="white", command=play_snake).pack(pady=8)
    Button(root, text="Exit", width=30, bg="gray", fg="white", command=root.destroy).pack(pady=20)

    root.mainloop()

main_menu() 
