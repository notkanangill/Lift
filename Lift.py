import random

#The code below is to ensure that the values remain same over different executions.
random.seed(0)

#Iintialising lift and weight variables:
lifts = [random.randint(-2,51), random.randint(-2,51), random.randint(-2,51)]
weights = [random.randint(25,600), random.randint(25,600), random.randint(25,600)]
button = int(input())
random_lift = random.randint(0,2)
lift_sent = 0
diff = [abs(lifts[0]-button), abs(lifts[1]-button), abs(lifts[2]-button)]

#Comparing the variables and conditions
if diff[0]>diff[1] and weights[1]<550:
    lifts[1] = button
    weights[1] = random.randint(25,120)
    lift_sent = "number 2"
    print("Lift 2 is coming for the people waiting. Please wait for sometime.")
elif diff[1]>diff[2] and weights[2]<550:
    lifts[2] = button
    weights[2] = random.randint(25,120)
    lift_sent = "number 3"
    print("Lift 3 is coming for the people waiting. Please wait for sometime.")
elif diff[1]>diff[0] and weights[0]<550:
    lifts[0] = button
    weights[0] = random.randint(25,120)
    lift_sent = "number 1"
    print("Lift 1 is coming for the people waiting. Please wait for sometime.")

#The else statement here helps to choose a lift in-case any two lifts are in the same situation, like, having same floor and/or and weights
else:
    lifts[random_lift] = button
    weights[random_lift] = random.randint(25,120)
    lift_sent = "number "+random_lift
    print("Lift",random.randint(1,2), "is coming for the people waiting. Please wait for sometime")

#Printing output in terminal
print()
print("------Below are some useful data------")
print("Lifts' current floor: ",lifts)
print("Lifts' current weight: ", weights)
print("Your current floor: ", button)
print("Random lift number: ", random_lift)
print("closest lift: ", diff)
print("The lift sent:", lift_sent)
