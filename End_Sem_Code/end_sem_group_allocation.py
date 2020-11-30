import re
import csv
import os
import pandas as pd
import shutil

from queue import Queue

average_group_members, average_cs_branch, average_ee_branch, average_mm_branch, average_me_branch, average_cb_branch, average_ce_branch = [
    0 for i in range(7)]
total_students, mm_branch_strength, cs_branch_strength, ee_branch_strength, me_branch_strength, cb_branch_strength, ce_branch_strength = [
    0 for i in range(7)]
mm_roll, mm_name, mm_email, me_roll, me_name, me_email, ee_roll, ee_name, ee_email, cb_roll, cb_name, cb_email, ce_roll, ce_name, ce_email, cs_roll, cs_name, cs_email = ([
] for i in range(18))

path = './data_file/'


def create_or_delete_folder():
    if os.path.exists("./data_file") == False:
        os.mkdir("./data_file")
    else:
        shutil.rmtree('./data_file')
        os.mkdir('./data_file')


def padding_convert_intostring(value):
    string_value = str(value)
    if len(string_value) == 2:
        return string_value
    else:
        return '0'+string_value


def branch(roll_no):
    return_val = ""
    for ij in roll_no:
        if ij.isdigit() == False:
            return_val += ij
    return return_val


def get_number(string):
    dummy_var = string.split('_')
    z = dummy_var[1].split('.')
    return_value = z[0][1:]
    return return_value


def strength_function(Branch, Single_stud_data):
    global mm_branch_strength, cs_branch_strength, ee_branch_strength, me_branch_strength, cb_branch_strength, ce_branch_strength
    global mm_roll, mm_name, mm_email, me_roll, me_name, me_email, ee_roll, ee_name, ee_email, cb_roll, cb_name, cb_email, ce_roll, ce_name, ce_email, cs_roll, cs_name, cs_email

    Roll_No = Single_stud_data.get("Roll")
    Name = Single_stud_data.get("Name")
    Email = Single_stud_data.get("Email")

    if Branch == "mm":
        mm_branch_strength += 1
        mm_roll.append(Roll_No)
        mm_name.append(Name)
        mm_email.append(Email)
    if Branch == "me":
        me_branch_strength += 1
        me_roll.append(Roll_No)
        me_name.append(Name)
        me_email.append(Email)
    if Branch == "ee":
        ee_branch_strength += 1
        ee_roll.append(Roll_No)
        ee_name.append(Name)
        ee_email.append(Email)
    if Branch == "cs":
        cs_branch_strength += 1
        cs_roll.append(Roll_No)
        cs_name.append(Name)
        cs_email.append(Email)
    if Branch == "ce":
        ce_branch_strength += 1
        ce_roll.append(Roll_No)
        ce_name.append(Name)
        ce_email.append(Email)
    if Branch == "cb":
        cb_branch_strength += 1
        cb_roll.append(Roll_No)
        cb_name.append(Name)
        cb_email.append(Email)


def average_function(total_students, mm_branch_strength, cs_branch_strength, ee_branch_strength, me_branch_strength, cb_branch_strength, ce_branch_strength):
    global average_group_members, average_cs_branch, average_ee_branch, average_mm_branch, average_me_branch, average_cb_branch, average_ce_branch
    average_group_members = (total_students/number_of_groups)
    average_cs_branch = (cs_branch_strength/number_of_groups)
    average_ce_branch = (ce_branch_strength/number_of_groups)
    average_cb_branch = (cb_branch_strength/number_of_groups)
    average_me_branch = (me_branch_strength/number_of_groups)
    average_mm_branch = (mm_branch_strength/number_of_groups)
    average_ee_branch = (ee_branch_strength/number_of_groups)


def task1(number_of_groups):
    global mm_branch_strength, cs_branch_strength, ee_branch_strength, me_branch_strength, cb_branch_strength, ce_branch_strength
    data = [['EE', ee_branch_strength], [
        'ME', me_branch_strength], ['CS', cs_branch_strength], ['CE', ce_branch_strength], ['CB', cb_branch_strength], ['MM', mm_branch_strength]]
    with open(path+'branch_strength.csv', 'w', newline='') as file:
        writer = csv.writer(file, dialect='excel')
        writer.writerow(["BRANCH_CODE", "STRENGTH"])
        writer.writerows(data)
