from math import atan2

# Vector class for extra readability
class Vector:
    def __init__(self, dx, dy, start):
        self.dx = dx
        self.dy = dy
        self.start = start

    # Component-wise vector multiplication
    def __mul__(self, other):
        dx = self.dx * other.dx
        dy = self.dy * other.dy

        return Vector(dx, dy, self.start or other.start)

    # The Squared length of the vector (to avoid expensive sqrt calculations)
    def __len__(self):
        return (self.dx - self.start.dx) ** 2 + (self.dy - self.start.dy) ** 2

    # Angle of vector shifted to the starting position
    def angle(self):
        y = self.dy - self.start.dy
        x = self.dx - self.start.dx
        return atan2(y, x)


# Room class to normalize parameters
class Room:

    # Redefines parameters as vectors for more readible calculations
    def __init__(self, dimensions, you, guard):
        self.dimensions = Vector(dimensions[0], dimensions[1], None)
        self.you = Vector(you[0], you[1], None)
        self.guard = Vector(guard[0], guard[1], None)

    # Finds all reflected projections of given person in the first quadrant
    def buildFirstQuadrant(self, distance, person):
        firstQuadrant = []
        squaredDistance = distance ** 2

        x = person.dx
        while x - self.you.dx <= distance:
            y = person.dy
            while y - self.you.dy <= distance:
                projectedVector = Vector(x, y, self.you)
                if len(projectedVector) > squaredDistance:
                    break

                firstQuadrant.append(projectedVector)

                if y % self.dimensions.dy == person.dy % self.dimensions.dy:
                    y += 2 * (self.dimensions.dy - person.dy)
                else:
                    y += 2 * person.dy

            if x % self.dimensions.dx == person.dx % self.dimensions.dx:
                x += 2 * (self.dimensions.dx - person.dx)
            else:
                x += 2 * person.dx

        return firstQuadrant

    # Builds mapping from an angle to the closest projected person to you
    # Gets all valid vectors from the first quadrant and reflects them
    # along the x and y axis to get the other quadrants
    def buildVectorMap(self, distance, person):
        firstQuadrant = self.buildFirstQuadrant(distance, person)
        vectorMap = {}
        squaredDistance = distance ** 2
        reflectionVectors = [
            Vector(1, 1, None),
            Vector(-1, 1, None),
            Vector(-1, -1, None),
            Vector(1, -1, None),
        ]

        for projectedVector in firstQuadrant:
            for reflection in reflectionVectors:
                reflectedVector = reflection * projectedVector

                if len(reflectedVector) <= squaredDistance:
                    reflectedAngle = reflectedVector.angle()
                    if reflectedAngle not in vectorMap:
                        vectorMap[reflectedAngle] = reflectedVector
                    elif len(reflectedVector) < len(vectorMap[reflectedAngle]):
                        vectorMap[reflectedAngle] = reflectedVector

        return vectorMap


# Instead of thinking of a vector reflecting off a wall and changing direction,
# we'll think of the vector keeping the same direction and entering a reflected world.
# If we project all these reflected worlds onto the x,y axis, we can calculate the locations
# of all the reflected guards and reflected you's. We then point a vector from the original you
# to all the reflected guards and if the vector never runs into a reflected you, then it is
# a valid path.
def solution(dimensions, your_position, guard_position, distance):
    room = Room(dimensions, your_position, guard_position)
    guardMap = room.buildVectorMap(distance, room.guard)
    youMap = room.buildVectorMap(distance, room.you)
    youMap.pop(0)  # Remove the original you

    total = 0
    for angle, guard in guardMap.items():
        if angle not in youMap:
            total += 1
        else:
            if len(guard) < len(youMap[angle]):
                total += 1

    return total


print(type(1))
