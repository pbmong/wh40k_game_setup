from os import listdir
from os.path import isfile, join

import random

from missions import secundary_missions

import tkinter as tk

class GUI:
    
    def __init__(self):
        self.size = (1800, 900)
        
        # --- Deployment, map and main mission APP ---
        
        self.app_map = tk.Tk()
        self.app_map.geometry("1800x900")
        self.app_map.config(background="grey")
        self.app_map.resizable(False, False)
        self.app_map.columnconfigure(0, weight=1)
        self.app_map.rowconfigure(0, weight=1)
        
        # Deployment and map variables
        self.deployment_name = None
                
        # --- Secundary tactical missions APP ---
        
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
        
        tk.Wm.wm_title(self.app, "Warhammer 40k battle setup - Secundary missions")
        
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
            self.app,
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
            self.app,
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
            self.app,
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
            self.app,
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
            self.app,
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
            self.app,
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
    
    
    def map_and_main_mission(self):
        # Styles
        style_background_color_1 = "#1cd8ed"
        style_borders__color_1 = "#204f54"
        style_font_color_1 = "white"

        # Frames
        map_frame = tk.Frame(
            self.app_map,
            highlightbackground=style_borders__color_1, 
            highlightcolor=style_borders__color_1, 
            highlightthickness=5, 
            width=self.size[0]*3.8/10, 
            height=self.size[1], 
            bg=style_background_color_1
        ).grid(
            row=0,
            column=0
        )
        
        main_mission_frame = tk.Frame(
            self.app_map,
            highlightbackground=style_borders__color_1, 
            highlightcolor=style_borders__color_1, 
            highlightthickness=5, 
            width=self.size[0]*(10-3.8)/10, 
            height=self.size[1], 
            bg=style_background_color_1
        ).grid(
            row=0,
            column=1
        )


        title_txt = tk.StringVar(self.app_map)

        tk.Wm.wm_title(self.app_map, "Warhammer 40k battle setup - map")

        # Widgets

        deployment_image = tk.PhotoImage(file="deployment/crucible_of_battle.png")
        
        self.deploy_img_label = tk.Label(
            map_frame,
            image=deployment_image
        )
        
        map_image = tk.PhotoImage(file="maps/nexoparia_map_1.png")
        
        self.map_img_label = tk.Label(
            map_frame,
            image=map_image
        )

        #deployment_onlyfiles = [f for f in listdir("./deployment") if isfile(join("./deployment", f))]
        #self.lb = tk.Listbox(self.app_map, selectmode="single", height = len(deployment_onlyfiles), font=("Arial",16)) # create Listbox
        #for x in deployment_onlyfiles: self.lb.insert(tk.END, x)
        #self.lb.place(x=600,y=200)

        tk.Button(self.app_map,text="Generate Deployment",command=self.printIt_deployment, font=("Arial",16)).place(x=10,y=10)
        tk.Button(self.app_map,text="Generate Map",command=self.printIt_map, font=("Arial",16)).place(x=300,y=10)

        
    def printIt_deployment(self): 
        
        images_list = [f for f in listdir("./deployment") if isfile(join("./deployment", f))]
        self.deployment_name = images_list[random.randint(0,len(images_list)-1)]
        image_file = tk.PhotoImage(file="deployment/" + self.deployment_name)
        self.deploy_img_label.config(image=image_file)
        self.deploy_img_label.place(
            x = 75,
            y = 75
        )
        self.app_map.mainloop()
        
    def printIt_map(self):
        
        images_list = [f for f in listdir("./maps") if isfile(join("./maps", f))]
        
        if self.deployment_name == "crucible_of_battle.png":
            maps_ind_list = [0, 1, 2, 3, 5, 6, 7]
        elif self.deployment_name == "dawn_of_war.png":
            maps_ind_list = [1, 2, 3, 4]
        elif self.deployment_name == "hammer_and_anvil.png":
            maps_ind_list = [0, 1, 2, 3, 4, 5, 6, 7]
        elif self.deployment_name == "search_and_destroy.png":
            maps_ind_list = [0, 1, 2, 3, 5, 6, 7]
        elif self.deployment_name == "sweeping_engagement.png":
            maps_ind_list = [0, 1, 2, 3, 4, 5, 7]            
        else:
            maps_ind_list = [range(len(images_list)-1)]
            
        map_ind = maps_ind_list[random.randint(0,len(maps_ind_list)-1)]
        image_file = tk.PhotoImage(file="maps/" + images_list[map_ind])
        self.map_img_label.config(image=image_file)
        self.map_img_label.place(
            x = 40,
            y = 465
        )
        self.app_map.mainloop()
            
window = GUI()
window.map_and_main_mission()
window.secundary_missions()