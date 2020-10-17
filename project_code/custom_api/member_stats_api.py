from flask import Flask, request, jsonify
import sqlite3
import os
import project_code.db_refresh.users_lifecycle_status_view_creation as gamesys_db_refresh

curr_path = os.getcwd()
db_path = os.path.join(os.path.split(curr_path)[0], "db_refresh", "db", "gamesys.db")

app = Flask(__name__)

@app.route('/gamesys',defaults={'stats_oper':'Invalid Operations ,  PLease Pass Valid Job Request'})
@app.route('/gamesys',methods=['GET'])
def get_stats():
    # Decide Wheather the main request is Valid or not
    list_of_valid_oper = ['total_win_amt','total_wager_amt','total_wager_count','refreshdb']
    stats_oper = [oper for oper in list_of_valid_oper if request.args.get('stats_oper',None) == oper]

    if len(stats_oper) == 0:
        return jsonify({'Response' : 'Invalid Operations ,  PLease Pass Valid Job Request'})

    if stats_oper[0].lower() == 'refreshdb':
        response = refresh_db_tables()
        return jsonify({'Response': response})

    # Check for Member Parameter
    if request.args.get('member_id',None) is None:
        return jsonify({'Response' : 'Member Value Not Specified, please specify member Id'})

    # Decide Optional Parameters
    member_id = request.args.get('member_id')
    game_id = request.args.get('game_id',None)
    x = 0
    for i in ['year', 'month']:
        x = x + 1 if request.args.get(i,None) is not None else x
    if x == 1:
        return jsonify({'Response' : 'PLease pass both Month and year combination e.g.. 2017 and January'})
    elif x == 2 :
        year_val = request.args.get('year')
        month_val = str(request.args.get('month')).capitalize()
    else:
        year_val = None
        month_val = None

    # Now Call Appropriate operations with appropriate column_name of table
    if stats_oper[0] == 'total_win_amt':
        response = get_total_operations('WIN_AMOUNT', member_id, year_val,month_val,game_id)
    elif stats_oper[0] == 'total_wager_amt':
        response = get_total_operations('WAGER_AMOUNT', member_id, year_val,month_val,game_id)
    else:
        response = get_total_operations('NUMBER_OF_WAGERS', member_id, year_val,month_val,game_id)

    return jsonify({'Response': response})


def get_total_operations(column_name, member_id, year=None, month=None, game_id=None):
    '''
    The SQL Query is Build Dynamically based on column_name passed , it will eventually call passed column name from table.
    Rest of the parameters are also used for dynamic sql query generation.
    '''

    if month is not None and game_id is not None:
        sql = '''
        with cal_month as 
        (
        select distinct CALENDAR_YEAR_MONTH from calendar where CALENDAR_YEAR = {} and CALENDAR_MONTH_NAME = '{}'
        )
        select 
        sum({}) AS TOTAL_{}
        from  
        revenue_analysis rev join cal_month cal on 
        rev.ACTIVITY_YEAR_MONTH = cal.CALENDAR_YEAR_MONTH
        where member_id = {}
        and GAME_ID = {}
        '''.format(year, month, column_name, column_name, member_id, game_id)
    elif month is not None and game_id is None:
        sql = '''
        with cal_month as 
        (
        select distinct CALENDAR_YEAR_MONTH from calendar where CALENDAR_YEAR = {} and CALENDAR_MONTH_NAME = '{}'
        )
        select 
        sum({}) AS TOTAL_{} 
        from  
        revenue_analysis rev join cal_month cal on 
        rev.ACTIVITY_YEAR_MONTH = cal.CALENDAR_YEAR_MONTH
        where member_id = {}
        '''.format(year, month, column_name, column_name, member_id)
    elif game_id is not None and month is None:
        sql = '''
        select 
        sum({}) AS TOTAL_{} 
        from  
        revenue_analysis
        where member_id = {}
        and GAME_ID = {}
        '''.format(column_name, column_name, member_id, game_id)
    else:
        sql = '''
        select 
        sum({}) AS TOTAL_{} 
        from  
        revenue_analysis
        where member_id = {}
        '''.format(column_name, column_name, member_id)
    print(sql)
    cur.execute(sql)
    rows = cur.fetchall()
    return rows


# This right here will refresh the Content of CSV Files present with its corresponding table present in database
def refresh_db_tables():
    try:
        conn_new = gamesys_db_refresh.create_db_tables(database=db_path)
        if conn_new:
            response = gamesys_db_refresh.load_csv_to_db_tables(conn_new)
            return response
        else:
            return 'No Connection Established with database'

    except Exception as e:
        print('Error:-', str(e))
        return 'Error :- ' + str(e)


if __name__ == '__main__':
    conn = sqlite3.connect(db_path,check_same_thread=False)
    cur = conn.cursor()
    app.run(debug=True)

