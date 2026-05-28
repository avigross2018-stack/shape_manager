import json
import logging
from square import Square
from circle import Circle
from rectangle import Rectangle

def get_logger():
    """Configures and returns a logger instance for the application.

    Sets up basic logging configurations with INFO level, logs to 'logger.log',
    and defines the timestamp and message format.

    Returns:
        logging.Logger: The configured logger instance for the module.
    """
    logging.basicConfig(level=logging.INFO,
                        filename='logger.log',
                        format='%(asctime)s | %(levelname)s | %(message)s')
    logger = logging.getLogger(__name__)
    return logger

logger = get_logger()

JSON_FILENAME = 'shapes.json'

class ShapeManager:
    """Manages the creation, retrieval, updating, deletion, and persistence of shapes.

    Attributes:
        SHAPE_CLS (dict): A registry mapping shape names to their classes and required arguments.
        shapes (list): A list intended to store shape instances.
        data (dict): A dictionary containing raw shape records loaded from a JSON file.
    """

    SHAPE_CLS = {'circle' : {
                    'cls' : Circle,
                    'arg' : ['radius']                    
                },
                'square' : {
                    'cls' : Square,
                    'arg' : ['side']                   
                },
                'rectangle' : {
                    'cls' : Rectangle,
                    'arg' : ['length', 'hight']                   
                }
                }

    def __init__(self):
        self.shapes = []
        self.data = self.load_from_json()
    
    def create_shape(self, shape):
        """Creates a new shape instance, appends it to the internal data, and saves to JSON.

        Args:
            shape (dict): A dictionary containing the shape name as a key and its 
                        parameters as a nested dictionary value.
        """
        shape_name = next(iter(shape))
        shape_arg = shape[shape_name]
        the_shape = self.SHAPE_CLS[shape_name]['cls'](self.get_id(), shape_name, **shape_arg)
        the_shape_data = the_shape.to_dict()
        self.data = self.data | the_shape_data
        self.save_to_json()
        logger.info(f"Created new {shape_name} shape.")
        print(f"Shape {shape_name} been added.")

    def get_all_shapes(self):
        """Prints all the shapes currently stored in the manager to the console.

        Iterates through the records in the data dictionary and outputs formatted 
        details of each shape. Logs an appropriate message if no data exists.
        """
        if self.data:
            logger.info("Show all shapes.")
            for k,v in self.data.items():
                print("============")
                print(f'ID - {k}\n------')
                for kk, vv in v.items():                
                    print(f'{kk} - {vv}')
        else:
            logger.info("There is no shapes in the file.")
            print("There is no shapes in the file.")

    def update_shape(self, shape_id, new_data):
        """Updates the parameters of an existing shape by its ID and saves the changes.

        Removes the old record, instantiates a new shape object with updated arguments,
        merges it back into the data dictionary, and persists the data.

        Args:
            shape_id (int): The identifier of the shape to update.
            new_data (dict): A dictionary containing the updated arguments for the shape.
        """
        shape_name = self.data[str(shape_id)]['type']
        shape_args = new_data
        del self.data[str(shape_id)]
        the_shape = self.SHAPE_CLS[shape_name]['cls'](shape_id - 1, shape_name, **shape_args)
        the_shape_data = the_shape.to_dict()
        self.data = self.data | the_shape_data
        self.save_to_json()
        logger.info(f"Update {shape_name} shape.")
        print(f"Shape {shape_name} been updated.")


    def delete_shape(self, shape_id):
        """Deletes a shape from the data dictionary by its ID and updates the JSON file.

        Args:
            shape_id (str): The identifier of the shape to be deleted.
        """
        logger.info("Try to delete shape by ID.")
        try:
            shape_id_int = int(shape_id)
            if str(shape_id_int) in self.data:
                del self.data[str(shape_id_int)]
                self.save_to_json()
                print("The shape was deleted.")
                logger.info("Deleted shape by ID.")
            else:
                logger.info("User enter ID that does not exist.")
                print("There is no shape with that ID.")
        except ValueError:
            logger.error("User try to input str ID.")
            print("You can enter only number.")

    def save_to_json(self):
        """Serializes and saves the current state of the shape data dictionary to a JSON file."""
        try:
            logger.info("Try loading JSON file to write.")
            with open(JSON_FILENAME, 'w') as f:
                json.dump(self.data, f)
            logger.info("dump to JSON successfully")
        except Exception as e:
            logger.error(f"JSON file not found ({e})")
            print(f"Json file not found ({e})")

    def load_from_json(self):
        """Loads shape data from the designated JSON file.

        Returns:
            dict: The loaded data from the JSON file, or an empty dictionary 
                if an exception or file access error occurs.
        """
        try:
            logger.info("Try loading JSON file to read.")
            with open(JSON_FILENAME, 'r') as f:
                data = json.load(f)
            logger.info("JSON load successfully")
        except Exception as e:
            logger.error(f"JSON file not found ({e})")
            print(f"Json file not found ({e})")
            data = {}
        return data
    
    def get_id(self):
        """Determines the next available shape ID based on the maximum existing ID key.

        Returns:
            int: The highest current integer ID found in the database, or 0 if no data exists.
        """
        if self.data:
            return int(max(self.data, key=int))
        return 0
    
    def get_arg_by_id(self, id):
        """Retrieves the expected parameter argument names for a shape type based on its ID.

        Args:
            id (int): The unique identifier of the shape.

        Returns:
            list: A list of string argument names required by the specific shape class,
                or None if the ID does not exist in the data.
        """
        if str(id) in self.data:
            return self.SHAPE_CLS[self.data[str(id)]['type']]['arg']
        else:
            print("There is no ID with this number.")