"""
Author: Parisa Arbab
Date: Feb 27 2024
Statement:“I have not given or received any unauthorized assistance on this assignment.”
YouTube Link:https://youtu.be/xUdABok2SX8

answered this question in the above link:
 Briefly show your code working on a simple case.  (e.g. two circles at the origin)
 Briefly show your code working on a more complicated example you came up with.
 Show the main loop of your algorithm.

"""
from warandpeace import WarAndPeacePseudoRandomNumberGenerator
import random


class Point:
    """
        Represents a point in 2D space with x and y coordinates.
        """
    def __init__(self, x, y):
        """
                Initializes a Point object.

                Args:
                    x (float): The x-coordinate of the point.
                    y (float): The y-coordinate of the point.
                """
        self.x = x
        self.y = y

class Ellipse:
    """
        Represents an ellipse defined by two foci and the width of its major axis.
        """
    def __init__(self, p1, p2, width):
        """
                Initializes an Ellipse object.

                Args:
                    p1 (Point): The first focal point of the ellipse.
                    p2 (Point): The second focal point of the ellipse.
                    width (float): The total distance across the longest part of the ellipse.
                """
        self.f1 = p1
        self.f2 = p2
        self.width = width
        self.area = self.compute_area ()

    def compute_area(self) :
        """
                Calculates the area of the ellipse.

                Returns:
                    float: The area of the ellipse.
                """
        # Approximation of ellipse area; correct for circles where foci coincide.
        distance = ((self.f1.x - self.f2.x) ** 2 + (self.f1.y - self.f2.y) ** 2) ** 0.5
        if distance == 0 :  # Circle case
            radius = self.width / 2
            return 3.14159 * radius * radius
        else :
            # Ellipse area calculation for non-circle case (simplified approximation)
            major_axis = self.width
            minor_axis = (major_axis ** 2 - distance ** 2) ** 0.5
            return 3.14159 * (major_axis / 2) * (minor_axis / 2)

def is_inside_ellipse(point, ellipse):
    """
        Determines if a point is inside an ellipse.

        Args:
            point (Point): The point to check.
            ellipse (Ellipse): The ellipse to check against.

        Returns:
            bool: True if the point is inside the ellipse, False otherwise.
        """
    d1 = ((point.x - ellipse.f1.x) ** 2 + (point.y - ellipse.f1.y) ** 2) ** 0.5
    d2 = ((point.x - ellipse.f2.x) ** 2 + (point.y - ellipse.f2.y) ** 2) ** 0.5
    return (d1 + d2) <= ellipse.width

def computeOverlapOfEllipses(e1, e2, trials =10000):
    """
       Estimates the area of overlap between two ellipses using a Monte Carlo method.

       Args:
           e1 (Ellipse): The first ellipse.
           e2 (Ellipse): The second ellipse.
           trials (int): The number of random points to generate for the estimation.

       Returns:
           tuple: A tuple containing the number of points within the overlap and the estimated area of the overlap.
       """
    #answer to question 2: two ellipses with different centers and axis length.
    prng = WarAndPeacePseudoRandomNumberGenerator ()
    overlap_count = 0
    # Main loop using the pseudo-random number generator
    # Define bounding box for the simulation
    # For simplicity, let's assume it's large enough to contain both ellipses fully
    # You may need to adjust this based on your specific ellipses
    min_x, max_x = -10, 10
    min_y, max_y = -10, 10
#answer to question 3:Main loop
    for _ in range ( trials ) :#generates random points
        x = min_x + (max_x - min_x) * random.random ()
        y = min_y + (max_y - min_y) * random.random ()
        point = Point ( x, y )
        #check if the random points are inside both ellipses to estimate the overlap area
        if is_inside_ellipse ( point, e1 ) and is_inside_ellipse ( point, e2 ) :
            overlap_count += 1

    total_area = (max_x - min_x) * (max_y - min_y)
    overlap_area = total_area * (overlap_count / trials)
    return overlap_count, overlap_area


# Example 1
p1 = Point(0, 0)
p2 = Point(0, 0)
e1 = Ellipse(p1, p2, 2)  # Circle with radius 1
e2 = Ellipse(p1, p2, 4)  # Circle with radius 2

overlap_count, overlap_area = computeOverlapOfEllipses(e1, e2)

print(f"Ellipse(Point(0,0), Point(0,0),2) has area {e1.area:.4f}.")
print(f"Ellipse(Point(0,0),Point(0,0),4) has area {e2.area:.4f}.")
print(f"{overlap_count} out of 10000 generated points are in both ellipses.")
print(f"The overlap of the two has area {overlap_area:.4f}.")

# Reusing the classes and function definitions from earlier

# Example 2
p1_e2 = Point(0, 0)  # Center for the first ellipse
p2_e2 = Point(0, 0)  # Same center for the first ellipse, making it a circle

# For the second ellipse, foci are (-1, 0) and (1, 0), making it slightly elongated
f1_e2 = Point(-1, 0)
f2_e2 = Point(1, 0)

e3 = Ellipse(p1_e2, p2_e2, 4)  # Circle with radius 2
e4 = Ellipse(f1_e2, f2_e2, 4)  # Ellipse with foci at (-1,0) and (1,0)

overlap_count_e2, overlap_area_e2 = computeOverlapOfEllipses(e3, e4)

# Printing the results for Example 2
print("******************************************************")
print(f"Ellipse(Point(0,0), Point(0,0),4) has area {e3.compute_area():.4f}.")
print(f"Ellipse(Point(-1,0),Point(1,0),4) has area {e4.compute_area():.4f}.")
print(f"{overlap_count_e2} out of 10000 generated points are in both ellipses.")
print(f"The overlap of the two has area {overlap_area_e2:.4f}.")
