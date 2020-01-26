from tkinter import *
import sys
import hashlib

class popupWindow(object):
    def __init__(self,master):
        self.master = master
        top = self.top = Toplevel(master)
        self.l = Label(top,text="Please enter your student email address:")
        self.l.pack()
        self.e = Entry(top)
        self.e.pack()
        self.b = Button(top,text='Submit',command=self.cleanup)
        self.b.pack()
        self.top.attributes("-topmost", True)

    def cleanup(self):
        self.value = self.e.get()
        self.top.destroy()

class mainWindow(object):
    def __init__(self,master):
        self.master = master
        self.master.geometry("400x400")
        self.master.title("Pre_class_work_selector")
        self.b = Button(master,text="Get Task",command=self.print_course)
        self.b.pack(pady=40)
        self.popup()

    def popup(self):
        if hasattr(self, 'label_warning'):
            self.label_warning.pack_forget()
            self.reopen_popup.pack_forget()
        self.w = popupWindow(self.master)
        self.master.wait_window(self.w.top)

    def entryValue(self):
        return self.w.value

    def print_course(self):
        try:
            problem_32 = self.problem_choice(self.w.value, '3.2', ['2-Logging', '3-Graphics'])
            problem_91 = self.problem_choice(self.w.value, '9.1', ['2-The Current Weather', '3-Crypto Exchange','4-Google directions', '5-Flying Aircraft'])

            self.label_top = Label(self.master,text='For seminar 3.2:').pack()
            self.label = Label(self.master,text=problem_32).pack()

            self.label_2_top = Label(self.master,text='For seminar 6.2:').pack()
            self.label_2 = Label(self.master,text=problem_91).pack()
        except AttributeError:
            self.label_warning = Label(self.master,text="You need to input your Minerva Email address first!")
            self.label_warning.pack()
            self.reopen_popup = Button(self.master,text="Enter Email",command=self.popup)
            self.reopen_popup.pack()

    def problem_choice(self, email, seminar, problems):
        email = email.strip().lower()
        if "@minerva.kgi.edu" not in email:
            raise AttributeError('Not Minerva Email Address')
        seminar = seminar.strip().lower()
        enc = (email + seminar).encode()
        md5 = hashlib.md5(enc).hexdigest()
        ind = int(md5, 16) % len(problems)
        return problems[ind]


if __name__ == "__main__":
    root=Tk()
    m=mainWindow(root)
    root.mainloop()
