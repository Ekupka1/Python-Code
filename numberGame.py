from tkinter import *
import random

if __name__ == '__main__':
  app.run(debug=True)

attempts = 10

answer = random.randint(0,100)

def check_answer():
    global attempts
    global text

    attempts -= 1
    guess = int(entry_window.get())

    if answer == guess:
        text.set("You win!")
        btn_check.pack_forget()
    elif attempts == 0 :
        text.set("You ran out of attempts")
        btn_check.pack_forget()
    elif guess < answer:
        text.set("Incorrect " + str(attempts) + " remaining - TRY HIGHER")
    elif guess > answer:
        text.set("Incorrect " + str(attempts) + " remaining - TRY LOWER")
    return

root = Tk()

root.title("Guess The Number")
root.geometry("500x150")

label = Label(root, text="Guess the number between 0 and 100")
label.pack()

entry_window = Entry(root, width=40, borderwidth=4)
entry_window.pack()

btn_check = Button(root, text="Check", command=check_answer)
btn_check.pack()

btn_quit = Button(root, text="Quit", command=root.destroy)
btn_quit.pack()

text = StringVar()
text.set("You have 10 attemps remaining")

guess_attempt = Label(root, textvariable=text)
guess_attempt.pack()

root.mainloop()
