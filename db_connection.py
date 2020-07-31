import math

import datetime
import mysql.connector
import pandas
import os


def connect_db():
    # was having issues with the conf file, so just using args for now
    # db = mysql.connector.connect(option_files=conf_path)
    db = mysql.connector.connect(option_files='mysql.conf')
    return db


# Todo: Add list options for patient ID's and table names
def main():
    # Patient ID is the name of the folder the data is all contained in, i.e. TeSt1
    print("Enter the patient ID for which you would like to export data to the MySQL database: ", end="")
    patient_id = input()

    if patient_id == "quit" or patient_id == "Quit":
        print("Goodbye!")
        exit(0)

    # Check if we can find the patient ID
    path = "Current Patients/" + patient_id
    patient_found = os.path.isdir(path)

    if not patient_found:
        print(
            "Error: Could not find patient " + patient_id + ". Please check the ID or type 'quit' to exit the program.")
        main()

    # Get the table name, i.e. Anthropometrics.
    print("Enter the name of the source table you would like to export: ", end="")
    table_name = input()

    if table_name == "quit" or table_name == "Quit":
        print("Goodbye!")
        exit(0)

    path += "/DataBases/Data/" + patient_id + "_" + table_name + "_Source.xlsx"
    file_found = os.path.isfile(path)
    if not file_found:
        print(
            "Error: Could not find table " + table_name + ". Please check the table name or type 'quit' to exit the program.")
        main()

    # Initialize the database
    db = connect_db()
    cursor = db.cursor()

    # Import the dataframe from the spreadsheet
    data = pandas.read_excel(path)

    if table_name == "Anthropometrics":
        export_anthropometrics_data(data, cursor)
    elif table_name == "Alertness":
        export_alertness_data(data, cursor)
    elif table_name == "Clinic_GI_Issues":
        export_clinic_gi_issues_data(data, cursor)
    elif table_name == "Daily_Intake":
        export_daily_intake_data(data, cursor)
    elif table_name == "Diet_Rx":
        export_diet_rx_data(data, cursor)
    elif table_name == "Med_Data":
        export_med_data(data, cursor)

    db.commit()


# All read functions take in a pandas dataframe
def read_anthropometrics_data(data, row_number):
    row = data.iloc[row_number]

    mrn = int(row["MRNumber"])
    kgid = get_kgid(mrn)

    collected_date = string_to_datetime(str(row["Date"]))
    first_date = get_first_date(data, "Date")
    collected_date_age = (collected_date - first_date).days  # gives an int

    day_type = convert_num(int(row["Day_Type"]))
    src = convert_str(str(row["Source"]))
    cp = convert_num(int(row["CP"]))
    pa = convert_num(float(row["PA"]))
    ht = convert_num(float(row["Ht"]))
    wt = convert_num(float(row["Wt"]))
    hc = convert_num(float(row["HC"]))
    uac = convert_num(float(row["UAC"]))
    tsf = convert_num(float(row["TSF"]))
    ssf = convert_num(float(row["SSF"]))
    usf = convert_num(float(row["USF"]))
    sisf = convert_num(float(row["SISF"]))
    mbsf = convert_num(float(row["MBSF"]))
    uc = convert_num(float(row["UC"]))
    r = convert_num(float(row["R"]))
    x = convert_num(float(row["X"]))

    entered_init = convert_str(str(row["Entered"]))
    if entered_init is not None:
        entered_init = entered_init[0:2]

    audited_init = convert_str(str(row["Audited"]))
    if audited_init is not None:
        audited_init = audited_init[0:2]

    comments = convert_str(str(row["Comments"]))

    return kgid, collected_date_age, day_type, src, cp, pa, ht, wt, hc, uac, tsf, ssf, usf, sisf, mbsf, uc, r, x, entered_init, audited_init, comments


