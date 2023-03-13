import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.text_box.bind('<KeyRelease>', self.on_modified)
        self.text = ""
        self.remaining_time = 5
        self.update_label()

    def create_widgets(self):
        self.text_box = tk.Text(self, width=120, height=50)
        self.text_box.pack()

    def on_modified(self, event=None):
        self.text = self.text_box.get("1.0", "end-1c")
        self.remaining_time = 5
        self.update_timer()

    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.master.after(10000, self.update_timer)


    def update_label(self):
        if self.remaining_time == 0:
            print('END')
            self.master.destroy()
        else:
            self.master.after(1000, self.update_label)


root = tk.Tk()
root.minsize(1100, 720)
app = Application(master=root)
app.mainloop()

