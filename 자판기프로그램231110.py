machine=['power','energy','water','beer','coffee']

def check_machine():
    print(machine)

def is_drink():
    drink=input('drink? ')
    if drink in machine:
        print('Y')
    else: 
        print('N')

def add_drink():
    drink=input('drink? ')
    machine.append(drink)
    print(machine)

def remove_drink():
    drink=input('drink? ')
    machine.remove(drink)
    print(machine)

check_machine()
is_drink()
add_drink()
remove_drink()