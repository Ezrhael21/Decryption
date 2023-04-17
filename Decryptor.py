# Ezrhael R. Sicat
# BSCpE 1-5
# 04/17/2023
# Program 2 - Decryption

# Ask the user for input
user_text = input("Input your message to decrypt: ")
# Replace the character to its corresponding value
decrypted_string = user_text.replace("*", "a").replace("&", "e").replace("#", "i").replace("+", "o").replace("!", "u")
# Print Output
print (decrypted_string)



