# minesweeper-api
Minesweeper REST API, developed using Django, Django REST Framewokr and Python

## Goal:
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
+ The API structure is scalable and follows the good practices of url names, data structures and documentation.
+ One model Game, that stores the board in 2 layers.

field_board => the first layer, is a matrix that stores where are the mines.
game_board => the second layer, is a matrix that stores the current visible board with all the plays (Unclicked cells, discovered cells, flags, and question marks.)
+ Time tracking in the UI can be calculated using the created_time value.
+ I include validations.
+ I include unit tests.
+ In the future, the /games/ endpoint could return the list of games of a logged user.
+ The configuration is handled in a specific module that contains a common configuration file, one file for the development environment and one for the production environment.
+ The deploy is on Heroku.
+ I did not have time to finish the frontend interface for work, I will continue working on it over the weekend.

### Symbols:
+ '': Empty cells in field_board. Unclicked cells in game_board.
+ 'm': Mine in field_board.
+ 'f': flag in game_board.
+ '?': Question mark in game_board.

## Run project in local:
+ Clone repo.
+ Locate at repo root folder.
`cd minesweeper-api`
+ Create a virtual environment.
+ Install dependencies:
`pip install -r requirenents.txt`
+ Create a postgres database in local.
+ Create a file ".envdev" for set local environment variables.
`touch .envdev`
+ Configure the file using the params in .envexample file.
+ Run migrations.
`python manage.py migrate`
+ Run Django development server.
`python manage.py runserver`

## Run tests:
+ Run Django test suite.
`python manage.py test`

## API URL demo:
https://minesweeperdemo.herokuapp.com/

# DOCUMENTATION:
2 options: swagger or text documentation.

## Swagger docs:
https://minesweeperdemo.herokuapp.com/docs/

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

