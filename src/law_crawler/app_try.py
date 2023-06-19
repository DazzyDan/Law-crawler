# SuperFastPython.com
# example of a parallel for loop
from time import sleep
from random import random
from multiprocessing import Pool
from scrape.try_manager import Try_M
from scrape.try_2 import Try_2
from multiprocessing import set_start_method

# task to execute in another process
d = {}


def task(arg):
    print(arg)
    if arg == 1:
        t = Try_M()
    elif arg == 0:
        t = Try_2()
    value = t.try_manager()

    return value


# entry point for the program
# set the start method
set_start_method("fork")
# create the process pool
with Pool() as pool:
    # call the same function with different data in parallel
    for result in pool.map(task, [1, 0]):
        # report the value to show progress
        d.update(result)
print(d)
