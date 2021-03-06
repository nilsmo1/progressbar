# Progress bar
# Python 3.10.2

from typing import Optional
from math import ceil, floor
from colorama import Fore, Style
from time import sleep

class ProgressBar:
    def __init__(self, total: int, *, long: bool=True) -> None:
        self.total = total
        self.current = 0
        self.long = long

    def add(self) -> None:
        self.current+=1

    def display(self, description: Optional[str]=None) -> None:
        progress = int(100 * self.current / float(self.total))
        remaining = 100 - progress
        output = lambda long, done, color: (f"\r|{color + Style.BRIGHT + '█' * floor(progress/10 if not long else progress) + Style.RESET_ALL}{color + Style.DIM + '█' * ceil(remaining/10 if not long else remaining) + Fore.RESET + Style.RESET_ALL}|{progress}%\t ({color}{self.current}{Fore.RESET}/{self.total}), Task: {description or 'N/A'}")
        done = self.current == self.total
        print(output(self.long, done, done*Fore.GREEN + (not done)*Fore.YELLOW) + "\n"*done, end="\r")


if __name__ == '__main__':
    p = ProgressBar(543)
    for i in range(543):
        p.add()
        p.display()
        sleep(0.01)
