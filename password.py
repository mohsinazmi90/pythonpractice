# The Gatekeeper: Ask the user how long they want their password to be. 
# Use a loop to ensure they actually enter a valid number (e.g., between 8 and 32 characters). 
# If they type "apple" or "4", tell them it's invalid and ask again.

# The Choices: Ask them if they want to include numbers (y/n) 
# and if they want to include special characters/symbols (y/n).

# The Generation: Generate the password randomly using their choices and 
# print it.

# The Evaluation: Print out whether the password is 
# "Weak", "Medium", or "Strong".

import random
import string

def generator():
    
    size_of_pass = None
    
    while size_of_pass is None:
        try:
            try_for_pass_size = int(input("Enter length of password between 8 to 32: "))
            if 8 <= try_for_pass_size <= 32:
                size_of_pass = try_for_pass_size
                break
            else:
                print("Size needs to be between 8 and 32")
        except:
            print("Please enter INT only between 8 to 32")

    the_password = "".join(random.choice(string.ascii_letters) for _ in range(size_of_pass))
    new_pass = does_it_have_password(the_password)
    new_pass = does_it_have_chars(new_pass)
    new_pass = "".join(random.sample(new_pass, len(new_pass)))

    evaluate_password(new_pass)
    
    return new_pass

    
def does_it_have_password(password):
    
    while True:
        try:
            want = str(input("Does password have numbers? "))
            want = want.lower()

            if want == "yes":
                new_pass = password + str(random.randint(0, 100))
                return new_pass
            elif want == "no":
                new_pass = password
                return new_pass
            else:
                print("You need to say Yes or No")
        except:
            print("Please say Yes or No")
    
    
def does_it_have_chars(password):
    
    while True:
        try:
            want = str(input("Does password have special chars? "))
            want = want.lower()
            
            if want == "yes":
                new_pass = password + str(random.choice(string.punctuation))
                return new_pass
            elif want == "no":
                new_pass = password
                return new_pass
            else:
                print("You need to say Yes or No")
        except:
            print("Please say Yes or No")

def evaluate_password(password):
    
    if len(password) < 10:
        print("Your password is weak")
    elif 10 <= len(password) < 20:
        print("Your password is medium")
    else:
        print("Your password is strong")

def main():
    print(generator())
    
    
    
if __name__ == "__main__":
    main()    
    