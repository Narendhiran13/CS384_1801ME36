import re
import csv
import os
import pandas as pd


average_group_members, average_cs_branch, average_ee_branch, average_mm_branch, average_me_branch, average_cb_branch, average_ce_branch = [
    0 for i in range(7)]
total_students, mm_branch_strength, cs_branch_strength, ee_branch_strength, me_branch_strength, cb_branch_strength, ce_branch_strength = [
    0 for i in range(7)]
mm_roll, mm_name, mm_email, me_roll, me_name, me_email, ee_roll, ee_name, ee_email, cb_roll, cb_name, cb_email, ce_roll, ce_name, ce_email, cs_roll, cs_name, cs_email = ([
] for i in range(18))


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
    with open('branch_strength.csv', 'w', newline='') as file:
        writer = csv.writer(file, dialect='excel')
        writer.writerow(["BRANCH_CODE", "STRENGTH"])
        writer.writerows(data)
# task2


def task2():
    data = {"Roll": cs_roll, "Name": cs_name, "Email": cs_email}
    df = pd.DataFrame(data)
    df.to_csv('CS.csv', index=False, header=True)

    data = {"Roll": ce_roll, "Name": ce_name, "Email": ce_email}
    df = pd.DataFrame(data)
    df.to_csv('CE.csv', index=False, header=True)

    data = {"Roll": cb_roll, "Name": cb_name, "Email": cb_email}
    df = pd.DataFrame(data)
    df.to_csv('CB.csv', index=False, header=True)

    data = {"Roll": ee_roll, "Name": ee_name, "Email": ee_email}
    df = pd.DataFrame(data)
    df.to_csv('EE.csv', index=False, header=True)

    data = {"Roll": me_roll, "Name": me_name, "Email": me_email}
    df = pd.DataFrame(data)
    df.to_csv('ME.csv', index=False, header=True)

    data = {"Roll": mm_roll, "Name": mm_name, "Email": mm_email}
    df = pd.DataFrame(data)
    df.to_csv('MM.csv', index=False, header=True)


'''
def task3(number_of_groups):
    global mm_branch_strength, cs_branch_strength, ee_branch_strength, me_branch_strength, cb_branch_strength, ce_branch_strength
    global average_group_members, average_cs_branch, average_ee_branch, average_mm_branch, average_me_branch, average_cb_branch, average_ce_branch
    print(average_cs_branch, average_ee_branch, average_mm_branch,
          average_me_branch, average_cb_branch, average_ce_branch)
    with open('branch_strength.csv', 'w', newline='') as file:
        writer = csv.writer(file, dialect='excel')
        writer.writerow(["group", "total", "EE", "ME", "CS", "CE", "CB", "MM"])
        for n in range(1, number_of_groups+1):

            if(average_group_members > (number_of_groups-n+1) * int(average_group_members)):
                grp_total_mem = int(average_group_members)+1
            else:
                grp_total_mem = int(average_group_members)

            if(average_ee_branch > (number_of_groups-n+1) * int(average_ee_branch)):
                ee_grp_total_mem = int(average_ee_branch)+1
            else:
                ee_grp_total_mem = int(average_ee_branch)

            if(average_ee_branch > (number_of_groups-n+1) * int(average_ee_branch)):
                ee_grp_total_mem = int(average_ee_branch)+1
            else:
                ee_grp_total_mem = int(average_ee_branch)

            for ee_grp + me_grp + cs_grp+ce_grp+cb_grp+mm_grp == grp_total_mem:
'''


def group_allocation(filename, number_of_groups):

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

    average_function(total_students, mm_branch_strength, cs_branch_strength,
                     ee_branch_strength, me_branch_strength, cb_branch_strength, ce_branch_strength)

    # Entire Logic
    # You can add more functions, but in the test case, we will only call the group_allocation() method,


filename = "Btech_2020_master_data.csv"
number_of_groups = 12
group_allocation(filename, number_of_groups)
print(average_group_members)
