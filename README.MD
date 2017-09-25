# Dojo Room Allocator
[![Build Status](https://travis-ci.org/isheebo/Dojo.svg?branch=master)](https://travis-ci.org/isheebo/Dojo)
[![Coverage Status](https://coveralls.io/repos/github/isheebo/Dojo/badge.svg?branch=master)](https://coveralls.io/github/isheebo/Dojo?branch=master)
[![CircleCI](https://circleci.com/gh/isheebo/Dojo.svg?style=svg)](https://circleci.com/gh/isheebo/Dojo)
![Python Version](https://img.shields.io/badge/Python-3.6-blue.svg)

The Dojo Room Allocator is a simple utility that demonstrates how room allocation can be carried out at Andela Kenya's main facility, the Dojo. 
It uses data structures (mainly dictionaries and lists) to staire and manipulate information that is provided unto it. Data storage for the mean time is non-persistent. Sqlite3 will be used to persist data in the near future.

## Justification
When a new Fellow joins Andela, they are assigned an office space and an optional living space if they choose to opt in. When a new Staff joins they are assigned an office space only. This simple application emulates a working model of how the rooms may be allocated.

## Usage
To get started, it is assumed you have [python 3.6](https://www.python.org) and [git](https://www.git-scm.com) installed. clone this repo by running `git clone https://github.com/isheebo/dojo.git`.

- install a virtual environment and configure it for the project.
```
$ pip install virtualenv
$ mkdir venv
$ virtualenv -p <path to your python executable> venv
$ cd venv/scripts/activate
```
- inside your virtual environment, install dependencies

```sh
$ pip install -r requirements.txt
```
- run the application
```
$ python main.py
```

## Documentation

**`create_room <room_type> <room_name>...`** creates a room or rooms of type *room_type*

**`add_person <first_name> <second_name> <FELLOW|STAFF> [<wants_accommodation>]`** adds a person of either type fellow or staff to the dojo. *wants_accommodation* is an optional parameter.

**`print_room <room_name>`** prints the details of a room specified by *room_name*

**`load_people <filename>`** adds people to the dojo from *filename* if filename is not empty

**`print_allocations [<-o=filename>]`** prints all rooms in the dojo and all related information

**`print_unallocated [<-o=filename>]`** prints unallocated people in the Dojo.

**`reallocate_person <first_name> <second_name> <new_room_name>`** reallocates a person to *new_room_name*

**`help`**     displays the usage message

**`clear`**    Clears the application screen

**`quit`**     Exits the application

