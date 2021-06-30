
# AirBnB_clone
<img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210624%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210624T220410Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a4288aedae9a73db7af51b0139dd50616babfda0d1d518fff7ecb462fd78679e" alt="" style="" />

---

This is a project for the holberton school academy, which consists of making an AirBnB clone - console.
the first step for this project is to make a command interpreter.

### The command interpreter

So far the command interpreter is capable of:
* create a new object
* destroy an object

### Instalation
```
git clone https://github.com/sneidergv/AirBnB_clone.git
cd AirBnB_clone
```

### Usage
Interactive mode

| COMMAND | DESCRPTION |
| --- | --- |
| `(hbnb) quit` | Exit the console |
| `(hbnb) quit` | Exit command interpreter |
| `(hbnb) help` | Displays available commands |
| `(hbnb) create` | """ |
| `(hbnb) show` | """ |
| `(hbnb) destroy` | """ |
| `(hbnb) all` | """ |
| `(hbnb) update` | """ |

### Example
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
Non-Interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

---

## Execution of tests
To run the unit tests of this project, the following command must be executed: python3 -m unittest discover tests

## Done in
* Language: Python3
* OS:
* style guide: PEP 8

## Author
* **Esneider Granada Valencia** - [sneidergv](https://github.com/sneidergv)
* **Julián Tabares** - [Julianeme](https://github.com/Julianeme)
* **Sergio velasquez** - [sergiovelasquez18](https://github.com/sergiovelasquez18)