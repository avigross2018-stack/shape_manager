from shape_manager import ShapeManager, get_logger

logger = get_logger(__name__)

def handle_create_shape(sm):
    shape_choice = {'1' : 'square', '2' : 'circle', '3' : 'rectangle'}
    shape_args = {}
    print("Choose the shape.")
    print("1) Square. \n2) Circle. \n3) Rectangle.")
    user_shape_choice = input("Enter a shape: \n")

    if user_shape_choice in shape_choice:   # check if user enter correct input.
        shape_type = shape_choice[user_shape_choice]   # hold the name of the shape.
        shape_args[shape_type] = {}  # update the shape name as a key DICT.

        for arg in sm.SHAPE_CLS[shape_type]['arg']:   # iter in amount of args for shape.
            logger.info("User trying to create shape.")
            try:
                arg_input = float(input(f'Enter the {arg}: '))
                if arg_input <= 0:
                    print("You can enter only positive numbers.")
                    break
                shape_args[shape_type][arg] = arg_input   # update arg key with INT value.                
            except ValueError:
                logger.error("User enter STR value not INT")
                print("You can enter only numbers.")
                break
        else:
            sm.create_shape(shape_args)   # creating the shape.
       
    else:
        logger.error("user enter invalid input in the shape menu.")
        print("You can enter only number (1-3).")


def handle_update_shape(sm):
    logger.info("User trying to update shape.")
    
    try:
        update_id = int(input("Enter the ID you want to update: "))
        shape_args = sm.get_arg_by_id(update_id)   # getting LIST of args for shape.
        if shape_args is not None:   # check if LIST non empty.
            update_args = {}    # hold name of arg as key and amount of arg as value.
            for arg in shape_args:   # iter in amount of args for shape.
                new_arg = float(input(f"Enter new {arg}: "))
                if new_arg <= 0:
                    print("You can enter only positive numbers.")
                    break
                update_args[arg] = new_arg   # update arg key with INT value.
            sm.update_shape(update_id, update_args)   # update the shape.
    except ValueError:
        logger.error("User enter STR value not INT")
        print("You can enter only numbers.")
    

def main():
    sm = ShapeManager()
    flag = True
    
    while flag:
        print("=== Shape Manager ===")
        print("1) Show all Shapes. \n2) Create new shape. \n3) Update Shape. \n4) Delete shape. \n5) Exit")
        user_choice = input("Enter an action: \n")
        match user_choice:
            case "1":
                sm.get_all_shapes()
            case "2":
                handle_create_shape(sm)
            case "3":
                handle_update_shape(sm)
            case "4":
                delete_id = input("Enter the ID you want to delete: ")
                sm.delete_shape(delete_id)
            case "5":
                logger.info('user exit the program.')
                print("Goodbye!!")
                break
            case _:
                logger.error("user enter invalid input in the main menu.")
                print('Invalid input (1-5)')

if __name__ == '__main__':
    main()