# task2


def task2():
    data = {"Roll": cs_roll, "Name": cs_name, "Email": cs_email}
    df = pd.DataFrame(data)
    df.to_csv(path+'CS.csv', index=False, header=True)

    data = {"Roll": ce_roll, "Name": ce_name, "Email": ce_email}
    df = pd.DataFrame(data)
    df.to_csv(path+'CE.csv', index=False, header=True)

    data = {"Roll": cb_roll, "Name": cb_name, "Email": cb_email}
    df = pd.DataFrame(data)
    df.to_csv(path+'CB.csv', index=False, header=True)

    data = {"Roll": ee_roll, "Name": ee_name, "Email": ee_email}
    df = pd.DataFrame(data)
    df.to_csv(path+'EE.csv', index=False, header=True)

    data = {"Roll": me_roll, "Name": me_name, "Email": me_email}
    df = pd.DataFrame(data)
    df.to_csv(path+'ME.csv', index=False, header=True)

    data = {"Roll": mm_roll, "Name": mm_name, "Email": mm_email}
    df = pd.DataFrame(data)
    df.to_csv(path+'MM.csv', index=False, header=True)


def sort_fn(pa, number_of_groups):
    df = pd.read_csv(pa)
    if os.path.exists('./data_file/stats_grouping.csv') == False:
        dataframe1 = pd.read_csv('./data_file/branch_strength.csv')
        data_list = ['group', 'total']
        for x in dataframe1['BRANCH_CODE']:
            data_list.append(x)
        df1 = pd.DataFrame([data_list])
        file = './data_file/stats_grouping.csv'
        df1.to_csv(file, mode='a+', index=False, header=False)
    dataframe1 = pd.read_csv('./data_file/branch_strength.csv')
    data_list_branch = []
    for x in dataframe1['BRANCH_CODE']:
        data_list_branch.append(x)
    for i in range(1, number_of_groups+1):
        for j in range(len(df['group'])):
            x = df.loc[j]
            grp = x['group']
            if str(i) in grp and i == int(get_number(grp)):
                data_list1 = [grp, x['total']]
                for b in data_list_branch:
                    data_list1.append(x[b])
                df_t = pd.DataFrame([data_list1])
                file = './data_file/stats_grouping.csv'
                df_t.to_csv(file, mode='a+', index=False, header=False)


def task4(filename, number_of_groups):
    files = os.listdir('./data_file')
    for single_file in files:
        if 'Group' in single_file:
            if os.path.exists('./data_file/stats grouping.csv') == False:
                data_list = ['group', 'total']
                dataframe1 = pd.read_csv('./data_file/branch_strength.csv')

                for x in dataframe1['BRANCH_CODE']:
                    data_list.append(x)
                df1 = pd.DataFrame([data_list])
                file_temp = './data_file/stats grouping.csv'
                df1.to_csv(file_temp, mode='a+', index=False, header=False)

            dict1 = {}
            csv_file = './data_file/'+single_file
            df2 = pd.read_csv(csv_file)
            total = len(df2['Roll'])
            for roll_no_val in df2['Roll']:
                branch_data_1 = branch(roll_no_val)
                if branch_data_1 in dict1:
                    dict1[branch_data_1] += 1
                else:
                    dict1[branch_data_1] = 1

            data_list_2 = [single_file, total]

            dataframe1 = pd.read_csv('./data_file/branch_strength.csv')
            for x in dataframe1['BRANCH_CODE']:
                data_list_2.append(dict1[x])
            df_7 = pd.DataFrame([data_list_2])
            file_temp1 = './data_file/'+'stats grouping.csv'
            df_7.to_csv(file_temp1, mode='a+', index=False, header=False)

    df_8 = pd.read_csv('./data_file/stats grouping.csv')
    df_8.sort_index(ascending=True, inplace=True)
    data_list = ['group', 'total']
    dataframe1 = pd.read_csv('./data_file/branch_strength.csv')
    for x in dataframe1['BRANCH_CODE']:
        data_list.append(x)
    df_te1 = pd.DataFrame([data_list])
    f1 = './data_file/stats grouping.csv'
    df_te1.to_csv(f1, mode='w', index=False, header=False)
    df_8.to_csv(f1, mode='a+', index=False, header=False)
    sort_fn('./data_file/stats grouping.csv', number_of_groups)


