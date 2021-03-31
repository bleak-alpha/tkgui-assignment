import tkinter as gui
from tkinter import messagebox as message

#global varibles
defaultbg = '#222831'
defaultfg = '#eeeeee'
buttonbg = '#ec7373'
defaultfont = 'Open Sans'

#window definitions
window = gui.Tk()
window.title("Questionnare")
window.configure(bg=defaultbg)
window.geometry('854x720')

#title
title = gui.Label(window, bg=defaultbg, fg=defaultfg, font=(defaultfont, 20, 'bold'), text='Please Answer The Following Questions')
title.place(relx=0.21, rely=0.02, anchor='nw')

#Questions
q1 = gui.Label(window, bg=defaultbg, fg=defaultfg, font=(defaultfont, 16), text='1. What is your name?')
q1.place(relx=0.05, rely=0.2, anchor='w')
q1a = gui.Entry(window, width=25)
q1a.place(relx=0.08, rely=0.225)

q2 = gui.Label(window, bg=defaultbg, fg=defaultfg, font=(defaultfont, 16), text='2. What is your age?')
q2.place(relx=0.05, rely=0.3, anchor='w')
q2a = gui.Entry(window, width=5)
q2a.place(relx=0.08, rely=0.325)

q3 = gui.Label(window, bg=defaultbg, fg=defaultfg, font=(defaultfont, 16), text='3. Where does your self-worth come from?')
q3.place(relx=0.05, rely=0.4, anchor='w')
q3a = gui.Entry(window, width=35)
q3a.place(relx=0.08, rely=0.425)

q4 = gui.Label(window, bg=defaultbg, fg=defaultfg, font=(defaultfont, 16), text='4. What harsh truths do you prefer to ignore?')
q4.place(relx=0.05, rely=0.5, anchor='w')
q4a = gui.Entry(window, width=40)
q4a.place(relx=0.08, rely=0.525)

q5 = gui.Label(window, bg=defaultbg, fg=defaultfg, font=(defaultfont, 16), text='5. Is it possible to live a normal life and not ever tell a lie?')
q5.place(relx=0.05, rely=0.6, anchor='w')
q5a = gui.Entry(window, width=5)
q5a.place(relx=0.08, rely=0.625)

q6 = gui.Label(window, bg=defaultbg, fg=defaultfg, font=(defaultfont, 16), text='6. Is the meaning of life the same for animals and humans?')
q6.place(relx=0.05, rely=0.7, anchor='w')
q6a = gui.Entry(window, width=5)
q6a.place(relx=0.08, rely=0.725)

q6 = gui.Label(window, bg=defaultbg, fg=defaultfg, font=(defaultfont, 16), text='7. How long will you be remembered after you die?')
q6.place(relx=0.05, rely=0.8, anchor='w')
q6a = gui.Entry(window, width=40)
q6a.place(relx=0.08, rely=0.825)

#done button
def msg():
	message.showinfo('Done', 'Thank You For Answering Our Questions, Now You May Dwell On Your Existentional Crisis.')
done = gui.Button(window, text='Done', fg=defaultfg, bg=buttonbg, command=msg)
done.place(relx=0.9, rely=0.95, anchor='se')

#window persistance
window.mainloop()