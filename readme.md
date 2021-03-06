# Terminal Application

#### scope

My application is a top down esque adventure game built entirely in terminal with text graphics.
The application serves as a prototype to demonstrate how a fully fleshed out game could be made to run within terminal.
Similar to other rpg games the user will input directional commands to move the character on the screen and explore a graphically created world where they can encounter events and ultimately win the game.
The game takes inspiration from the legend of zelda as well as pokemon however will aim to provide the audience with a unique experience being that is is run from a console using python.

I set out to create the application with the intention of gaining a knowledge in how games are created. By using a text based graphical interface I am able to ignore the need to create graphics and can focus on code creation. This will also be my first project in python so I hope to be able to gain a working understanding of python.

As python is limited to what can be input the user will type out full commands into the console to move the character rather than short button presses. e.g. "Move Left". The application should handle all the back end work so the user can just sit back and enjoy
the experience. This includes managing save data, creating the maps, and writing to the maps.

Finally the application should be shipped with only 4 .py files which when run should create .txt and .json files which will contain the save data and maps.
The user will be able to reset save data from within the application.

For the end user the app aims to provide a brief form of entertainment to temporarily relieve stress and boredom.
Because of this the target audience is anyone who is interested enough to invest time into playing the game.

#### features

- **Map loading and state saving**
  - Maps will be written entirely in plain text into txt files that the code will access to print a relevant slice to the console.

  - The map files will retain non volatile data i.e. The progress of the player will persist regardless of whether the application is terminated

  - Each time the character on screen moves the section of the world that is displayed centers around the new location of the character. The map file will change to reflect this.

  - When the character enters into a new area i.e. "cave" a new map file will be loaded and that will be used instead

  - The save state will be contained in a similar way i.e. in a file that can be written to and read from

  - When the player starts up the application for the first time the maps and save data will be generated in a folder

  - The save file will be easily mutatable from the files

- **Movement**
  - The user will be able to navigate throughout the world using written commands such as "Left".

  - The user controlled character's position will be tracked using a coordinate system automtically derived from the map files. Its position retained within a variable.

  - This character will check for collision with objects and will not be able to move into restricted areas or overwrite objects.

  - If the character manages to move out of bounds the application will exit and will print an error to the console.

  - The user will be able to move multiple steps at once by providing a variable after the command.

  - For example if the user types: "Left 5". A 'for' loop will execute for each of those 5 movements to the left to ensure that each move is valid. The for loop will terminate early if the next move in the iteration is invalid.

- **Inventory, interaction and help file**
  - Using the character the user can interact with objects in the world

  - A separate file will keep track of items the player has encountered. Certain states can only be accessed if the required items are present in the inventory e.g. "key"

  - Hints will be given as to which item is required to further progress the game

  - The player can interact with objects by entering the command "interact" which will interact with all adjacent spaces executing conditional statements for each one

  - When the user types in "help" into the terminal a list of acceptable commands will be generated with descriptions on what each command does. This will also be written into a text file that the user can read in a text editor

- **Initialization of files and management**
  - When save data is missing the application will create the save files that the user requires

  - The application should be fully capable of running with just the python modules

  - The user can input a command such as "reset" to reinitialise the application

#### word on variable scope

All relevant variables will be retained within the defined functions. When data is requested from the save file they are loaded into the function as required which returns an outcome that another function can act on.
As I have not learned about global variables I will not be using them in this task.

![flowchart](/docs/flowchart.png)

#### user interaction and experience

- When the application begins the user will have the option of submitting the keyword "help" to the console to print out a list of commands that they user can use and a description of what each command does.
- The user will submit all commands through the console input meaning that if they wish to move left they will have to type "left" and submit it to the console
- Save data will be handled by the application. If save data is not present it will automatically create the save data so that the user does not have to do anything.
- Similarly the application will decide what to load depending on the current state which is handled automatically by conditional statements
- This backend approach limits the possibility for the user to make mistakes and corrupt their data
- When errors occur the application will quit and give the user an error code that gives a brief explanation as to what occurred. 

#### implementation plan

I plan to implement the application in stages. I will be using a check list on trello to help me manage my work. It is important that I first build a prototype map so that I know exactly what I am working with. Following that I will begin working on the map loading and saving functions as they are at the core of the application.
I need to be able to write to and retrieve a map from a file that will persist as long as it is not deleted from the hard drive.

Moving on to the second stage I will need to program the ability for the program to locate the player then use the fetch function from the first stage to create a viewport centered around the position of the player. As soon as that is complete I can begin to implement movement of the player.
I will allow user input during this stage to make integration seamless. It's important that it's carried out in this order as I can test the application while I am building it.
After getting the basic player movement down I plan to implement conditional statements for collision and will wrap up player movement by introducing multimovement.

The third stage prioritizes the minor details such as win conditions, inventory and user help. I will first implement the inventory system as the win condition can only be triggered by the inventory. Afterwards I will create user inputs for all the functions and finally create a helpfile.

Moving on to the fourth stage I will implement a clean hierarchial structure, separating the application into modules and begin building the basis for the initialization. The application should create the data for the app to work with when it is first run.

***

##### checklists

* **Map loading and State saving**
  - Create prototype map in txt file

  - Write code to pull map from txt file and print to console

  - Write code to locate “*” on map

  - Create code to generate viewport around “*” and print to console

  - Create a function which writes an array containing strings to map file

  - Create second map file and refine first

  - Create a variable which holds the current maps directory

  - Create a module that handles generating the map files from python strings and creates a save file defining which map is the current map which is read from and written to the current map variable

**Finish above by end of first day**

***

* **Movement**
  - Incorporate movement in one direction. Writing to the map file the new position of the asterix, removing the old position of the asterix from the file and overwriting what was previously in the new position

  - Incorporate movement in all directions

  - Use conditional statements to check what the spot the asterix will move to currently holds

  - Limit movement only to spaces which are occupied by a “.”

  - Implement the ability for multiple moves to be made at once

  - Allocate a string character such as “~”,”_” or “^” that when the character moves over switches the current map variable from one file to the other map file

  - Use the map loading function to load the current viewport after every move

**Finish above by end of second day**

***

* **Inventory, Interaction and Help file**
  - Introduce an inventory variable as a list

  - Define a function which fetches what is contained in each adjacent space using a loop and stores the values in a list

  - Define a function which uses a for loop to check the list for particular characters

  - Create an if statement that runs on the for loop to check if there is a “k” character within the list. 
    If it is present remove “k” from the map and create a key file

  - Create an if statement that runs on the for loop to check if there is a “0” character within the list and the key file exists. 
    If true end the game and go to victory screen

  - Elif key file does not exist print a hint to the user explaining that a key is required for the interaction

  - Use a while loop to run a inventory check on every turn which appends “key” to the inventory list if key file exists

  - Write a function to print the inventory list to the console

**Finish above by end of third day**

***

* **Initialisation and testing**
  - Separate into modules and functions

  - Create initialisations for all files

  - Create reset command

  - Test application extensively

**Finish above by due date**

***

### screenshots

![initial](/docs/trello1.png)

![first-day](/docs/trello2.png)

![second-day](/docs/trello3.png)

![third-day](/docs/trello4.png)

![last-day](/docs/trello5.png)
