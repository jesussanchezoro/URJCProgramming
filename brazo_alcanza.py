import math

def getExactSolution(x0, y0, x1, y1, r0, r1):
    """
    Return the exact solution for two segments of size r0,r1 from (x0,y0) to (x1,y1)
    """
    D = math.sqrt((x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0))
    a = (r0 * r0 - r1 * r1 + D * D) / (2 * D)
    h = math.sqrt(r0 * r0 - a * a)
    x = x0 + (x1 - x0) * a / D + (y0 - y1) * h / D
    y = y0 + (y1 - y0) * a / D + (x1 - x0) * h / D
    return [(round(x,2), round(y,2)),(round(x1,2),round(y1,2))]


def distance(startPoint, endPoint):
    return math.sqrt((startPoint[0] - endPoint[0]) * (startPoint[0] - endPoint[0]) + (startPoint[1] - endPoint[1]) * (
        startPoint[1] - endPoint[1]))

def posibleSolutionTo(startPoint, endPoint, segmentList):
    """
    Return true if it is possible to get endPoint from startpoint using this segmentList
    """
    distanceBetweenPoints = distance(startPoint, endPoint)
    return (distanceBetweenPoints <= sum(segmentList)) and (distanceBetweenPoints >= minElongation(segmentList))

def recursiveGetPosition(startPoint, endPoint, segmentList):
    """
    Uses dinamic programig to choose a point in the circle that fix the first segment in such way that the solution is posible.
    Then call the method with the rest of the arm.
    """
    if len(segmentList) == 2:
        return getExactSolution(startPoint[0], startPoint[1], endPoint[0], endPoint[1], segmentList[0], segmentList[1])

    angle = 0
    while True:
        newPoint = (startPoint[0] + math.cos(angle) * segmentList[0], startPoint[1] + math.sin(angle) * segmentList[0])
        if posibleSolutionTo(newPoint, endPoint, segmentList[1:]):
            return [round(newPoint[0],2),round(newPoint[1],2)] + recursiveGetPosition(newPoint, endPoint, segmentList[1:])
        angle += 1

def maxElongation(x, y, segmentList):
    """
    Return the max elongation of the segments looking for (x,y)
    """
    D = math.sqrt(x * x + y * y)
    sx, sy = 0, 0
    output = []

    for s in segmentList:
        dx = x * s / D
        dy = y * s / D
        sx += dx
        sy += dy
        output.append((round(sx,2), round(sy,2)))

    output.append((round(x,2), round(y,2)))    
    return output


def minElongation(segmentList):
    """
    If the max section is bigger than the sum of the other sections, you can't reach the start point with the arm
    """
    maxSection = max(segmentList)
    restOfSections = sum(segmentList) - maxSection
    if maxSection > restOfSections:
        return maxSection - restOfSections
    else:
        return 0


def getPosition(point, segmentList):
    """
    Main method
    """    
    if distance((0, 0), point) >= sum(segmentList):
        return maxElongation(point[0], point[1], segmentList)
    min_elongation = minElongation(segmentList)
    if distance((0, 0), point) < min_elongation:
        factor = min_elongation / distance((0, 0), point)
        point = [e * factor for e in point]

    return recursiveGetPosition((0, 0), point, segmentList)


print(getPosition((3,2),[5,4,2]))
print(getPosition((20,20),[5,4,2]))
print(getPosition((1,0),[3,1]))