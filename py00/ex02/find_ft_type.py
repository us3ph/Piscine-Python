def all_thing_is_obj(object: any) -> int:
    # (object: any) mean that the function can accept any type of object as an argument.
    # isinstance() function is used to check if the object is of a specific type or not. , but type() function is used to get the type of the object.
    #type(object) function is used to get the type of the object.
    match object:
        case list():
            rslt = type(object)
            print("List :", rslt)
        case tuple():
            rslt = type(object)
            print("Tuple :", rslt)
        case set():
            rslt = type(object)
            print("Set :", rslt)
        case dict():
            rslt = type(object)
            print("Dict :", rslt)
        case str():
            rslt = type(object)
            print(object, "is in the kitchen :", rslt)
        case _:
          print("Type not found")
    return 42