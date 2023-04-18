# Ezrhael R. Sicat
# BSCpE 1-5
# 04/17/2023
# Program 2 - Decryption

import pyfiglet

print ("=" * 100)
font = pyfiglet.figlet_format("Code Decryption", font = "big" )
print ("=" * 100)

# Introduction to the program
print ("=" * 100)
Name=input("Enter your username: ")
print ("=" * 100)
print ("Hello!", Name,)
print ("Today, we are going to decrypt a code")

moredata = True
while moredata:

    # Ask the user for input
    print ("=" * 100)
    user_text = input("Input your message to decrypt: ")

    # Time Delay
    print ("=" * 100)
    print ("Processing...")
    import time
    time.sleep(5)
    
    # Replace the character to its corresponding value
    decrypted_string = user_text.replace("*", "a").replace("&", "e").replace("#", "i").replace("+", "o").replace("!", "u")
    
    # Print Output
    print ("=" * 100)
    print ("Original Message : ", user_text)
    print ("Decrypted Message: ", decrypted_string)
    print ("=" * 100)

    while True:
        repeat = input("Do you want to try again? (Yes/No): ")
        if repeat.lower() == "yes":
            break
        elif repeat.lower() == "no":
            moredata = False
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

print ("=" * 100)
print ("Thank you for using this program.")
print ("=" * 100)
    
    



