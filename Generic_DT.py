import pybullet as p
import numpy as np
import pybullet_data
import time
import tkinter as tk
from tkinter import ttk
from tkinter import *
import os
import sys
import time
import math
#Niryo NED
def callback2():
    robot.move_joints(current_value1.get() , current_value2.get() , current_value3.get() , 
                current_value4.get() , current_value5.get() , current_value6.get())
    v1 = p.getJointInfo(robot2 , 1)[8]+(((current_value1.get()+2.97)/5.94)*((p.getJointInfo(robot2 , 1)[9])-(p.getJointInfo(robot2 , 1)[8])))
    v2 = p.getJointInfo(robot2 , 2)[8]+((((current_value2.get()+2.09)/2.7))*((p.getJointInfo(robot2 , 2)[9])-(p.getJointInfo(robot2 , 2)[8])))
    v3 = p.getJointInfo(robot2 , 3)[8]+(((current_value3.get()+1.34)/2.91)*((p.getJointInfo(robot2 , 3)[9])-(p.getJointInfo(robot2 , 3)[8])))
    v4 = p.getJointInfo(robot2 , 4)[8]+(((current_value4.get()+2.09)/4.18)*((p.getJointInfo(robot2 , 4)[9])-(p.getJointInfo(robot2 , 4)[8])))
    v5 = p.getJointInfo(robot2 , 5)[8]+(((current_value5.get()+1.75)/2.71)*((p.getJointInfo(robot2 , 5)[9])-(p.getJointInfo(robot2 , 5)[8])))
    v6 = p.getJointInfo(robot2 , 6)[8]+(((current_value6.get()+2.53)/5.06)*((p.getJointInfo(robot2 , 6)[9])-(p.getJointInfo(robot2 , 6)[8])))

    for step in range(80):
        p.setJointMotorControlArray(robot2 , [1,2,3,4,5,6] , p.POSITION_CONTROL , targetPositions = [v1,v2,v3,v4,v5,v6])
        focus_position , _ = p.getBasePositionAndOrientation(robot2)
        p.resetDebugVisualizerCamera(cameraDistance = 2 , cameraYaw = 0 , cameraPitch = 60 ,
        cameraTargetPosition = robot2)
        p.stepSimulation()
        time.sleep(0.01)

