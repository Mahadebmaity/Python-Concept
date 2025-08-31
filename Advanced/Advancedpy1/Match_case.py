#  use match case  in advanced python 

day = input("Enter  week day name:")
match day:
    case "suterday" | "sunday":
        print("This day is Weekend day bro")
    case "monday" | "tuesday" | "wednesday" |"thursday" |"friday":
        print("this day  is working professional day bro")
    case _:
        print("Invalid day name.")


