# 1. Write a function that calculates and 
# returns the Body Mass Index (BMI) based
#  on height (in meters) and weight (in kilograms). 
#  The function should return the result rounded
#   to two decimal places. The formula for calculating 
#   BMI is weight divided by height squared.

def calculate_bmi(weight, meters):
    return weight / meters ** 2

x = calculate_bmi(70, 1.75)  # bmi should be approximately 22.86
x = calculate_bmi(85, 1.8)   # bmi should be approximately 26.23
