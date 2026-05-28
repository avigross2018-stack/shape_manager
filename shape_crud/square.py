from shape import Shape

class Square(Shape):
    """Represents a square shape, inheriting from the base Shape class.

    Attributes:
        side (float): The length of a side of the square.
        shape_id (int): The unique identifier for the shape.
        shape_type (str): The type of the shape.
    """
    def __init__(self, shape_id, shape_type, side):
        super().__init__(shape_id, shape_type)
        self.side = side

    def get_area(self):
        """Calculates the area of the square.

        Returns:
            str: The calculated area of the square as a string.
        """       
        return str(self.side ** 2)
    
    def get_perimeter(self):
        """Calculates the perimeter of the square.

        Returns:
            str: The calculated perimeter of the square as a string.
        """
        return str(self.side * 4)
    
    def to_dict(self):
        """Converts the square's properties into a nested dictionary format.

        Returns:
            dict: A dictionary mapping the square's string ID to its details 
                (type, side, area, perimeter).
        """
        return {str(self.id) : {
            "type" : self.shape_type,
            "side" : self.side,
            "area" : self.get_area(),
            "perimeter" : self.get_perimeter()
        }}
   
