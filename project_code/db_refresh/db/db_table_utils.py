import sqlite3
from sqlite3 import Error


def create_connection(db_file,timeout=5):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    x = timeout
    try:
        conn = sqlite3.connect(db_file,timeout=x)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def drop_table(conn, db_table):
    """ drop a table of mentioned schema and table from db_table
    :param conn: Connection object
    :param db_table: db_name.table_name or simply table_name
    :return:
    """
    try:
        c = conn.cursor()
        c.execute("""DROP TABLE IF EXISTS {}""".format(db_table))
    except Error as e:
        print(e)


def create_db_tables(database = "db/gamesys.db"):

    sql_create_revenue_analysis_table = """ CREATE TABLE REVENUE_ANALYSIS
                                ( ACTIVITY_DATE DATE NOT NULL,
                                  MEMBER_ID INTEGER NOT NULL,
                                  GAME_ID SMALLINT NOT NULL,
                                  WAGER_AMOUNT REAL NOT NULL,
                                  NUMBER_OF_WAGERS INTEGER NOT NULL,
                                  WIN_AMOUNT REAL NOT NULL,
                                  ACTIVITY_YEAR_MONTH INTEGER NOT NULL,
                                  BANK_TYPE_ID SMALLINT DEFAULT 0 NOT NULL
                                  ) """

    sql_create_calendar_table = """CREATE TABLE CALENDAR 
                                ( CALENDAR_DATE DATE NOT NULL,
                                  CALENDAR_YEAR INTEGER NOT NULL,
                                  CALENDAR_MONTH_NUMBER INTEGER NOT NULL,
                                  CALENDAR_MONTH_NAME VARCHAR(100),
                                  CALENDAR_DAY_OF_MONTH INTEGER NOT NULL,
                                  CALENDAR_DAY_OF_WEEK  INTEGER NOT NULL,
                                  CALENDAR_DAY_NAME VARCHAR(100),
                                  CALENDAR_YEAR_MONTH INTEGER NOT NULL 
                                  )"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # drop if exists tables
        drop_table(conn, 'REVENUE_ANALYSIS')
        drop_table(conn, 'CALENDAR')

        # create projects table
        create_table(conn, sql_create_revenue_analysis_table)

        # create tasks table
        create_table(conn, sql_create_calendar_table)
    else:
        print("Error! cannot create the database connection.")
    return conn

