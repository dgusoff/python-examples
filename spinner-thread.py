# runs spin() in a spearate process and shits it down when after slow() returns


import itertools
import time
from threading import Thread, Event
def spin(msg: str, done: Event) -> None:
    for char in itertools.cycle(r'|\/'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        wait = done.wait(.1)
        if(wait):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

def slow() -> int:
    time.sleep(3)
    return 42

def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=('thinking', done))   
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result

def main() -> None:
    result = supervisor()
    print(f'answer: {result}')

if __name__ == '__main__':
    print('starting the program')
    main()
