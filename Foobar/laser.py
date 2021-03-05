from math import pi, sin, cos, sqrt, gcd

# from fractions import gcd

# Vector class for extra readability
class Vector:
    def __init__(self, dx, dy, start):
        self.dx = dx
        self.dy = dy
        self.start = start

    # Component-wise vector addition
    def __add__(self, other):
        dx = self.dx + other.dx
        dy = self.dy + other.dy

        return Vector(dx, dy, self.start or other.start)

    # Component-wise vector subtraction
    def __sub__(self, other):
        dx = self.dx - other.dx
        dy = self.dy - other.dy

        return Vector(dx, dy, self.start or other.start)

    # Component-wise vector multiplication
    def __mul__(self, other):
        if isinstance(other, Vector):
            dx = self.dx * other.dx
            dy = self.dy * other.dy
        else:
            dx = self.dx * other
            dy = self.dy * other

        return Vector(dx, dy, self.start or other.start)

    def isBetween(self, left, right):
        relativeToLeft = self - left.start
        dotLeft = left.dx * (-relativeToLeft.dy) + left.dy * relativeToLeft.dx

        relativeToRight = self - right.start
        dotRight = right.dx * (-relativeToRight.dy) + right.dy * relativeToRight.dx

        return dotLeft > 0 and dotRight <= 0

    def isOn(self, other):
        relativeToOther = self - other.start
        rotatedDot = other.dx * (-relativeToOther.dy) + other.dy * relativeToOther.dx
        dot = other.dx * relativeToOther.dx + other.dy * relativeToOther.dy
        return dot > 0 and rotatedDot > -0.00001 and rotatedDot < 0.00001

    def __repr__(self):
        return "(" + str(self.dx) + "," + str(self.dy) + ")"


class Room:
    def __init__(self, dimensions, you, guard):
        self.dimensions = Vector(dimensions[0], dimensions[1], None)
        self.you = Vector(you[0], you[1], None)
        self.guard = Vector(guard[0], guard[1], None)

    def findWallCollision(self, direction):
        walls = [
            [0, self.dimensions.dx],  # Min and max x-vals
            [0, self.dimensions.dy],  # Min and max y-vals
        ]
        min_t = float("inf")
        reflectVals = Vector(1, 1, None)
        for wall in walls[0]:
            if direction.dx != 0:
                t = (wall - direction.start.dx) / float(direction.dx)
                if t > 0:
                    if t < min_t:
                        min_t = t
                        reflectVals.dx = -1
                        reflectVals.dy = 1
                    elif t == min_t:
                        reflectVals.dx = -1

        for wall in walls[1]:
            if direction.dy != 0:
                t = (wall - direction.start.dy) / float(direction.dy)
                if t > 0:
                    if t < min_t:
                        min_t = t
                        reflectVals.dx = 1
                        reflectVals.dy = -1
                    elif t == min_t:
                        reflectVals.dy = -1

        collisionPoint = direction.start + direction * min_t
        newDirection = direction * reflectVals

        return Vector(newDirection.dx, newDirection.dy, collisionPoint)


def distanceBetween(vector1, vector2):
    return sqrt(
        (vector1.start.dx - vector2.start.dx) ** 2
        + (vector1.start.dy - vector2.start.dy) ** 2
    )


def tracePath(room, direction, distance):

    currDirection = direction

    while distance > 0:
        guardIsOn = room.guard.isOn(currDirection)
        youAreOn = room.you.isOn(currDirection)
        if guardIsOn and youAreOn:
            distanceToGuard = distanceBetween(currDirection, Vector(0, 0, room.guard))
            distanceToYou = distanceBetween(currDirection, Vector(0, 0, room.you))
            if distanceToGuard < distanceToYou and distanceToGuard < distance:
                # print(direction)
                return 1
            else:
                return 0

        if guardIsOn:
            distanceToGuard = distanceBetween(currDirection, Vector(0, 0, room.guard))
            if distanceToGuard < distance:
                # print(direction)
                return 1

        if youAreOn:
            return 0

        collisionPoint = room.findWallCollision(currDirection)
        distance -= distanceBetween(currDirection, collisionPoint)

        currDirection = collisionPoint

    return 0


def is_prime(n):
    if n == 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def solution(dimensions, your_position, guard_position, distance):
    room = Room(dimensions, your_position, guard_position)

    total = 0
    for i in range(-distance, distance + 1):
        for j in range(-distance, distance + 1):
            if abs(gcd(i, j)) == 1:
                total += tracePath(room, Vector(i, j, room.you), distance)

    return total


print(solution([3, 2], [1, 1], [2, 1], 4))
# print(solution([300, 275], [150, 150], [185, 100], 500))
