##### scope
My application is a top down esque role playing game built entirely in terminal and with text graphics.
Similar to other rpg games the user will input directional commands to move the character on the screen
and explore a graphically created world where they can encounter events and ultimately win the game.
The game takes inspiration from the legend of zelda as well as pokemon however will aim to provide
the audience with a unique experience.
As python is limited in inputs the user will type out full commands to move the character rather than
short button presses. e.g. "Move Left".
The user will also select from multiple choice options where their
decisions will have an impact on the outcome of the game.
It aims to provide users with a brief form of entertainment to temporarily relieve stress and boredom.
The application serves as a prototype to demonstrate how a fully fleshed out game could be made to run within terminal.
Because of this the target audience is anyone who is interested enough to invest time into playing the game.

##### features
###### map creation
- A map will be written in a txt file that the code will access to print a relevant slice to the console.
- The map will be loaded into row array's with each position in the row array representing what is in the column.
- Each time the character on screen moves the section of the world that is displayed centers around the new
location of the character.
- As the character nears the edges of the map the slice will be retained in a position where the character remains
on screen without reducing the amount of information displayed


###### movement
- The user will be able to navigate throughout the world using written commands such as "Move Left".
- The user controlled character's position will be tracked using a coordinate system. Its position retained within a variable.
- This character will check for collision with objects and will not be able to move into restricted areas or overwrite
objects.
- If the character manages to move out of bounds the application will exit and will print an error to the console.

- The user will be able to move multiple steps at once by providing a variable after the command.
For example if the user types: "Move Left 5".
A for loop will execute for each of those 5 movements to the left to ensure that each move is valid.
The for loop will terminate early if the next move in the iteration is invalid.


