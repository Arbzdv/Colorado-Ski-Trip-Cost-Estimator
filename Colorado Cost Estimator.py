#ski trip cost estimator

#get cost of general things
while True:
    try:
        trip_cost = float(input('How much did your lift ticket cost? :  '))
        break
    except ValueError:
        print('Enter ONLY a number and try again...')
while True:
    try:
        ski_cost = float(input('How much do your rentals cost? :  '))
        break
    except ValueError:
        print('If you already have skis or a snowboard, enter 0, enter a number and try again...')
while True:
    try:
        food_cost = float(input('How much money do you want to spend on food? : '))
        break
    except ValueError:
        print('You will be hungry food is needed, enter a number and try again...')
while True:
    try:
        Air_B = float(input('How much does your air bnb cost? : '))
        break
    except ValueError:
        print('Only enter the Number no need for dollar signs')

#calculate general cost of things for later
general_cost = trip_cost + ski_cost + food_cost + Air_B 

#get information to calculate amount of gas needed
while True:
    try:
        total_distance = float(input('How many miles is it to Colorado : '))
        break
    except ValueError:
        print('Enter ONLY a number and try again...')
while True:
    try:
        car_gas_mileage = float(input('What is the gas mileage of your car? : '))
        break
    except ValueError:
        print('Enter ONLY a number and try again...')
while True:
    try:
       average_gas_price = float(input('What is the average cost of gas from missouri to colorado? : '))
       break
    except ValueError:
        print('Enter ONLY a number and try again...')
while True:
    try:
       number_passengers = float(input('How many people are driving with you to colorado? : '))
       break
    except ValueError:
        print('enter ONLY a number and try again...')

#calculate how many gallons of gas are needed
gallons_needed = total_distance / car_gas_mileage 

#calculate cost of gas to colorado

full_gas_cost= gallons_needed * average_gas_price

gas_price= full_gas_cost / number_passengers * 2 

#calculate everything up

final_cost= general_cost + gas_price

#print final cost

print("The cost of the trip will be", final_cost)

            

    
    

                                  