def export_anthropometrics_data(data, db_cursor):
    # Check if the table exists, create it if not
    table_query = """SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'Anthropometrics'"""
    db_cursor.execute(table_query)
    if not db_cursor.fetchone()[0] == 1:
        creation_query = """
            CREATE TABLE `Anthropometrics` (
            `kgid` char(6) NOT NULL,
            `days_since_initial_data` smallint(4) NOT NULL,
            `day_type` tinyint(4) NOT NULL,
            `src` tinyint(4) NOT NULL,
            `cp` tinyint(4) DEFAULT NULL,
            `pa` float(3,2) DEFAULT NULL,
            `ht` float(4,1) DEFAULT NULL,
            `wt` float(3,1) DEFAULT NULL,
            `hc` float(3,1) DEFAULT NULL,
            `uac` float(3,1) DEFAULT NULL,
            `tsf` float(3,1) DEFAULT NULL,
            `ssf` float(3,1) DEFAULT NULL,
            `usf` float(3,1) DEFAULT NULL,
            `sisf` float(3,1) DEFAULT NULL,
            `mbsf` float(3,1) DEFAULT NULL,
            `uc` float(3,1) DEFAULT NULL,
            `r` float(3,1) DEFAULT NULL,
            `x` float(3,1) DEFAULT NULL,
            `entered_init` char(2) DEFAULT NULL,
            `audited_init` char(2) DEFAULT NULL,
            `comments` varchar(2048) DEFAULT NULL
        )"""
        db_cursor.execute(creation_query)

    # Go through each row of the sheet. Keep a record of kgid's we've already deleted so we don't delete new data.
    deleted_kgid = []
    for i in range(0, data.shape[0]):
        row_tuple = read_anthropometrics_data(data, i)
        kgid = row_tuple[0]

        # Delete all rows in the table with matching kgid
        if kgid not in deleted_kgid:
            deletion_query = "DELETE FROM Anthropometrics WHERE kgid='{}'".format(kgid)
            db_cursor.execute(deletion_query)
            deleted_kgid.append(kgid)

        # Insert the new row
        query = "INSERT INTO Anthropometrics (kgid, days_since_initial_data, day_type, src, cp, pa, ht, wt, hc, uac, tsf, ssf, usf, sisf, mbsf, uc, r, x, entered_init, audited_init, comments) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        db_cursor.execute(query, row_tuple)


def read_alertness_data(data, row_number):
    row = data.iloc[row_number]

    mrn = int(row["MRNumber"])
    kgid = get_kgid(mrn)

    collected_date = string_to_datetime(str(row["Date"]))
    first_date = get_first_date(data, "Date")
    collected_date_age = (collected_date - first_date).days  # gives an int

    day_type = str(row["Day_Type"])
    alertness = convert_str(str(row["Alertness"]))
    activity = convert_str(str(row["Activity"]))
    development = convert_str(str(row["Development"]))

    entered_init = convert_str(str(row["Entered"]))
    if entered_init is not None:
        entered_init = entered_init[0:2]

    audited_init = convert_str(str(row["Audited"]))
    if audited_init is not None:
        audited_init = audited_init[0:2]

    comments = convert_str(str(row["Comments"]))

    return kgid, collected_date_age, day_type, alertness, activity, development, entered_init, audited_init, comments


def export_alertness_data(data, db_cursor):
    # Check if the table exists, create it if not
    table_query = """SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'Alertness'"""
    db_cursor.execute(table_query)
    if not db_cursor.fetchone()[0] == 1:
        creation_query = """
                CREATE TABLE `Alertness` (
                `kgid` char(6) NOT NULL,
                `days_since_initial_data` smallint(4) NOT NULL,
                `day_type` tinyint(4) NOT NULL,
                `alertness` varchar(2048) DEFAULT NULL,
                `actvity` varchar(2048) DEFAULT NULL,
                `development` varchar(2048) DEFAULT NULL, 
                `entered_init` char(2) DEFAULT NULL,
                `audited_init` char(2) DEFAULT NULL,
                `comments` varchar(2048) DEFAULT NULL
            )"""
        db_cursor.execute(creation_query)

    # Go through each row of the sheet. Keep a record of kgid's we've already deleted so we don't delete new data.
    deleted_kgid = []
    for i in range(0, data.shape[0]):
        row_tuple = read_alertness_data(data, i)
        kgid = row_tuple[0]

        # Delete all rows in the table with matching kgid
        if kgid not in deleted_kgid:
            deletion_query = "DELETE FROM Alertness WHERE kgid='{}'".format(kgid)
            db_cursor.execute(deletion_query)
            deleted_kgid.append(kgid)

        # Insert the new row
        query = "INSERT INTO Alertness (kgid, days_since_initial_data, day_type, alertness, actvity, development, entered_init, audited_init, comments) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        db_cursor.execute(query, row_tuple)


