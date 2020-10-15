import csv
import re
import os


def course():
    # Read csv and process
    Created_directory = "./analytics/course"
    try:  # Create a Directory if necessary
        os.makedirs(Created_directory)
    except:
        pass

    Order_followed = re.compile("[0-9]{4}[a-z]{2}[0-9]{2}", re.I)

    Heading_Title = ["id", "full_name", "country", "email",
                     "gender", "dob", "blood_group", "state"]

    Student_csv = open("studentinfo_cs384.csv", "r")
    read_dire = csv.DictReader(Student_csv, Heading_Title)

    for Single_stud_data in read_dire:  # For every Student, One by one

        if re.match(Order_followed, Single_stud_data.get("id")):
            # 1801ME36
            Roll_No = Single_stud_data.get("id")
            Year = Roll_No[:2]
            Map_variable = Roll_No[2:4]
            Branch = Roll_No[4:6].lower()
            Mapping_Var_change = {
                "01": "btech",
                "11": "mtech",
                "12": "msc",
                "21": "phd",
            }

            Directory_folder_name = "{}/{}/{}".format(Created_directory,
                                                      Branch, Mapping_Var_change.get(Map_variable))
            File_name = "{}{}{}.csv".format(
                Year, Branch, Mapping_Var_change.get(Map_variable))

            try:  # Create a Directory if necessary
                os.makedirs(Directory_folder_name)
            except:
                pass

            # open the New File according to the Roll No
            f = open("{}/{}".format(Directory_folder_name, File_name), "a")
            # Writing in the File about the Student
            read_write = csv.DictWriter(f, Heading_Title)
            read_write.writerow(Single_stud_data)

        else:
            # open the New File according to the Roll No
            f = open("{}/misc.csv".format(Created_directory), "a")
            # Writing in the File about the Student
            read_write = csv.DictWriter(f, Heading_Title)
            read_write.writerow(Single_stud_data)
    pass


def country():
    # Read csv and process
    pass


def email_domain_extract():
    # Read csv and process
    pass


def gender():
    # Read csv and process
    pass


def dob():
    # Read csv and process
    pass


def state():
    # Read csv and process
    pass


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass
