class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member =False, gold_card_points =0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(f"First name: {self.first_name} \nLast name: {self.last_name} \nEmail: {self.email} \nAge: {self.age} \nIs he/she rewards member: {self.is_rewards_member} \nPoints of gold card: {self.gold_card_points}")
        return self

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        if self.is_rewards_member:
            print("User already a member")
            return False
        else:
            return True

    def spend_points(self, amount):
        if (self.gold_card_points - amount) >= 0:
            self.gold_card_points -= amount
            print(f"Your points = {self.gold_card_points}")
        else:
            print("You don't have enough points")
        return self


first_user = User("first", "user", "email@mail.com", 26, True, 400)
# first_user.display_info()
# first_user.enroll()
# first_user.spend_points(100)

second_user = User("second", "user","another_email@mail.com",15, 600)
third_user = User("third", "user", "third_email@mail.com", 40, True, 500)
first_user.spend_points(50).display_info()
second_user.display_info().spend_points(80).enroll()
# second_user.spend_points(80)
# first_user.display_info()
# second_user.display_info()
third_user.display_info().spend_points(40).display_info()
# third_user.spend_points(40)


