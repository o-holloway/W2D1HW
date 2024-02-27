#Take in a users input for their age
#if they are younger than 18 print kids
#if they're 18 to 65 print adults, else print seniors

def age_classifier():
    try:
        age = int(input("Enter Your Age in Years: "))
        if age < 18:
            print("kids")
        elif age < 66:
            print("adults")
        else:
            print("seniors")
    except:
        print("Enter your age in years as a positive integer!")

age_classifier()