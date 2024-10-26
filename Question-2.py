# Using a while loop, write a function that continuously asks the user for input until they type the word "exit".
# The program should print each word entered by the user before asking for the next input.

def repeat_input():
    while True:
        user_input = input("Enter a word (type 'exit' to stop): ")
        if user_input.lower() == "exit":
            print("Exiting...")
            break
        print("You entered:", user_input)

repeat_input()
