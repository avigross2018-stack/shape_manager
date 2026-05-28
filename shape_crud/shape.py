class Shape:
    """Base class representing a generic geometric shape.

    Attributes:
        shape_id (int): The unique identifier for the shape.
        shape_type (str): The type or designation of the shape.
    """
    def __init__(self, shape_id:int, shape_type:str):
 
        self.id = shape_id
        self.shape_type = shape_type
        self.id += 1
    def get_area(self):
        """Calculates and returns the area of the shape.

        Returns:
            str: The area of the shape as a string.
        """       
        pass

    def get_perimeter(self):
        """Calculates and returns the perimeter of the shape.

        Returns:
            str: The perimeter of the shape as a string.
        """
        pass

    def to_dict(self):
        """Converts the shape's attributes into a dictionary representation.

        Returns:
                dict: A dictionary containing the shape data indexed by its.
        """
        pass

