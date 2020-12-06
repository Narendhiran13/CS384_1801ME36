from tkinter import *
from tkinter import messagebox
import datastore
import os
import time
import queue
import threading
import csv


class screen:
    def __init__(self):
        # DataStore & Tkinter variabless
        self.folder_mas = Tk()
        self.DataStore_user = datastore.user_datastore()
        # register variables
        self.roll_register = StringVar()
        self.password_register = StringVar()
        self.Name_register = StringVar()
        self.whatsapp_no_register = StringVar()
        # login variables
        self.roll_login = StringVar()
        self.password_login = StringVar()
        # Function runned
        self.screen()
        # -------------------------
        self.folder_mas.mainloop()

    def screen(self):
        # Header_file
        self.header = Label(self.folder_mas, text="Login", font=('', 35))
        self.header.pack()

        # login frame
        frame_login = Frame(self.folder_mas, padx=5, pady=5)
        Label(frame_login, text='Roll No. : ', font=(
            '', 20), pady=5, padx=5).grid(sticky=W)
        Entry(frame_login, textvariable=self.roll_login,
              bd=5, font=('', 15)).grid(row=0, column=1)
        Label(frame_login, text='Password : ', font=(
            '', 20), pady=5, padx=5).grid(sticky=W)
        Entry(frame_login, textvariable=self.password_login, bd=5,
              font=('', 15), show='*').grid(row=1, column=1)
        Button(frame_login, text=' Login : ', bd=3, font=('', 15),
               padx=5, pady=5, command=self.login).grid()
        Button(frame_login, text=' Register : ', bd=3, font=('', 15), padx=5,
               pady=5, command=self.rg_screen).grid(row=2, column=1)
        self.frame_login = frame_login
        self.frame_login.pack()

        # Register Frame
        frame_register = Frame(self.folder_mas)
        frame_register = Frame(self.folder_mas, padx=5, pady=5)
        Label(frame_register, text='Name: ', font=(
            '', 20), pady=5, padx=5).grid(sticky=W)
        Entry(frame_register, textvariable=self.Name_register,
              bd=5, font=('', 15)).grid(row=0, column=1)
        Label(frame_register, text='Password: ', font=(
            '', 20), pady=5, padx=5).grid(sticky=W)
        Entry(frame_register, textvariable=self.password_register, bd=5,
              font=('', 15), show='*').grid(row=1, column=1)
        Label(frame_register, text='Roll No: ', font=(
            '', 20), pady=5, padx=5).grid(sticky=W)
        Entry(frame_register, textvariable=self.roll_register,
              bd=5, font=('', 15)).grid(row=2, column=1)
        Label(frame_register, text='Whatsapp_No: ', font=(
            '', 20), pady=5, padx=5).grid(sticky=W)
        Entry(frame_register, textvariable=self.whatsapp_no_register,
              bd=5, font=('', 15)).grid(row=3, column=1)
        Button(frame_register, text='Register', bd=3, font=('', 15),
               padx=5, pady=5, command=self.register).grid()
        Button(frame_register, text='Back', bd=3, font=('', 15), padx=5,
               pady=5, command=self.login_screen).grid(row=4, column=1)
        self.frame_register = frame_register

    def login_screen(self):
        self.roll_login.set('')
        self.password_login.set('')
        self.frame_register.pack_forget()
        self.header["text"] = "Login"
        self.frame_login.pack()

    def rg_screen(self):
        self.roll_register.set('')
        self.password_register.set('')
        self.Name_register.set('')
        self.whatsapp_no_register.set('')
        self.frame_login.pack_forget()
        self.header['text'] = 'Register'
        self.frame_register.pack()

    def login(self):
        data_match = self.DataStore_user.check_cred(
            self.roll_login.get(), self.password_login.get())
        if data_match.get("success") == False:
            messagebox.showerror("Error", data_match.get("msg"))
        else:
            data_of_user = self.DataStore_user.get_user(
                self.roll_login.get()).get("data")
            self.folder_mas.destroy()
            home_screen(data_of_user[0], data_of_user[2])

    def register(self):
        dummy_variable = self.DataStore_user.register(
            self.roll_register.get(),
            self.password_register.get(),
            self.Name_register.get(),
            self.whatsapp_no_register.get()
        )
        if dummy_variable:
            messagebox.showinfo("Success", "successfully registered")
        else:
            messagebox.showerror(
                "Error", "{} already exists".format(self.roll_register.get()))


