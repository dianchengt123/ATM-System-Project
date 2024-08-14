from os import system
from time import sleep

"""method used for clearing the 
console to avoid cluttering."""
def clear():
  sleep(3)
  system("clear")

"""Atm class"""
class Atm:

  """constructor; sets pin and balance to 
  default values and calls on the menu method."""
  def __init__(self):
    self.__pin = None
    self.__balance = 0
    self.__menu()

  """displays the actions the user can take and 
  calls on other methods within the class 
  depending on the user's input."""
  def __menu(self):
    while True:
      print("""Menu:\n
1. Generate Pin
2. Change Pin
3. Check Balance
4. Withdraw Money
5. Deposit Money
6. Exit""")
      ans = input("> ")
      system("clear")
      if ans == "6":
        exit()
      elif ans == "1":
        self.__generate_pin()
      elif ans == "2":
        self.__change_pin()
      elif ans == "3":
        self.__check_balance()
      elif ans == "4":
        self.__withdraw()
      elif ans == "5":
        self.__deposit()
      else:
        continue

  """asks the user to input a pin and checks if 
  it's a valid input. returns the inputted pin."""
  def __get_pin(self):
    userPin = ""
    while True:
      userPin = input("Enter a 4-digit pin: ")
      # checks if the pin is 4 digits
      if len(userPin) != 4:
        print("Your pin must be 4 digits")
        clear()
        continue
      try:
        # checks if the pin only contains numbers
        int(userPin)
      except:
        print("Your pin cannot contain any characters")
        clear()
        continue
      return userPin

  """asks the user to confirm their pin.
  returns the inputted pin."""
  def __verify_pin(self):
    confirmPin = input("Confirm your pin: ")
    return confirmPin

  """calls on the __get_pin and __verify_pin methods.
  if both methods return the same value, the pin 
  will be set to that value. if not, the user will 
  be asked to try again."""
  def __generate_pin(self):
    # checks if pin is already set
    if self.__pin is not None:
      print("Your pin is already set")
      clear()
    else:
      while True:
        userPin = self.__get_pin()
        confirmPin = self.__verify_pin()
        if userPin != confirmPin:
          print("Your pins don't match")
          clear()
        else:
          self.__pin = userPin
          print("Pin created")
          clear()
          break

  """allows the user to change their pin. asks 
  them to enter their old pin. if the old pin 
  is correct, they can create a new pin following 
  the same constraints and instructions as before."""
  def __change_pin(self):
    # pin has to be set first
    if self.__pin is None:
      print("You must set a pin before changing it")
      clear()
    else:
      oldUserInputPin = input("Enter your old pin: ")
      if oldUserInputPin == self.__pin:
        system("clear")
        while True:
          newUserInputPin = input("Enter a new pin: ")
          # these lines of code are similar to the __get_pin, __verify_pin, and __generate_pin methods
          # but I had to rewrite them because I want to print different things 
          if len(newUserInputPin) != 4:
            print("Your pin must be 4 digits")
            clear()
            continue
          try:
            int(newUserInputPin)
          except:
            print("Your pin cannot contain any characters")
            clear()
            continue
          confirmUserInputPin = input("Confirm your new pin: ")
          if newUserInputPin == confirmUserInputPin:
            self.__pin = newUserInputPin
            print("Your pin has been changed")
            clear()
            break
          else:
            print("Your new pins don't match")
            clear()
      else:
        print("Incorrect pin")
        clear()

  """allows the user to check their balance 
  after confirming they have the right pin"""
  def __check_balance(self):
    # pin has to be set first
    if self.__pin is None:
      print("You must set a pin before checking your balance")
      clear()
    else:
      userInputPin = input("Enter your pin: ")
      if userInputPin == self.__pin:
        while True:
          system("clear")
          print(f"Your balance is ${self.__balance} dollars.")
          goBack = input("\nReturn to main menu?(y/n): ").strip().lower()
          if goBack == "y":
            system("clear")
            break
      else:
        print("Incorrect pin")
        clear()

  """allows the user to withdraw money from 
  their balance based on certain constraints"""
  def __withdraw(self):
    #1 pin has to be set first
    if self.__pin is None:
      print("You must set a pin before withdrawing money")
      clear()
    else:
      userInputPin = input("Enter your pin: ")
      #2 pin must be correct
      if userInputPin == self.__pin:
        while True:
          system("clear")
          amt = input("Enter the amount you would like to withdraw: ")
          try:
            #3 amount must be an interger value greater than 0, less than the balance, and divisible by 100
            amt = int(amt)
            if amt > self.__balance or amt < 0 or amt % 100 != 0:
              print("Invalid amount")
              clear()
            else:
              # subtracts the amt from the balance
              self.__balance -= amt
              print(f"\n💵 Here is ${amt} dollars")
              print(f"Your new balance is ${self.__balance}")
              clear()
              break
          except:
            print("Invalid input")
            clear()
      else:
        print("Incorrect pin")
        clear()

  """allows the user to deposit money into 
  their balance based on certain constraints"""
  def __deposit(self):
    #1 pin has to be set first
    if self.__pin is None:
      print("You must set a pin before depositing money")
      clear()
    else:
      #2 pin must be correct
      userInputPin = input("Enter your pin: ")
      if userInputPin == self.__pin:
        while True:
          system("clear")
          amt = input("Enter the amount you would like to deposit: ")
          try:
            #3 amount must be an interger value greater than 0 and divisible by 100
            amt = int(amt)
            if amt < 0 or amt % 100 != 0:
              print("Invalid amount")
              clear()
            else:
              # add the amount to their balance
              self.__balance += amt
              print(f"\n💵 ${amt} dollars have been added to your balance")
              print(f"Your new balance is ${self.__balance}")
              clear()
              break
          except:
            print("Invalid input")
            clear()
      else:
        print("Incorrect pin")
        clear()
