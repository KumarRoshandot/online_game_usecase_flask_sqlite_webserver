from gamesys.db_refresh.db_table_utils import *
import csv
import os

csv_path = os.path.join(os.path.split(os.getcwd())[0], "db_refresh")

revenue_analysis_csv = os.path.join(csv_path, 'db','DB_Setup','Revenue_Analysis_Test_Data.csv')
calender_csv = os.path.join(csv_path, 'db','DB_Setup','Calendar_Test_Data.csv')


def load_csv_to_db_tables(conn):
    try:
        curs = conn.cursor()
        print(revenue_analysis_csv)
        print(calender_csv)
        # This is Loading of revenue_analysis csv file  to REVENUE_ANALYSIS table
        reader = csv.reader(open(revenue_analysis_csv, 'r'), delimiter=',')
        next(reader, None)  # skip the headers
        for row in reader:
            # print(row)
            to_db = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
            curs.execute("INSERT INTO REVENUE_ANALYSIS "
                         "(ACTIVITY_DATE,MEMBER_ID,GAME_ID,WAGER_AMOUNT,NUMBER_OF_WAGERS,WIN_AMOUNT,ACTIVITY_YEAR_MONTH,BANK_TYPE_ID) "
                         "VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db)

        # This is Loading of calendar csv file  to CALENDAR table
        reader = csv.reader(open(calender_csv, 'r'), delimiter=',')
        next(reader, None)  # skip the headers
        for row in reader:
            # print(row)
            to_db = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
            curs.execute("INSERT INTO CALENDAR "
                         "(CALENDAR_DATE,CALENDAR_YEAR,CALENDAR_MONTH_NUMBER,CALENDAR_MONTH_NAME,CALENDAR_DAY_OF_MONTH,CALENDAR_DAY_OF_WEEK,CALENDAR_DAY_NAME,CALENDAR_YEAR_MONTH)"
                         " VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db)

        conn.commit()

        curs.close()
        conn.close()
        print('DATABASE TABLE REFRESHED')
        return 'DATABASE TABLE REFRESHED'
    except Exception as e:
        print('EXCEPTION OCCURED :- ' + str(e))
        return 'EXCEPTION OCCURED :- ' + str(e)


'''
if __name__ == "__main__":
    # get connection to db
    try:
        conn = create_db_tables()
        load_csv_to_db_tables(conn)
        conn.commit()

    except Exception as e:
        print(e)
'''

