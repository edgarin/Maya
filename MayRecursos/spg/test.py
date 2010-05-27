import pygame
from pygame import font

import gui
from gui import *

#Some culture stuff :D
strings = ["A bad penny always turns up.",
           "A fox smells its own lair first. and A fox smells its own stink first.",
           "Always care about your flowers and your friends. Otherwise they'll fade, and soon your house will be empty.",
           "A stitch in timeLock saves nine.",
           "Sell a man a fish, he eats for a day, teach a man how to fish, you ruin a wonderful business opportunity.",
           "Never let the right hand know what the left hand is doing.",
            ]

#PYGAME INITIALIZATION AND EXTRA STUFF
pygame.init()

screen = pygame.display.set_mode((800,600), pygame.DOUBLEBUF)

clock = pygame.time.Clock()

run = True



back = pygame.image.load('art/back.jpg').convert()

#END

#GUI STUFF
#This way it's easy to load the example gui skin:
import defaultStyle

defaultStyle.init(gui)

#First, we create a desktop to contain all the widgets
desktop = Desktop()

#Create a label passing some parameters.
#TRICKY THING HERE: if you want to use an already defined style, just copy it, and set new parameters as you wish
labelStyleCopy = gui.defaultLabelStyle.copy()
labelStyleCopy['border-width'] = 1
labelStyleCopy['wordwrap'] = True
labelStyleCopy['autosize'] = False

label = Label(position = (50,60),size = (200,100), parent = desktop, text = "Click the button for a proverb!", style = labelStyleCopy)

#Create the button
button = Button(position = (50,165), size = (200,0), parent = desktop, text = "Teach me!")

#Create the onClick callback for the button
import random
clicked = 0
def buttonOnClick(button):
    global clicked
    clicked += 1
    label.text ="Clicked %d times.\nHere's the proverb: \"%s\"" % (clicked, random.choice(strings))

#...and pass it to the button setting its onClick attribute.
button.onClick = buttonOnClick

button2 = Button(position = (50, 190), size = (200,0), parent = desktop, text = "Quit")
button2.onClick = lambda button:pygame.quit()


#Let's create a window

button3 = Button(position = (50, 220), size = (200,0), parent = desktop, text = "Demo Window")
button3.count = 0

def button3_onClick(button):
    button.count += 1
    win = Window(position = (300,220), size = (400,200), parent = desktop, text = "Window %d" % button.count)
    
    Label(position = (10,40), parent = win, text = "Write something in the textbox")
    
    win.textbox = TextBox(position = (10, 60), parent = win) 
     
    CheckBox(position = win.nextPosition(5), parent = win, text = 'Do something')
    CheckBox(position = win.nextPosition(1), parent = win, text = 'Do something')
    CheckBox(position = win.nextPosition(1), parent = win, text = 'Do something')

       
    b = Button(position = (310,70), size = (80,0) , parent= win, text = "Say it!")
    b.onClick = lambda button :Label(position = (10,30), text = win.textbox.text, parent = Window(size = (win.textbox.textWidth + 20,50), parent = desktop, text = "Hello World"))
    
button3.onClick = button3_onClick

#Let's create a window

button4 = Button(position = (300, 165), size = (200,0), parent = desktop, text = "Callbacks Window")

def button4_onClick(button):
    win = Window(position = (300,220), size = (400,200), parent = desktop, text = "A Callback Window")
    
    Label(position = (10,40), parent = win, text = "Move the window or shade it.")
    def changeTitle(text):
        def temp(window):
            window.text=text
        return temp
    win.onMove=changeTitle('I\'m Moving!')
    win.onMoveStop=changeTitle('I\'m Not Moving!')
    win.onShade=changeTitle('I\'m Shaded!')
    win.onUnshade=changeTitle('I\'m Not Shaded!')
    win.onClose= lambda button :Label(position = (10,30), text = 'You closed my favorite window', parent = Window(size = (200,50), parent = desktop, text = "Sob"))
    
button4.onClick = button4_onClick

#Textbox
txt = TextBox(position = (50,250), size = (200, 0), parent = desktop, text = "What a wonderful")

#Checkbox
chk = CheckBox(position = (50,290), size = (200,40), parent = desktop, text = "Check me if you can")

def onChkValueChanged(chk):
    button3.enabled = chk.value

chk.onValueChanged = onChkValueChanged

OptionBox(position = desktop.nextPosition(5), parent = desktop, text = "Option 1", value = True)
OptionBox(position = desktop.nextPosition(1), parent = desktop, text = "Option 2")
OptionBox(position = desktop.nextPosition(1), parent = desktop, text = "Option 3")

def itemSelected(widget):
  label.text = "You selected the row number " + str(widget.selectedIndex)
  
ListBox(position = desktop.nextPosition(5), size = (150, 100), parent = desktop,  items =["Row number %d" % i for i in range(10)]).onItemSelected = itemSelected




#EXECUTION
while run:
    clock.tick()
    display.set_caption(str(int(clock.get_fps())))
    
    #Just for exit        
    for e in gui.setEvents(pygame.event.get()):
        if e.type == pygame.QUIT:
            run = False
    
    #UPDATE YOUR LOGIC BEFORE UPDATING THE GUI
    #...
    
    #The desktop should be the last thing you update (for performance reasons)
    #First let the gui know events occurred
    
    
    #Then update the desktop you're using
    desktop.update()
    
    #Here begins rendering
    screen.fill((20,40,50))               
    
    #YOUR RENDERING HERE!!!
    screen.blit(back, (0,0))
    #END CUSTOM RENDERING
    
    #Last thing to draw, desktop
    desktop.draw()

    #Flips!
    pygame.display.flip()

#Bye bye
pygame.quit()
