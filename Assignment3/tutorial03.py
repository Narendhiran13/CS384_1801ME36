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
    Created_directory = "./analytics/country"
    try:  # Create a Directory if necessary
        os.makedirs(Created_directory)
    except:
        pass

    Heading_Title = ["id", "full_name", "country", "email",
                     "gender", "dob", "blood_group", "state"]

    Student_csv = open("studentinfo_cs384.csv", "r")  # open the Student File
    read_dire = csv.DictReader(Student_csv, Heading_Title)

    for Single_stud_data in read_dire:
        # india
        country_var = Single_stud_data.get("country").lower()

        File_name = "{}.csv".format(country_var)

        # open the New File according to the country
        f = open("{}/{}".format(Created_directory, File_name), "a")
        # Writing in the File about the Student
        read_write = csv.DictWriter(f, Heading_Title)
        read_write.writerow(Single_stud_data)

    pass


def email_domain_extract():
    # Read csv and process

    Created_directory = "./analytics/email_domain"
    try:  # Create a Directory if necessary
        os.makedirs(Created_directory)
    except:
        pass

    # Remove
    with open("./studentinfo_cs384.csv", "r") as Student_csv:

        read_dire = csv.DictReader(Student_csv)
        Heading_Title = read_dire.fieldnames
        next(read_dire, None)  # skip the heading line

        for Single_stud_data in read_dire:
            email_var = Single_stud_data.get("email")
            domain = email_var.split("@")[1].split(".")[0]
            File_name = "{}/{}.csv".format(Created_directory, domain)
            with open(File_name, "w") as f:
                # Writing in the File about the Student
                csv.DictWriter(f, Heading_Title).writeheader()
    with open("./studentinfo_cs384.csv", "r") as Student_csv:
        read_dire = csv.DictReader(Student_csv)
        Heading_Titles = read_dire.fieldnames
        next(read_dire, None)  # skip header
        for Single_stud_data in read_dire:
            email_var = Single_stud_data.get("email")
            domain = email_var.split("@")[1].split(".")[0]
            File_name = "{}/{}.csv".format(Created_directory, domain)
            with open(File_name, "a") as f:
                csv.DictWriter(f, Heading_Titles).writerow(
                    Single_stud_data)  # Writing in the File about the Student
    pass


def gender():
    # Read csv and process
    Created_directory = "./analytics/gender"
    try:  # Create a Directory if necessary
        os.makedirs(Created_directory)
    except:
        pass

    Heading_Titles = ["id", "full_name", "country", "email",
                      "gender", "dob", "blood_group", "state"]

    Student_csv = open("studentinfo_cs384.csv", "r")
    read_dire = csv.DictReader(Student_csv, Heading_Titles)

    for Single_stud_data in read_dire:
        # Male/Female
        gender_var = Single_stud_data.get("gender").lower()

        if (gender_var == "male" or gender_var == "female"):

            File_name = "{}.csv".format(gender_var)

            # open the New File according to the gender
            f = open("{}/{}".format(Created_directory, File_name), "a")
            # Writing in the File about the Student
            read_write = csv.DictWriter(f, Heading_Titles)
            read_write.writerow(Single_stud_data)
        else:
            continue

    pass


def dob():
    # Read csv and process
    Created_directory = "analytics/dob"
    try:  # Create a Directory if necessary
        os.makedirs(Created_directory)
    except:
        pass

    with open("./studentinfo_cs384.csv", "r") as Student_csv:
        read_dir = csv.DictReader(Student_csv)
        fieldname = read_dir.fieldnames
        next(read_dir, None)
        Mapping_Var_change = {
            1: csv.DictWriter(open("{}/bday_1995_1999.csv".format(Created_directory), "w"), fieldname),
            2: csv.DictWriter(open("{}/bday_2000_2004.csv".format(Created_directory), "w"), fieldname),
            3: csv.DictWriter(open("{}/bday_2005_2009.csv".format(Created_directory), "w"), fieldname),
            4: csv.DictWriter(open("{}/bday_2010_2014.csv".format(Created_directory), "w"), fieldname),
            5: csv.DictWriter(open("{}/bday_2015_2020.csv".format(Created_directory), "w"), fieldname)
        }
        for i in range(len(Mapping_Var_change)):
            Mapping_Var_change.get(i+1).writeheader()
        for Single_stud_data in read_dir:
            if re.match(re.compile("[0-9]{2}-[0-9]{2}-[0-9]{4}"), Single_stud_data.get("dob")):
                year = Single_stud_data.get("dob").split("-")[-1]
                condition = -1
                if 1995 <= int(year) <= 1999:
                    condition = 1
                elif 2000 <= int(year) <= 2004:
                    condition = 2
                elif 2005 <= int(year) <= 2009:
                    condition = 3
                elif 2010 <= int(year) <= 2014:
                    condition = 4
                elif 2015 <= int(year) <= 2020:
                    condition = 5
                if condition != -1:
                    Mapping_Var_change.get(
                        condition).writerow(Single_stud_data)
    pass


def state():
    # Read csv and process

    Created_directory = "./analytics/state"
    try:  # Create a Directory if necessary
        os.makedirs(Created_directory)
    except:
        pass

    Heading_Titles = ["id", "full_name", "country", "email",
                      "gender", "dob", "blood_group", "state"]

    Student_csv = open("studentinfo_cs384.csv", "r")
    read_dire = csv.DictReader(Student_csv, Heading_Titles)

    for Single_stud_data in read_dire:
        # Tamil Nadu
        gender_var = Single_stud_data.get("state").lower()

        File_name = "{}.csv".format(gender_var)

        # open the New File according to the state
        f = open("{}/{}".format(Created_directory, File_name), "a")
        # Writing in the File about the Student
        read_write = csv.DictWriter(f, Heading_Titles)
        read_write.writerow(Single_stud_data)

    pass


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass
