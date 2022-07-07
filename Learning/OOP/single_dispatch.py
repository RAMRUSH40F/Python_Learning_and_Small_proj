from functools import singledispatch

@singledispatch
def my_func(arg):
    print('Default my_func', arg)

@my_func.register
def my_func_for_ints(arg: int):
    print('This is a int')