def read_clinic_gi_issues_data(data, row_number):
    row = data.iloc[row_number]

    mrn = int(row["MRNumber"])
    kgid = get_kgid(mrn)

    collected_date = string_to_datetime(str(row["Date"]))
    first_date = get_first_date(data, "Date")
    collected_date_age = (collected_date - first_date).days  # gives an int

    day_type = str(row["Day_Type"])
    clinic_const = str(row["Clinic_Const"])
    clinic_dia = str(row["Clinic_Dia"])
    clinic_vom = str(row["Clinic_Vom"])
    clinic_nausea = str(row["Clinic_Nausea"])
    clinic_gag_retch = str(row["Clinic_Gag_Retch"])
    clinic_nissen = str(row["Clinic_Nissen"])
    clinic_descr_const = str(row["Clinic_Descr_Const"])
    clinic_desc_dia = str(row["Clinic_Descr_Dia"])
    clinic_desc_vom = str(row["Clinic_Descr_Vom"])
    clinic_descr_nausea = str(row["Clinic_Descr_Nausea"])
    clinic_descr_gag_retch = str(row["Clinic_Descr_Gag_Retch"])

    entered_init = convert_str(str(row["Entered"]))
    if entered_init is not None:
        entered_init = entered_init[0:2]

    audited_init = convert_str(str(row["Audited"]))
    if audited_init is not None:
        audited_init = audited_init[0:2]

    comments = convert_str(str(row["Comments"]))

    return kgid, collected_date_age, day_type, clinic_const, clinic_dia, clinic_vom, clinic_nausea, clinic_gag_retch, clinic_nissen, clinic_descr_const, clinic_desc_dia, clinic_desc_vom, clinic_descr_nausea, clinic_descr_gag_retch, entered_init, audited_init, comments


def export_clinic_gi_issues_data(data, db_cursor):
    # Check if the table exists, create it if not
    table_query = """SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'Clinic_GI_Issues'"""
    db_cursor.execute(table_query)
    if not db_cursor.fetchone()[0] == 1:
        creation_query = """
                CREATE TABLE `Clinic_GI_Issues` (
                `kgid` char(6) NOT NULL,
                `days_since_initial_data` smallint(4) NOT NULL,
                `day_type` tinyint(4) NOT NULL,
                `clinic_const` varchar(3) DEFAULT NULL,
                `clinic_dia` varchar(3) DEFAULT NULL,
                `clinic_vom` varchar(3) DEFAULT NULl,
                `clinic_nausea` varchar(3) DEFAULT NULL,
                `clinic_gag_retch` varchar(3) DEFAULT NULL,
                `clinic_nissen` varchar(3) DEFAULT NULl,
                `clinic_descr_const` varchar(2048) DEFAULT NULL,
                `clinic_descr_dia` varchar(2048) DEFAULT NULL,
                `clinic_descr_vom` varchar(2048) DEFAULT NULL,
                `clinic_descr_nausea` varchar(2048) DEFAULT NULL,
                `clinic_descr_gag_retch` varchar(2048) DEFAULT NULL,
                `entered_init` char(2) DEFAULT NULL,
                `audited_init` char(2) DEFAULT NULL,
                `comments` varchar(2048) DEFAULT NULL
            )"""
        db_cursor.execute(creation_query)

    # Go through each row of the sheet. Keep a record of kgid's we've already deleted so we don't delete new data.
    deleted_kgid = []
    for i in range(0, data.shape[0]):
        row_tuple = read_clinic_gi_issues_data(data, i)
        kgid = row_tuple[0]

        # Delete all rows in the table with matching kgid
        if kgid not in deleted_kgid:
            deletion_query = "DELETE FROM Clinic_GI_Issues WHERE kgid='{}'".format(kgid)
            db_cursor.execute(deletion_query)
            deleted_kgid.append(kgid)

        # Insert the new row
        query = "INSERT INTO Clinic_GI_Issues (kgid, days_since_initial_data, day_type, clinic_const, clinic_dia, clinic_vom, clinic_nausea, clinic_gag_retch, clinic_nissen, clinic_descr_const, clinic_descr_dia, clinic_descr_vom, clinic_descr_nausea, clinic_descr_gag_retch, entered_init, audited_init, comments) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        db_cursor.execute(query, row_tuple)


