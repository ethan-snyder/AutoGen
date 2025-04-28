import random
import string
import pyperclip

# Random letter
letter = random.choice(string.ascii_letters)  # picks a random letter (uppercase or lowercase)
symbol = random.choice(string.punctuation)    # picks a random punctuation symbol
number_char = random.choice(string.digits)    # picks a random digit ('0'-'9')
password = ''


# Main function iterates 20 times and chooses if the character is a num/symbol/digit. Then the proper charac
#ter type is chosen at random
for i in range(20):
    # Random num for choosing weather character will be letter/symbol/num
    num_char_chooser = random.choice('012')
    if(num_char_chooser == '0'):
        curr_char = random.choice(string.ascii_letters)  # picks a random letter (uppercase or lowercase)
    elif(num_char_chooser == '1'):
        curr_char = random.choice(string.punctuation)
    elif(num_char_chooser == '2'):
        curr_char = random.choice(string.digits)
    password += curr_char


pyperclip.copy(password) # Copies password to clipboard
