import mysql.connector
import SpreadSheetAccess
import pandas


def connect_db(conf_path):
    # was having issues with the conf file, so just using args for now
    # db = mysql.connector.connect(option_files=conf_path)
    db = mysql.connector.connect(host="ict-prod-hosting01.mysql.osg.ufl.edu", database="ifasitmysql06", user="ifasitmysql06", password="Q1B#f83F@KdLH@o2HLOH", port=3352)
    return db


# Pass in return value of connect_db as db
def sync_anthropometric_data(db):
    if not db:
        print("Unable to access database!")

    cursor = db.cursor()

    # Translate the mrn into kgid
    kgid = "KG0001"

    # todo Convert into using day ages instead of dates for HIPAA compliance. i.e. calculate the length of care rather
    # todo than storing the dates.

    # Drop all related data.
    # deletion_query = "DELETE FROM ANTHROPOMETRICS WHERE KGID='{}'".format(kgid)
    # cursor.execute(deletion_query)

    # Get all rows from spreadsheet

    data = SpreadSheetAccess.getAnthropometricsDataFrame("TeSt1")

    num_rows = data.shape[0]
    for i in range(0, num_rows):
        row = data.iloc[i]

        # Convert the MRN to KGID
        mrn = int(row["MRNumber"])
        kgid = get_kgid(mrn)

        collected_date = str(row["Date"].date())
        day_type = str(row["Day_Type"])
        src = str(row["Source"])

        query = "INSERT INTO ANTHROPOMETRICS (KGID, COLLECTED_DATE, DAY_TYPE, SRC, CP, PA, HT, WT, HC, UAC, TSF, SSF, USF, SISF, MBSF, UC, R, X, ENTERED_INIT, AUDITED_INIT, AUDITED_DATE, COMMENTS) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (
            kgid, collected_date, day_type, src, None, None, None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None)

        cursor.execute(query, values)
        db.commit()


def get_translation_table(path):
    df = pandas.read_excel(path)
    return df


def get_kgid(mrn):
    df = get_translation_table(r"Current Patients\\KGID_Translation_Test.xlsx")
    num_rows = df.shape[0]
    for i in range(0, num_rows):
        row = df.iloc[i]
        mrn_i = int(row["MRNUMBER"])
        if mrn_i == mrn:
            kgid = str(row["KGID"])
            return kgid


# This deidentifies spreadsheet data and syncs it to the mysql database.
def main():
    db = connect_db("mysql.conf")
    sync_anthropometric_data(db)


if __name__ == "__main__":
    main()
