# Overlapping-Ellipses
This code estimates the area where two ellipses overlap by simulating random points within a specific area and checking how many of these points fall inside both ellipses. It leverages classes to represent points and ellipses in 2D space and uses a pseudo-random number generator for the simulation.
Calculating Min, Max, and Mean
Min and Max: These are the smallest and largest numbers generated in the 10,000 numbers.
Mean: This is the average of all 10,000 numbers, calculated by adding them all up and dividing by 10,000.


__init__ (within Point and Ellipse classes): These are constructor methods used to initialize new instances of the Point and Ellipse classes. For a Point, it stores x and y coordinates. For an Ellipse, it stores two focal points (f1, f2) and the width of the long axis, and calculates its area upon initialization.

compute_area (within Ellipse class): This method calculates the area of an ellipse. If the ellipse is actually a circle (both foci at the same point), it calculates the area using the formula for a circle's area. If it's an ellipse, it approximates the area using the major axis (width) and the distance between the foci to find the minor axis, then applies the standard area formula for ellipses.

is_inside_ellipse: This function determines whether a given point is inside a specific ellipse. It calculates the sum of the distances from the point to each of the ellipse's foci. If this sum is less than or equal to the ellipse's width (the major axis length), the point is considered inside the ellipse.

computeOverlapOfEllipses: This function estimates the overlap area between two ellipses using the Monte Carlo method. It randomly generates points within a predefined bounding box and counts how many of these points fall inside both ellipses. The ratio of points inside both ellipses to the total number of points generated, multiplied by the area of the bounding box, gives an estimate of the overlap area.
