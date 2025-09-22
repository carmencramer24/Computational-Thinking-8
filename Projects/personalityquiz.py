cat_points = 0
dog_points = 0


answer = input("On a weekend would you rather A) nap all day, or B) go on a hike?")
if answer == "A" or answer == "a":
	cat_points += 1
elif answer == "B" or answer == "b":
	dog_points += 1


answer = input("Are you A) an extrovert, or B) an introvert?")
if answer == "A" or answer == "a":
	dog_points += 1
elif answer == "B" or answer == "b":
	cat_points += 1


answer = input("Would you rather eat lunch A) by yourself, or B) with a group?")
if answer == "A" or answer == "a":
	cat_points += 1
elif answer == "B" or answer == "b":
	dog_points += 1


answer = input("When you are at a pool would you rather A) swim in the water, or B) sun bathe?")
if answer == "A" or answer == "a":
	dog_points += 1
elif answer == "B" or answer == "b":
	cat_points += 1


answer = input("Do you like to eat a lot of food? yes or no?")
if answer == "yes" and  cat_points > dog_points:
	cat_points += 1
elif answer == "B" and dog_points > cat_points == "b":
	dog_points += 1
	

# end of quz
if cat_points > dog_points:
    print ("you are a cat person!")
if dog_points > cat_points:
    print("you are a dog person!")