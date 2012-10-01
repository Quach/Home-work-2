# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#!/usr/bin/env python
# -*- coding:utf8 -*-
"home work - forth interpreter"

STACK = []

def put(arg):
    "Put in ths stack"
    global STACK
    STACK.append(arg)
    return len(STACK) - 1

def pop():
    "Pop top"
    global STACK
    if len(STACK) > 0:
        end_of_stack = STACK[-1]
        STACK = STACK[:-1]
        return end_of_stack
    else:
        raise IndexError("Stack is empty") 

def add():
    "Add two last stack elements"
    try:
        second_arg = pop()
        first_arg = pop()
    except IndexError:
        raise IndexError("There are less than 2 arguments in a stack") 

    res = first_arg + second_arg
    put(res)
    return res

def sub():
    "subbing two last stack element"
    try:
        second_arg = pop()
        first_arg = pop()
    except IndexError:
        raise IndexError("There are less than 2 arguments in a stack") 

    res = first_arg - second_arg
    put(res)
    return res

def print_stack():
    "Print top stack element"
    try:
        end_of_stack = pop()
        put(end_of_stack)
        return end_of_stack
    except:
        raise IndexError("Stack is empty") 

def eval_forth(cmd_str):
    "Get the Forth comand"
    cmd_args = []
    cmd_args = cmd_str.split(" ")
    if len(cmd_args) == 1:
        if cmd_args[0] == "pop":
            pop()
            return
        if cmd_args[0] == "print":
            print print_stack()
            return
        if cmd_args[0] == "add":
            add()
            return
        if cmd_args[0] == "sub":
            sub()
            return
        #open file
        #try:
        #    file = open(cmd_args[0], 'r')
        #    lines = file.xreadlines()
        #    for line in lines:
        #        eval_forth(line[:-1])
        #        return
        #except Exception as inst:
        #    print inst.args[0]
        raise SyntaxError("There is no such comand")
    if cmd_args[0] == "put":
        if len(cmd_args) == 2:
            try:
                int_input_arg = int(cmd_args[1])
                put(int_input_arg)
                return
            except: #pylint!!! what erro type?
                if (cmd_args[1][0] is '"') and (cmd_args[1][-1] is '"'):
                    input_arg = cmd_args[1][1:-1]
                    if input_arg.find('"') == -1:
                        put(input_arg)
                        return
        else:
            input_arg = cmd_str[4:]
            if (input_arg[0] is '"') and (input_arg[-1] is '"'):
                input_arg = input_arg[1:-1]
                if input_arg.find('"') == -1:
                    put(input_arg)
                    return
    raise SyntaxError("There is no such comand")

def main():
    "main"
    while 1:
        eval_forth(raw_input())
    return 0

if __name__ == "__main__":
    exit(main())