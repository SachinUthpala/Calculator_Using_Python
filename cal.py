import tkinter as tk

LIGTH_GRAY = "#F5F5F5"
LABLE_COLOR = "#25265E"
SMALL_TEXT = ("Arial", 16)
LARGE_FONT = ("Arial" , 40 , "bold")
WHITE = "#FFFFFF"
DIGIT_FONT_VALUE = ("Arial" , 24 , "bold")
DEFAULT_FONT_STYLE = ("Arial" , 20)
OFF_WHITE = "#F8FAFF"
LIGHT_BLUE = "#CCEDFF"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("CalBySachin")

        self.total_expression = ""
        self.current_expression = ""

        self.display_frame = self.create_display_frame()

        self.total_lable , self.lable = self.create_display_lables()

        self.button_frame = self.create_button_frame()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.create_digit_button()
        self.create_operator_buttons()
        self.create_special_buttona()

        self.button_frame.rowconfigure(0, weight=1)

        for x in range(1,5):
            self.button_frame.rowconfigure(x, weight=1)
            self.button_frame.columnconfigure(x, weight=1)

    def create_special_buttona(self):
        self.create_clear_button()
        self.create_equal_button()

    def create_display_lables(self):
        total_lable = tk.Label(self.display_frame, text= self.total_expression, anchor=tk.E,
                               bg=LIGTH_GRAY, fg=LABLE_COLOR, padx=24, font= SMALL_TEXT )
        total_lable.pack(expand=True, fill="both" )

        lable = tk.Label(self.display_frame, text= self.current_expression, anchor=tk.E,
                               bg=LIGTH_GRAY, fg=LABLE_COLOR, padx=24, font=LARGE_FONT )
        lable.pack(expand=True, fill="both" )

        return total_lable,lable


    def append_operator(self,operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_lable()
        self.update_lable()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGTH_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.button_frame, text=symbol, bg=OFF_WHITE, fg=LABLE_COLOR,
                               font=DEFAULT_FONT_STYLE, borderwidth=0, command= lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.total_expression = ""
        self.current_expression = ""
        self.update_total_lable()
        self.update_lable()
    def create_clear_button(self):
        button = tk.Button(self.button_frame, text="C", bg=OFF_WHITE, fg=LABLE_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command= self.clear)
        button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)



    def evaluvate(self):
        self.total_expression += self.current_expression
        self.update_total_lable()

        self.current_expression = str(eval(self.total_expression))
        self.total_expression = ""
        self.update_lable()

    def create_equal_button(self):
        button = tk.Button(self.button_frame, text="=", bg=LIGHT_BLUE, fg=LABLE_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command= self.evaluvate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value ):
        self.current_expression += str(value)
        self.update_lable()

    def create_digit_button(self):
        for digit, grid_valur in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), bg= WHITE, fg=LABLE_COLOR, font=DIGIT_FONT_VALUE,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_valur[0], column=grid_valur[1], sticky=tk.NSEW)

    def run(self):
        self.window.mainloop()

    def update_total_lable(self):
        self.total_lable.config(text=self.total_expression)

    def update_lable(self):
        self.lable.config(text=self.current_expression)



if __name__ == "__main__":
     cal = Calculator()
     cal.run()
