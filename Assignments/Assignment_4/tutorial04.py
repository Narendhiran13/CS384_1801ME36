import os
import csv
import shutil

import pandas as pd


# Reading the CSV file
path = "acad_res_stud_grades.csv"
data = pd.read_csv(path)

# print(data.columns)
shutil.rmtree('grades')
os.mkdir('grades')


def mapping_GATE_and_SCORE(grade):
    if grade == 'AA':
        return 10
    if grade == 'AB':
        return 9
    if grade == 'BB':
        return 8
    if grade == 'BC':
        return 7
    if grade == 'CC':
        return 6
    if grade == 'CD':
        return 5
    if grade == 'DD':
        return 4
    else:
        return 0


roll_numbers = list()

# Extract the data from the file and Alocate the data in a different format
with open('acad_res_stud_grades.csv', 'r') as data_file:
    data_reader = csv.reader(data_file)
    # print(data_reader)
    for data_row in data_reader:
        path = 'grades/'+str(data_row[1])+"_individual.csv"
        if(os.path.isfile(path) == False):
            roll_numbers.append(data_row[1])
            with open(path, 'a') as file2:
                writer = csv.writer(file2)
                writer.writerow(['Roll', 'semester', 'Year', 'sub_code', 'total_credits',
                                 'credit_obtained', 'sub_type'])
        with open(path, 'a') as file2:
            writer = csv.writer(file2)
            writer.writerow(
                [data_row[1], data_row[2], data_row[3], data_row[4], data_row[5], data_row[6], data_row[8]])

roll_numbers.remove('roll')

for _3_digit in roll_numbers:

    TOTAL_credit_uptodate, helper = [
        0 for i in range(2)]  # Variable

    Semester_data, Semester_Credits, Semester_Credits_Cleared, SPI, Total_Credits, Total_Credits_Cleared, _CPI_ = [
        list() for i in range(7)]

    path = 'grades/' + str(_3_digit) + "_individual.csv"
    # CREATE an csv file and the read the csv file
    data_file = pd.read_csv(path)

    # total semsetr completed
    total_semester = data_file['semester'].unique().max()

    CPI = 0  # initial constant CPI value
    print('Semester-Wise score for roll no: ', _3_digit,
          '& Total semester are', total_semester)

    for sem in range(1, total_semester+1):

        Semester_data.append(sem)
        semesterwise = data_file[(data_file['semester'] == sem)]

        credit_array = list(
            semesterwise['credit_obtained'].apply(mapping_GATE_and_SCORE))

        totalcred = list(semesterwise['total_credits'])

        x_dummy_value = 0

        for y in range(0, len(credit_array)):
            x_dummy_value += credit_array[y]*totalcred[y]

        # ADD all the data into the LIST files
        helper = helper+x_dummy_value
        TOTAL_credit_uptodate = TOTAL_credit_uptodate + \
            semesterwise['total_credits'].sum()
        Semester_Credits.append(semesterwise['total_credits'].sum())
        Semester_Credits_Cleared.append(semesterwise['total_credits'].sum())
        SPI.append(round(x_dummy_value/semesterwise['total_credits'].sum(), 2))
        Total_Credits.append(TOTAL_credit_uptodate)
        Total_Credits_Cleared.append(TOTAL_credit_uptodate)
        _CPI_.append(round(helper/TOTAL_credit_uptodate, 2))

    # Saving the data In a dictionary format
    dict = {'Semester': Semester_data, 'Semester Credits': Semester_Credits, 'Semester_Credits_Cleared': Semester_Credits_Cleared, 'SPI': SPI,
            'Total Credits': Total_Credits, 'Total Credits Cleared': Total_Credits_Cleared, 'CPI': _CPI_}

    df = pd.DataFrame(dict)
    filename = "grades/"+str(_3_digit)+"_overall.csv"
    # UPLOADING THE DATA by A DATAFRAME
    df.to_csv(filename)
    print(roll_numbers)
    print('done')
