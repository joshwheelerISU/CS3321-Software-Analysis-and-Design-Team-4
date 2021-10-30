import tkinter
from tkinter import *
import random

position = 0  # temp variable for moving the token 1
player2_position = 0  # temp variable for moving the token 2
house_num = 0


class GameBoard:

    def __init__(self):
        self.window = Tk()
        self.window.title("MonopolyLite")
        self.window.geometry("1300x770")
        self.window.resizable(False, False)
        self.initialize_spaces()   # Creates board spaces
        self.deactivate_space_button()  # Deactivates spaces, so they can't be clicked
        self.create_player_token()   # Creates all player token
        self.initialize_houses()    # Initializes house labels
        self.window.config(bg="#BFDBAE")

        self.window.mainloop()

    # Initializes board spaces with images
    def initialize_spaces(self):
        # Go-space space
        # Coordinates (x=0, y=670)

        self.go = PhotoImage(file='Resources\go.png')
        self.go_button = Button(self.window, image=self.go, bg="#BFDBAE")
        self.go_button.place(x=0, y=670)

        # Brown Mediterranean space
        # Coordinates (x=0, y=606)

        self.mediterranean = PhotoImage(file='Resources/Brown_Mediterranean_1.png')
        self.brown_mediterranean_button = Button(self.window, image=self.mediterranean, bg="#BFDBAE")
        self.brown_mediterranean_button.place(x=0, y=606)

        # Community Chest space
        # Coordinates (x=0, y=542)
        self.community_chest_img = PhotoImage(file='Resources/Community Chest_1.png')
        self.community_chest_button = Button(self.window, image=self.community_chest_img, bg="#BFDBAE")
        self.community_chest_button.place(x=0, y=542)

        # baltic_avenue space
        # Coordinates (x=0, y=478)
        self.baltic_avenue_img = PhotoImage(file='Resources/Brown_Baltic_1.png')
        self.baltic_avenue_button = Button(self.window, image=self.baltic_avenue_img, bg="#BFDBAE")
        self.baltic_avenue_button.place(x=0, y=478)

        # income_tax space
        # Coordinates (x=0, y=414)
        self.income_tax_img = PhotoImage(file='Resources/Income Tax_1.png')
        self.income_tax_button = Button(self.window, image=self.income_tax_img, bg="#BFDBAE")
        self.income_tax_button.place(x=0, y=414)

        # reading_railroad space
        # Coordinates (x=0, y=350)
        self.reading_railroad_img = PhotoImage(file='Resources/Reading Railroad_1.png')
        self.reading_railroad_button = Button(self.window, image=self.reading_railroad_img, bg="#BFDBAE")
        self.reading_railroad_button.place(x=0, y=350)

        # Community Chest
        # Coordinates (x=0, y=286)
        self.oriental_Avenue_img = PhotoImage(file='Resources/SkyBlue_Oriental_1.png')
        self.oriental_Avenue__button = Button(self.window, image=self.oriental_Avenue_img, bg="#BFDBAE")
        self.oriental_Avenue__button.place(x=0, y=286)

        # chance space
        # Coordinates (x=0, y=222)
        self.pink_chance_img = PhotoImage(file='Resources/pinkChance_1.png')
        self.pink_chance_button = Button(self.window, image=self.pink_chance_img, bg="#BFDBAE")
        self.pink_chance_button.place(x=0, y=222)

        # vermont space
        # Coordinates (x=0, y=158)
        self.vermont_img = PhotoImage(file='Resources/SkyBlue_Vermont_1.png')
        self.vermont_button = Button(self.window, image=self.vermont_img, bg="#BFDBAE")
        self.vermont_button.place(x=0, y=158)

        # connecticut space
        # Coordinates (x=0, y=94)
        self.connecticut_img = PhotoImage(file='Resources/SkyBlue_Connecticut_1.png')
        self.connecticut_button = Button(self.window, image=self.connecticut_img, bg="#BFDBAE")
        self.connecticut_button.place(x=0, y=94)

        # Jail space
        # Coordinates (x=0, y=0)
        self.jail_img = PhotoImage(file='Resources/jail.png')
        self.jail_button = Button(self.window, image=self.jail_img, bg="#BFDBAE")
        self.jail_button.place(x=0, y=0)

        # ST. Charles space
        # Coordinates (x=99, y=0)
        self.charles_img = PhotoImage(file='Resources/Purple_ST.Charles_1.png')
        self.charles_button = Button(self.window, image=self.charles_img, bg="#BFDBAE")
        self.charles_button.place(x=99, y=0)

        # Electric space
        # Coordinates (x=160, y=0)
        self.electric_img = PhotoImage(file='Resources/Electric company_1.png')
        self.electric_button = Button(self.window, image=self.electric_img, bg="#BFDBAE")
        self.electric_button.place(x=160, y=0)

        # States Avenue space
        # Coordinates (x=224, y=0)
        self.states_img = PhotoImage(file='Resources/purpleStates_1.png')
        self.states_button = Button(self.window, image=self.states_img, bg="#BFDBAE")
        self.states_button.place(x=224, y=0)

        # Virginia space
        # Coordinates (x=287, y=0)
        self.virginia_img = PhotoImage(file='Resources/Purple_Virginia_1.png')
        self.virginia_button = Button(self.window, image=self.virginia_img, bg="#BFDBAE")
        self.virginia_button.place(x=287, y=0)

        # Pennsylvania railroad space
        # Coordinates (x=352, y=0)
        self.penn_railroad_img = PhotoImage(file='Resources/Pennsylvania_1.png')
        self.penn_railroad_button = Button(self.window, image=self.penn_railroad_img, bg="#BFDBAE")
        self.penn_railroad_button.place(x=352, y=0)

        # Orange_ST.James_1 space
        # Coordinates (x=416, y=0)
        self.james_img = PhotoImage(file='Resources/Orange_ST.James_1.png')
        self.james_button = Button(self.window, image=self.james_img, bg="#BFDBAE")
        self.james_button.place(x=416, y=0)

        # Community Chest_2 space
        # Coordinates (x=480, y=0)
        self.community_chest_2_img = PhotoImage(file='Resources/Community Chest_2.png')
        self.community_chest_2_button = Button(self.window, image=self.community_chest_2_img, bg="#BFDBAE")
        self.community_chest_2_button.place(x=480, y=0)

        # Pennsylvania railroad space
        # Coordinates (x=544, y=0)
        self.tennessee_img = PhotoImage(file='Resources/Orange_Tennessee_1.png')
        self.tennessee_button = Button(self.window, image=self.tennessee_img, bg="#BFDBAE")
        self.tennessee_button.place(x=544, y=0)

        # Orange_New York_1 space
        # Coordinates (x=608, y=0)
        self.new_york_img = PhotoImage(file='Resources/Orange_New York_1.png')
        self.new_york_button = Button(self.window, image=self.new_york_img, bg="#BFDBAE")
        self.new_york_button.place(x=608, y=0)

        # Parking space
        # Coordinates (x=672, y=0)
        self.parking_img = PhotoImage(file='Resources/parking.png')
        self.parking_button = Button(self.window, image=self.parking_img, bg="#BFDBAE")
        self.parking_button.place(x=672, y=0)

        # kentucky space
        # Coordinates (x=672, y=99)
        self.kentucky_img = PhotoImage(file='Resources/Red_Kenteucky_1.png')
        self.kentucky_button = Button(self.window, image=self.kentucky_img, bg="#BFDBAE")
        self.kentucky_button.place(x=672, y=99)

        # Chance space
        # Coordinates(x=672, y=158)
        self.chance_img = PhotoImage(file='Resources/CHANCE_1.png')
        self.chance_button = Button(self.window, image=self.chance_img, bg="#BFDBAE")
        self.chance_button.place(x=672, y=158)

        # Indiana space
        # Coordinates (x=672, y=222)
        self.indiana_img = PhotoImage(file='Resources/Red_Indiana_1.png')
        self.indiana_button = Button(self.window, image=self.indiana_img, bg="#BFDBAE")
        self.indiana_button.place(x=672, y=222)

        # Illinois space
        # Coordinates (x=672, y=286)
        self.illnois_img = PhotoImage(file='Resources/Red_Illinois_1.png')
        self.illnois_button = Button(self.window, image=self.illnois_img, bg="#BFDBAE")
        self.illnois_button.place(x=672, y=286)

        # B&O railroads space
        # Coordinates (x=672, y=350)
        self.b_o_railroad_img = PhotoImage(file='Resources/RailRoad_1.png')
        self.b_o_railroad_button = Button(self.window, image=self.b_o_railroad_img, bg="#BFDBAE")
        self.b_o_railroad_button.place(x=672, y=350)

        # Atlantic space
        # Coordinates (x=672, y=414)
        self.atlantic_img = PhotoImage(file='Resources/Yellow_Atlantic_1.png')
        self.atlantic_button = Button(self.window, image=self.atlantic_img, bg="#BFDBAE")
        self.atlantic_button.place(x=672, y=414)

        # Ventnor space
        # Coordinates (x=672, y=478)
        self.ventnor_img = PhotoImage(file='Resources/Yellow_Ventnor_1.png')
        self.ventnor_button = Button(self.window, image=self.ventnor_img, bg="#BFDBAE")
        self.ventnor_button.place(x=672, y=478)

        # water_works space
        # Coordinates (x=545, y=670)
        self.water_works_img = PhotoImage(file='Resources/water works_1.png')
        self.water_works_button = Button(self.window, image=self.water_works_img, bg="#BFDBAE")
        self.water_works_button.place(x=672, y=542)

        # marvin space
        # Coordinates (x=672, y=606)
        self.marvin_img = PhotoImage(file='Resources/Yellow_Marvin_1.png')
        self.marvin_button = Button(self.window, image=self.marvin_img, bg="#BFDBAE")
        self.marvin_button.place(x=672, y=606)

        # go_to_jail space
        # Coordinates (x=672, y=670)
        self.go_to_jail_img = PhotoImage(file='Resources/gotojail.png')
        self.go_to_jail_button = Button(self.window, image=self.go_to_jail_img, bg="#BFDBAE")
        self.go_to_jail_button.place(x=672, y=670)

        # broadwalk space
        # Coordinates (x=99, y=670)
        self.broadwalk_img = PhotoImage(file='Resources/Dark-Blue_Broadwalk_1.png')
        self.broadwalk_button = Button(self.window, image=self.broadwalk_img, bg="#BFDBAE")
        self.broadwalk_button.place(x=99, y=670)

        # luxury_tax space
        # Coordinates (x=160, y=670)
        self.luxury_tax_img = PhotoImage(file='Resources/Luxury Tax_1.png')
        self.luxury_tax_button = Button(self.window, image=self.luxury_tax_img, bg="#BFDBAE")
        self.luxury_tax_button.place(x=160, y=670)

        # luxury_tax space
        # Coordinates (x=224, y=670)
        self.park_place_img = PhotoImage(file='Resources/DarkBlue_Park_1.png')
        self.park_place_button = Button(self.window, image=self.park_place_img, bg="#BFDBAE")
        self.park_place_button.place(x=224, y=670)

        # orange_chance space
        # Coordinates (x=287, y=670)
        self.orange_chance_img = PhotoImage(file='Resources/orangeChance_1.png')
        self.orange_chance_button = Button(self.window, image=self.orange_chance_img, bg="#BFDBAE")
        self.orange_chance_button.place(x=287, y=670)

        # short_line space
        # Coordinates (x=352, y=670)
        self.short_line_img = PhotoImage(file='Resources/Short Line_1.png')
        self.short_line_button = Button(self.window, image=self.short_line_img, bg="#BFDBAE")
        self.short_line_button.place(x=352, y=670)

        # Pennsylvania_street space
        # Coordinates (x=416, y=670)
        self.pennsylvania_img = PhotoImage(file='Resources/Green_Pennsylvania_1.png')
        self.pennsylvania_button = Button(self.window, image=self.pennsylvania_img, bg="#BFDBAE")
        self.pennsylvania_button.place(x=416, y=670)

        # community_chest space
        # Coordinates (x=480, y=670)
        self.community_chest_3_img = PhotoImage(file='Resources/Community Chest_3.png')
        self.community_chest_3_button = Button(self.window, image=self.community_chest_3_img, bg="#BFDBAE")
        self.community_chest_3_button.place(x=480, y=670)

        # north_carolina_street space
        # Coordinates (x=545, y=670)
        self.north_carolina_img = PhotoImage(file='Resources/Green_North Carolina_1.png')
        self.north_carolina_button = Button(self.window, image=self.north_carolina_img, bg="#BFDBAE")
        self.north_carolina_button.place(x=545, y=670)

        # pacific_street space
        # Coordinates (x=608, y=670)
        self.pacific_img = PhotoImage(file='Resources/Green_Pacific_1.png')
        self.pacific_button = Button(self.window, image=self.pacific_img, bg="#BFDBAE")
        self.pacific_button.place(x=608, y=670)

        # Buttons
        self.move_button = Button(self.window, text="Player 1", command=self.player_one_position,
                                  font=('Arial', 12, 'bold'), width=7)
        self.move_button.place(x=1000, y=700)

        self.new_button = Button(self.window, text="Player 2", command=self.player_two_position,
                                 font=('Arial', 12, 'bold'), width=7)
        self.new_button.place(x=1100, y=700)

        self.purchase_button = Button(self.window, text="Buy Property", command=self.button_purchase,
                                      font=("arial", 12, 'bold'), width=15)
        self.purchase_button.place(x=140, y=120)
        self.build_house_button = Button(self.window, text="Build House", command=self.button_house,
                                         font=("arial", 12, 'bold'), width=15)
        self.build_house_button.place(x=310, y=120)
        self.build_hotel_button = Button(self.window, text="Build Hotel", command=self.button_hotel,
                                         font=("arial", 12, 'bold'), width=15)
        self.build_hotel_button.place(x=480, y=120)

        self.roll_button = Button(self.window, text="Roll Dice", command=self.button_roll,
                                  font=("arial", 12, 'bold'), width=15)
        self.roll_button.place(x=310, y=600)

    # Initializes player tokens
    def create_player_token(self):
        ## Player 1 token
        self.player_one_img = PhotoImage(file='Resources/one.png')
        self.player_one_label = Label(self.window, image=self.player_one_img, bg="#33CCFF")
        self.player_one_label.place(x=7, y=725)

        ## Player 2 token
        self.player_two_img = PhotoImage(file='Resources/two.png')
        self.player_two_label = Label(self.window, image=self.player_two_img, bg="#FF0000")
        self.player_two_label.place(x=35, y=725)

    def initialize_houses(self):

        # house image
        self.house_img = PhotoImage(file='Resources/house.png')
        ##Houses
        #  Mediterranean house label
        self.brown_mediterranean_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.brown_mediterranean_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.brown_mediterranean_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.brown_mediterranean_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # Baltic avenue house label
        self.baltic_avenue_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.baltic_avenue_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.baltic_avenue_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.baltic_avenue_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # Oriental avenue house label
        self.oriental_Avenue_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.oriental_Avenue_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.oriental_Avenue_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.oriental_Avenue_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # Vermont house  label
        self.vermont_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.vermont_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.vermont_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.vermont_Avenue_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # Connecticut house label
        self.connecticut_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.connecticut_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.connecticut_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.connecticut_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # ST Charles house label
        self.st_charles_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.st_charles_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.st_charles_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.st_charles_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # States house label
        self.states_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.states_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.states_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.states_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # Virginia house label
        self.virginia_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.virginia_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.virginia_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.virginia_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # ST James house label
        self.st_james_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.st_james_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.st_james_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.st_james_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # Tennessee house label
        self.tennessee_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.tennessee_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.tennessee_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.tennessee_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # New York house label
        self.new_york_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.new_york_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.new_york_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.new_york_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # kentucky house label
        self.kentucky_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.kentucky_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.kentucky_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.kentucky_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # Indiana house label
        self.indiana_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.indiana_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.indiana_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.indiana_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # Illnois house label
        self.illnois_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.illnois_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.illnois_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.illnois_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # Atlantic house label
        self.atlantic_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.atlantic_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.atlantic_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.atlantic_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # Ventor house label
        self.ventnor_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.ventnor_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.ventnor_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.ventnor_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # Marvin house label
        self.marvin_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.marvin_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.marvin_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.marvin_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # Pacific house label
        self.pacific_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.pacific_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.pacific_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.pacific_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # North Carolina house label
        self.north_carolina_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.north_carolina_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.north_carolina_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.north_carolina_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # Pennsylvania house label
        self.pennsylvania_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.pennsylvania_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.pennsylvania_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.pennsylvania_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # Park house label
        self.park_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.park_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.park_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.park_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

        # Broadwalk house label
        self.broadwalk_house_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.broadwalk_house2_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.broadwalk_house3_label = Label(self.window, image=self.house_img, bg="#90EE90")
        self.broadwalk_house4_label = Label(self.window, image=self.house_img, bg="#90EE90")

    # Moves player one position
    # param Player one index
    def player_one_position(self):
        global position
        position = (position + 1) % 40

        if position == 0:
            self.player_one_label.place(x=5, y=725)
        elif position == 1:
            self.player_one_label.place(x=5, y=639)
        elif position == 2:
            self.player_one_label.place(x=5, y=570)
        elif position == 3:
            self.player_one_label.place(x=5, y=505)
        elif position == 4:
            self.player_one_label.place(x=5, y=449)
        elif position == 5:
            self.player_one_label.place(x=5, y=385)
        elif position == 6:
            self.player_one_label.place(x=5, y=320)
        elif position == 7:
            self.player_one_label.place(x=5, y=257)
        elif position == 8:
            self.player_one_label.place(x=5, y=190)
        elif position == 9:
            self.player_one_label.place(x=5, y=130)
        elif position == 10:
            self.player_one_label.place(x=7, y=65)
        elif position == 11:
            self.player_one_label.place(x=108, y=7)
        elif position == 12:
            self.player_one_label.place(x=175, y=7)
        elif position == 13:
            self.player_one_label.place(x=240, y=7)
        elif position == 14:
            self.player_one_label.place(x=300, y=7)
        elif position == 15:
            self.player_one_label.place(x=370, y=7)
        elif position == 16:
            self.player_one_label.place(x=430, y=7)
        elif position == 17:
            self.player_one_label.place(x=490, y=7)
        elif position == 18:
            self.player_one_label.place(x=562, y=7)
        elif position == 19:
            self.player_one_label.place(x=626, y=7)
        elif position == 20:
            self.player_one_label.place(x=740, y=7)
        elif position == 21:
            self.player_one_label.place(x=740, y=115)
        elif position == 22:
            self.player_one_label.place(x=740, y=184)
        elif position == 23:
            self.player_one_label.place(x=740, y=244)
        elif position == 24:
            self.player_one_label.place(x=740, y=310)
        elif position == 25:
            self.player_one_label.place(x=740, y=374)
        elif position == 26:
            self.player_one_label.place(x=740, y=438)
        elif position == 27:
            self.player_one_label.place(x=740, y=504)
        elif position == 28:
            self.player_one_label.place(x=740, y=567)
        elif position == 29:
            self.player_one_label.place(x=740, y=632)
        elif position == 30:
            self.player_one_label.place(x=740, y=732)
        elif position == 31:
            self.player_one_label.place(x=635, y=738)
        elif position == 32:
            self.player_one_label.place(x=571, y=738)
        elif position == 33:
            self.player_one_label.place(x=507, y=738)
        elif position == 34:
            self.player_one_label.place(x=434, y=738)
        elif position == 35:
            self.player_one_label.place(x=369, y=738)
        elif position == 36:
            self.player_one_label.place(x=305, y=738)
        elif position == 37:
            self.player_one_label.place(x=241, y=738)
        elif position == 38:
            self.player_one_label.place(x=177, y=738)
        elif position == 39:
            self.player_one_label.place(x=113, y=738)

    # Moves Player two token
    # param Player two index
    def player_two_position(self):
        global player2_position
        player2_position = (player2_position + 1) % 40

        if player2_position == 0:
            self.player_two_label.place(x=35, y=725)
        elif player2_position == 1:
            self.player_two_label.place(x=35, y=639)
        elif player2_position == 2:
            self.player_two_label.place(x=35, y=570)
        elif player2_position == 3:
            self.player_two_label.place(x=35, y=505)
        elif player2_position == 4:
            self.player_two_label.place(x=35, y=449)
        elif player2_position == 5:
            self.player_two_label.place(x=35, y=385)
        elif player2_position == 6:
            self.player_two_label.place(x=35, y=320)
        elif player2_position == 7:
            self.player_two_label.place(x=35, y=257)
        elif player2_position == 8:
            self.player_two_label.place(x=35, y=190)
        elif player2_position == 9:
            self.player_two_label.place(x=35, y=130)
        elif player2_position == 10:
            self.player_two_label.place(x=37, y=65)
        elif player2_position == 11:
            self.player_two_label.place(x=108, y=37)
        elif player2_position == 12:
            self.player_two_label.place(x=175, y=37)
        elif player2_position == 13:
            self.player_two_label.place(x=240, y=37)
        elif player2_position == 14:
            self.player_two_label.place(x=300, y=37)
        elif player2_position == 15:
            self.player_two_label.place(x=370, y=37)
        elif player2_position == 16:
            self.player_two_label.place(x=430, y=37)
        elif player2_position == 17:
            self.player_two_label.place(x=490, y=37)
        elif player2_position == 18:
            self.player_two_label.place(x=562, y=37)
        elif player2_position == 19:
            self.player_two_label.place(x=626, y=37)
        elif player2_position == 20:
            self.player_two_label.place(x=740, y=37)
        elif player2_position == 21:
            self.player_two_label.place(x=710, y=115)
        elif player2_position == 22:
            self.player_two_label.place(x=710, y=184)
        elif player2_position == 23:
            self.player_two_label.place(x=710, y=244)
        elif player2_position == 24:
            self.player_two_label.place(x=710, y=310)
        elif player2_position == 25:
            self.player_two_label.place(x=710, y=374)
        elif player2_position == 26:
            self.player_two_label.place(x=710, y=438)
        elif player2_position == 27:
            self.player_two_label.place(x=710, y=504)
        elif player2_position == 28:
            self.player_two_label.place(x=710, y=567)
        elif player2_position == 29:
            self.player_two_label.place(x=710, y=632)
        elif player2_position == 30:
            self.player_two_label.place(x=710, y=732)
        elif player2_position == 31:
            self.player_two_label.place(x=635, y=708)
        elif player2_position == 32:
            self.player_two_label.place(x=571, y=708)
        elif player2_position == 33:
            self.player_two_label.place(x=507, y=708)
        elif player2_position == 34:
            self.player_two_label.place(x=434, y=708)
        elif player2_position == 35:
            self.player_two_label.place(x=369, y=708)
        elif player2_position == 36:
            self.player_two_label.place(x=305, y=708)
        elif player2_position == 37:
            self.player_two_label.place(x=241, y=708)
        elif player2_position == 38:
            self.player_two_label.place(x=177, y=708)
        elif player2_position == 39:
            self.player_two_label.place(x=113, y=708)

    # Builds the player house
    # Player position && Number of Houses
    def create_house(self, player_position, house_no):

        if player_position == 1:
            if house_no == 1:
                self.brown_mediterranean_house_label.place(x=85, y=658)
            elif house_no == 2:
                self.brown_mediterranean_house2_label.place(x=85, y=643)
            elif house_no == 3:
                self.brown_mediterranean_house3_label.place(x=85, y=628)
            elif house_no == 4:
                self.brown_mediterranean_house4_label.place(x=85, y=613)

        elif player_position == 3:
            if house_no == 1:
                self.baltic_avenue_house_label.place(x=85, y=530)
            elif house_no == 2:
                self.baltic_avenue_house2_label.place(x=85, y=515)
            elif house_no == 3:
                self.baltic_avenue_house3_label.place(x=85, y=500)
            elif house_no == 4:
                self.baltic_avenue_house4_label.place(x=85, y=485)

        elif player_position == 6:
            if house_no == 1:
                self.oriental_Avenue_house_label.place(x=85, y=338)
            elif house_no == 2:
                self.oriental_Avenue_house2_label.place(x=85, y=323)
            elif house_no == 3:
                self.oriental_Avenue_house3_label.place(x=85, y=308)
            elif house_no == 4:
                self.oriental_Avenue_house4_label.place(x=85, y=293)

        elif player_position == 8:
            if house_no == 1:
                self.vermont_house_label.place(x=85, y=210)
            elif house_no == 2:
                self.vermont_house2_label.place(x=85, y=195)
            elif house_no == 3:
                self.vermont_house3_label.place(x=85, y=180)
            elif house_no == 4:
                self.vermont_Avenue_house4_label.place(x=85, y=165)

        elif player_position == 9:
            if house_no == 1:
                self.connecticut_house_label.place(x=85, y=146)
            elif house_no == 2:
                self.connecticut_house2_label.place(x=85, y=131)
            elif house_no == 3:
                self.connecticut_house3_label.place(x=85, y=116)
            elif house_no == 4:
                self.connecticut_house4_label.place(x=85, y=101)

        elif player_position == 11:
            if house_no == 1:
                self.st_charles_house_label.place(x=101, y=80)
            elif house_no == 2:
                self.st_charles_house2_label.place(x=116, y=80)
            elif house_no == 3:
                self.st_charles_house3_label.place(x=131, y=80)
            elif house_no == 4:
                self.st_charles_house4_label.place(x=146, y=80)

        elif player_position == 13:
            if house_no == 1:
                self.states_house_label.place(x=227, y=80)
            elif house_no == 2:
                self.states_house2_label.place(x=242, y=80)
            elif house_no == 3:
                self.states_house3_label.place(x=257, y=80)
            elif house_no == 4:
                self.states_house4_label.place(x=273, y=80)

        elif player_position == 14:
            if house_no == 1:
                self.virginia_house_label.place(x=291, y=80)
            elif house_no == 2:
                self.virginia_house2_label.place(x=307, y=80)
            elif house_no == 3:
                self.virginia_house3_label.place(x=322, y=80)
            elif house_no == 4:
                self.virginia_house4_label.place(x=337, y=80)

        elif player_position == 16:
            if house_no == 1:
                self.st_james_house_label.place(x=420, y=80)
            elif house_no == 2:
                self.st_james_house2_label.place(x=435, y=80)
            elif house_no == 3:
                self.st_james_house3_label.place(x=450, y=80)
            elif house_no == 4:
                self.st_james_house4_label.place(x=465, y=80)

        elif player_position == 18:
            if house_no == 1:
                self.tennessee_house_label.place(x=548, y=80)
            elif house_no == 2:
                self.tennessee_house2_label.place(x=563, y=80)
            elif house_no == 3:
                self.tennessee_house3_label.place(x=578, y=80)
            elif house_no == 4:
                self.tennessee_house4_label.place(x=593, y=80)

        elif player_position == 19:
            if house_no == 1:
                self.new_york_house_label.place(x=612, y=80)
            elif house_no == 2:
                self.new_york_house2_label.place(x=627, y=80)
            elif house_no == 3:
                self.new_york_house3_label.place(x=642, y=80)
            elif house_no == 4:
                self.new_york_house4_label.place(x=657, y=80)

        elif player_position == 21:
            if house_no == 1:
                self.kentucky_house_label.place(x=677, y=102)
            elif house_no == 2:
                self.kentucky_house2_label.place(x=677, y=117)
            elif house_no == 3:
                self.kentucky_house3_label.place(x=677, y=132)
            elif house_no == 4:
                self.kentucky_house4_label.place(x=677, y=147)

        elif player_position == 23:
            if house_no == 1:
                self.indiana_house_label.place(x=677, y=225)
            elif house_no == 2:
                self.indiana_house2_label.place(x=677, y=238)
            elif house_no == 3:
                self.indiana_house3_label.place(x=677, y=253)
            elif house_no == 4:
                self.indiana_house4_label.place(x=677, y=268)

        elif player_position == 24:
            if house_no == 1:
                self.illnois_house_label.place(x=677, y=290)
            elif house_no == 2:
                self.illnois_house2_label.place(x=677, y=305)
            elif house_no == 3:
                self.illnois_house3_label.place(x=677, y=320)
            elif house_no == 4:
                self.illnois_house4_label.place(x=677, y=335)

        elif player_position == 26:
            if house_no == 1:
                self.atlantic_house_label.place(x=677, y=418)
            elif house_no == 2:
                self.atlantic_house2_label.place(x=677, y=433)
            elif house_no == 3:
                self.atlantic_house_label.place(x=677, y=448)
            elif house_no == 4:
                self.atlantic_house_label.place(x=677, y=463)

        elif player_position == 27:
            if house_no == 1:
                self.ventnor_house_label.place(x=677, y=482)
            elif house_no == 2:
                self.ventnor_house2_label.place(x=677, y=497)
            elif house_no == 3:
                self.ventnor_house3_label.place(x=677, y=512)
            elif house_no == 4:
                self.ventnor_house4_label.place(x=677, y=527)

        elif player_position == 29:
            if house_no == 1:
                self.marvin_house_label.place(x=677, y=610)
            elif house_no == 2:
                self.marvin_house2_label.place(x=677, y=625)
            elif house_no == 3:
                self.marvin_house3_label.place(x=677, y=640)
            elif house_no == 4:
                self.marvin_house4_label.place(x=677, y=655)

        elif player_position == 31:
            if house_no == 1:
                self.pacific_house_label.place(x=614, y=677)
            elif house_no == 2:
                self.pacific_house2_label.place(x=629, y=677)
            elif house_no == 3:
                self.pacific_house3_label.place(x=644, y=677)
            elif house_no == 4:
                self.pacific_house4_label.place(x=659, y=677)

        elif player_position == 32:
            if house_no == 1:
                self.north_carolina_house_label.place(x=550, y=677)
            elif house_no == 2:
                self.north_carolina_house2_label.place(x=565, y=677)
            elif house_no == 3:
                self.north_carolina_house3_label.place(x=580, y=677)
            elif house_no == 4:
                self.north_carolina_house4_label.place(x=595, y=677)

        elif player_position == 34:
            if house_no == 1:
                self.pennsylvania_house_label.place(x=420, y=677)
            elif house_no == 2:
                self.pennsylvania_house2_label.place(x=435, y=677)
            elif house_no == 3:
                self.pennsylvania_house3_label.place(x=450, y=677)
            elif house_no == 4:
                self.pennsylvania_house4_label.place(x=465, y=677)

        elif player_position == 37:
            if house_no == 1:
                self.park_house_label.place(x=228, y=677)
            elif house_no == 2:
                self.park_house2_label.place(x=243, y=677)
            elif house_no == 3:
                self.park_house3_label.place(x=258, y=677)
            elif house_no == 4:
                self.park_house4_label.place(x=273, y=677)

        elif player_position == 39:
            if house_no == 1:
                self.broadwalk_house_label.place(x=103, y=677)
            elif house_no == 2:
                self.broadwalk_house2_label.place(x=118, y=677)
            elif house_no == 3:
                self.broadwalk_house3_label.place(x=133, y=677)
            elif house_no == 4:
                self.broadwalk_house4_label.place(x=148, y=677)

    def deactivate_space_button(self):
        self.space_button_list = [self.go_button, self.brown_mediterranean_button, self.community_chest_button,
                                  self.baltic_avenue_button, self.income_tax_button
            , self.reading_railroad_button, self.oriental_Avenue__button, self.pink_chance_button, self.vermont_button,
                                  self.connecticut_button
            , self.jail_button, self.charles_button, self.electric_button, self.states_button, self.virginia_button,
                                  self.penn_railroad_button, self.james_button
            , self.community_chest_2_button, self.tennessee_button, self.new_york_button, self.parking_button,
                                  self.kentucky_button, self.chance_button
            , self.indiana_button, self.illnois_button, self.b_o_railroad_button, self.atlantic_button,
                                  self.ventnor_button, self.water_works_button,
                                  self.marvin_button
            , self.go_to_jail_button, self.broadwalk_button, self.luxury_tax_button, self.park_place_button,
                                  self.orange_chance_button, self.short_line_button
            , self.pennsylvania_button, self.community_chest_3_button, self.north_carolina_button, self.pacific_button]

        for i in range(len(self.space_button_list)):
            self.space_button_list[i]['command'] = 1
            self.space_button_list[i]['relief'] = 'sunken'

    # get request to /api/roll
    def button_roll(self):
        test = "test"

    # get request to /api/purchase
    def button_purchase(self):
        test = "test"

    # get request to /api/build/house
    def button_house(self):
        # Temp method to make player buy house
        global position, house_num

        self.create_house(position, house_num + 1)
        house_num = (house_num + 1) % 5
        test = "test"

    # get request to /api/build/house
    def button_hotel(self):
        test = "test"

    # submit a get request to /api/update, receive the board update object through json, apply to the current gameboard.
    def get_board_update(self):
        test = "test"

board = GameBoard()
