import mysql.connector


def connect_db(conf_path):
    db = mysql.connector.connect(option_files=conf_path)
    return db


# Pass in return value of connect_db as db
def save_anthropometric_data(db, mrn, collected_date, day_type, src, cp=None, pa=None, ht=None, wt=None, hc=None, uac=None, tsf=None, ssf=None, usf=None, sisf=None, mbsf=None, uc=None, r=None, x=None, entered_init=None, audited_init=None, audited_date=None, comments=None):
    if not db:
        print("Unable to access database!")

    cursor = db.cursor()
    query = "INSERT INTO ANTHROPOMETRICS (MRN, COLLECTED_DATE, DAY_TYPE, SRC, CP, PA, HT, WT, HC, UAC, TSF, SSF, USF, SISF, MBSF, UC, R, X, ENTERED_INIT, AUDITED_INIT, AUDITED_DATE, COMMENTS) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (mrn, collected_date, day_type, src, cp, pa, ht, wt, hc, uac, tsf, ssf, usf, sisf, mbsf, uc, r, x, entered_init, audited_init, audited_date, comments)
    cursor.execute(query, values)
    db.commit()


# test the db connection by writing dummy data to the anthro table.
def main():
    db = connect_db("mysql.conf")
    save_anthropometric_data(db, 10, "2000-03-11", 3, 4, wt=6)


if __name__ == "__main__":
    main()

