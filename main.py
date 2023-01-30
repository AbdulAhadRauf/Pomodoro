from tkinter import *
import math

TIMERLAB = "TIMER"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ""
the_timer = None


def reset_timer():
    global the_timer
    window.after_cancel(the_timer)
    timer_label.config(text= "TIMER", fg= GREEN)
    canvas.itemconfig(c_text, text= "00:00")
    check_mark.config(text= '')


def timer():
    global reps
    reps+=1

    lbreaksec = LONG_BREAK_MIN*60
    sbreaksec = SHORT_BREAK_MIN*60
    worksec = WORK_MIN*60

    if reps%8==0:
        count(lbreaksec)
        canvas.itemconfig(timer_label, text ="Long Break", fg=RED)
    elif reps%2==0:
        count(sbreaksec)
        canvas.itemconfig(timer_label, text ="Short Break", fg=PINK)
    else:
        count(worksec)
    

def count(c):
    global reps, the_timer
    actual_mins = math.floor(c/60)
    actual_secs = c % 60
    if actual_secs <10:
        actual_secs = f"0{actual_secs}"
    canvas.itemconfig(c_text, text= f"{actual_mins}:{actual_secs}")
    if c >0 :
        the_timer = window.after(1000, count, c-1)
    else:
        timer()
        if reps%2==0:
            marks += "✔"


window = Tk()
window.title(string="Pomodoro")
window.config(bg= YELLOW, padx= 100, pady= 50)

timer_label = Label(text= TIMERLAB, bg= YELLOW, fg= GREEN, font= (FONT_NAME, 35,"bold"))
timer_label.grid(row=0,column= 1)

canvas = Canvas(bg=YELLOW, width= 200, height= 224, highlightthickness= 0)
tomato_image = PhotoImage(file= "tomato.png")
canvas.create_image(100,112,image= tomato_image)
c_text = canvas.create_text(100,130, text= "00:00", fill="white",font= (FONT_NAME, 20, "bold"))
canvas.grid(row=1,column= 1)

start_button = Button(text= "Start", command = timer, highlightthickness= 0)
start_button.grid(row=2, column=0)

reset_button = Button(text= "Reset", command= reset_timer , highlightthickness= 0)
reset_button.grid(row=2, column=2)

check_mark = Label(text = marks, bg = YELLOW, fg= GREEN)
check_mark.grid(row=3, column= 1)


window.mainloop()