def nedfun():
    robot = NiryoRobot("10.10.10.10")
    robot.calibrate_auto()
    
    p.connect(p.GUI)
    p.resetSimulation()
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0,0,-9.8)
    p.setRealTimeSimulation(0)
    #loading assets
    p.loadURDF("plane.urdf" , [0,0,0,] , [0 ,0 , 0 , 1])
    robot2 = p.loadURDF("xarm/xarm6_robot_white.urdf" , [0,0,0,] , [0 ,0 , 0 , 1] , useFixedBase = True)
    obj_of_focus  = robot2

    # root window
    root2 = tk.Tk()
    root2.geometry('500x300')
    root2.resizable(True, True)
    root2.title('Niryo NED Coordinates')

    root2.columnconfigure(0, weight=1)
    root2.columnconfigure(1, weight=2)

    # slider current value
    current_value1 = tk.DoubleVar()
    current_value2 = tk.DoubleVar()
    current_value3 = tk.DoubleVar()
    current_value4 = tk.DoubleVar()
    current_value5 = tk.DoubleVar()
    current_value6 = tk.DoubleVar()

    def get_current_value1():
        return '{: .2f}'.format(current_value1.get())
    def get_current_value2():
        return '{: .2f}'.format(current_value2.get())
    def get_current_value3():
        return '{: .2f}'.format(current_value3.get())
    def get_current_value4():
        return '{: .2f}'.format(current_value4.get())
    def get_current_value5():
        return '{: .2f}'.format(current_value5.get())
    def get_current_value6():
        return '{: .2f}'.format(current_value6.get())

    def slider_changed1(event):
        value_label1.configure(text=get_current_value1())
    def slider_changed2(event):
        value_label2.configure(text=get_current_value2())
    def slider_changed3(event):
        value_label3.configure(text=get_current_value3())
    def slider_changed4(event):
        value_label4.configure(text=get_current_value4())
    def slider_changed5(event):
        value_label5.configure(text=get_current_value5())
    def slider_changed6(event):
        value_label6.configure(text=get_current_value6())

    #  sliders
    slider1 = ttk.Scale(
        root2,
        from_=-2.97,
        to=2.97,
        orient='horizontal',  # vertical
        command=slider_changed1,
        variable=current_value1
    )
    slider2 = ttk.Scale(
        root2,
        from_=-2.09,
        to=0.61,
        orient='horizontal',  # vertical
        command=slider_changed2,
        variable=current_value2
    )
    slider3 = ttk.Scale(
        root2,
        from_=-1.34,
        to=1.57,
        orient='horizontal',  # vertical
        command=slider_changed3,
        variable=current_value3
    )
    slider4 = ttk.Scale(
        root2,
        from_=-2.09,
        to=2.09,
        orient='horizontal',  # vertical
        command=slider_changed4,
        variable=current_value4
    )
    slider5 = ttk.Scale(
        root2,
        from_=-1.75,
        to=0.96,
        orient='horizontal',  # vertical
        command=slider_changed5,
        variable=current_value5
    )
    slider6 = ttk.Scale(
        root2,
        from_=-2.53,
        to=2.53,
        orient='horizontal',  # vertical
        command=slider_changed6,
        variable=current_value6
    )

    slider1.grid(
        column=1,
        row=1,
        sticky='we'
    )
    slider2.grid(
        column=1,
        row=2,
        sticky='we'
    )
    slider3.grid(
        column=1,
        row=4,
        sticky='we'
    )
    slider4.grid(
        column=1,
        row=6,
        sticky='we'
    )
    slider5.grid(
        column=1,
        row=8,
        sticky='we'
    )
    slider6.grid(
        column=1,
        row=10,
        sticky='we'
    )

    # current value label
    Subtitle_label = ttk.Label(
        root2,
        text='Please enter the coordinates of the 6 axis:'
    )
    Subtitle_label.grid(
        row=0,
        columnspan=1,
        sticky='n',
        ipadx=10,
        ipady=10
    )
    label1 = ttk.Label(
        root2,
        text='1st axis:'
    )
    label1.grid(
        row=1,
        sticky='n',
        ipadx=40,
        ipady=0
    )
    label2 = ttk.Label(
        root2,
        text='2nd axis:'
    )
    label2.grid(
        row=2,
        columnspan=1,
        sticky='n',
        ipadx=40,
        ipady=0
    )
    label3 = ttk.Label(
        root2,
        text='3rd axis:'
    )
    label3.grid(
        row=4,
        columnspan=1,
        sticky='n',
        ipadx=40,
        ipady=0
    )
    label4 = ttk.Label(
        root2,
        text='4th axis:'
    )
    label4.grid(
        row=6,
        columnspan=1,
        sticky='n',
        ipadx=40,
        ipady=0
    )
    label5 = ttk.Label(
        root2,
        text='5th axis:'
    )
    label5.grid(
        row=8,
        columnspan=1,
        sticky='n',
        ipadx=40,
        ipady=0
    )
    label6 = ttk.Label(
        root2,
        text='6th axis:'
    )
    label6.grid(
        row=10,
        columnspan=1,
        sticky='n',
        ipadx=40,
        ipady=0
    )
    # value labels
    value_label1 = ttk.Label(
        root2,
        text=get_current_value1()
    )
    value_label1.grid(
        row=1,
        columnspan=1,
        sticky='n'
    )
    value_label2 = ttk.Label(
        root2,
        text=get_current_value2()
    )
    value_label2.grid(
        row=2,
        columnspan=1,
        sticky='n'
    )
    value_label3 = ttk.Label(
        root2,
        text=get_current_value3()
    )
    value_label3.grid(
        row=4,
        columnspan=1,
        sticky='n'
    )
    value_label4 = ttk.Label(
        root2,
        text=get_current_value4()
    )
    value_label4.grid(
        row=6,
        columnspan=1,
        sticky='n'
    )
    value_label5 = ttk.Label(
        root2,
        text=get_current_value5()
    )
    value_label5.grid(
        row=8,
        columnspan=1,
        sticky='n'
    )
    value_label6 = ttk.Label(
        root2,
        text=get_current_value6()
    )
    value_label6.grid(
        row=10,
        columnspan=1,
        sticky='n'
    )

    #button
    btn = Button(root2, text = 'Do it!', bd = '2',
                            command =callback2 )

    # Set the position of button on the top of window.  
    #btn.pack(side = 'top')
    btn.grid(
        row=12,
        columnspan=1,
        sticky='n'
    )
    root2.mainloop()
    #robot.move_pose(0.2, -0.1, 0.25, 0.0, 1.57, 0.0)
    robot.close_connection()

    # print coordinates:
    # print (current_value1.get())
    # print (current_value2.get())
    # print (current_value3.get())
    # print (current_value4.get())
    # print (current_value5.get())
    # print (current_value6.get())

