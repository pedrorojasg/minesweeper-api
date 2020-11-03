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
Create a new game.

fields: rows(int)[opt], cols(int)[opt], mines(int)[opt], name(str) [opt].

### [GET] /games/
List games.

### [GET] /games/<uuid>/
Get detail of a game.

### [PATCH] /games/<uuid>/
Save game status.

fields: board_game(array), name(str) [opt].

## Data structure
Game:
{
    
    "id": uuid,
    
    "owner": user_id or null,
    
    "created_time": datetime[str],
    
    "last_update_time": datetime[str],
    
    "finished_time": null or datetime[str],,
    
    "secret": str,
    
    "status": "started" or "won" or "lost,
    
    "rows": int,
    
    "cols": int,
    
    "mines": int,
    
    "field_board": Array[Array[str]],
    
    "game_board": Array[Array[str]],
    
    "name": ""
}


Example:
{
    
    "id": "f0b96dfe-8fe8-4b8b-8cf1-6e664fed63a5",
    
    "owner": null,
    
    "created_time": "2020-11-03T15:37:24.890257-06:00",
    
    "last_update_time": "2020-11-03T15:37:24.917880-06:00",
    
    "finished_time": null,
    
    "secret": "A24F3926C10B",
    
    "status": "started",
    
    "rows": 4,
    
    "cols": 4,
    
    "mines": 5,
    
    "field_board": [
        
        [
            
            "m",
            
            "",
            
            "",
            
            "m"
            
        ],
        
        [
            
            "",
            
            "m",
            
            "",
            
            ""
            
        ],
        
        [
            
            "",
            
            "",
            
            
            "",
            
            ""
            
        ],
        
        [
            
            "",
            
            "m",
            
            "",
            
            "m"
            
        ]
        
    ],
    
    "game_board": [
        
        [
            
            "",
            
            "",
            
            "",
            
            ""
            
        ],
        
        [
            
            "",
            
            "",
            
            "",
            
            ""
            
        ],
        
        [
            
            "",
            
            "",
            
            "",
            
            ""
            
        ],
        
        [
            
            "",
            
            "",
            
            "",
            
            ""
            
        ]
        
    ],
    
    "name": ""
}

