from typing import Union
from typing import Optional
from sys import stdin

class Quick_find:
    id: Optional[list[int, ...]]

    def __init__(self):
        self.id = []


    def __str__(self):
        return ' '.join(list(map(str, self.id)))

    def make_set(self):
        self.id.append(len(self.id))

    def union(self, x: int, y: int):
        ident = self.id[y]
        for i in range(len(self.id)):
            if self.id[i] == ident:
                self.id[i] = self.id[x]

    def find_set(self, x: int):
        return self.id[x]

    def connected(self, x: int, y: int):
        return self.id[x] == self.id[y]

if __name__ == '__main__':
    N: int = int(input())
    snm: Quick_find = Quick_find()
    for i in range(N):
        snm.make_set()
    commands: list[str, ...] = []
    for i in stdin:
        if i == '\n':
            break
        commands.append(i.rstrip('\n'))
    for i in commands:
        if i == 'print':
            print(snm)
        else:
            com: list[str, ...] = i.split()
            if com[0] == '+':
                snm.union(int(com[1]), int(com[2]))
            if i[0] == '?':
                print(snm.connected(int(com[1]), int(com[2])))
