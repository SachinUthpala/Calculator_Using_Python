import tkinter as tk

LIGTH_GRAY = "#F5F5F5"
LABLE_COLOR = "#25265E"
SMALL_TEXT = ("Arial", 16)
LARGE_FONT = ("Arial" , 40 , "bold")
WHITE = "#FFFFFF"
DIGIT_FONT_VALUE = ("Arial" , 24 , "bold")

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("CalBySachin")

        self.total_expression = "0"
        self.current_expression = "0"

        self.display_frame = self.create_display_frame()

        self.total_lable , self.lable = self.create_display_lables()

        self.button_frame = self.create_button_frame()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.create_digit_button()

    def create_display_lables(self):
        total_lable = tk.Label(self.display_frame, text= self.total_expression, anchor=tk.E,
                               bg=LIGTH_GRAY, fg=LABLE_COLOR, padx=24, font= SMALL_TEXT )
        total_lable.pack(expand=True, fill="both" )

        lable = tk.Label(self.display_frame, text= self.current_expression, anchor=tk.E,
                               bg=LIGTH_GRAY, fg=LABLE_COLOR, padx=24, font=LARGE_FONT )
        lable.pack(expand=True, fill="both" )

        return total_lable,lable

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGTH_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def create_digit_button(self):
        for digit, grid_valur in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), bg= WHITE, fg=LABLE_COLOR, font=DIGIT_FONT_VALUE, borderwidth=0 )
            button.grid(row=grid_valur[0], column=grid_valur[1], sticky=tk.NSEW)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
     cal = Calculator()
     cal.run()