# todo do this one (it's the super long one)
def read_clinical_labs_data(data, row_number):
    pass


def read_daily_intake_data(data, row_number):
    row = data.iloc[row_number]

    mrn = int(row["MRNumber"])
    kgid = get_kgid(mrn)

    collected_date = string_to_datetime(str(row["Date"]))
    first_date = get_first_date(data, "Date")
    collected_date_age = (collected_date - first_date).days  # gives an int

    day_type = str(row["Day_Type"])
    pkt_recipe_number = str(row["PKT_Recipe_Number"])
    data_quality_d = str(row["Data_Quality_D"])
    day_quality_d = str(row["Day_Quality_D"])

    entered_init = convert_str(str(row["Entered"]))
    if entered_init is not None:
        entered_init = entered_init[0:2]

    audited_init = convert_str(str(row["Audited"]))
    if audited_init is not None:
        audited_init = audited_init[0:2]

    comments = convert_str(str(row["Comments"]))

    return kgid, collected_date_age, day_type, pkt_recipe_number, data_quality_d, day_quality_d, entered_init, audited_init, comments

def export_daily_intake_data(data, db_cursor):
    # Check if the table exists, create it if not
    table_query = """SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'Daily_Intake'"""
    db_cursor.execute(table_query)
    if not db_cursor.fetchone()[0] == 1:
        creation_query = """
                CREATE TABLE `Daily_Intake` (
                `kgid` char(6) NOT NULL,
                `days_since_initial_data` smallint(4) NOT NULL,
                `day_type` tinyint(4) NOT NULL,
                `pkt_recipe_number` varchar(5) DEFAULT NULL,
                `data_quality_d` tinyint(2) DEFAULT NULL,
                `day_quality_d` tinyint(2) DEFAULT NULL,
                `entered_init` char(2) DEFAULT NULL,
                `audited_init` char(2) DEFAULT NULL,
                `comments` varchar(2048) DEFAULT NULL
            )"""
        db_cursor.execute(creation_query)

    # Go through each row of the sheet. Keep a record of kgid's we've already deleted so we don't delete new data.
    deleted_kgid = []
    for i in range(0, data.shape[0]):
        row_tuple = read_daily_intake_data(data, i)
        kgid = row_tuple[0]

        # Delete all rows in the table with matching kgid
        if kgid not in deleted_kgid:
            deletion_query = "DELETE FROM Daily_Intake WHERE kgid='{}'".format(kgid)
            db_cursor.execute(deletion_query)
            deleted_kgid.append(kgid)

        # Insert the new row
        query = "INSERT INTO Daily_Intake (kgid, days_since_initial_data, day_type, pkt_recipe_number, data_quality_d, day_quality_d, entered_init, audited_init, comments) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        db_cursor.execute(query, row_tuple)

def read_diet_rx_data(data, row_number):
    row = data.iloc[row_number]

    mrn = int(row["MRNumber"])
    kgid = get_kgid(mrn)

    collected_date = string_to_datetime(str(row["Date"]))
    first_date = get_first_date(data, "Date")
    collected_date_age = (collected_date - first_date).days  # gives an int

    day_type = str(row["Day_Type"])
    rof_pr = str(row["ROF_Pr"])
    reason_for_change_diet = str(row["Reason_For_Change_Diet"])
    snack_cal_pr = str(row["Snack_Cal_Pr"])
    snack_ratio_pr = str(row["Snack_Ratio_Pr"])
    snack_number_pr = str(row["Snack_Number_Pr"])
    meal_number_pr = str(row["Meal_Number_Pr"])
    ratio_pr = str(row["Ratio_Pr"])
    cal_pr = str(row["Cal_Pr"])
    pro_pr = str(row["Pro_Pr"])

    entered_init = convert_str(str(row["Entered"]))
    if entered_init is not None:
        entered_init = entered_init[0:2]

    audited_init = convert_str(str(row["Audited"]))
    if audited_init is not None:
        audited_init = audited_init[0:2]

    comments = convert_str(str(row["Comments"]))

    return kgid, collected_date_age, day_type, rof_pr, reason_for_change_diet, snack_cal_pr, snack_ratio_pr, snack_number_pr, meal_number_pr, ratio_pr, cal_pr, pro_pr, entered_init, audited_init, comments


def export_diet_rx_data(data, db_cursor):
    # Check if the table exists, create it if not
    table_query = """SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'Diet_Rx'"""
    db_cursor.execute(table_query)
    if not db_cursor.fetchone()[0] == 1:
        creation_query = """
                CREATE TABLE `Diet_Rx` (
                `kgid` char(6) NOT NULL,
                `days_since_initial_data` smallint(4) NOT NULL,
                `day_type` tinyint(4) NOT NULL,
                `rof_pr` varchar(5) NOT NULL,
                `reason_for_change` tinyint(2) NOT NULL,
                `snack_cal_pr` float(4,1) DEFAULT NULL,
                `snack_ratio_pr` float(3,2) DEFAULT NULL,
                `snack_number_pr` tinyint(2) DEFAULT NULL,
                `meal_number_pr` tinyint(2) NOT NULL,
                `ratio_pr` float(3,2) NOT NULL,
                `cal_pr` float(6,2) NOT NULL,
                `pro_pr` float(4,2) NOT NULL,
                `entered_init` char(2) DEFAULT NULL,
                `audited_init` char(2) DEFAULT NULL,
                `comments` varchar(2048) DEFAULT NULL
            )"""
        db_cursor.execute(creation_query)

    # Go through each row of the sheet. Keep a record of kgid's we've already deleted so we don't delete new data.
    deleted_kgid = []
    for i in range(0, data.shape[0]):
        row_tuple = read_diet_rx_data(data, i)
        kgid = row_tuple[0]

        # Delete all rows in the table with matching kgid
        if kgid not in deleted_kgid:
            deletion_query = "DELETE FROM Diet_Rx WHERE kgid='{}'".format(kgid)
            db_cursor.execute(deletion_query)
            deleted_kgid.append(kgid)

        # Insert the new row
        query = "INSERT INTO Diet_Rx VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        db_cursor.execute(query, row_tuple)


def read_med_data(data, row_number):
    row = data.iloc[row_number]

    mrn = int(row["MRNumber"])
    kgid = get_kgid(mrn)

    collected_date = string_to_datetime(str(row["Date"]))
    first_date = get_first_date(data, "Date")
    collected_date_age = (collected_date - first_date).days  # gives an int

    day_type = convert_num(int(row["Day_Type"]))
    ndid = convert_num(int(row["NDID"]))
    med_id = convert_num(int(row["Med_ID"]))
    reason_for_change_med = convert_num(int(row["Reason_For_Change_Med"]))
    prod_name = convert_str(str(row["Prod_Name"]))
    daily_med_dose_mg = convert_num(int(row["Daily_Med_Dose_Mg"]))
    med_doses = convert_num(float(row["Med_Doses"]))
    med_comments = convert_str(str(row["Med_Comments"]))

    entered_init = convert_str(str(row["Entered"]))
    if entered_init is not None:
        entered_init = entered_init[0:2]

    audited_init = convert_str(str(row["Audited"]))
    if audited_init is not None:
        audited_init = audited_init[0:2]

    comments = convert_str(str(row["Comments"]))

    return kgid, collected_date_age, day_type, ndid, med_id, reason_for_change_med, prod_name, daily_med_dose_mg, med_doses, med_comments, entered_init, audited_init, comments


