class Restaurant():
    def __init__(self, restaurant_name, cuisin_type):
        self.restaurant_name = restaurant_name
        self.cuisin_type = cuisin_type

    def describe_restaurant(self):
        print("The restaurant's name is: " + self.restaurant_name)
        print("The restaurant's cuisin type is: " + self.cuisin_type)
    
    def open_restaurant(self):
        print("The restaurant is open.")

restaurant = Restaurant('qilixiang', 'zhongcan')
restaurant1 = Restaurant('chouguiyu', 'huicai')
restaurant2 = Restaurant('dayu', 'tiebanshao')
print(restaurant.restaurant_name)
print(restaurant.cuisin_type)
restaurant.describe_restaurant()
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant.open_restaurant()
