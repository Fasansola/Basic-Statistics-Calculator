
# PROJECT 1
# BASIC STATISTICS CALCULATOR
# GOAL: A Functional Mean, Variance, and Standard Deviation Calculator


# Our calculator will take a list of numbers and find the:
# mean, median, mode, variance and standard deviation of the list of numbers


import math


def statistics_calculator(numbers):

    # Default Variables
    num_count = len(numbers)
    sum_of_squared_diff = 0

    # Mean Calculator
    mean = sum(numbers)/len(numbers)

    # Mode Calculator
    mode = max(numbers)

    # Median Calculator
    index = num_count // 2
    if num_count % 2 == 0:
        median = (numbers[index] + numbers[index - 1]) / 2
    else:
        median = numbers[index]

    # Variance Calculator = ∑(x - mean)^2 / N
    for number in numbers:
        mean_diff = (number - mean)**2
        sum_of_squared_diff += mean_diff
    variance = sum_of_squared_diff / num_count

    # SD = √Variance
    standard_deviation = math.sqrt(variance)

    print(f"""\nThe Mean is {mean} \n
The Median is {median} \n
The Mode is {mode} \n
The Variance is {variance} \n
The Standard deviation is {standard_deviation}\n""")

    return mean, median, mode, variance, standard_deviation


# INPUT YOUR NUMBERS HERE:
numbers = [0, 1, 1, 2, 3, 5, 8, 3, 2, 4, 6]


# PRINT ALL STATISTICS OUT

mean, median, mode, variance, standard_deviation = statistics_calculator(
    numbers)


# UNCOMMENT TO PRINT INDIVIDUALLY

print(mean)
# print(median)
# print(mode)
# print(variance)
# print(standard_deviation)
