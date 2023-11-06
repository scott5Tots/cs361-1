import os

def clear():
    os.system('cls')

# Display welcome message
def welcome():
    welcome = """
    Welcome to the Expense Tracker!
    This tool will allow you to track your weekly expenses and
    view various analyses so that you can better understand where
    your money goes and how to budget.
    """
    print(welcome)

# Display general tutorial information
def tutorial():
    tutorial_text = """
    Tutorial: This page will show you how to use the Expense Tracker and all its features.\n
    [Input Expenses]: This feature will allow you to create a new weekly expense, 
        choose which category it goes in, then input the dollar amount as well as a name for the expense.\n
    [Input Income]: This feature will allow you to input either your monthly or weekly income
        so that it can be used in the analysis to compare income amounts with expense amounts.\n
    [View Analyses]: This feature will alllow you to select from different options to view
        information about your weekly expenses, such as which categories account for the most money.
    """
    print(tutorial_text)
    val = input("\nPress [x] to go back: ")
    while val != "x":
        val = input("\nPress [x] to go back: ")
    main_menu()
        
# Check user input for main menu choice
def menu_choice():
    val = input("Enter choice: ")
    clear()
    if val == "1":
        tutorial()
    elif val == "2":
        expenses()
    elif val == "3":
        income()
    elif val == "4":
        analyses()
    elif val == "5":
        exit()
    else:
        print("That is not an option.\n")
        menu_choice()

# Display main menu
def main_menu():
    print("\n- MAIN MENU -\nPlease enter the number for which feature you would like to use:")
    choices = """
    [1] View Tutorial
    [2] Input Expenses
    [3] Input Income
    [4] View Anlyses
    [5] Exit
    """
    print(choices)
    menu_choice()

# Check user input for expense menu choice
def expense_choices():
    val = input("Enter choice: ")
    clear()
    if val == "1":
        temp = 1
    elif val == "2":
        temp = 1
    elif val == "3":
        temp = 1
    elif val == "4":
        temp = 1
    elif val == "5":
        temp = 1
    elif val == "6":
        temp = 1
    elif val == "7":
        temp = 1
    elif val == "x":
        main_menu()
    else:
        print("That is not an option.\n")
        expense_choices()

# Display expense categories menu
def expenses():
    print("\n- EXPENSE MENU -\nSelect a category for your expense:")
    choices = """
    [1] Housing
    [2] Transportation
    [3] Food
    [4] Utilities
    [5] Insurance 
    [6] Entertainment
    [7] Other
    [x] Go Back
    """
    print(choices)
    expense_choices()

# Check user input for income menu choice
def income_choices():
    val = input("Enter choice: ")
    clear()
    if val == "1":
        temp = 1
    elif val == "2":
        temp = 1
    elif val == "3":
        temp = 1
    elif val == "x":
        main_menu()
    else:
        print("That is not an option.\n")
        income_choices()

# Display input income menu
def income():
    print("\n- INCOME MENU -\nTo input income, select weekly, monthly, or yearly income:")
    choices = """
    [1] Weekly Income
    [2] Monthly Income
    [3] Yearly Income
    [x] Go Back
    """
    print(choices)
    income_choices()

def analyses_choices():
    val = input("Enter choice: ")
    clear()
    if val == "1":
        temp = 1
    elif val == "2":
        temp = 1
    elif val == "3":
        temp = 1
    elif val == "x":
        main_menu()
    else:
        print("That is not an option.\n")
        income_choices()

def analyses():
    print("\n- ANALYSES MENU -\nSelect an analysis view: ")
    choices = """
    [1] Expense Overview
    [2] Sort categories by expense amount
    [3] Show percent budget consumed per expense
    [x] Go Back
    """
    print(choices)
    analyses_choices()


def main():
    welcome()
    main_menu()

main()