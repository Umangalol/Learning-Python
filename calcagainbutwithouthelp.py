print("---Calculator man---")
print("Type exit to close the program at any time.")

while True:
    user_input = input("Enter your calculation, eg (9 + 10): ")
    if user_input.lower() == "exit":
            print ("Goodbye gng.")
            break
            
            
    try:
       n1, ope, n2 = user_input.split()
       a = float(n1)
       b = float(n2)
       
       if ope not in ["+", "-", "*", "/"]:
        print ("Choose smth valid like + or -")
        continue
        
    except:
        print ("Try to add spaces in between.")
        continue
        
        
    if ope == "+":
        print(f"result: {a + b}")
    elif ope == "-":
        print(f"result: {a - b}")
    elif ope == "*":
        print(f"result: {a *  b}")
    elif ope == "/":
        if b == 0:
            print("Dis shi impossible twin, try again")
        else:
            print(f"result: {a / b}")