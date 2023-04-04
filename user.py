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
          if (self.is_rewards_member):
            print("user already a member")
            return False
          self.is_rewards_member = True
          self.gold_card_points = 200

        def spend_points(self, amount):
          if self.gold_card_points < amount:
            "You don't have enough points"
            return
          
          
          self.gold_card_points -= amount 
          
        
        
first_user = User('David','Gonzalez','nyrojaen@gmail.com',23)
first_user.display_info().enroll().spend_points(100).display_info()

second_user = User('Lionel','Messi','email@gmail.com',28)
second_user.display_info().enroll().spend_points(400).display_info()

third_user = User('Cristiano','Ronaldo','Randomemail@gmail.com',38)
third_user.display_info().enroll().spend_points(20).display_info()