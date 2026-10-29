bank_dict = {
    "Priya": {"balance": 100, "pin": "4821"},
    "Carlos": {"balance": 300, "pin": "1092"},
    "Amira": {"balance": 0, "pin": "0000"},
    "Jordan": {"balance": 7788, "pin": "9999"},
}


'''
Name: print_welcome
Task: Prints the welcome message to the terminal
Input: None
Side Effects (printing/display): the welcome message
Return: None
'''
def print_welcome():
    print("====Welcome to Berklee Bank====")
'''
Name: get_username
Task: Prompt the user for their name
Input: None
Side Effects (printing/display): Prompt "What is your name?"
Return: return the username
'''
def print_welcome():
    print("What is your name?")
    name = input()
'''
Name: get_pin
Task: Prompt the user for their pin
Input: None
Side Effects (printing/display): Prompt "What is your pin"
Return: return the pin
'''
def print_welcome():
    print("What is your pin")
    return print
'''
Name: verify_identity
Task: Take the name and pin and see if there's a valid user in the system. If so, get their data. IF not, fail.
Input: username, pin
Side Effects (printing/display): If they don't exist, it says "Access Denied"
Return: True if user exists, False if not
'''
def verify_identity(username, pin):
    if bank_dict.get(username):
        user_values = bank_dict.get(username)
        if pin == user_values.get("pin"):
            return True
    print("Access Denied for", username, "with pin", pin)
    return False
'''
Name: get_menu_choice
Task: Print the functionality of the bank (the commands they can do) to the terminal, and ask what they want
Input: None
Side Effects (printing/display):  do you wanna deposit, withdraw, get balance, quit (they type their answer)
Return: the string the user typed in
'''
def get_menu_choice():
    choice = ("Do you want to...deposit withdaw balance quit")
    return choice

'''
Name: get_balance
Task:  gets the balance and prints it
Input: username
Side Effects (printing/display):  the balance
Return: None
'''
def get_balance(username):
    if bank_dict.get(username):
        user_values = bank_dict.get(username)
        balance = users_values.get("balance")
        print("Your balance is", balance)

'''
Name: deposit_money
Task: Ask the user how much they want to deposit then add that to the balance
Input: username
Side Effects (printing/display): prompting the user for the amount to deposit
Return: None
'''
def deposit_money(usename):
    deposit_amount = int(input("How much would you like to deposit?"))
    if bank_dict.get(username):
        user_values = bank_dict.get(username)
        previous_bal = users_values.get("balance")
        new_bal = previous_bal + deposit_amount
        user_values.update({"balance": new_bal})

    return None

'''
Name: withdraw_money
Task:  Ask the user how much they want to withdraw. If they have enough, reduce balance. If not, tell them.
Input: username
Side Effects (printing/display): Asking the user the amount, telling them if successful
Return: None
'''
def withdraw_money(usename):
    withdraw_amout = int(input("How much would you like to withdraw?"))
    if bank_dict.get(username):
        users_values = bank_dict.get(username)
        previous_bal = user_values.get("balance")
        new_bal = previous_bal - withdraw_amout
        if new_bal < 0:
            print("Insufficient funds...")
        else:
            users_values.update({"balance":new_bal})

def run_tests():
    #withdraw_money("Priya") #Asks for amount, if 200 fail
    #withdraw_money("Priya") #Asks for amount, if 100 should succeed

    #deposit_money("priya")#Asks for amout, if 100 should succed
    #get_balance("Priya")#print $100

    #verify_identity("Priya","8421")#Expecting succesful login
    #verify_identity("Priya","0000")#Expecting fail login

    #print_welcome()#Expecting 
    #get_pin()#Expecting
    #get_username()#Expecting

def main():
    print_welcome()
    name = get_username()
    pin = get_pin()
    valid = verify_identity(name,pin)
    if not valid:
        return

    while True:
        user_choice = get_menu_choice()
        if user_choice == "balance":
            get_balance(name)
        elif user_choice == "withdraw":
            withdraw_money(name)
        elif user_choice == "deposit":
            deposit_money(name)
        elif user_choice == "quit":
            break
        else:
            print("You can not be that...")