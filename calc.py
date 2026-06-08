print("A calculator or something gng")
print("Just type exit if you wanna close the program")

while True:
    user_input = input("\nEnter your calculation man like eg: (9 + 10) or smth or just type exit: ")
    if user_input.lower() == "exit":
        print("Thanks for using dis")
        break
        
    try:
        n1, ope, n2 = user_input.split()
        a = float(n1)
        b = float(n2)
            
        if ope not in ["+", "-", "*", "/"]:
            print ("Choose something valid man fix your operator")
            continue
            
    except:
        print ("Try to add space, like a + b")
        continue
                
                
    if ope == "+":
        print (f"result: {a + b}")
    elif ope == "-":
        print (f"result: {a - b}")
    elif ope == "*":
        print (f"result: {a * b}")
    elif ope == "/":
        if b == 0:
            print ("Dude this aint possible try again")
        else:
                print (f"result: {a / b}")
                
    
    