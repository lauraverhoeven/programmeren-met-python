# main program file

# load CBS data set
print("To do: Load the CBS data set.")

# create a loop for the entire program, which runs until option 5 is selected.
while True:
    choice = input("""What do you want to analyse?    
    1\tHow has the total avoided use of fossil energy due to wind energy changed over the period 2010-2018?\nWhat part of this avoided use of fossil energy can be assigned to wind power on land and wind power at sea?
    2\tHow much has the CO2 emission in the Netherlands changed in the period 1990 to 2018 and which renewable energy source has relatively reduced CO2 emission the most?    
    3\tWhat is the difference in usage of wood in a household regarding a freestanding wooden stove and a freestanding pallet stove?    
    4\tWhich energy source was the most efficient in 2018 in terms of producing energy with the highest prevention of CO2 emission?    
    5\tExit the program.
    """)    

# evaluate user choice and proceed accordingly
    if choice == "1":
        wind_power = input("Which kind of wind power do you want to analyse? ('at sea' or 'on land') ")
        period_rq1 = input("Which period do you want to analyse? (2010-2018) ")
        print("To do: create bar graph using the right kind of wind power and period.")
    elif choice == "2":
        energy_source = input("Which kind of energy source do you want to analyse? ")
        period_rq2 = input("Which period do you want to analyse? (1990-2018) ")
        print("To do: create line chart using the right kind of period and energy source.")
    elif choice == "3":
        stove = input("Which kind of stove do you want to analyse? ('wooden' or 'pallet') ")
        period_rq3 = input("Which period do you want to analyse? ")
        print("To do: create bar graph using the right kind of stove and period.")
    elif choice == "4":
        energy = input("Which kind of energy source do you want to analyse? ")
        print("To do: create bar plot using the right kind of energy source.")
    elif choice == "5":
        print("Thank you for your participation. Bye!")
        break
    else: 
        print("Choice was not recognized, or invalid input. Please try again")
        