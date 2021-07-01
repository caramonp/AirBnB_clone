### AirBnB: The console.

![AirBnB](https://github.com/caramonp/AirBnB_clone/blob/main/images/images.png)

### :computer: About the proyect :computer:
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

### Prerequisites :information_desk_person:
 - Install Git

 - Clone repository

 - Install python

    $ sudo apt-get install git
    $ sudo apt-get install python3-pep8

### How to install

- In your linux terminal use the command `git clone https://github.com/caramonp/AirBnB_clone.git`

### To run the shell: :runner:

Execution
Your shell should work like this in interactive mode:

![$ ./console.py](https://github.com/caramonp/AirBnB_clone/blob/main/images/uso_consola.png)

But also in non-interactive mode: (like the Shell project in C)

![$ ./console.py](https://github.com/caramonp/AirBnB_clone/blob/main/images/modo_no_interactivo.png)

basically the console do :sunglasses:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc
- Do operations on objects (count, compute stats, etc)
- Update attributes of an object
- Destroy an object
- show - show an object (based on id)
- all - show all objects, of one type or all types
- quit/EOF - quit the console
- help - see descriptions of commands

### Commands

- `create`: Creates a new instance, saves it (to the JSON file) and prints the instance id.
- `show`: Prints the string representation of an instance based on the class name and instance id.
- `destroy`:  Deletes an instance based on the class name and id.
- `all`: Prints all string representation of all instances based or not on the class name.
- `update`: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

### Classes allowed

- `BaseModel`: that defines all common attributes/methods for other classes.
- `State`
- `City`
- `Amenity`
- `Place`
- `Review`

### How to use it

![$ usos](https://github.com/caramonp/AirBnB_clone/blob/main/images/usos.png)


### Objetive Console
![Objetive Console](https://github.com/caramonp/AirBnB_clone/blob/main/images/objetive_console.JPG)


The console will be a tool to validate this storage engine.

The console has the ability to:
- create a data model
- manage (create, update, destroy, etc) objects via a console / command interpreter.
- store and persist objects to a file (JSON file).


### Flowchard

![Flowchard](https://github.com/caramonp/AirBnB_clone/blob/main/images/Airbnb_c14_flowchard.jpg)
See the full image [here](https://miro.com/app/board/o9J_l9Ohrcw=/?moveToWidget=3074457360852427129&cot=14)

### Rsources :closed_book:

- [Packages](https://docs.python.org/3.4/tutorial/modules.html#packages)
- [Python packages](https://intranet.hbtn.io/concepts/66)
- [Cmd](https://docs.python.org/3.4/library/cmd.html)
- [Arguments](https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3)

### Authors
- Carolina Ramon Palacio 2966@holbertonschool.com
- Vannesa Garcia Vargas 2380@holbertonschool.com
- Dania Puertas Mangones 2875@holbertonschool.com
