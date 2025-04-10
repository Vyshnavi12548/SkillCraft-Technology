import tkinter as tk

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("300x250")
        self.root.resizable(False, False)

        self.running = False
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0

        self.time_display = tk.Label(root, text="00:00:00", font=("Helvetica", 40), fg="#333")
        self.time_display.pack(pady=30)

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.start_btn = tk.Button(btn_frame, text="Start", width=10, command=self.start)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.pause_btn = tk.Button(btn_frame, text="Pause", width=10, command=self.pause)
        self.pause_btn.grid(row=0, column=1, padx=5)

        self.reset_btn = tk.Button(root, text="Reset", width=23, command=self.reset)
        self.reset_btn.pack(pady=10)

    def update_time(self):
        if self.running:
            self.milliseconds += 10
            if self.milliseconds >= 1000:
                self.milliseconds = 0
                self.seconds += 1
            if self.seconds >= 60:
                self.seconds = 0
                self.minutes += 1

            formatted_time = f"{self.minutes:02d}:{self.seconds:02d}:{self.milliseconds//10:02d}"
            self.time_display.config(text=formatted_time)

            self.root.after(10, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def pause(self):
        self.running = False

    def reset(self):
        self.running = False
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.time_display.config(text="00:00:00")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
