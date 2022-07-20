from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# ---------------------------- UI SETUP ------------------------------- #
try:
    df = pd.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    to_learn = pd.read_csv("data/spanish_english.csv").to_dict(orient="records")
else:
    to_learn = df
def get_word():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    spanish_word = current_card["Spanish"]
    canvas.itemconfig(item_title,text="Spanish",fill = "black")
    canvas.itemconfig(item_word,text=spanish_word,fill="black")
    canvas.itemconfig(card_background, image = front_of_card)
    flip_timer=window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(item_title, text="English",fill = "white")
    canvas.itemconfig(item_word, text=current_card["English"],fill="white")
    canvas.itemconfig(card_background, image=back_of_card)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data=pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    get_word()





window = Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526)
back_of_card = PhotoImage(file="images/card_back.png")
front_of_card = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=front_of_card)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
item_title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
item_word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

cross_image=PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0,command=get_word)
unknown_button.grid(row=1,column=0)

checkmark_image = PhotoImage(file="images/right.png")
known_button = Button(image=checkmark_image,highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)

get_word()

#--------------------Buttons-------------------------------------------------------------

window.mainloop()