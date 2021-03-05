# from queue import Queue
# from math import gcd


# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# def buildTrees(tree1, tree2, depth):
#     if depth == 0:
#         return

#     tree1.left = TreeNode(tree1.val)
#     tree2.left = TreeNode(tree1.val + tree2.val)
#     tree1.right = TreeNode(tree2.val + tree1.val)
#     tree2.right = TreeNode(tree2.val)

#     buildTrees(tree1.left, tree2.left, depth - 1)
#     buildTrees(tree1.right, tree2.right, depth - 1)


# def addTrees(tree1, tree2, depth):
#     if depth < 0:
#         return

#     sumTree = TreeNode((tree1.val, tree2.val))
#     sumTree.left = addTrees(tree1.left, tree2.left, depth - 1)
#     sumTree.right = addTrees(tree1.right, tree2.right, depth - 1)

#     return sumTree


# def printTree(tree, depth):
#     frontier = Queue()
#     frontier.put(tree)
#     frontier.put(None)

#     print()
#     while not frontier.empty():
#         curr = frontier.get()

#         if not curr:
#             print()
#             print()
#             if depth == 0:
#                 break
#             depth -= 1
#             frontier.put(None)
#         else:
#             frontier.put(curr.left)
#             frontier.put(curr.right)
#             space = " " * (2 ** (depth + 1) - 2)
#             print(space, curr.val, space, " ", sep="", end="")


# def test():
#     tree1 = TreeNode(1)
#     tree2 = TreeNode(1)

#     depth = 5
#     buildTrees(tree1, tree2, depth)
#     sumTree = addTrees(tree1, tree2, depth)
#     printTree(tree1, depth)
#     printTree(sumTree, depth)


# bombMap = {}


# def makeBombs(x, y, maxX, maxY):
#     if x == maxX and y == maxY:
#         return 0

#     if x > maxX or y > maxY:
#         return -1

#     # if (x,y) in bombMap:
#     #     return bombMap[(x,y)]

#     first = makeBombs(x, y + x, maxX, maxY)

#     if first >= 0:
#         return first + 1

#     second = makeBombs(x + y, y, maxX, maxY)

#     if second >= 0:
#         return second + 1

#     return -1


# def solution(x, y):
#     # # There is a bijective relationship between there being an answer and x,y being coprime
#     # if gcd(x, y) != 1:
#     #     return 0
#     frontier = []

#     frontier.append((1, 1, 0))

#     while len(frontier) > 0:
#         currX, currY, depth = frontier.pop()
#         if currX == x and currY == y:
#             return depth

#         if currX <= x and currY <= y:
#             frontier.append((currX, currY + currX, depth + 1))
#             frontier.append((currX + currY, currY, depth + 1))

#     return -1


def solution(x, y):
    x = int(x)
    y = int(y)
    
    steps = -1
    while y:
        steps += x // y
        x, y = y, x % y

    if x != 1:
        return "impossible"

    return str(steps)


print solution('4', '7')

# for x in range(1, 1000):
#     print(
#         x,
#         [computeGCD(x, y) for y in range(1, x + 1)]
#         == [computeGCD(x, y) for y in range(1, x + 1)],
#     )