def group_allocation(filename, number_of_groups):
    create_or_delete_folder()
    ind_value = 1
    Order_followed = re.compile("[0-9]{4}[a-z]{2}[0-9]{2}", re.I)

    Heading_Title = ["Roll", "Name", "Email"]
    Student_csv = open(filename, "r")
    read_dire = csv.DictReader(Student_csv, Heading_Title)
    for Single_stud_data in read_dire:  # For every Student, One by one
        if re.match(Order_followed, Single_stud_data.get("Roll")):

            Roll_No = Single_stud_data.get("Roll")

            global total_students
            total_students += 1
            Branch = Roll_No[4:6].lower()
            strength_function(Branch, Single_stud_data)

    task1(number_of_groups)
    task2()

    if number_of_groups == 0 or number_of_groups > total_students:
        print("\nInvalid 'Number of Groups' value given, kindly change accordingly!\n\n\t0 < number_of_groups < total_students\n")
        return

    df = pd.read_csv('./data_file/branch_strength.csv')
    queque_use = Queue()

    for no_of_group in range(1, number_of_groups+1):
        group_file = 'Group_G'+padding_convert_intostring(no_of_group)+'.csv'
        for ij in range(len(df['BRANCH_CODE'])):
            branch_code = df.loc[ij]
            branch_strength = branch_code[1]
            average_stud_perGrp = branch_strength//number_of_groups
            file = './data_file/'+branch_code[0]+'.csv'
            df1 = pd.read_csv(file)
            for index in range(average_stud_perGrp*(no_of_group-1), average_stud_perGrp*no_of_group):
                student = df1.loc[index]
                path = './data_file/'+group_file
                if os.path.exists(path) == False:
                    df_un_new = pd.DataFrame([['Roll', 'Name', 'Email']])
                    df_un_new.to_csv(
                        path, mode='a+', index=False, header=False)
                df_new = pd.DataFrame(
                    [[student['Roll'], student['Name'], student['Email']]])
                df_new.to_csv(path, mode='a+', index=False, header=False)

    for i in range(len(df['BRANCH_CODE'])):
        stud_data_x = df.loc[i]
        f = './data_file/'+stud_data_x[0]+'.csv'
        dataframe = pd.read_csv(f)
        average_stud_perGrp = stud_data_x[1]//number_of_groups
        for jk in range(average_stud_perGrp*number_of_groups, stud_data_x[1]):
            stud_data = dataframe.loc[jk]
            queque_use.put(
                (stud_data['Roll'], stud_data['Name'], stud_data['Email']))

    while queque_use.empty() == False:
        if ind_value > number_of_groups:
            ind_value = 1
        group_file1 = 'Group_G'+padding_convert_intostring(ind_value)+'.csv'
        path_value = './data_file/'+group_file1

        x_value = queque_use.get()
        df_3 = pd.DataFrame([[x_value[0], x_value[1], x_value[2]]])
        df_3.to_csv(path_value, mode='a+', index=False, header=False)
        ind_value += 1

    task4(filename, number_of_groups)
    os.remove('./data_file/stats grouping.csv')

    average_function(total_students, mm_branch_strength, cs_branch_strength,
                     ee_branch_strength, me_branch_strength, cb_branch_strength, ce_branch_strength)

    # Entire Logic
    # You can add more functions, but in the test case, we will only call the group_allocation() method,


# hello updated
filename = "Btech_2020_master_data.csv"
number_of_groups = int(input("Enter the number of groups\n"))
group_allocation(filename, number_of_groups)
