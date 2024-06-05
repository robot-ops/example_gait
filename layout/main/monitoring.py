from PIL import Image, ImageTk
import cv2
from datetime import datetime
from tkinter import Frame, Label, PhotoImage, messagebox, Button
import tkinter as tk
from design.Entry import Entry
import threading
import modules.processing as wf

def mon_display(root):

    bg = Frame(root, width=1050, height=700)
    bg.place(x=0, y=0)

    bg.load = PhotoImage(file='assets\\mon_bgr.png')
    img = Label(root, image=bg.load)
    img.place(x=0, y=0)

    # left
    lf = Frame(root, width=400, height=550, bg="#1e1e1e")
    lf.place(x=50, y=100)
    
    # Angle Joint
    hip_label = Label(lf, text='Hip Joint', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    hip_label.place(x=10, y=10)
    
    # left angle
    left_hip_entry = Label(lf, text='0', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    left_hip_entry.place(x=10, y=30)
    
    # right angle
    right_hip_entry = Label(lf, text='0', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    right_hip_entry.place(x=25, y=30)
    
    knee_label = Label(lf, text='Knee Joint', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    knee_label.place(x=130, y=10)
    
    # left angle
    left_knee_entry = Label(lf, text='0', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    left_knee_entry.place(x=130, y=30)
    
    # right angle
    right_knee_entry = Label(lf, text='0', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    right_knee_entry.place(x=145, y=30)
    
    ankle_label = Label(lf, text='Ankle Joint', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    ankle_label.place(x=270, y=10)
    
    # left angle
    left_ankle_entry = Label(lf, text='0', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    left_ankle_entry.place(x=270, y=30)
    
    # right angle
    right_ankle_entry = Label(lf, text='0', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    right_ankle_entry.place(x=285, y=30)
    
    # EMG Level
    emg1_label = Label(lf, text='EMG1', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    emg1_label.place(x=10, y=100)
    emg1_entry = Label(lf, text="0", font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    emg1_entry.after(5000)
    emg1_entry.place(x=10, y=130)
    
    emg2_label = Label(lf, text='EMG2', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    emg2_label.place(x=130, y=100)
    emg2_entry = Label(lf, text="0", font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    emg2_entry.after(5000)
    emg2_entry.place(x=130, y=130)
    
    emg3_label = Label(lf, text='EMG3', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    emg3_label.place(x=240, y=100)
    emg3_entry = Label(lf, text="0", font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    emg3_entry.after(5000)
    emg3_entry.place(x=240, y=130)
    
    emg4_label = Label(lf, text='EMG4', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    emg4_label.place(x=320, y=100)
    emg4_entry = Label(lf, text="0", font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    emg4_entry.after(5000)
    emg4_entry.place(x=320, y=130)

    
    # Distance
    distance_label = Label(lf, text='Jarak', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    distance_label.place(x=10, y=194)
    distance_entry = Entry(lf, width=10)
    distance_entry.place(x=100, y=190)
    distance_sat = Label(lf, text='m', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    distance_sat.place(x=230, y=190)
    
    # Speed
    speed_label = Label(lf, text='Kecepatan', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    speed_label.place(x=10, y=236)
    speed_entry =Label(lf,text='0', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    speed_entry.place(x=100, y=240)
    speed_sat = Label(lf, text='m/s', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    speed_sat.place(x=230, y=240)
        

    # Time
    time_label = Label(lf, text='Waktu', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    time_label.place(x=10, y=300)
    time_entry = Label(lf,text='00:00', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    time_entry.place(x=100, y=306)
    time_sat = Label(lf, text='S', font=('normal', 12, 'bold'), bg='#1e1e1e', fg="#ECF2FF")
    time_sat.place(x=230, y=306)
    
    # Right
    global tab, cap, is_playing,stop_flag, temp, after_id
    
    tab = Frame(root)
    tab.place(x=471, y=140, width=530, height=460)
    
    # Create a black box (Canvas) for video display
    video_canvas = tk.Canvas(tab, width=530, height=460)
    video_canvas.pack(fill="x")
    
    cap = None
    is_playing = False
    stop_flag = False
    temp = 0
    after_id = ''
    
    def sec():
        global temp, after_id
        after_id = root.after(1000, sec)
        
        f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
        
        time_entry['text'] = str(f_temp)
        temp += 1
        
    def speed():
        distance_value = float(distance_entry.get().strip())
        times_value = float(temp)
        speeds = float(round((distance_value / times_value),2))
        speed_entry['text'] = str(speeds)
        
    def start_video_capture():
        global cap, is_playing
        cap = cv2.VideoCapture(0)  
        
        # Create a thread to display the video in the GUI
        is_playing = True
        pose_thread = threading.Thread(target=display_video)
        if distance_entry.get().strip() == "":
            messagebox.showinfo('ALERT!', 'Silahkan Input Jarak')
        else:
            pose_thread.start()
            sec()
            
    def display_video():
        global cap, is_playing
        while is_playing:
            frame = wf.pose_estimation(cap)  # Get the processed frame from processing.py
            if frame is not None:
                global latest_frame
                latest_frame = frame
                if tab:
                    tab.after(1, update_video_display)  # Schedule the update in the main thread

    def pause_video_capture():
        global is_playing
        is_playing = False
        video_canvas.after_cancel(after_id)
        speed()
        
    def update_video_display():
        global latest_frame
        frame = latest_frame
        # Convert the frame to a PhotoImage
        photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
        # Update the video canvas with the new frame
        video_canvas.create_image(0, 0, image=photo, anchor=tk.NW)
        video_canvas.image = photo
            
    # Button
    lf.start = PhotoImage(file='assets\\start_btn.png')
    start_btn = Button(lf, image=lf.start, bg='#1e1e1e', bd=0, activebackground='#1e1e1e', command=start_video_capture)
    start_btn.place(x=10, y=450)

    lf.stop = PhotoImage(file='assets\\stop_btn.png')
    stop_btn = Button(lf, image=lf.stop, bg='#1e1e1e', bd=0, activebackground='#1e1e1e', command=pause_video_capture)
    stop_btn.place(x=150, y=450)
    