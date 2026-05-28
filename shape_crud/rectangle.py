from shape import Shape

class Rectangle(Shape):
    """Represents a rectangle shape, inheriting from the base Shape class.

    Attributes:
        length (float): The length of the rectangle.
        hight (float): The height of the rectangle.
        shape_id (int): The unique identifier for the shape.
        shape_type (str): The type of the shape.
    """
    def __init__(self, shape_id, shape_type,length, hight):
        super().__init__(shape_id, shape_type)
        self.length = length
        self.hight = hight
    
    def get_area(self):
        """Calculates the area of the rectangle.

        Returns:
            str: The calculated area of the rectangle as a string.
        """
        return str(self.length * self.hight)

    def get_perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            str: The calculated perimeter of the rectangle as a string.
        """
        return str((self.length * 2) + (self.hight * 2))
        
    def to_dict(self):
        """Converts the rectangle's properties into a nested dictionary format.

        Returns:
            dict: A dictionary mapping the rectangle's string ID to its details 
                (type, length, hight, area, perimeter).
        """
        return {str(self.id) : {
            "type" : self.shape_type,
            "length" : self.length,
            "hight" : self.hight,
            "area" : self.get_area(),
            "perimeter" : self.get_perimeter()
        }}
