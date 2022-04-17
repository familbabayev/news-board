# News Board API

News Board API for test assessment

## Features
- CRUD Post Api
- CRUD Comment Api (Nested Api under Posts)
- Upvote a Post

## Installation

1. Clone this repo

    `git clone https://github.com/familbabayev/news-board.git`
2. Run the container (if you get an error, run again) (for linux use sudo)
    
    `docker-compose up --build`

## Linter and Formater
To check flake8 linting

`docker-compose run --rm app sh -c "flake8"`

To check black formatter (line length is selected 79, because flake8 checks line length with 79)

`docker-compose run --rm app sh -c "black --line-length 79 .""`