#XARM6
def callback():
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
    from xarm.wrapper import XArmAPI


    #######################################################
    """
    Just for test example
    """
    if len(sys.argv) >= 2:
        ip = sys.argv[1]
    else:
        try:
            from configparser import ConfigParser
            parser = ConfigParser()
            parser.read('../robot.conf')
            ip = parser.get('xArm', 'ip')
        except:
            ip = '192.168.1.216'
            if not ip:
                print('input error, exit')
                sys.exit(1)
    ########################################################


    arm = XArmAPI(ip)
    arm.motion_enable(enable=True)
    arm.set_mode(0)
    arm.set_state(state=0)

    arm.reset(wait=True)

    speed = 50
    arm.set_servo_angle(angle=[current_value1.get() , current_value2.get() , current_value3.get() ,
                current_value4.get() , current_value5.get() , current_value6.get()], speed=speed, wait=True)
    v1 = ((current_value1.get()*12.56637061)/720)
    v2 = ((current_value2.get()*4.1534)/238)
    v3 = ((current_value3.get()*4.11898)/236)
    v4 = ((current_value4.get()*12.56637061)/720)
    v5 = ((current_value5.get()*4.834562654)/277)
    v6 = ((current_value6.get()*12.56637061)/720)

    for step in range(80):
        p.setJointMotorControlArray(robot2 , [1,2,3,4,5,6] , p.POSITION_CONTROL , targetPositions = [v1,v2,v3,v4,v5,v6])
        focus_position , _ = p.getBasePositionAndOrientation(robot2)
        p.resetDebugVisualizerCamera(cameraDistance = 2 , cameraYaw = 0 , cameraPitch = 60 ,
        cameraTargetPosition = robot2)
        p.stepSimulation()
        time.sleep(0.01)

