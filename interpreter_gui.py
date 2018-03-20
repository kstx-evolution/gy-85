#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.10
# In conjunction with Tcl version 8.6
#    Mar 14, 2018 10:19:57 PM
# ===================================================================
#
#   n.jOy[dream]    |   ver0.01 @ mar 14 2018AD
#       
#
#   "Do you have any limburger?"
#
# ===================================================================

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import interpreter_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)
    interpreter_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel_1 (w)
    interpreter_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None

# nobody expects the spanish toplevel

class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("1920x1052+0+0")
        top.title("New Toplevel 1")



        self.GyroX = Canvas(top)
        self.GyroX.place(relx=0.01, rely=0.02, relheight=0.21, relwidth=0.28)
        self.GyroX.configure(borderwidth="2")
        self.GyroX.configure(relief=RIDGE)
        self.GyroX.configure(selectbackground="#c4c4c4")
        self.GyroX.configure(width=531)

        self.GyroY = Canvas(top)
        self.GyroY.place(relx=0.3, rely=0.02, relheight=0.21, relwidth=0.28)
        self.GyroY.configure(borderwidth="2")
        self.GyroY.configure(relief=RIDGE)
        self.GyroY.configure(selectbackground="#c4c4c4")
        self.GyroY.configure(width=531)

        self.GyroZ = Canvas(top)
        self.GyroZ.place(relx=0.59, rely=0.02, relheight=0.21, relwidth=0.28)
        self.GyroZ.configure(borderwidth="2")
        self.GyroZ.configure(relief=RIDGE)
        self.GyroZ.configure(selectbackground="#c4c4c4")
        self.GyroZ.configure(width=531)

        self.AccelX = Canvas(top)
        self.AccelX.place(relx=0.01, rely=0.28, relheight=0.21, relwidth=0.28)
        self.AccelX.configure(borderwidth="2")
        self.AccelX.configure(relief=RIDGE)
        self.AccelX.configure(selectbackground="#c4c4c4")
        self.AccelX.configure(width=531)

        self.AccelY = Canvas(top)
        self.AccelY.place(relx=0.3, rely=0.28, relheight=0.21, relwidth=0.28)
        self.AccelY.configure(borderwidth="2")
        self.AccelY.configure(relief=RIDGE)
        self.AccelY.configure(selectbackground="#c4c4c4")
        self.AccelY.configure(width=531)

        self.AccelZ = Canvas(top)
        self.AccelZ.place(relx=0.59, rely=0.28, relheight=0.21, relwidth=0.28)
        self.AccelZ.configure(borderwidth="2")
        self.AccelZ.configure(relief=RIDGE)
        self.AccelZ.configure(selectbackground="#c4c4c4")
        self.AccelZ.configure(width=531)

        self.MagX = Canvas(top)
        self.MagX.place(relx=0.01, rely=0.53, relheight=0.21, relwidth=0.28)
        self.MagX.configure(borderwidth="2")
        self.MagX.configure(relief=RIDGE)
        self.MagX.configure(selectbackground="#c4c4c4")
        self.MagX.configure(width=531)

        self.MagY = Canvas(top)
        self.MagY.place(relx=0.3, rely=0.53, relheight=0.21, relwidth=0.28)
        self.MagY.configure(borderwidth="2")
        self.MagY.configure(relief=RIDGE)
        self.MagY.configure(selectbackground="#c4c4c4")
        self.MagY.configure(width=531)

        self.MagZ = Canvas(top)
        self.MagZ.place(relx=0.59, rely=0.53, relheight=0.21, relwidth=0.28)
        self.MagZ.configure(borderwidth="2")
        self.MagZ.configure(relief=RIDGE)
        self.MagZ.configure(selectbackground="#c4c4c4")
        self.MagZ.configure(width=531)

        self.StatusHeader = Message(top)
        self.StatusHeader.place(relx=0.89, rely=0.01, relheight=0.03
                , relwidth=0.09)
        self.StatusHeader.configure(text='''Current Status''')
        self.StatusHeader.configure(width=165)

        self.HDG = Message(top)
        self.HDG.place(relx=0.89, rely=0.05, relheight=0.03, relwidth=0.03)
        self.HDG.configure(text='''Heading:''')
        self.HDG.configure(width=65)

        self.Pitch = Message(top)
        self.Pitch.place(relx=0.89, rely=0.08, relheight=0.03, relwidth=0.03)
        self.Pitch.configure(text='''Pitch:''')
        self.Pitch.configure(width=65)

        self.Roll = Message(top)
        self.Roll.place(relx=0.89, rely=0.1, relheight=0.03, relwidth=0.03)
        self.Roll.configure(text='''Roll:''')
        self.Roll.configure(width=65)

        self.YAcc = Message(top)
        self.YAcc.place(relx=0.88, rely=0.13, relheight=0.03, relwidth=0.05)
        self.YAcc.configure(text='''Upwards Accel:''')
        self.YAcc.configure(width=105)

        self.RollR = Message(top)
        self.RollR.place(relx=0.89, rely=0.16, relheight=0.03, relwidth=0.03)
        self.RollR.configure(text='''Roll Rate:''')
        self.RollR.configure(width=65)

        self.YawRate = Message(top)
        self.YawRate.place(relx=0.89, rely=0.19, relheight=0.03, relwidth=0.03)
        self.YawRate.configure(text='''Yaw Rate:''')
        self.YawRate.configure(width=65)

        self.PitchRate = Message(top)
        self.PitchRate.place(relx=0.89, rely=0.22, relheight=0.03, relwidth=0.03)

        self.PitchRate.configure(text='''Pitch Rate:''')
        self.PitchRate.configure(width=65)

        self.PitchRate1 = Message(top)
        self.PitchRate1.place(relx=0.88, rely=0.25, relheight=0.03
                , relwidth=0.05)
        self.PitchRate1.configure(text='''Current Temp:''')
        self.PitchRate1.configure(width=105)






if __name__ == '__main__':
    vp_start_gui()

