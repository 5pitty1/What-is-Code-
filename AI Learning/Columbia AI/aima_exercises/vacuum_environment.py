import random


class Panel:
    def __init__(self):
        self.agent = None
        # self.is_dirty = random.choice([True, False])
        self.is_dirty = False

    def tick(self):
        if not self.is_dirty:
            self.is_dirty = random.choice([True, False])

    def __repr__(self):
        return str((self.agent, self.is_dirty))


class Environment:
    def __init__(self):
        self.locations = [Panel() for i in range(20)]

    def __repr__(self):
        return ", ".join(repr(loc) for loc in self.locations)

    def tick(self):
        for panel in self.locations:
            panel.tick()


def main():
    e = Environment()
    count = 0
    size = 1000000
    for i in range(size):
        for i in range(10):
            e.tick()
        for loc in e.locations:
            if not loc.is_dirty:
                count += 1
        e = Environment()

    print(count)
    print((count/size)*100)



if __name__ == '__main__':
    main()
