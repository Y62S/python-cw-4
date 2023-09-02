def my_name():
    print("my name is yousef.")
my_name()

def my_meal(food , drink):
    print(f"I like to eat {food} and while drinking {drink}")
my_meal("burger" , "cola")

def cube(number):
    return number **3

def by_three(number):
    if number % 3 == 0:
      cube(number) 
    else:
        print("false")
print(cube(4))
by_three(2)

