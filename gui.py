import tkinter as tk
import Register

class RegisterWidget(tk.Frame):
    def __init__(self, parent, reg, index):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.initUI(reg, index)
    def initUI(self, reg, index):
        self.register_frame = tk.LabelFrame(text='Register' + str(index))
        self.register_name = tk.Label(self.register_frame, text=reg.register_name).pack()
        colNum = (index//10)
        index = index - (colNum*10)
        colNum += 1
        self.register_frame.grid(row=index, column=colNum, padx=2, pady=2)
        # self.register_frame.pack()

class RegisterWindow(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.registers = parent.registers
        self.initUI()

    def initUI(self):
        self.registers_frame = tk.LabelFrame(text='REGISTERS')
        for dex, item in enumerate(self.registers):
            self.temp_wid = RegisterWidget(self.registers_frame, item, dex)
            # self.temp_wid.grid(row=0, column=1)

        self.registers_frame.grid(row=0, column=1, rowspan=10, columnspan=4, padx=5, pady=5)


# input for code
class InputBox(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.initUI()

    def initUI(self):
        self.text_frame = tk.LabelFrame(text='CODE')
        self.text_box = tk.Text(self.text_frame).pack(side='left')
        self.text_frame.grid(row=0, column=0, rowspan=10, padx=1, pady=1)

class ErrorWindow(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.initUI()

    def initUI(self):
        self.error_frame = tk.LabelFrame(text='ERRORS')
        self.error_window = tk.Text(self.error_frame).pack()
        self.error_frame.grid(row=11, column=0, columnspan=2)

class MainWIndow(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.get_data()
        self.initUI()


    def initUI(self):
        self.parent.title("My Application")

        self.pack()

        self.text_area = InputBox(self)
        # self.text_area.grid(row=0, column=0)

        self.register_area = RegisterWindow(self)
        # self.register_area.grid(row=0, column=1)

        self.error_area = ErrorWindow(self)
        # self.error_area.grid(row=1, column=0, columnspan=2)



    def get_data(self):
        self.registers = []

        for i in range(1, 34):
            self.registers.append(Register.Register(i))





if __name__ == "__main__":

    root = tk.Tk()
    MainWIndow(root).grid(row=0, column=0)
    # root.resizable(0,0)
    root.mainloop()