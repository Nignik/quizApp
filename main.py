from tkinter import *
from tkinter import messagebox
import pandas
from random import randint

# ---------------------------- CONSTANTS ------------------------------- #
BLACK = "#0D0208"
GREY = "#3C4048"
PURPLE = "#3F0071"
PINK = "#FB2576"
MATRIX = "#008F11"

score = 0
with open("max_score.txt") as score_file:
    max_score = score_file.read()

# ---------------------------- INITIALIZATION ------------------------------- #

data = pandas.read_csv("quiz_data.csv")

data_dict = data.to_dict()
temp_list = data["question"].to_list()
nr_question = randint(1, len(temp_list) - 1)

question = data_dict["question"][nr_question]
right_answer = data_dict["answer"][nr_question]

# ---------------------------- GET QUESTION ------------------------------- #
def get_data():
    global question
    global right_answer
    data = pandas.read_csv("quiz_data.csv")

    data_dict = data.to_dict()
    temp_list = data["question"].to_list()
    nr_question = randint(1, len(temp_list) - 1)

    question = data_dict["question"][nr_question]
    right_answer = data_dict["answer"][nr_question]

    question_label.config(text=f"{question}")

# ---------------------------- SUBMIT ------------------------------- #
def submit(event):
    global right_answer
    global score
    global max_score
    answer = answer_entry.get()

    if answer == right_answer:
        answer_entry.delete(0, END)
        score += 1
        if score > int(max_score):
            with open("max_score.txt", "w") as score_file:
                score_file.write(str(score))
                max_score = score
            max_score_label.config(text=f"Max score: {max_score}", bg=BLACK, fg=MATRIX, font=("", 10))
    else:
        messagebox.askquestion(title="WRONG", message=f"Right answer is:\n{right_answer}\nYour answer was:\n{answer}\nCONTINUE?")
        answer_entry.delete(0, END)
        score = 0

    score_label.config(text=f"Score: {score}", bg=BLACK, fg=MATRIX, font=("", 10))
    get_data()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Quiz App")
window.geometry("650x300")
window.config(padx=50, pady=50, bg=BLACK)
window.eval("tk::PlaceWindow . center")

# Labels
question_label = Label(text=f"{question}", bg=BLACK, fg=MATRIX, font=("", 10))
question_label.grid(row=0, column=0, pady=20, columnspan= 3)

answer_label = Label(text="Answer:", bg=BLACK, fg=MATRIX, font=("", 10))
answer_label.grid(row=1, column=0, pady=20)

score_label = Label(text=f"Score: {score}", bg=BLACK, fg=MATRIX, font=("", 10))
score_label.grid(row=2, column=0, pady=10)

max_score_label = Label(text=f"Max score: {max_score}", bg=BLACK, fg=MATRIX, font=("", 10))
max_score_label.grid(row=3, column=0, pady=10)

# Entries
answer_entry = Entry(width=70, bg=BLACK, fg=MATRIX)
answer_entry.grid(row=1, column=1)
answer_entry.focus()


window.bind('<Return>', submit)







window.mainloop()