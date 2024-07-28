Programming Language: Python

Structure of the code:
A single python file is developed named red_blue_nim.py. In this code, there are three main components, red_blue_nim function helps in processing and printing results. 2 classes have been implemented one for the standard version and the other for the misere version.

->When the command line is executed, the game starts by displaying the stats of red, blue balls and player.

->depending on the player, either human or computer starts playing. In human's chance, we need to choose the pile and select no of balls.

-> repeat the above step until either of the pile gets to zero(0). 

-> Then the result is displayed as the player who wins/loses the game and final score is shown.



Libraries used:
sys: Used this library to interact the python file with the command line arguments, sys.argv provides the access for it.

Need to run the code from terminal (command_line_argument)

 We have to provide 5 arguments, following the order as <file_name> <num_red> <num_blue> <version> <player> <depth>

they are:
1. Python execution file
2. No of Red Balls
3. No of Blue Balls
4. version can be either standard or misere, by default the standard version is played
5. player can be either human or computer, by default the computer plays first


Example to run the code: 

For standard Version:-  python red_blue_nim.py 8 6 standard human 2
			
			(or)
			
			python red_blue_nim.py 8 6 human 2 (if the version is not mentioned)


For Misere Version:-     python red_blue_nim.py 8 6 misere human 3

