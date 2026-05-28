from shape_manager import ShapeManager, logger


def handle_create_shape(sm, shape_choice):
    shape_args = {}
    print("Choose the shape.")
    print("1) Square. \n2) Circle. \n3) Rectangle.")
    user_shape_choice = input("Enter a shape: \n")
    if user_shape_choice in shape_choice:
        shape_args[shape_choice[user_shape_choice]] = {}
        for arg in sm.SHAPE_CLS[shape_choice[user_shape_choice]]['arg']:
            logger.info("User trying to create shape.")
            try:
                arg_input = float(input(f'Enter the {arg}: '))
                if arg_input <= 0:
                    break
                shape_args[shape_choice[user_shape_choice]][arg] = arg_input
                sm.create_shape(shape_args)
            except ValueError:
                logger.error("User enter STR value not INT")
                print("You can enter only numbers.")
                break
        
    else:
        print("You can enter only number (1-3).")


def handle_update_shape(sm):
    logger.info("User trying to update shape.")
    try:
        update_id = int(input("Enter the ID you want to update: "))
        shape_args = sm.get_arg_by_id(update_id)
        if shape_args is not None:
            update_args = {}
            for arg in shape_args:
                new_arg = float(input(f"Enter new {arg}: "))
                if new_arg <= 0:
                    break
                update_args[arg] = new_arg
            sm.update_shape(update_id, update_args)
    except ValueError:
        logger.error("User enter STR value not INT")
        print("You can enter only numbers.")
    

def main():
    sm = ShapeManager()
    flag = True
    shape_choice = {'1' : 'square', '2' : 'circle', '3' : 'rectangle'}
    while flag:
        print("=== Shape Manager ===")
        print("1) Show all Shapes. \n2) Create new shape. \n3) Update Shape. \n4) Delete shape. \n5) Exit")
        user_choice = input("Enter an action: \n")
        match user_choice:
            case "1":
                sm.get_all_shapes()
            case "2":
                handle_create_shape(sm, shape_choice)
            case "3":
                handle_update_shape(sm)
            case "4":
                delete_id = input("Enter the ID you want to delete.")
                sm.delete_shape(delete_id)
            case "5":
                print("Goodbye!!")
                break

if __name__ == '__main__':
    main()