name, age = input("Enter your name and age:").split()

age = int(age)
DOB = 2026 - age

print (f"Hello {name}, how are you? So you are just {age} years old huh? Let me guess, you were born in {2026-age} right? or am I wrong?")

reply = input("Your reply: ").lower()

if reply == "yes" or reply == "yeah":
 print ("Haha see, my calculations are flawless.")
 
 
if reply == "no" or reply == "nah":
 print ("I dont really care anyway. So how are you then?")
  
 next_reply = int(input("Your reply: "))
 if next_reply < 2010:
      print ("Wow you are pretty old.")
 if next_reply > 2010:
            print ("Grow up kid.")                                     else: 
 print ("Ah, so you were born in 2010?")
                 