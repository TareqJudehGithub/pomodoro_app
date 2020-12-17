from tkinter import Canvas
from app_UI import UI

ui = UI()
timer_text = ui.timer_text()


class Timer:
    def __init__(self):
        self.WORK_MIN = 1
        self.SHORT_BREAK_MIN = 2
        self.LONG_BREAK_MIN = 20
        self.reps = 0
        self.timer = None

    def count_down(self, count):
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
            timer = window.after(1000, count_down, count - 1)
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


