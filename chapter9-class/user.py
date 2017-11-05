class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("The user's full name is: " + self.first_name.title() + " " + self.last_name.title())
    
    def greet_user(self):
        print("Welcome, " + self.first_name.title() + " " + self.last_name.title())

user1 = User('jiao', 'qiyuan')
user2 = User('liu', 'cuicui')
user3 = User('jiao', 'xuhan')
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
