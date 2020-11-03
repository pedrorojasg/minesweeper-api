# minesweeper-api
Minesweeper REST API, developed using Django, Django REST Framewokr and Python

Target:
The following is a list of items (prioritized from most important to least important) we wish to see:

+ Design and implement a documented RESTful API for the game (think of a mobile app for your API)
+ When a cell with no adjacent mines is revealed, all adjacent squares will be revealed (and repeat)
+ Ability to 'flag' a cell with a question mark or red flag
+ Detect when game is over
+ Persistence
+ Time tracking
+ Ability to start a new game and preserve/resume the old ones
+ Ability to select the game parameters: number of rows, columns, and mines
+ Ability to support multiple users/accounts

### Decisions taken and important notes:
+ One model Game, that stores the board in 2 layers.

field_board => the first layer, is a matrix that stores where are the mines.
game_board => the second layer, is a matrix that stores the current visible board with all the plays (discovered cells, flags, and question marks.)
+ Time tracking in the UI can be calculated using the created_time value.
+ I include validations.
+ In the future, the /games/ endpoint could return the list of games of a logged user.

## API URL demo:
https://minesweeperdemo.herokuapp.com/

## DOCUMENTATION:
2 options, browsable API or text documentation.

## Browsable API:
Use a browser and query each endpoint for more info.

# TEXT documentation.

Endpoints:

### [POST] /games/
fields: rows(int)[opt], cols(int)[opt], mines(int)[opt], name(str) [opt].
Create a new game.

### [GET] /games/
List games.

### [GET] /games/<uuid>/
Get detail of a game.

### [PATCH] /games/<uuid>/
fields: board_game(array), name(str) [opt].
Save game status.
