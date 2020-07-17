##### scope
My application is a top down esque role playing game built entirely in terminal and with text graphics.
Similar to other rpg games the user will input directional commands to move the character on the screen
and explore a graphically created world where they can encounter events and ultimately win the game.
The game takes inspiration from the legend of zelda as well as pokemon however will aim to provide
the audience with a unique experience.
As python is limited in inputs the user will type out full commands to move the character rather than
short button presses. e.g. "Move Left".
It aims to provide users with a brief form of entertainment to temporarily relieve stress and boredom.
The application serves as a prototype to demonstrate how a fully fleshed out game could be made to run within terminal.
Because of this the target audience is anyone who is interested enough to invest time into playing the game.

##### features
###### map loading and state saving
- Maps will be written entirely in plain text into txt files that the code will access to print
a relevant slice to the console.
- The map files will retain non volatile data i.e. The progress of the player will persist regardless of
whether the application is terminated
- Each time the character on screen moves the section of the world that is displayed centers around the new
location of the character. The map file will change to reflect this.
- When the character enters into a new area i.e. "cave" a new map file will be loaded and that will be used instead
- The save state will be contained in a similar way i.e. in a file that can be written to and read from
- When the player starts up the application for the first time the maps and save data will be generated in a folder
- The save file will be easily mutatable from the files

###### movement
- The user will be able to navigate throughout the world using written commands such as "Left".
- The user controlled character's position will be tracked using a coordinate system automtically derived from the map files. 
Its position retained within a variable.
- This character will check for collision with objects and will not be able to move into restricted areas or overwrite
objects.
- If the character manages to move out of bounds the application will exit and will print an error to the console.
- The user will be able to move multiple steps at once by providing a variable after the command.
For example if the user types: "Left 5".
A 'for' loop will execute for each of those 5 movements to the left to ensure that each move is valid.
The for loop will terminate early if the next move in the iteration is invalid.

###### inventory, interaction and help file
- Using the character the user can interact with objects in the world
- A separate file will keep track of items the player has encountered
certain states can only be accessed if the required items are present in the inventory e.g. "key"
- Hints will be given as to which item is required to further progress the game
- The player can interact with objects by entering the command "interact" which will interact with
all adjacent spaces executing conditional statements for each one
- When the user types in "help" into the terminal a list of acceptable commands will be generated with descriptions
on what each command does. This will also be written into a text file that the user can read in a text editor

###### initialization of files and management
- When save data is missing the application will create the save files that the user requires
- The application should be fully capable of running with just the python modules
- The user can input a command such as "reset" to reinitialise the application

###### word on variable scope
All relevant variables will be retained within the defined functions. When data is requested from the save file they are
loaded into the function as required which returns an outcome that another function can act on.
As I have not learned of global variables I will not be using them in this task.

#### user interaction and experience
- When the application begins the user will have the option of submitting the keyword "help" to the console
to print out a list of commands that they user can use and a description of what each command does.
- The user will submit all commands through the console input meaning that if they wish to move left
they will have to type "left" and submit it to the console
- Save data will be handled by the application. If save data is not present it will automatically create the 
save data so that the user does not have to do anything.
- Similarly the application will decide what to load depending on the current state which is handled automatically
by conditional statements
- This backend approach limits the possibility for the user to make mistakes and corrupt their data
- When errors occur the application will quit and give the user an error code that gives a brief explanation as
to what occurred. 

#### implementation plan
I plan to implement the application in stages. I will be using a check list on trello to help me manage
my work. It is important that I first build a prototype map so that I know exactly what I am working with.
Following that I will begin working on the map loading and saving functions as they are at the core of
the application.
I need to be able to write to and retrieve a map from a file that will persist as long as it is not deleted 
from the hard drive.

Moving on to the second stage I will need to program the ability for the program to locate the player then use
the fetch function from the first stage to create a viewport centered around the position of the player.
As soon as that is complete I can begin to implement movement of the player.
I will allow user input during this stage to make integration seamless. It's important that it's carried 
out in this order as I can test the application while I am building it.
After getting the basic player movement down I plan to implement conditional statements for collision and 
will wrap up player movement by introducing multimovement.

The third stage prioritizes the minor details such as win conditions, inventory and user help.
I will first implement the inventory system as the win condition can only be triggered by the inventory.
I will create user inputs for all the functions and finally create a helpfile.

Moving on to the fourth stage I implement the proper hierarchial structure separating the application into modules 
and begin building the basis for the initialization. The application should create the data for the app to work 
with when it is first run.

