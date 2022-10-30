from tkinter import *
from tkinter import messagebox
import pandas
from random import choice, randint

# ---------------------------- CONSTANTS ------------------------------- #
BLACK = "#0D0208"
GREY = "#3C4048"
PURPLE = "#3F0071"
PINK = "#FB2576"
MATRIX = "#008F11"

# ---------------------------- ADDING NEW ENTRY ------------------------------- #
def save():
    question = question_entry.get()
    answer = answer_entry.get()

    if len(question) == 0 or len(answer) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        with open("quiz_data.csv", "a") as quiz_data:
            quiz_data.write(f"\n{question},{answer}")
            question_entry.delete(0, END)
            answer_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Quiz App")
window.geometry("650x300")
window.config(padx=50, pady=50, bg=BLACK)
window.eval("tk::PlaceWindow . center")

# Labels
question_label = Label(text="Question: ", bg=BLACK, fg=MATRIX, font=("", 10))
question_label.grid(row=0, column=0, pady=20)

answer_label = Label(text="Answer:", bg=BLACK, fg=MATRIX, font=("", 10))
answer_label.grid(row=1, column=0, pady=20)

# Entries
question_entry = Entry(width=70, bg=BLACK, fg=MATRIX)
question_entry.grid(row=0, column=1)
question_entry.focus()

answer_entry = Entry(width=70, bg=BLACK, fg=MATRIX)
answer_entry.grid(row=1, column=1)


#Buttons
add_button = Button(text="Add", width=59, bg=BLACK, fg=MATRIX, command=save)
add_button.grid(row=2, column=1)





window.mainloop()