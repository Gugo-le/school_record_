name = input("What's your name")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")                
    
    
    
match name:
    case "Harry":
        print("Gryffindor")    
    
    case _:
        print("Who?")    