class home_screen:
    def __init__(self, roll, name):
        self.roll_no = roll
        self.Name = name
        master_data = Tk()
        Label(master_data, text="Select Quiz", font=(
            "Verdana", 20, "bold italic")).pack()
        selected_quiz = StringVar()
        for file_name in os.listdir("./quiz_wise_questions"):
            if file_name.endswith(".csv"):
                Radiobutton(master_data, text=file_name[:-4], variable=selected_quiz,
                            value=file_name, anchor="e", justify=LEFT).pack()
        Button(master_data, text="Click!!", command=lambda: [
               master_data.destroy(), self.start_quiz(selected_quiz.get())]).pack()
        master_data.mainloop()

    def start_quiz(self, filename):
        Quiz_tab = Tk()

        def unattemp_task(event):
            self.__get_unattem()
        Quiz_tab.bind("<Control_L><Alt_L><U>", unattemp_task)

        def goto_task(event):
            self.__go_to()
        Quiz_tab.bind("<Control_L><Alt_L><G>", goto_task)

        def submit_task(event):
            self.submit()
        Quiz_tab.bind("<Control_L><Alt_L><F>", submit_task)

        def export_task(event):
            self.__export_csv()
        Quiz_tab.bind("<Control_L><Alt_L><E>", export_task)

        ##############################################################

        self.file_name = filename
        self.user_marks_ds = datastore.users_marks_datastore()
        self.quiz_ds = datastore.quiz_datastore(filename).get_quiz()
        frame_info = Frame(Quiz_tab)
        frame_info.pack(side=TOP)
        self.channel = queue.Queue()
        self.max_timer = self.quiz_ds.get("q_time")
        thread = threading.Thread(target=self.timer)
        Label(frame_info, text="Timer: ").grid(row=0, sticky=W)
        self.timer_lb = Label(frame_info, text="")
        self.timer_lb.grid(row=0, column=1)
        Label(frame_info, text="Roll_No. : ").grid(row=1, sticky=W)
        Label(frame_info, text=self.roll_no).grid(row=1, column=1)
        Label(frame_info, text="Name: ").grid(row=2, sticky=W)
        Label(frame_info, text=self.Name).grid(row=2, column=1)
        Button(frame_info, text="Un-attempted Questions",
               command=self.__get_unattem).grid(row=3, sticky=W)
        Button(frame_info, text="Go to Question:",
               command=self.__go_to).grid(row=3, column=1)
        Button(frame_info, text="Export Database into CSV",
               command=self.__export_csv).grid(row=4, sticky=W)
        self.frame_info = frame_info
        thread.start()
        # Question frame
        self.response = {key: value for key, value in zip(self.quiz_ds.get(
            "questions").keys(), [-1]*len(self.quiz_ds.get("questions")))}
        self.ques_frame = Frame(Quiz_tab)
        self.ques_frame.pack()
        self.ques_numb = 1
        self.quest = self.create_q(self.ques_numb)
        self.options = self.create_options()
        self.display_q(self.ques_numb)
        self.next_btn = Button(
            self.ques_frame, text="Save & Next Ques.", command=self.next)
        self.submit_btn = Button(
            self.ques_frame, text="Submit & Quit", command=self.submit)
        self.next_btn.pack(pady=10, padx=5, side=LEFT)
        self.submit_btn.pack(pady=10, padx=5)
        #########################################################
        self.Quiz_tab = Quiz_tab
        Quiz_tab.mainloop()

    def next(self):
        if self.ques_numb >= len(self.quiz_ds.get("questions")):
            messagebox.showwarning(
                "Warning", "You are viewing the last Question. Press Submit to proceed")
        else:
            self.response["{}".format(self.ques_numb)
                          ] = self.opt_selected.get()
            self.ques_numb += 1
            self.opt_selected.set(self.response["{}".format(self.ques_numb)])
            self.display_q(self.ques_numb)

    def submit(self):
        self.response["{}".format(self.ques_numb)] = self.opt_selected.get()
        self.end_quiz()

    def check_quiz(self):
        total_marks = 0
        total_quiz_marks = 0
        total_unattempted = 0
        total_cor_ques = 0
        total_wrong_ques = 0
        out_fname = "individual_responses/{}_{}.csv".format(
            self.file_name.split(".csv")[0], self.roll_no)
        writer = csv.DictWriter(open(out_fname, "w"), fieldnames=["ques_no", "question", "option1", "option2", "option3", "option4",
                                                                  "correct_option", "marks_correct_ans", "marks_wrong_ans", "compulsory", "marked_choice", "Total", "Legend"])
        writer.writeheader()
        for ques in self.quiz_ds.get("questions").values():
            total = 0
            resp = self.response[ques.get("ques_no")]
            ques["marked_choice"] = resp
            if resp == -1:
                ques["marked_choice"] = ""
                ques["Legend"] = "Unattempted"
                total_unattempted += 1
            if resp == int(ques.get("correct_option")):
                total = int(ques.get("marks_correct_ans"))
                ques["Legend"] = "Correct Choice"
                total_cor_ques += 1
            elif resp == -1 and ques.get("compulsory") == "y":
                total = int(ques.get("marks_wrong_ans"))
                ques["Legend"] = "Wrong Choice"
                total_wrong_ques += 1
            elif resp != -1 and resp != int(ques.get("correct_option")):
                total = int(ques.get("marks_wrong_ans"))
                ques["Legend"] = "Wrong Choice"
                total_wrong_ques += 1
            ques["Total"] = total
            ques["option1"] = ques.get("options")[0]
            ques["option2"] = ques.get("options")[1]
            ques["option3"] = ques.get("options")[2]
            ques["option4"] = ques.get("options")[3]
            ques.pop("options")
            writer.writerow(ques)
            total_marks += total
            total_quiz_marks += int(ques.get("marks_correct_ans"))
        self.user_marks_ds.update_mark(
            self.roll_no, self.file_name, total_marks)
        temp_dct = {key: value for key, value in zip(
            writer.fieldnames, [""]*len(writer.fieldnames))}
        temp_dct["Total"] = total_marks
        temp_dct["Legend"] = "Marks Obtained"
        writer.writerow(temp_dct)
        temp_dct["Total"] = total_quiz_marks
        temp_dct["Legend"] = "Total Quiz Marks"
        writer.writerow(temp_dct)
        return {
            "total_ques": len(self.quiz_ds.get("questions")),
            "total_attemp": len(self.quiz_ds.get("questions"))-total_unattempted,
            "total_Correct": total_cor_ques,
            "total_wrong": total_wrong_ques,
            "total_marks": total_marks,
            "total_quiz_marks": total_quiz_marks
        }

    def end_quiz(self):
        self.ques_frame.destroy()
        self.frame_info.destroy()
        result = self.check_quiz()
        Label(self.Quiz_tab, text="Quiz Submitted!\nHere The Result").grid(row=0)
        Label(self.Quiz_tab, text="Total Quiz Questions: ").grid(
            row=1, sticky=W)
        Label(self.Quiz_tab, text=result.get(
            "total_ques")).grid(row=1, column=1)
        Label(self.Quiz_tab, text="Total Quiz Questions Attempted: ").grid(
            row=2, sticky=W)
        Label(self.Quiz_tab, text=result.get(
            "total_attemp")).grid(row=2, column=1)
        Label(self.Quiz_tab, text="Total Correct Questions: ").grid(
            row=3, sticky=W)
        Label(self.Quiz_tab, text=result.get(
            "total_Correct")).grid(row=3, column=1)
        Label(self.Quiz_tab, text="Total Wrong Questions: ").grid(
            row=4, sticky=W)
        Label(self.Quiz_tab, text=result.get(
            "total_wrong")).grid(row=4, column=1)
        Label(self.Quiz_tab, text="Total Marks Obtained: ").grid(
            row=5, sticky=W)
        Label(self.Quiz_tab, text=result.get(
            "total_marks")).grid(row=5, column=1)

    def create_options(self):
        b_val = 0
        create_option = []
        self.opt_selected = IntVar()
        self.opt_selected.set(-1)
        while b_val < 4:
            btn = Radiobutton(self.ques_frame, text="",
                              variable=self.opt_selected, value=b_val + 1)
            create_option.append(btn)
            btn.pack()
            b_val = b_val + 1
        self.if_correct_label = Label(self.ques_frame, text="")
        self.ng_marking = Label(self.ques_frame, text="")
        self.is_com = Label(self.ques_frame, text="")
        self.if_correct_label.pack()
        self.ng_marking.pack()
        self.is_com.pack()
        return create_option

    def create_q(self, ques_num):
        q = self.quiz_ds.get("questions").get(
            "{}".format(ques_num)).get("question")
        q_Label = Label(self.ques_frame, text=q)
        q_Label.pack()
        return q_Label

    def display_q(self, ques_num):
        b_val = 0
        q = self.quiz_ds.get("questions").get("{}".format(ques_num))
        self.quest['text'] = "Q"+str(ques_num) + ". " + q.get("question")
        for op in q.get("options"):
            self.options[b_val]['text'] = op
            b_val = b_val + 1
        self.if_correct_label["text"] = "Credits if Correct Option: {}".format(
            q.get("marks_correct_ans"))
        self.ng_marking["text"] = "Negative Marking: {}".format(
            q.get("marks_wrong_ans"))
        self.is_com["text"] = "Is compulsory: {}".format(q.get("compulsory"))

    def timer(self):
        min, sec = divmod(self.max_timer, 60)
        self.timer_lb["text"] = '{:02d}:{:02d}'.format(min, sec)
        if self.max_timer == 0:
            self.channel.put("Stop")
            print("time out")
            self.end_quiz()
            return
        self.timer_lb.after(1000, self.timer)
        self.max_timer -= 1

    def __export_csv(self):
        self.user_marks_ds.export_csv()
        print("csv files exported")

    def __get_unattem(self):
        temp_screen = Tk()
        temp_screen.geometry("300x100")
        temp_screen.title("Unattempted Questions")
        for q in self.response:
            if self.response[q] == -1:
                Label(temp_screen, text="Q{}".format(q)).pack()
        Button(temp_screen, text="OK", command=lambda:  [
               temp_screen.destroy()]).pack()

    def __go_to(self):
        temp_screen = Tk()
        temp_screen.title("Go To")
        f = Frame(temp_screen)
        f.pack()
        go_to_var = StringVar(f)
        go_to_var.set("")
        Label(f, text='Go To').grid(row=0, column=0)
        Entry(f, textvariable=go_to_var, bd=5).grid(row=0, column=1)

        def jump():
            new_f = Frame(temp_screen)
            new_f.pack()
            if go_to_var.get() != "":
                in_q = go_to_var.get()
                go_to_var.set("")
                if in_q in [i for i in self.response.keys()]:
                    q = self.quiz_ds.get("questions").get("{}".format(in_q))
                    Label(f, text="Q{}. {}".format(
                        q.get("ques_no"), q.get("question"))).grid(sticky=W)
                    o_selected = IntVar(f)
                    o_selected.set(-1)
                    for i in range(4):
                        Radiobutton(f, text=q.get("options")[
                                    i], variable=o_selected, value=i+1).grid(sticky=W)

                def ano_belo():
                    self.response[q.get("ques_no")] = o_selected.get()
                    if q.get("ques_no") == str(self.ques_numb):
                        self.opt_selected.set(o_selected.get())
                Button(f, text="Save", command=ano_belo).grid(sticky=W)
        Button(f, text="Jump", command=jump).grid(row=1, column=0)
        Button(f, text="Close X", command=lambda: [
               temp_screen.destroy()]).grid(row=1, column=1)


        # temp_screen.mainloop()
scr = screen()
