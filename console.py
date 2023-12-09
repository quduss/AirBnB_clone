#!/usr/bin/python3
"""command line interpreter for testing and debugging"""

import cmd
from models.base_model import BaseModel
from models import storage


def cne():
    """prints error message"""
    print("** class doesn't exist **")


def cnm():
    """prints error messages"""
    print("** class name missing **")


def idm():
    """prints error messages"""
    print("** instance id missing **")


def nif():
    """prints error messages"""
    print("** no instance found **")


def anm():
    """prints error messages"""
    print("** attribute name missing **")


def vm():
    """prints error messages"""
    print("** value missing **")


def list_instances(my_dict):
    """returns list of string represenations of all
    instances in the __objects dictionary"""
    list_ = []
    for key in my_dict.keys():
        obj = my_dict[key]
        list_.append(str(obj))
    return list_


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """end-of-file marker"""
        return True

    def emptyline(self):
        """default function called when enter is pressed
        on an empty line"""
        pass

    def do_create(self, line):
        """command handler for the create command
        that creates a new BaseModel instance"""
        args_list = line.split()
        try:
            if args_list[0] == 'BaseModel':
                my_obj = BaseModel()
                my_obj.save()
                print(my_obj.id)
            else:
                cne()
        except IndexError:
            cnm()

    def do_show(self, line):
        """displays the string representaion of an instance"""
        args = line.split()
        try:
            if args[0] == 'BaseModel':
                try:
                    key = 'BaseModel' + '.' + args[1]
                    my_dict = storage.all()
                    if key in my_dict:
                        print(my_dict[key])
                    else:
                        nif()
                except IndexError:
                    idm()
            else:
                cne()
        except IndexError:
            cnm()

    def do_destroy(self, line):
        """destroys an instance and updates the json file"""
        args = line.split()
        try:
            if args[0] == 'BaseModel':
                try:
                    key = 'BaseModel' + '.' + args[1]
                    my_dict = storage.all()
                    if key in my_dict:
                        del my_dict[key]
                        storage.save()
                    else:
                        nif()
                except IndexError:
                    idm()
            else:
                cne()
        except IndexError:
            cnm()

    def do_all(self, line):
        """prints the list of string representations of all
        instances"""
        args = line.split()
        my_dict = storage.all()
        try:
            if args[0] == 'BaseModel':
                my_list = list_instances(my_dict)
                print(my_list)
            else:
                cne()
        except IndexError:
            my_list = list_instances(my_dict)
            print(my_list)

    def do_update(self, line):
        """updates an attribute of an instance with a new value"""
        args = line.split()
        try:
            if args[0] == 'BaseModel':
                try:
                    key = args[0] + '.' + args[1]
                    my_dict = storage.all()
                    if key in my_dict:
                        try:
                            if args[2]:
                                try:
                                    value = args[3]
                                    obj = my_dict[key]
                                    obj.set_attribute(args[2], eval(value))
                                    obj.save()
                                except IndexError:
                                    vm()
                        except IndexError:
                            anm()
                    else:
                        nif()
                except IndexError:
                    idm()
            else:
                cne()
        except IndexError:
            cnm()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
