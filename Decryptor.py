# Ezrhael R. Sicat
# BSCpE 1-5
# 04/17/2023
# Program 2 - Decryption

# Introduction to the program
Name=input("Enter your username: ")
print ("Hello!", Name,)
print ("Today, we are going to decrypt a code")

moredata = True
while moredata:

    # Ask the user for input
    user_text = input("Input your message to decrypt: ")
    
    # Replace the character to its corresponding value
    decrypted_string = user_text.replace("*", "a").replace("&", "e").replace("#", "i").replace("+", "o").replace("!", "u")
    
    # Print Output
    print ("Original Message : ", user_text)
    print ("Decrypted Message: ", decrypted_string)

    while True:
        repeat = input("Do you want to try again? (Yes/No): ")
        if repeat.lower() == "yes":
            break
        elif repeat.lower() == "no":
            moredata = False
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

print ("Thank you for using this program.")
    
    



