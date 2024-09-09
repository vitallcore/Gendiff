### Hexlet tests and linter status:
[![Actions Status](https://github.com/vitallcore/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/vitallcore/python-project-50/actions)
<a href="https://codeclimate.com/github/vitallcore/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/f0a76ea8589689b816c1/maintainability" /></a>
<a href="https://codeclimate.com/github/vitallcore/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/f0a76ea8589689b816c1/test_coverage" /></a>
---
# The Gendiff project
This project was made to help to find out the difference between two files and make this process easier and faster, enjoy!
---
## How to show help message:

Use CLI and type this command: "gendiff -h"
[![asciicast](https://asciinema.org/a/674356.svg)](https://asciinema.org/a/674356)

## To compare two files (JSON or YAML) use this command:

gendiff filepath1.json filepath2.json

gendiff filepath1.yml filepath2.yml

## To use built in formatters use this command:

-f/--format - the flag which allows to choose any formatter

gendiff -f stylish filepath1 filepath2 - to show stylish ouput

gendiff -f plain filepath1 filepath2 - to show plain output

gendiff -f json filepath1 filepath2 - to show json output

## Here's the example of 'stylish' comparing JSON and YAML files:
[![asciicast](https://asciinema.org/a/674836.svg)](https://asciinema.org/a/674836)
## Here's the example of 'plain' comparing JSON and YAML files:
[![asciicast](https://asciinema.org/a/674986.svg)](https://asciinema.org/a/674986)
## Here's the example of formattind diff into JSON format:
[![asciicast](https://asciinema.org/a/674993.svg)](https://asciinema.org/a/674993)
---
### Installation requirements and instruction.

Installation requirements:
1. CPython.
2. Poetry.
3. Git.
4. Make.

How to install the project:
1. Clone this project repo(git clone "url of the project").
2. Cd to the cloned project.
3. Use command "make build" to build the package.
4. Install the built package using pip.
5. Use the project.

## Important note:

If you want to check the project's code you always can use "make lint" command to use a linter built in a project.
---
### Links

This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://python-poetry.org/)                                        | "Python dependency management and packaging made easy"  |
| [flake8](https://flake8.pycqa.org/)                                         | "Your tool for style guide enforcement" |

---
