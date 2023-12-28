import tkinter as tk

import cal


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("CalBySachin")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
     cal = Calculator()
     cal.run()
