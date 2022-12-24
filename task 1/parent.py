#!/usr/bin/python3
import os
import sys
import random

CHILD_PROGRAM_FILE = './child.py'


def fork():
    child = os.fork()
    if child > 0:
        print(f'Parent[{os.getpid()}]: I ran children process with PID {child}')
    else:
        os.execl(CHILD_PROGRAM_FILE, CHILD_PROGRAM_FILE, str(random.randint(5, 10)))

    return child


n = int(sys.argv[1])

while n > 0:
    child = fork()
    if child > 0:
        n -= 1

n = int(sys.argv[1])
while n > 0:
    child_pid, status = os.wait()
    if status != 0:
        child = fork()
    else:
        print(f'Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit Status {status}.')
        n = n - 1

os._exit(os.EX_OK)
