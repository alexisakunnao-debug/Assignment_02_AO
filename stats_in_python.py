import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    # Complete the function so it loads the data from the file into a list
    # The function returns a tuple that contains the list of values and the total number 
    # of values in the column
   
    numbers = []
    total_values = 0

    #checking column number 
    if column <0:
        print("The column must be 0 or greater.")
        sys.exit() 

    #reading the file a line at a time
    with open(filepath, "r") as infile:
        for line in infile:
            total_values += 1 

            #getting the value from the selected column
            try:
                value = line.split("\t")[column]

            except IndexError:
                print(f"There is no valid 'list index' in column {column} in line {total_values} in file: {filepath}")
                sys.exit()

            #adding valid numbers ot the list 
            try:
                if value.strip() != "NaN":
                    number = float(value)
                    numbers.append(number)

            except ValueError:
                pass 

        #checking if valid numbers were found 
        if len(numbers) == 0:
            print(f"There were no valid numbers in column {column} in file: {filepath}.")
            sys.exit()

        return numbers, total_values

def calculate_average(numbers:list)->float:
    # Complete the function to return the average of the list of numbers

    #adding the numbers together
    total = 0

    for number in numbers:
        total += number 

    #calculating average 
    average = total / len(numbers)

    return average 

def get_max_and_min(numbers:list)->tuple[float, float]:
    #Complete the function to return a tuple with the maximum and minimum
    # values in the list, in that order
    
    #starting with the first number 
    max = numbers[0]
    min = numbers[0]

    #checking each number
    for number in numbers:
        if number > max:
            max = number 

        if number < min:
            min = number 

    return max, min

def calculate_variance(numbers:list)->float:
    #Complete the function to return the variance of the numbers in the list
    
    if len(numbers) > 1:
        mean = calculate_average(numbers)
        sq_deviation_sum = 0

        #adding squared deviations 
        for number in numbers:
            deviation = number - mean
            sq_deviation = deviation ** 2
            sq_deviation_sum += sq_deviation

        #calculating sample variance
        variance = sq_deviation_sum / (len(numbers) - 1)

    else:
        return 0.0

    return variance

def calculate_std_dev(numbers:list)->float:
    #Complete the function to return the standard deviation of the numbers in the list
    
    #getting variance 
    variance = calculate_variance(numbers)

    #calculating standard deviation
    std_dev = math.sqrt(variance)

    return std_dev

def calculate_median(number:list)->float:
    # Complete the function to return the median of the numbers in the list
    
    #sorting the numbers in ascending order
    ordered_numbers = sorted(number)

    #counting length of list + finding middle number
    count = len(ordered_numbers)
    middle_num = count // 2

    #if count is odd, middle_num = median
    if count % 2 == 1: 
        median = float(ordered_numbers[middle_num])

    #if even, median is the average of the 2 middle numbers
    else:
        median = (ordered_numbers[middle_num] + ordered_numbers[middle_num - 1]) / 2 

    return median 