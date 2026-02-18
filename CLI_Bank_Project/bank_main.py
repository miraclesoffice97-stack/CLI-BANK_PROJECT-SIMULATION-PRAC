import random
import account_creation
#bank main 
class bank_main:
  def __init__(self):
    self.account = account_creation.account_details()
    self.computer_details = {"user id": 800, "balance": 234000}
    self.account_bal = 670000
    self.user_id = 0
    self.account.user_code = False
    
  def access(self): #account creation
    while True:
      self.bank_login = f'''{"-" * 40} \n Welcome to Cli Bank test \n {"-" * 40}
      \n 1. Create Account 
      \n 2 Return to menu'''
      print (self.bank_login)
      
      user_opt = input ("Enter an options: ")
      
      if user_opt == "1":
        self.account.user_name_requirements()
        self.account.password_checker()
        self.account.user_pin()
        self.user_id = random.randint(100, 1000)
        self.account.password_username_store["User id"] = self.user_id
        print (f"your uid is {self.user_id}")
        print (f"Available funds: +${self.account_bal:,}")
        print ("Account created successfully ☑️")
        break
      
      elif user_opt == "2":
        print ("Returning to main menu...")
        break
      
      else:
        print ("invalid selection")
        
        
        
  def home(self): # home or dashboard view..
    if self.account.user_code:
      self.enter_pin = input("Enter the 4 digit pin you created: ")
      if self.enter_pin == self.account.user_code:
        print (f"{'-' * 40} \nwelcome to CLI bank proj \n{'-' * 40}")
        
        print (f"Welcome {self.account.user_name}")
        print (f"User Id 👤:{self.user_id}")
        print (f"Balance \n{'*' * 30} \n${self.account_bal:,}")
        
        
      else:
        print ("invalid pin please try again!")
    else:
      print ("No active dashboard. \nCreate an account first!...")
    
   
  def send(self): #code to execute fund transfer to computer 800..
    while True:
      if self.account.password_username_store:
        try:
          recipient_id = int(input("Enter the recipient id: "))
          if recipient_id == self.computer_details["user id"]:
            print (self.computer_details)
            amount_send = int(input("Enter amount to transfer: "))
            
            
            if amount_send <= self.account_bal:
              self.enter_pin = input("Enter the 4 digit pin you created: ")
              
              if self.enter_pin == self.account.user_code:
                self.computer_details["balance"] += amount_send
                self.account_bal -= amount_send
                print(f"new balance: ${self.account_bal:,}")
                break
              
              else:
                pin = input("incorrect pin try again or x to quit: ")
                if pin == "x":
                  print("cancelled 🚫")
                  break
                
                else:
                  print("try again!")
                  
              
            else:
              print("insufficient funds!")
          
          else:
            opt = input("Invalid id! please try again or x to quit")
            if opt == "x":
              print("cancelled 🚫")
              break
            
           
        except ValueError:
          print ("please enter a number only!")
      else:
        print("User not found! create an account..")
        break
      
  def profile(self): #Profile view see account info..
    
    if self.account.password_username_store:
     enter_pin = input("Enter 4 digit pin: ")
      
     if enter_pin == self.account.user_code:
         print (f"User Profile \n{'*' * 30} \n${self.account_bal:,}")
         print (f"User ID: {self.user_id}")
         print(self.account.password_username_store)
        
     else:
       print("invalid pin")
         
    
    else:
      print("User not found! create an account..")

print(f"{'-' * 40} \nNew User! Welcome to dc bank \n{'-' * 40}")

bank_apt = bank_main()

while True:
  print("1. Create account \n2. View dashboard \n3. Transfer money \n4. View profile details \n5. computer view  \n6. exit app")
  
  selection = input("select from the menu: ")
  if selection == "1":
    bank_apt.access()
  
  elif selection == "2":
   bank_apt.home()
    
  elif selection == "3":
    bank_apt.send()
    
  elif selection == "4":
    bank_apt.profile()
    
  elif selection == "5": 
    print(f"Computer (ID 800) Status")
    print(f"Current Balance: ${bank_apt.computer_details['balance']:,}")
    
  elif selection == "6":
    print("Good bye 👻")
    break
  
  else:
    print("invalid selection!")