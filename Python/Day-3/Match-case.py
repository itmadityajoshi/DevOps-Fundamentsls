status = 404

match status:
    case 200:
        print("success!")
    case 404:
        print("Not found")
    case _:
        print("Unknown Status")