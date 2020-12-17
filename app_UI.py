from tkinter import Tk, Canvas, PhotoImage, Label, Button
YELLOW = "#f7f5dd"
IMAGE = PhotoImage(file="tomato.png")

# TODO Setting up the UI:
class Canvas(Canvas):
    def __init__(self, width, height, bg, highlightthickness):
        super().__init__()
        self.width = width
        self.height = height
        self.bg = bg
        self.highlightthickness = highlightthickness
        self.image()

    def image(self):
        self.create_image(100, 112, image=IMAGE)

# class UI:
#     def __init__(self):
#         self.PINK = "#e2979c"
#         self.RED = "#e7305b"
#         self.GREEN = "#9bdeac"
#         self.YELLOW = "#f7f5dd"
#         self.FONT_NAME = "Courier"
#         self.timer = None
#         self.timer_text = None
#
#     def window(self):
#         window = Tk()
#         window.title("El Pomodoro")
#         window.title("Pomodoro")
#         window.config(padx=50, pady=50, bg=self.YELLOW)
#
#         # Adding image using Canvas:
#         canvas = Canvas(width=200, height=240, bg=self.YELLOW,
#                         highlightthickness=0)
#         tomato_img = PhotoImage(file="tomato.png")
#         canvas.create_image(100, 112, image=tomato_img)
#         self.timer_text = canvas.create_text(
#             100, 140, text="00:00", fill="white",
#             font=(self.FONT_NAME, 25, "bold")
#         )
#         canvas.grid(column=1, row=1)
#
#         self.label()
#         self.buttons()
#
#         window.mainloop()
#
#     def label(self):
#         # Labels:
#         timer_label = Label(text="Timer", fg=self.GREEN, bg=self.YELLOW,
#                             width=13,
#                             font=(self.FONT_NAME, 20, "bold"))
#         timer_label.config(pady=30)
#         timer_label.grid(column=1, row=0)
#
#         check_label = Label(fg=self.GREEN, bg=self.YELLOW,
#                             font=(self.FONT_NAME, 30, "bold"))
#         check_label.grid(column=1, row=3)
#
#     def buttons(self):
#         # Buttons:
#         start_btn = Button(
#             text="Start", bg=self.YELLOW, font=(self.FONT_NAME, 10, "bold"),
#             # command=start_timer
#         )
#         start_btn.config(pady=10)
#         start_btn.grid(column=0, row=2)
#
#         reset_btn = Button(
#             text="Reset", bg=self.YELLOW, font=(self.FONT_NAME, 10, "bold"),
#             # command=reset_timer
#         )
#         reset_btn.config(pady=10)
#         reset_btn.grid(column=2, row=2)
#
#     def timer_text(self):
#         # Timer text:
#         self.timer_text = self.canvas.create_text(
#             100, 140, text="00:00", fill="white",
#             font=(self.FONT_NAME, 25, "bold")
#         )
#
#     def count_down(self):
#         # Convert seconds to minutes:
#         count_min = self.timer // 60
#         # The remainder of a min, is the seconds counter:
#         count_sec = self.timer % 60
#         # Update Timer text:
#
#         if count_sec < 10:
#             count_sec = f"0{count_sec}"
#
#         self.canvas.itemconfig(self.timer_text(), text=f"0{count_min}:{count_sec}")
#         if self.timer > 0:
#             self.timer = self.window().after(1000, self.count_down(), self.timer - 1)
#         # else:
        #     start_timer()
        #     # Add a check mark after each working session:
        #     if reps % 2 == 0:
        #         check_marks = ""
        #         work_session = reps // 2
        #         print(f"Work Session: {work_session}")
        #         for _ in range(work_session):
        #             check_marks += "✓"
        #         check_label.config(text=check_marks)
