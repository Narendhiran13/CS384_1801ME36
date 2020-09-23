import math
# All decimal 3 places


#Functiont to check the Values are the float or int values
def CHECKINT(first_list):
    if length(first_list) == 0:
        print("ERROR: Please Enter some values in the String")
        return True
    
    for i in first_list:
        if isinstance(i, int) or isinstance(i, float):
            i = i
        else:
            print("One of the value is InValid Number")
            return True
        
    return False

#Function checks the same no of string elements
def EqualNoString(first_list, second_list):
    if(length(first_list) != length (second_list)):
        print("\t\tERROR: Unequal no of string elements")
        return True
    return False
    
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
        value /= 10
        
    value = int(value)
    value /= 1000
    
    return value
    
# Function to compute mean
def mean(first_list):
    # mean Logic
    if CHECKINT(first_list) is True:
        return 0
    
    summ = summation(first_list)
    n = length(first_list)

    mean_value = summ / n
    
    mean_value = roundUP(mean_value)
    return mean_value


# Function to compute median. You cant use Python functions
def median(first_list1):
    # median Logic
    first_list = first_list1[:]
    if CHECKINT(first_list) is True:
        return 0
    
    first_list = Sorting(first_list)
    if length(first_list) % 2 == 1:
        median_value = first_list[int(length(first_list) / 2)]
    else:
        median_value = 0.5 * (first_list[int(length(first_list) / 2) - 1] + first_list[int(length(first_list) / 2)])
    
    median_value = roundUP(median_value)
    
    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    if CHECKINT(first_list) is True:
        return 0
    
    summ = 0
    n = length(first_list)
    mean_value1 = mean(first_list)
    for i in first_list:
        summ+= ( (i-mean_value1) * (i-mean_value1) )
    summ /= n
    standard_deviation_value = math.sqrt(summ)
    standard_deviation_value = roundUP(standard_deviation_value)
    
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    if CHECKINT(first_list) is True:
        return 0
    
    summ = 0
    n = length(first_list)
    mean_value1 = mean(first_list)
    for i in first_list:
        summ+= ( (i-mean_value1) * (i-mean_value1) )
    variance_value = summ/ n 
    
    variance_value = roundUP(variance_value)
    
    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    if CHECKINT(first_list) is True or CHECKINT(second_list) is True or EqualNoString(first_list, second_list) is True:
        return 0
    
    summ = 0
    n = length(first_list)
    
    for i in range(length(first_list)):
        summ+= ( (first_list[i] - second_list[i]) * (first_list[i] - second_list[i]) )
    summ /= n
    rmse_value = math.sqrt(summ)
    rmse_value = roundUP(rmse_value)
    
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    if CHECKINT(first_list) is True or CHECKINT(second_list) is True or EqualNoString(first_list, second_list) is True:
        return 0
    
    mse_value = 0
    for i in range(length(first_list)):
        mse_value +=( (first_list[i] - second_list[i]) * (first_list[i] - second_list[i]) )
        
    n = length(first_list)
    mse_value /= n
    
    mse_value = roundUP(mse_value)
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    if CHECKINT(first_list) is True or CHECKINT(second_list) is True or EqualNoString(first_list, second_list) is True:
        return 0
     
    mae_value = 0
    for i in range(length(first_list)):
        if (first_list[i] - second_list[i]) >= 0:
            mae_value +=(first_list[i] - second_list[i])
        else:
            mae_value -=(first_list[i] - second_list[i])
    n = length(first_list)
    mae_value /= n
    
    mae_value = roundUP(mae_value)
    
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    if CHECKINT(first_list) is True or CHECKINT(second_list) is True or EqualNoString(first_list, second_list) is True:
        return 0
    mean_value = mean(first_list)
    
    nse_value1 = 0
    for i in range(length(first_list)):
        nse_value1 +=( (first_list[i] - second_list[i]) * (first_list[i] - second_list[i]) )
    nse_value2 = 0
    for i in range(length(first_list)):
        nse_value2 +=( (first_list[i] - mean_value) * (first_list[i] - mean_value) )
    
    nse_value = 1-(nse_value1/nse_value2)
    nse_value = roundUP(nse_value)
    
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    
    if CHECKINT(first_list) is True or CHECKINT(second_list) is True or EqualNoString(first_list, second_list) is True:
        return 0
    
    mean_valueX = mean(first_list)
    mean_valueY = mean(second_list)
    pcc_value1 = 0
    for i in range(length(first_list)):
        pcc_value1 +=( (first_list[i] - mean_valueX) * (second_list[i]-mean_valueY) )
    
    pcc_value2 = 0
    for i in range(length(first_list)):
        pcc_value2 +=( (first_list[i] - mean_valueX) * (first_list[i] - mean_valueX) )
    pcc_value2 = math.sqrt(pcc_value2)    

    pcc_value3 = 0
    for i in range(length(first_list)):
        pcc_value3 +=( (second_list[i]-mean_valueY) * (second_list[i]-mean_valueY) )
    pcc_value3 = math.sqrt(pcc_value3)
    
    pcc_value = pcc_value1/(pcc_value2*pcc_value3)
    pcc_value = roundUP(pcc_value)
    
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    if CHECKINT(first_list) is True:
        return 0
    
    summ = 0
    n = length(first_list)
    mean_value1 = mean(first_list)
    standard_deviation_value1 = standard_deviation(first_list)
    
    for i in first_list:
        summ+= ( ((i-mean_value1)/standard_deviation_value1) * ((i-mean_value1)/standard_deviation_value1) * ((i-mean_value1)/standard_deviation_value1) )
    skewness_value = summ/ n 
    
    skewness_value = roundUP(skewness_value)
    
    return skewness_value

#Function to sort out in Ascending Order
def Sorting(first_list):
    unsorted_list = first_list
    sorted_list = []
    while unsorted_list:
        minimum = unsorted_list[0]
        for item in unsorted_list:
            if item < minimum:
                minimum = item
        sorted_list.append(minimum)
        unsorted_list.remove(minimum)

    return sorted_list

# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    if CHECKINT(first_list) is True:
        return 0
    
    summ = 0
    n = length(first_list)
    mean_value1 = mean(first_list)
    standard_deviation_value1 = standard_deviation(first_list)
    
    for i in first_list:
        summ+= ( ((i-mean_value1)/standard_deviation_value1) * ((i-mean_value1)/standard_deviation_value1) * ((i-mean_value1)/standard_deviation_value1) * ((i-mean_value1)/standard_deviation_value1) )
    kurtosis_value = summ/ n 
    
    kurtosis_value = roundUP(kurtosis_value)
    
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    if CHECKINT(first_list) is True:
        return 0
    
    summation_value = 0
    for i in first_list:
        
        summation_value += i
       
    roundUP(summation_value)
    return summation_value