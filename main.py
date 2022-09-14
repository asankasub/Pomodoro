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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label["text"] = "Timer"
    tick_label["text"] = ""
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0



    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = 60*25
    short_break_sec = 5*60
    long_break_sec = 60*20
    
    reps += 1
    
    if len(tick_label["text"]) ==4:
        tick_label["text"]=""
    
    if reps == 2 or reps == 4 or reps == 6 or reps == 8 :
        tick_label["text"] += "✓"
    if reps == 9:
        reps = 1

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        timer_label["text"] = "Get working!"
        timer_label["fg"] = GREEN
    elif reps == 8:
        count_down(long_break_sec)
        timer_label["text"] = "Long break :))"
        timer_label["fg"] = RED
       
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_sec)
        timer_label["text"] = "Short break :)"
        timer_label["fg"] = PINK

   
  









# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        start_timer()
    
    
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodor")
window.config(padx=100, pady=50, bg=YELLOW)


canvas=Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_image=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_image)
canvas.grid(row=1,column=1)
timer_text = canvas.create_text(100, 130, text = "00:00", fill="white", font=(FONT_NAME, 35, "bold"))


timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
timer_label.grid(row = 0, column = 1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row = 2, column = 0)


reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row = 2, column = 2)

tick_label = Label(fg= GREEN, bg=YELLOW)
tick_label.grid(row=3, column=1)









window.mainloop()