def export_med_data(data, db_cursor):
    # Check if the table exists, create it if not
    table_query = """SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'Med_Data'"""
    db_cursor.execute(table_query)
    if not db_cursor.fetchone()[0] == 1:
        creation_query = """
                CREATE TABLE `Med_Data` (
                `kgid` char(6) NOT NULL,
                `days_since_initial_data` smallint(4) NOT NULL,
                `day_type` tinyint(4) NOT NULL,
                `ndid` char(8) NOT NULL,
                `med_id` char(8) NOT NULL,
                `reason_for_change` tinyint(2) DEFAULT NULL,
                `prod_name` varchar(1024) DEFAULT NULL,
                `daily_med_dose_mg` float(6,2) DEFAULT NULL,
                `med_doses` tinyint(2) DEFAULT NULL,
                `med_comments` varchar(2048) DEFAULT NULL,
                `entered_init` char(2) DEFAULT NULL,
                `audited_init` char(2) DEFAULT NULL,
                `comments` varchar(2048) DEFAULT NULL
            )"""
        db_cursor.execute(creation_query)

    # Go through each row of the sheet. Keep a record of kgid's we've already deleted so we don't delete new data.
    deleted_kgid = []
    for i in range(0, data.shape[0]):
        row_tuple = read_med_data(data, i)
        kgid = row_tuple[0]

        # Delete all rows in the table with matching kgid
        if kgid not in deleted_kgid:
            deletion_query = "DELETE FROM Med_Data WHERE kgid='{}'".format(kgid)
            db_cursor.execute(deletion_query)
            deleted_kgid.append(kgid)

        # Insert the new row
        query = "INSERT INTO Med_Data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        db_cursor.execute(query, row_tuple)


def read_menus_data(data, row_number):
    row = data.iloc[row_number]

    mrn = int(row["MRNumber"])
    kgid = get_kgid(mrn)

    collected_date = string_to_datetime(str(row["Date"]))
    first_date = get_first_date(data, "Date")
    collected_date_age = (collected_date - first_date).days  # gives an int

    cal_prcnt = str(row["Cal_Prcnt"])
    procnt_prcnt = str(row["Procnt_Prcnt"])
    ratio_pr = str(row["Ratio_Pr"])
    meal_number_pr = str(row["Meal_Number_Pr"])
    snack_number_pr = str(row["Snack_Number_Pr"])
    pkt_recipe_name = str(row["PKT_Recipe_Name"])
    pkt_recipe_number = str(row["PKT_Recipe_Number"])
    pkt_recipe_ingredient_amount = str(row["PKT_Recipe_Ingredient_Amount"])
    ndid = str(row["NDID"])
    prod_name = str(row["Prod_Name"])
    recipe_type = str(row["Recipe_Type"])

    entered_init = convert_str(str(row["Entered"]))
    if entered_init is not None:
        entered_init = entered_init[0:2]

    audited_init = convert_str(str(row["Audited"]))
    if audited_init is not None:
        audited_init = audited_init[0:2]

    comments = convert_str(str(row["Comments"]))

    return kgid, collected_date_age, cal_prcnt, procnt_prcnt, ratio_pr, meal_number_pr, snack_number_pr, pkt_recipe_name, pkt_recipe_number, pkt_recipe_ingredient_amount, ndid, prod_name, recipe_type, entered_init, audited_init, comments


def get_first_date(data, column_label):
    num_rows = data.shape[0]

    first_row = data.iloc[0]
    first_date = string_to_datetime(str(first_row[column_label]))

    if num_rows == 1:
        return first_date
    for i in range(1, num_rows):
        row = data.iloc[i]
        j_date = string_to_datetime(str(row[column_label]))
        diff = int((first_date - j_date).days)
        if diff > 0:  # j_date comes first
            first_date = j_date

    return first_date


def string_to_datetime(string):
    if " " in string:
        string = string.split(" ")[0]
    if string[2] == "/":
        string = datetime.datetime.strptime(string, "%m/%d/%Y")
    else:
        string = datetime.datetime.strptime(string, "%Y-%m-%d")
    return string


def get_translation_table(path):
    df = pandas.read_excel(path)
    return df


def get_kgid(mrn):
    df = get_translation_table("Current Patients/KGID_Translation_Test.xlsx")
    num_rows = df.shape[0]
    for i in range(0, num_rows):
        row = df.iloc[i]
        mrn_i = int(row["MRNUMBER"])
        if mrn_i == mrn:
            kgid = str(row["KGID"])
            return kgid


def convert_num(num):
    if math.isnan(num):
        return None
    return num


def convert_str(string):
    if string == "nan":
        return None
    return string


if __name__ == "__main__":
    main()
