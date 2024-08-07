def main():
    number = get_number()
    bark(number)
    
def get_number():
    while True:
        n = int(input("What's n?"))
        if n > 0:
            break
        return n
    
    
def bark(n):
    for _ in range(n):
        print("bark")
        
main()            