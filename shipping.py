weight = 4.8
cost = 0
premium_cost = 125
#Ground Shipping
if weight <= 2:
    cost = 20 + 1.50 * weight
elif weight > 2 and weight <= 6:
    cost = 20 + 3.00 * weight
elif weight > 6 and weight <= 10:
    cost = 20 + 4.00 * weight
elif weight > 10:
    cost = 20 + 4.75 * weight
print(cost)
print("Premium shipping cost will be $" + str(premium_cost))


#Drone Shipping
if weight <= 2:
    cost = 4.50 * weight
elif weight > 2 and weight <= 6:
    cost = 9.00 * weight
elif weight > 6 and weight <= 10:
    cost = 12.00 * weight
elif weight > 10:
    cost = 14.25 * weight
print(cost)