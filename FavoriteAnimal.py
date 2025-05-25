#1st input
animal_str = str(input("Whats your favorite animal? "))
#2nd input
if animal_str == "dog":
    #output 1
    dog_age = float(input("How old is your dog?"))
    if dog_age < 1:
        #output 2
        print("aww puppy")
    elif dog_age < 10:
        #output 3
        print("cute")
    else:
        #output 4
        print("wow, it's getting old")
else:
    print("Dogs 4 life")
  
