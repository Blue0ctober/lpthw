# setting a value for cars
cars = 100
# setting a value for space ina a car
space_in_a_car = 4.0
# setting a value for drivers
drivers = 30
#setting a value for passengers
passengers = 90
# using the above variables to do some math
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars avilable."
print "There are only", drivers, "drivers avilable."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
