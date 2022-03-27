#################################################################
# Name: Mosa Alsalih, Angel Beltran, and Anthony Karam
# Date: 02/22/2022
# Description: Room Adventure
# Resources:
#   Kitchen: https://www.pinterest.com/pin/288652657348413180/
#   Bathroom: https://archive.curbed.com/2018/10/5/17929942/toilets-with-threatening-auras-meme-scary-spooky-bathroom
#   Garage: https://www.flickr.com/photos/fotonormann/14890321607
#   Door: https://www.pinterest.com/guineveredoura/technical-theatre-design-portals-and-doors/
#   Bedroom: https://www.reddit.com/r/creepy/comments/iwljwp/ordinary_bedroom/
#   Entrance Room: https://roomstyler.com/rooms/16009747/design-217-haunted-house-living-room
#   Hallway: https://www.pinterest.com.au/pin/806848089473516893/
#################################################################


from tkinter import *       # Import everything from tkinter library
import pygame               # Import pygame

# the blueprint for the room
class Room(object):
    # the constructor
    def __init__(self, name, image):
        # rooms have a name, an image (the name of a file), exits, exit locations,
        # items, item descriptions, and grabbables
        self.name = name
        self.image = image
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
        self.grabbableUse = []
        self.grabbableDesc = []

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    @property
    def grabbableUse(self):
        return self._grabbableUse

    @grabbableUse.setter
    def grabbableUse(self, value):
        self._grabbableUse = value

    @property
    def grabbableDesc(self):
        return self._grabbableDesc

    @grabbableDesc.setter
    def grabbableDesc(self, value):
        self._grabbableDesc = value


    # adds an exit to the room
    # the exit is a string
    # the rooms is an instance of a Room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)

    # adds an item to the room
    # the item is a string
    # the description is a string that describes the item
    def addItems(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)

    # adds a grabbable item to the room
    # the item is a string
    def addGrabbable(self, item, use, desc):
        # append to the item to the list
        self._grabbables.append(item)
        self._grabbableUse.append(use)
        self._grabbableDesc.append(desc)
        #print(desc)

    # removes a grabbable item from the room
    # the item is a string
    def delGrabbable(self, item):
        # remove the item from the list
        self._grabbables.remove(item)

    # returns a string description of the room
    def __str__(self):
        # first, the room name
        s = "You are in {},\n".format(self.name)

        # next, the items in the room
        s += "You see: "
        for item in self.items:
            s += item + " "
        s += "\n"
        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "
        return s

# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
    # the constructor
    def __init__(self, parent):
        # call the constuctor in the superclass
        Frame.__init__(self, parent)

    # creates the rooms
    def createRooms(self):
        # r1 through r4 are the four rooms in the mansion
        # currentRoom is the room the player is currently in
        # since the currentRoom needs to be changed in the main part of the program

        # create the rooms and give them meaningful names and an image in the current directory

        r1 = Room("Entrance Room", "entrance.gif")
        r2 = Room("Hallway", "hallway.gif")
        r3 = Room("Bedroom", "bedroom.gif")
        r4 = Room("Kitchen", "kitchen.gif")
        r5 = Room("Bathroom", "bathroom.gif")
        r6 = Room("Garage", "garage.gif")
        r7 = Room("Exit Room", "exit.gif")

        # add exits to room 1 (Entrance Room)
        r1.addExit("hallway", r2)
        r1.addExit("kitchen", r4)
        r1.addExit("exit", r7)

        # add items to room 1
        r1.addItems("chair", "It is made of wicker and no one is sitting on it.")
        r1.addItems("table", "It is made of oak. There is a candlestick on it which is too heavy to lift.")

        # add exits to room 2 (Hallway)
        r2.addExit("entrance", r1)
        r2.addExit("bedroom", r3)
        r2.addExit("bathroom", r5)

        # add items to room 2
        r2.addItems("rug", "It is nice and Indian. It also needs to be vacuumed.")
        r2.addItems("torch", "It is nice and bright. But its mounted to the wall.")

        # add exits to room 3 (Bedroom)
        r3.addExit("hallway", r2)
        r3.addExit("window", None)  # DEATH!

        # add grabbables to room 3
        r3.addGrabbable("key", "door", "Door is open! You have escaped!")

        # add items to room 3
        r3.addItems("bed", "It is made out of oak wood, and it seems like no one has been using it.")
        r3.addItems("lamp", "The lamp is broken, so go figure!")
        r3.addItems("drawer", "You open it and find a glistening key!")

        # add exits to room 4 (Kitchen)
        r4.addExit("entrance", r1)
        r4.addExit("garage", r6)

        # add grabbables to room 4
        r4.addGrabbable("fork", None, None)

        # add items to room 4
        r4.addItems("sink", "It is fully of dirty dishes, I wouldn't put my hand in their if I was you!")
        r4.addItems("fridge", "It is out of power. And it has bad odor.")
        r4.addItems("oven", "It is made out of stones, and it is full of ashes. Oddly, there is also a fork placed in there.")
        r4.addItems("note", "There is a note that has some writing \non it. It reads:\n\nWhen you look at me, I smile at you. \nWhen you wink at me, I wink at you."
                            "When you kiss me, I kiss you back. When you say you love me, I say it back. Who am I?")

        # add exits to room 5 (Bathroom)
        r5.addExit("hallway", r2)

        # add grabbables to room 5
        r5.addGrabbable("toothbrush", None, None)

        # add items to room 5
        r5.addItems("toilet", "It is made out of ceramic, and it seems like the color of it has been fading \nout. There is a toothbrush on the edge of the seat.")
        r5.addItems("mirror", "It consist of broken glass. Watch out don't hurt your self now?")
        r5.addItems("note", "There is a note that has some writing \non it. It reads:\n\nWhat you seek is near where one rests")
        # add exits to room 6 (Garage)
        r6.addExit("kitchen", r4)

        # add grabbables to room 6
        r6.addGrabbable("wrench", None, None)

        # add items to room 6
        r6.addItems("car", "It is a 1992 Chevrolet, but it is out of gas.")
        r6.addItems("ladder", "It is made out of oak wood. It also looks old and fragile")
        r6.addItems("storage_shelves", "There is a wrench on the shelf. Also, there seems like there is some can\nfood, but the expiration date has passed and it is too gross to touch.")

        # add exits to room 7 (Exit)
        r7.addExit("entrance", r1)

        # add items to room 7
        r7.addItems("door", "It seems like the door is locked. Find the special key.")

        # set room 1 as the current room at the beginning of the game
        Game.currentRoom = r1

        # initialize the player's inventory
        Game.inventory = []

        # initialize what outputs from using items from the player's inventory
        Game.inventoryUnlock = []

    # sets up the GUI
    def setupGUI(self):
        # organize the GUI
        self.pack(fill=BOTH, expand=1)

        # setup the image to the left of GUI
        # the widget is a Tkinter Label
        # don't let the image control the widget's size
        img = None
        Game.image = Label(self, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)

        # setup the player input at the bottom of the GUI
        # the widget is a Tkinter Entry
        # set its background to white and bind the return key to the function process in the class
        # push it to the bottom of the GUI and let it fill horizontally
        # give it focus so the player doesn't have to click on it

        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        # setup the text tot he right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=(WIDTH / 2))
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)


    # set the current room image
    def setRoomImage(self):
        if (Game.currentRoom == None):
            # if dead, set the skull image
            Game.img = PhotoImage(file="images/skull.gif")
        else:
            # otherwise grab the image for the current room
            fileName = "images/" + Game.currentRoom.image
            Game.img = PhotoImage(file=fileName)

        # display the image on the left of the GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img

    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disabled it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            # if dead, let the player know
            Game.text.insert(END, "You are dead. The only thing you can do is quit.\n")
        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, str(Game.currentRoom) + "\nYou are carrying: " + str(Game.inventory) + "\n\n" + status)
        Game.text.config(state=DISABLED)

    # play the game
    def play(self):
        # add the rooms to the game
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the current status
        self.setStatus("")

    # processes the player's input
    def process(self, event):
        # used to connect which item is used for what
        dict = {}
        dict['key'] = 'door'
        # grab the player's input from the input at the bottom of the GUI
        action = Game.player_input.get()
        # set the user's input to lowercase to make it easier to compare the verb and noun to known values
        action = action.lower()
        # set a default response
        response = "I don't understand. Try verb noun of valid verbs are go, look, take, and use."
        # exit the game if the player wants to leave (supports quit, exit, bye)
        if (action == "quit" or action == "exit" or action == "bye" or action == "sionara!"):
            exit(0)

        # if the player is dead if goes/went south from room 4
        if (Game.currentRoom == None):
            # clears the player's input
            Game.player_input.delete(0, END)
            return

        # split the user input into words (words are separated by spaces) and store the words in a list
        words = action.split()

        # the game only understands two word inputs
        if (len(words) == 2):
            # isolate the vern and noun
            verb = words[0]
            noun = words[1]

            # the verb is: go
            if (verb == "go"):
                # set a default response
                response = "Invalid exit."

                # check for valid exits in the current room
                for i in range(len(Game.currentRoom.exits)):
                    # a valid exit is found
                    if (noun == Game.currentRoom.exits[i]):
                        # change the current room to the one that is associated with it
                        Game.currentRoom = Game.currentRoom.exitLocations[i]
                        # set the response (success)
                        response = "Room changed"
                        # no need to check any more exits
                        break

            # if the verb is: look
            elif (verb == "look"):
                # sets a default response
                response = "I don't see that item."

                # check for valid items in the current room
                for i in range(len(Game.currentRoom.items)):
                    # a valid item is found
                    if (noun == Game.currentRoom.items[i]):
                        # set the response to the item's decription
                        response = Game.currentRoom.itemDescriptions[i]
                        # no need to check any more items
                        break

            # if the verb is: take
            elif (verb == "take"):
                # sets a default response
                response = "I don't see that item."

                # check for valid grabbable items in the current room
                for i in range(len(Game.currentRoom.grabbables)):
                    # a valid grabbable item is found
                    if (noun == Game.currentRoom.grabbables[i]):
                        # add the grabbable item ot the player's inventory
                        Game.inventory.append(Game.currentRoom.grabbables[i])
                        Game.inventoryUnlock.append(Game.currentRoom.grabbableDesc[i])
                        # remove the grabbable item from the room
                        Game.currentRoom.delGrabbable(Game.currentRoom.grabbables[i])
                        # set the response (success)
                        response = "Item grabbed."
                        # no need to check anymore grabbable items
                        break

            # if the verb is: use
            elif (verb == "use"):
            # sets a default response
                response = "You can't use that here."

                # check for valid items in inventory
                for i in range(len(Game.inventory)):

                    # a valid item use is found and item is in inventory
                    # only valid item use is key for door
                    if ((noun == 'key') and ('key' in Game.inventory)):
                        # compares item in a room to see if it is the same as the use of the grabbable
                        for j in range(len(Game.currentRoom.items)):
                            if (Game.currentRoom.items[j] == 'door'):
                                # set the response (success)
                                response = "Item was used\n" + Game.inventoryUnlock[Game.inventory.index('key')]
                                # no need to check any more item uses
                                break
                    break

        # display the response on the right of the GUI
        # display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0, END)

# this main function takes care of everything
# It will display a

#initiallizing screen
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Room Adventure')


#Starting screen

#Loads image for start screen
starting_screen = pygame.image.load('images/official_zombie.jpg')
# font used fro title screen
font = pygame.font.Font('game_graphics/glitch.ttf', 20)
# sets up text location and color
start = font.render('Press space to start', False, (255,255,255))
start_rect = start.get_rect(center=(400, 500))
# Loading and playing music file
music = pygame.mixer.music.load('music/Intro_2.wav')
pygame.mixer.music.play(-1)

#game loop
active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # this is the start screen
        # while active is true screen will remain
        if active:
            screen.blit(starting_screen, (0, 0))
            screen.blit(start, start_rect)

        # if the space bar is pressed the startscreen closes and moves to GUI
        if active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    active = False
                    WIDTH = 800
                    HEIGHT = 600

                    # create the window
                    window = Tk()
                    window.geometry("{}x{}".format(WIDTH, HEIGHT))
                    window.title("Room Adventure")

                    # create the GUI as a Tkinter canvas inside the window
                    g = Game(window)
                    g.play()

                    # wait for the window to close
                    window.mainloop()

    # makes sure to update
    pygame.display.update()

