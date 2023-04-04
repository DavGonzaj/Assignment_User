class User:
      
        def __init__(self, first_name, last_name, email, age):
          self.first_name = first_name
          self.last_name = last_name
          self.email = email
          self.age = age
          self.is_rewards_member = False
          self.gold_card_points = 0
          
        def display_info(self):
          print("==========================")
          print(f"First name: {self.first_name}")
          print(f"Last name: {self.last_name}")
          print(f"Email: {self.email}")
          print(f"Age: {self.age}")
          print(f"Member: {self.is_rewards_member}")
          print(f"Current Points: {self.gold_card_points}")
          print("==========================")
            
        def enroll(self):
            self.is_rewards_member = True
            self.gold_card_points = 200
            if(self.enroll == True):
              print("user already a member")
              return False
            else:
              return True

        def spend_points(self, amount):
            self.gold_card_points = self.gold_card_points - amount 
        
        
First_User = User('David','Gonzalez','nyrojaen@gmail.com',23)
First_User.display_info()
First_User.enroll()
First_User.display_info()
First_User.spend_points(100)
First_User.display_info()

