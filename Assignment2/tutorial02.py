import numpy
# All decimal 3 places

#Function checks the same no of string elements
def EqualNoString(first_list, second_list):
    if(length(first_list) != length (second_list)):
        print("\t\tERROR: Unequal no of string elements")
        
# Function to Find the length of the String
def length(first_list):
    count = 0
    for i in first_list:
        count += 1
    return count

#Function which Round UP the Values to 3 digit decimals
def roundUP(value):
    value *= 10000
    if value % 10 >= 5:
        value /= 10
        value += 1
    else:
        value /=10
        
    value = int(value)
    value /= 1000
    
    return value
    
# Function to compute mean
def mean(first_list):
    # mean Logic

    summ = summation(first_list)
    n = length(first_list)

    mean_value = summ / n
    print(mean_value)
    
    mean_value = roundUP(mean_value)
    return mean_value


# Function to compute median. You cant use Python functions
def median(first_list):
    # median Logic
    
    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    EqualNoString(first_list, second_list)
    
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    EqualNoString(first_list,second_list)
    mse_value = 0
    for i in range(first_list):
        mse_value +=( (first_list[i] - second_list[i]) * (first_list[i] - second_list[i]) )
        
    n = length(first_list)
    mse_value /= n
        
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    EqualNoString(first_list, second_list)
    
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    EqualNoString(first_list, second_list)
    
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    EqualNoString(first_list, second_list)
    
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    return skewness_value


def sorting(first_list):
    # Sorting Logic
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic

    summation_value = 0
    for i in first_list:

        if isinstance(i, int) or isinstance(i, numpy.float64):
            summation_value += i
        else:
            print("One of the value is InValid Number")
            return 0

    return summation_value
