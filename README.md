# advent2025

These are solved puzzles for [12 days challenge for 2025](https://adventofcode.com)


Each puzzles has its own directory. 
A virtual env is shared by all days in the root folder using uv. Remember to do a "uv pip freeze > requirements.txt" when adding new modules, since we're being to lazy to create a project toml file

For each day, go into the directory:

to test:

```
uv run pytest --log-cli-level=DEBUG
```

ro run:

```
uv run <day>.py < {day}.txt
```
