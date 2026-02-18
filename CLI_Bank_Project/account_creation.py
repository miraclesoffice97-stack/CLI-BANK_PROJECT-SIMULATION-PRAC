#username and password mechanisms
class account_details:
  def __init__(self):
    
    self.user_name = ""
    self.password_username_store = {}
  
  def user_name_requirements(self):
    while True:
      requirements = f'''{"-" * 30} \nusername requirements \n{"-" * 30}
    \nInclude an Uppercase leter 
    \nDo not include any special characters'''
      print (requirements)
      self.user_name = input("Enter a user name: ")
      username_requirements = [any(char.isupper() for char in self.user_name), all(char.isalnum() for char in self.user_name ), all(not char.isdigit() for char in self.user_name)]
      
      if all(username_requirements):
        print("✓")
        break
      else:
        print ("! please follow the username requirements")
       
  
  def password_checker(self):
    while True:
      requirements_pas = f'''{"-" * 30} \nPassword requirements \n{"-" * 30}
      \nMust be 8 letters or more
      \nInclude an Uppercase leter 
      \ninclude at least one special character any special characters'''
      print (requirements_pas)
      
      self.user_password = input("Enter a password: ")
      
      pass_requirements = [len(self.user_password) >= 8, 
      any(char.isupper() for char in self.user_password),
      any(not char.isalnum() for char in self.user_password)]
      
      if all(pass_requirements):
        print ("successfully created an account!")
        self.password_username_store["user name"] = self.user_name
        self.password_username_store["password"] = self.user_password
        break
      else:
        opt = input("try again or enter x to exit to menu: ")
        if opt == "x":
          print ("Returning to menu...")
          break
        else:
          print (f"{'•' * 40} \nRetry \n{'•' * 40}")
      
  def user_pin(self):
    while True:
      self.user_code = input("Create a 4 digit pin: ")
      option = [len(self.user_code) == 4, all(char.isdigit() for char in self.user_code)]
     
      
      if all(option):
        self.password_username_store["User pin"] = self.user_code
        print("successfully created user pin")
        print (self.user_code)
        break
        
      else:
        print ("retry")
        