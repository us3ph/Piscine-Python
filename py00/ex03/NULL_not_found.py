def NULL_not_found(object: any) -> int:
    match object:
        case None:
            rslt = type(object)
            print("Nothing: ", object, rslt)
        case float():
            rslt = type(object)
            print("Cheese: ", object, rslt)
        case False:
            rslt = type(object)
            print("Fake: ", object, rslt)
        case 0:
            rslt = type(object)
            print("Zero: ", object, rslt)
        case "":
            rslt = type(object)
            print("Empty: ", object, rslt)
        case _:
            print("Type not found")
    return 1