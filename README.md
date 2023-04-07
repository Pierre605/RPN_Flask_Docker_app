## Reverse Polish Notation Calculator

*Developer : Pierre L. (2023)*

Flask app with front view in Docker.

You need Docker Engine and Docker Compose running on your machine before running docker commands.

`docker-compose up --build` within the app directory

And you are good to go.

### Correct PNI calculation query syntax:

>"3 2 + 2 -" <=> (3 + 2) - 2

>"5 3 1 + + 1 5 x - 8 3 - / 2 +" <=> ((((1 + 3) + 5) - (5 * 1)) / (8 - 3)) + 2

**One space between each number and operator.**
**'x' char for multiplication.**

You can consume the API with CLI by running `python3 query_api_by_cli.py` within the app directory.

`docker-compose down` to stop and remove containers