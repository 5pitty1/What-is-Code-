from heapq import heappush, heappop


class Stack:

    def __init__(self):
        self.items = []
        self.exists = set()

    def push(self, value):
        self.items.append(value)
        self.exists.add(value)

    def pop(self):
        item = self.items.pop()
        self.exists.remove(item)
        return item

    def is_empty(self):
        return not self.items

    def __contains__(self, item):
        return item in self.exists


class Queue:
    def __init__(self):
        self.items = []
        self.exists = set()

    def add(self, value):
        self.items.insert(0, value)
        self.exists.add(value)

    def remove(self):
        item = self.items.pop()
        self.exists.remove(item)
        return item

    def is_empty(self):
        return not self.items

    def __contains__(self, item):
        return item in self.exists


class PriorityQueue:
    def __init__(self):
        self.items = []
        self.exists = set()

    def add(self, value):
        heappush(self.items, value)
        self.exists.add(value)

    def remove(self):
        item = heappop(self.items)
        self.exists.remove(item)
        return item

    def is_empty(self):
        return not self.items

    def __contains__(self, item):
        return item in self.exists
