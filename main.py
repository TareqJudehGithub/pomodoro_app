from tkinter import Tk, Canvas, PhotoImage, Label, Button

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER STOP/RESET ------------------------------- #
def reset_timer():
    # Stop Timer:
    window.after_cancel(timer)

    # Change timer label back to "Timer":
    timer_label.config(text="Timer", fg=GREEN)

    # timer counter reset:
    canvas.itemconfig(timer_text, text="00:00")

    # mark_check reset:
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global timer_label

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec - 1)
        print(reps)
        timer_label.config(text="Long Break", fg=GREEN)

    elif reps % 2 == 0:
        count_down(short_break_sec - 1)
        print(reps)
        timer_label.config(text="Short Break", fg="orange")

    else:
        count_down(work_sec - 1)
        print(reps)
        timer_label.config(text="Coding Time!", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count, *args):
    # Convert seconds to minutes:
    count_min = count // 60
    # The remainder of a min, is the seconds counter:
    count_sec = count % 60
    # Update Timer text:

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"0{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(100, count_down, count - 1)
    else:
        start_timer()
        # Add a check mark after each working session:
        if reps % 2 == 0:
            check_marks = ""
            work_session = reps // 2
            print(f"Work Session: {work_session}")
            for _ in range(work_session):
                check_marks += "✓"
            check_label.config(text=check_marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

# TODO Setting up the UI:
# Canvas
canvas = Canvas(width=200, height=240, bg=YELLOW, highlightthickness=0)
# Adding image:
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

# Timer:
timer_text = canvas.create_text(
    100, 140, text="00:00", fill="white", font=(FONT_NAME, 25, "bold")
)
canvas.grid(column=1, row=1)

# Labels:
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, width=13,
                    font=(FONT_NAME, 20, "bold"))
timer_label.config(pady=30)
timer_label.grid(column=1, row=0)

check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
check_label.grid(column=1, row=3)

# Buttons:
start_btn = Button(
    text="Start", bg=YELLOW, font=(FONT_NAME, 10, "bold"), command=start_timer
)
start_btn.config(pady=10)
start_btn.grid(column=0, row=2)

reset_btn = Button(
    text="Reset", bg=YELLOW, font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset_btn.config(pady=10)
reset_btn.grid(column=2, row=2)

window.mainloop()
