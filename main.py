from os import listdir
from os.path import isfile, join

import random

from missions import secundary_missions

import tkinter as tk

class GUI:
    
    def __init__(self):
        self.size = (1800, 900)
        
        self.app = tk.Tk()
        self.app.geometry("1800x900")
        self.app.config(background="grey")
        self.app.resizable(False, False)

        self.app.columnconfigure(0, weight=1)
        self.app.rowconfigure(0, weight=1)
        
        # Defender missions variables
        self.def_missions_list = list(range(len(secundary_missions.secundary_missions_list)))
        self.def_missions_1_number = -1
        self.def_missions_2_number = -1
        
        # Attacker missions variables
        self.atc_missions_list = list(range(len(secundary_missions.secundary_missions_list)))
        self.atc_missions_1_number = -1
        self.atc_missions_2_number = -1
    
    def secundary_missions(self):
        # Styles
        style_background_color_def = "#99ff99"
        style_background_color_atc = "#ff9999"
        style_background_color_gen = "#e0e0e0"
        
        style_borders__color_1 = "#204f54"
        style_font_color_1 = "black"
        
        # Fonts
        font_title = ("Arial", 20)
        font_missions = ("Arial", 15)
        
        # Frames
        def_frame = tk.Frame(
            self.app,
            highlightbackground=style_borders__color_1, 
            highlightcolor=style_borders__color_1, 
            highlightthickness=5, 
            borderwidth=10,
            width=self.size[0]/2,
            height=self.size[1],
            bg=style_background_color_def
        ).grid(
            row=0,
            column=0,
            
        )
        
        atc_frame = tk.Frame(
            self.app,
            highlightbackground=style_borders__color_1, 
            highlightcolor=style_borders__color_1, 
            highlightthickness=5, 
            width=self.size[0]/2, 
            height=self.size[1], 
            bg=style_background_color_atc
        ).grid(
            row=0,
            column=1
        )

        # -- Defender Frame --
        tk.Label(
            def_frame,
            text="Defender secundary missions",
            bg=style_background_color_def,
            font=font_title,
            fg=style_font_color_1,
            highlightbackground=style_borders__color_1, 
            highlightcolor=style_borders__color_1,
            justify="center",
            width=50,
            height=1
        ).place(
            x = 10,
            y = 10)
        
        # Mission 1
        self.def_mis_1_text = tk.StringVar(self.app)
        
        tk.Label(
            def_frame,
            name="defender mission 1",
            text="NO MISSION",
            bg=style_background_color_gen,
            font = font_missions,
            fg=style_font_color_1,
            highlightbackground=style_borders__color_1, 
            highlightcolor=style_borders__color_1,
            justify="left",
            width=77,
            height=15,
            textvariable=self.def_mis_1_text
        ).place( x = 20, y = 110)
        
        tk.Button(self.app,text="Generate",command=self.generate_defender_mission_1, font=font_missions).place(x=20,y=60)
        tk.Button(self.app,text="Discard",command=self.discard_defender_mission_1, font=font_missions).place(x=160,y=60)
        tk.Button(self.app,text="Clean",command=self.clean_defender_mission_1, font=font_missions).place(x=280,y=60)
        
        # Mission 2
        self.def_mis_2_text = tk.StringVar(self.app)
        
        tk.Label(
            def_frame,
            name="defender mission 2",
            text="NO MISSION",
            bg=style_background_color_gen,
            font = font_missions,
            fg=style_font_color_1,
            highlightbackground=style_borders__color_1, 
            highlightcolor=style_borders__color_1,
            justify="left",
            width=77,
            height=15,
            textvariable=self.def_mis_2_text
        ).place( x = 20, y = 530)
        
        tk.Button(self.app,text="Generate",command=self.generate_defender_mission_2, font=font_missions).place(x=20,y=480)
        tk.Button(self.app,text="Discard",command=self.discard_defender_mission_2, font=font_missions).place(x=160,y=480)
        tk.Button(self.app,text="Clean",command=self.clean_defender_mission_2, font=font_missions).place(x=280,y=480)
        
        # -- Attacker Frame --
        tk.Label(
            atc_frame,
            text="Attacker secundary missions",
            bg=style_background_color_atc,
            font=font_title,
            fg=style_font_color_1,
            highlightbackground=style_borders__color_1, 
            highlightcolor=style_borders__color_1,
            justify="center",
            width=50,
            height=1
        ).place(
            x = 910,
            y = 10)
        
        # Mission 1
        self.atc_mis_1_text = tk.StringVar(self.app)
        
        tk.Label(
            atc_frame,
            name="attacker mission 1",
            text="NO MISSION",
            bg=style_background_color_gen,
            font = font_missions,
            fg=style_font_color_1,
            highlightbackground=style_borders__color_1, 
            highlightcolor=style_borders__color_1,
            justify="left",
            width=77,
            height=15,
            textvariable=self.atc_mis_1_text
        ).place( x = 920, y = 110)
        
        tk.Button(self.app,text="Generate",command=self.generate_attacker_mission_1, font=font_missions).place(x=920,y=60)
        tk.Button(self.app,text="Discard",command=self.discard_attacker_mission_1, font=font_missions).place(x=1060,y=60)
        tk.Button(self.app,text="Clean",command=self.clean_attacker_mission_1, font=font_missions).place(x=1180,y=60)
        
        # Mission 2
        self.atc_mis_2_text = tk.StringVar(self.app)
        
        tk.Label(
            atc_frame,
            name="attacker mission 2",
            text="NO MISSION",
            bg=style_background_color_gen,
            font = font_missions,
            fg=style_font_color_1,
            highlightbackground=style_borders__color_1, 
            highlightcolor=style_borders__color_1,
            justify="left",
            width=77,
            height=15,
            textvariable=self.atc_mis_2_text
        ).place( x = 920, y = 530)
        
        tk.Button(self.app,text="Generate",command=self.generate_attacker_mission_2, font=font_missions).place(x=920,y=480)
        tk.Button(self.app,text="Discard",command=self.discard_attacker_mission_2, font=font_missions).place(x=1060,y=480)
        tk.Button(self.app,text="Clean",command=self.clean_attacker_mission_2, font=font_missions).place(x=1180,y=480)
        
        self.app.mainloop()
    
    # -- Defender missions functions --
    # Mission 1 functions
    def generate_defender_mission_1(self):
        l = len(self.def_missions_list)
        if l > 0:
            ind = random.randint(0, l-1)
            self.def_missions_1_number = self.def_missions_list[ind]
            self.def_mis_1_text.set(secundary_missions.secundary_missions_list[self.def_missions_1_number]["description"])
        else:
            self.def_missions_1_number = -1
            self.def_mis_1_text.set("NO MISSION")
        self.app.mainloop()
        
    def discard_defender_mission_1(self):
        if self.def_missions_1_number > -1:
            self.def_missions_list.remove(self.def_missions_1_number)
            self.def_missions_1_number = -1
        self.clean_defender_mission_1()
        
    def clean_defender_mission_1(self):
        self.def_mis_1_text.set("NO MISSION")
        self.app.mainloop()
        
    # Mission 2 functions
    def generate_defender_mission_2(self):
        l = len(self.def_missions_list)
        if l > 0:
            ind = random.randint(0, l-1)
            self.def_missions_2_number = self.def_missions_list[ind]
            self.def_mis_2_text.set(secundary_missions.secundary_missions_list[self.def_missions_2_number]["description"])
        else:
            self.def_missions_2_number = -1
            self.def_mis_2_text.set("NO MISSION")
        self.app.mainloop()
        
    def discard_defender_mission_2(self):
        if self.def_missions_2_number > -1:
            self.def_missions_list.remove(self.def_missions_2_number)
            self.def_missions_2_number = -1
        self.clean_defender_mission_2()
        
    def clean_defender_mission_2(self):
        self.def_mis_2_text.set("NO MISSION")
        self.app.mainloop()
    
    # -- Attacker missions functions --
    # Mission 1 functions
    def generate_attacker_mission_1(self):
        l = len(self.atc_missions_list)
        if l > 0:
            ind = random.randint(0, l-1)
            self.atc_missions_1_number = self.atc_missions_list[ind]
            self.atc_mis_1_text.set(secundary_missions.secundary_missions_list[self.atc_missions_1_number]["description"])
        else:
            self.atc_missions_1_number = -1
            self.atc_mis_1_text.set("NO MISSION")
        self.app.mainloop()
        
    def discard_attacker_mission_1(self):
        if self.atc_missions_1_number > -1:
            self.atc_missions_list.remove(self.atc_missions_1_number)
            self.atc_missions_1_number = -1
        self.clean_attacker_mission_1()
        
    def clean_attacker_mission_1(self):
        self.atc_mis_1_text.set("NO MISSION")
        self.app.mainloop()
        
    # Mission 2 functions
    def generate_attacker_mission_2(self):
        l = len(self.atc_missions_list)
        if l > 0:
            ind = random.randint(0, l-1)
            self.atc_missions_2_number = self.atc_missions_list[ind]
            self.atc_mis_2_text.set(secundary_missions.secundary_missions_list[self.atc_missions_2_number]["description"])
        else:
            self.atc_missions_2_number = -1
            self.atc_mis_2_text.set("NO MISSION")
        self.app.mainloop()
        
    def discard_attacker_mission_2(self):
        if self.atc_missions_2_number > -1:
            self.atc_missions_list.remove(self.atc_missions_2_number)
            self.atc_missions_2_number = -1
        self.clean_attacker_mission_2()
        
    def clean_attacker_mission_2(self):
        self.atc_mis_2_text.set("NO MISSION")
        self.app.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def main(self):
        # Styles
        style_background_color_1 = "#1cd8ed"
        style_borders__color_1 = "#204f54"
        style_font_color_1 = "white"

        # Frames
        map_frame = tk.Frame(
            self.app,
            borderwidth=10,
            width=self.size[0]/3,
            height=self.size[1],
            bg=style_background_color_1
        ).grid(
            row=0,
            column=0,
            
        )
        
        main_mission_frame = tk.Frame(
            highlightbackground=style_borders__color_1, 
            highlightcolor=style_borders__color_1, 
            highlightthickness=5, 
            width=self.size[0]/3, 
            height=self.size[1], 
            bg=style_background_color_1
        ).grid(
            row=0,
            column=1
        )

        secundary_missions_frame = tk.Frame(
            self.app,
            borderwidth=10,
            width=self.size[0]/3,
            height=self.size[1],
            bg=style_background_color_1
        ).grid(
            row=0,
            column=2
        )

        title_txt = tk.StringVar(self.app)
        input_txt = tk.StringVar(self.app)

        tk.Wm.wm_title(self.app, "Warhammer 40k Battle setup")

        # Widgets

        tk.Label(
            map_frame,
            text="Tittle",
            bg=style_background_color_1,
            fg=style_font_color_1,
            highlightbackground=style_borders__color_1, 
            highlightcolor=style_borders__color_1,
            justify="center",
            textvariable=title_txt,
            width=10,
            height=5
        ).place(
            x = 200,
            y = 300)

        #tk.Entry(            map_frame,            bg="white",            fg="black",            justify="center",            textvariable=input_txt        ).place(                x = 10,                y = 300            )

        deployment_image = tk.PhotoImage(file="deployment/crucible_of_battle.png")
        self.img_label = tk.Label(
            map_frame,
            image=deployment_image
        )
        self.img_label.place(
            x = 500,
            y = 300
        )

        onlyfiles = [f for f in listdir("./deployment") if isfile(join("./deployment", f))]

        self.lb = tk.Listbox(self.app, selectmode="single", height = len(onlyfiles), font=("Arial",16)) # create Listbox
        for x in onlyfiles: self.lb.insert(tk.END, x)
        self.lb.place(x=600,y=200)

        tk.Button(self.app,text="Start",command=self.printIt, font=("Arial",16)).place(x=730,y=200)

        self.app.mainloop()
        
    def printIt(self): 
        SelectList = self.lb.curselection()
        selection_list=[self.lb.get(i) for i in SelectList] # this will print the value you select
        deployment_image = tk.PhotoImage(file="deployment/" + selection_list[0])
        self.img_label.config(image=deployment_image)
        self.img_label.place(
            x = 500,
            y = 300
        )
        self.app.mainloop()
            
window = GUI()
window.secundary_missions()