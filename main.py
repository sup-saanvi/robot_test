"""
This is a game where there is a robot delivery team that
delivers certain things.
"""

# make a main function that will store the following options for delivery
# and those are Downtown, Suberbs, and Industrials 

def main():
    """This is where I will add functions """
    delivery = delivery_rout()
    print("n/Welcome to", delivery)

    print("\n1- downtown")
    print("2- Suberbs ")
    print("3- Industial")

    choice = input ("Choose a location to send your robot")

    if choice == "1":
        downtown()

    elif choice == "2":
        suberbs()

    elif choice == "3":
        Industial()

    else:
        print("Invalid choice")

if__delivery__ == "__main__":
main()

    








# get the total delivery distance that is inbetween 5-500 km

# get the weight of the cargo that each robot is carring that's in between 1and 50 kg

# get the weather conditions to see if its clear, rain, or storm 

# check if weight is over 50 kg or if the distance is more than 300 km or if the weather 
# is storm if it is then print deploment unsafe !

# If it is safe then put down a summary of the weather, zone, and weight print 
# robots ready for delivery!
