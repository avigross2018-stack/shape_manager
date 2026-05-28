from shape import Shape

class Circle(Shape):
    """Represents a circle shape, inheriting from the base Shape class.

    Attributes:
        pi (float): The value of pi used for geometric calculations.
        radius (float): The radius of the circle.
        shape_id (int): The unique identifier for the shape.
        shape_type (str): The type of the shape.
    """
    def __init__(self, shape_id, shape_type, radius):
        super().__init__(shape_id, shape_type)
        self.pi = 3.14
        self.radius = radius
    
    def get_area(self):
        """Calculates the area of the circle.

        Returns:
            str: The calculated area of the circle as a string.
        """
        return str(self.pi * self.radius ** 2)
    
    def get_perimeter(self):
        """Calculates the perimeter (circumference) of the circle.

        Returns:
            str: The calculated perimeter of the circle as a string.
        """
        return str(2 * self.pi * self.radius)
    
    def to_dict(self):
        """Converts the circle's properties into a nested dictionary format.

        Returns:
            dict: A dictionary mapping the circle's string ID to its details 
                (type, radius, area, perimeter).
        """
        return {str(self.id) : {
            "type" : self.shape_type,
            "radius" : self.radius,
            "area" : self.get_area(),
            "perimeter" : self.get_perimeter()
        }}
    