def xarmfun():
    p.connect(p.GUI)
    p.resetSimulation()
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0,0,-9.8)
    p.setRealTimeSimulation(0)
    #loading assets
    p.loadURDF("plane.urdf" , [0,0,0,] , [0 ,0 , 0 , 1])
    robot2 = p.loadURDF("xarm/xarm6_robot_white.urdf" , [0,0,0,] , [0 ,0 , 0 , 1] , useFixedBase = True)
    obj_of_focus  = robot2


    # root window
    root3 = tk.Tk()
    root3.geometry('500x300')
    root3.resizable(True, True)
    root3.title('xArm Coordinates')

    root3.columnconfigure(0, weight=1)
    root3.columnconfigure(1, weight=2)

    # slider current value
    current_value1 = tk.DoubleVar()
    current_value2 = tk.DoubleVar()
    current_value3 = tk.DoubleVar()
    current_value4 = tk.DoubleVar()
    current_value5 = tk.DoubleVar()
    current_value6 = tk.DoubleVar()

    def get_current_value1():
        return '{: .2f}'.format(current_value1.get())
    def get_current_value2():
        return '{: .2f}'.format(current_value2.get())
    def get_current_value3():
        return '{: .2f}'.format(current_value3.get())
    def get_current_value4():
        return '{: .2f}'.format(current_value4.get())
    def get_current_value5():
        return '{: .2f}'.format(current_value5.get())
    def get_current_value6():
        return '{: .2f}'.format(current_value6.get())

    def slider_changed1(event):
        value_label1.configure(text=get_current_value1())
    def slider_changed2(event):
        value_label2.configure(text=get_current_value2())
    def slider_changed3(event):
        value_label3.configure(text=get_current_value3())
    def slider_changed4(event):
        value_label4.configure(text=get_current_value4())
    def slider_changed5(event):
        value_label5.configure(text=get_current_value5())
    def slider_changed6(event):
        value_label6.configure(text=get_current_value6())

    #  sliders
    slider1 = ttk.Scale(
        root3,
        from_=-360,
        to=360,
        orient='horizontal',  # vertical
        command=slider_changed1,
        variable=current_value1
    )
    slider2 = ttk.Scale(
        root3,
        from_=-118,
        to=120,
        orient='horizontal',  # vertical
        command=slider_changed2,
        variable=current_value2
    )
    slider3 = ttk.Scale(
        root3,
        from_=-225,
        to=11,
        orient='horizontal',  # vertical
        command=slider_changed3,
        variable=current_value3
    )
    slider4 = ttk.Scale(
        root3,
        from_=-360,
        to=360,
        orient='horizontal',  # vertical
        command=slider_changed4,
        variable=current_value4
    )
    slider5 = ttk.Scale(
        root3,
        from_=-97,
        to=180,
        orient='horizontal',  # vertical
        command=slider_changed5,
        variable=current_value5
    )
    slider6 = ttk.Scale(
        root3,
        from_=-360,
        to=360,
        orient='horizontal',  # vertical
        command=slider_changed6,
        variable=current_value6
    )

    slider1.grid(
        column=1,
        row=1,
        sticky='we'
    )
    slider2.grid(
        column=1,
        row=2,
        sticky='we'
    )
    slider3.grid(
        column=1,
        row=4,
        sticky='we'
    )
    slider4.grid(
        column=1,
        row=6,
        sticky='we'
    )
    slider5.grid(
        column=1,
        row=8,
        sticky='we'
    )
    slider6.grid(
        column=1,
        row=10,
        sticky='we'
    )

    # current value label
    Subtitle_label = ttk.Label(
        root3,
        text='Please enter the coordinates of the 6 axis:'
    )
    Subtitle_label.grid(
        row=0,
        columnspan=1,
        sticky='n',
        ipadx=10,
        ipady=10
    )
    label1 = ttk.Label(
        root3,
        text='1st axis:'
    )
    label1.grid(
        row=1,
        sticky='n',
        ipadx=40,
        ipady=0
    )
    label2 = ttk.Label(
        root3,
        text='2nd axis:'
    )
    label2.grid(
        row=2,
        columnspan=1,
        sticky='n',
        ipadx=40,
        ipady=0
    )
    label3 = ttk.Label(
        root3,
        text='3rd axis:'
    )
    label3.grid(
        row=4,
        columnspan=1,
        sticky='n',
        ipadx=40,
        ipady=0
    )
    label4 = ttk.Label(
        root3,
        text='4th axis:'
    )
    label4.grid(
        row=6,
        columnspan=1,
        sticky='n',
        ipadx=40,
        ipady=0
    )
    label5 = ttk.Label(
        root3,
        text='5th axis:'
    )
    label5.grid(
        row=8,
        columnspan=1,
        sticky='n',
        ipadx=40,
        ipady=0
    )
    label6 = ttk.Label(
        root3,
        text='6th axis:'
    )
    label6.grid(
        row=10,
        columnspan=1,
        sticky='n',
        ipadx=40,
        ipady=0
    )
    # value labels
    value_label1 = ttk.Label(
        root3,
        text=get_current_value1()
    )
    value_label1.grid(
        row=1,
        columnspan=1,
        sticky='n'
    )
    value_label2 = ttk.Label(
        root3,
        text=get_current_value2()
    )
    value_label2.grid(
        row=2,
        columnspan=1,
        sticky='n'
    )
    value_label3 = ttk.Label(
        root3,
        text=get_current_value3()
    )
    value_label3.grid(
        row=4,
        columnspan=1,
        sticky='n'
    )
    value_label4 = ttk.Label(
        root3,
        text=get_current_value4()
    )
    value_label4.grid(
        row=6,
        columnspan=1,
        sticky='n'
    )
    value_label5 = ttk.Label(
        root3,
        text=get_current_value5()
    )
    value_label5.grid(
        row=8,
        columnspan=1,
        sticky='n'
    )
    value_label6 = ttk.Label(
        root3,
        text=get_current_value6()
    )
    value_label6.grid(
        row=10,
        columnspan=1,
        sticky='n'
    )

    #button
    btn = Button(root3, text = 'Do it!', bd = '2',
                            command =callback )

    # Set the position of button on the top of window.  
    #btn.pack(side = 'top')
    btn.grid(
        row=12,
        columnspan=1,
        sticky='n'
    )
    root3.mainloop()


# root window
root = tk.Tk()
root.geometry('400x150')
root.resizable(True, True)
root.title('xArm Coordinates')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

Subtitle_label = ttk.Label(
    root,
    text='Please choose your robotic arm:'
)
Subtitle_label.grid(
    row=0,
    columnspan=1,
    sticky='n',
    ipadx=10,
    ipady=10
)
#button
btn = Button(root, text = 'xArm6', bd = '2',
                          command =xarmfun )

btn2 = Button(root, text = 'Niryo NED', bd = '2',
                          command =nedfun )

# Set the position of button on the top of window.  
#btn.pack(side = 'top')
btn.grid(
    row=6,
    columnspan=1,
    sticky='n'
)
btn2.grid(
    row=6,
    columnspan=2,
    sticky='n'
)
root.mainloop()