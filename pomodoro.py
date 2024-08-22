from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    my_label.config(text="Timer", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
    checkmark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_sec)
        my_label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        my_label.config(text="Break", fg=PINK)

    else:
        count_down(work_sec)
        my_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
        # timer refreshes every 1000ms
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
            checkmark_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)
def say_sth(thing):
    print(thing)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# tomato_img = PhotoImage(file="tomato.png")
# canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()
my_label = Label(text="Timer", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
my_label.place(x=50, y=-30)
checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.place(x=88, y=240)
button_1 = Button(text="Start", command=start_timer)
button_1.place(x=-20, y=210)


button_2 = Button(text="Reset", command=reset_timer)
button_2.place(x=180, y=220)

window.mainloop()