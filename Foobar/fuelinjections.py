# import math
# from queue import Queue


# def solution(n):
#     # The main idea is that dividing by 2 is the fastest path to 1
#     # We want to divide as much as possible

#     n = int(n)
#     # path = [n]
#     count = 0

#     while n != 1:

#         if n % 2 == 0:
#             # If n is even, then divide by 2
#             newVal = n // 2
#         else:
#             # If n is odd, then find out which power of 2 it is closest to
#             logn = math.log(n, 2)

#             lower = 2 ** math.floor(logn)
#             upper = 2 ** math.ceil(logn)

#             # But even if n is closer to the upper power, we have to consider that we're going farter away from 1
#             # So we find out if the steps going up is faster than the division from going down
#             # print(upper - n, n - lower)
#             # print(math.log(upper - n, 2), math.log(n - lower, 2))
#             if upper - n < n - lower and upper - n < math.log(n - lower, 2):
#                 newVal = n + 1
#             else:
#                 newVal = n - 1

#         # path += [newVal]
#         count += 1
#         n = newVal

#     # print(path)
#     # return len(path)
#     return count


# def solution2(n):
#     # The main idea is that dividing by 2 is the fastest path to 1
#     # We want to divide as much as possible

#     n = int(n)
#     count = 0

#     while n != 1:

#         if n % 2 == 0:
#             # If n is even, then divide by 2
#             newVal = n // 2
#         else:
#             # If n is odd, then find out which power of 2 it is closest to
#             logn = math.log(n, 2)

#             lower = 2 ** math.floor(logn)
#             upper = 2 ** math.ceil(logn)

#             # But even if n is closer to the upper power, we have to consider that we're going farter away from 1
#             # So we find out if the steps going up is faster than the division from going down
#             if upper - n < n - lower:
#                 newVal = n + 1
#             else:
#                 newVal = n - 1

#         count += 1
#         n = newVal

#     return count


# def mathySolution(n):
#     # The main idea is that dividing by 2 is the fastest path to 1

#     n = int(n)
#     count = 0

#     while n != 1:

#         if n % 2 == 0:
#             # If n is even, then divide by 2
#             newVal = n // 2
#         else:
#             # If n is odd, then find out which power of 2 it is closest to
#             newVal = n - 1

#         count += 1
#         # print(f"{n} -> {newVal}: {count}")
#         n = newVal

#     # print(f"Count: {count}")
#     return count

from queue import Queue

def solution(n):
    n = int(n)
    frontier = Queue()
    visited = {}

    frontier.put((n, 0))

    while not frontier.empty():
        curr, count = frontier.get()
        if curr not in visited:
            visited[curr] = count

            if curr == 1:
                return count

            if curr % 2 == 0:
                frontier.put((curr // 2, count + 1))
            else:
                frontier.put((curr + 1, count + 1))
                frontier.put((curr - 1, count + 1))

    return 0


print solution('15')

# for i in range(1, 300000000000000):
#     sol1 = bfsSolution(i)
#     sol2 = solution(i)

#     if sol1 > sol2:
#         print("Found one!")
