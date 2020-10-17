# game_customer_monthly_status
customer Status who play games online with wager money ( python + sqlite + flask )


## Use case
### 1) Two Tables (REVENUE_ANALYSIS &  CALENDAR)
### 2) One View The required solution is a view with the following columns:-

          MEMBER_ID,
          CALENDAR_YEAR_MONTH,
          MEMBER_LIFECYCLE_STATUS,
          LAPSED_MONTHS

The view should display one row per member per month, starting from the month in which they first placed a real money wager. 
This view should give their lifecycle status for that month, and if the member has lapsed, 
it should show a rolling count of the number of months since they were last active.

Active means that the member has made a minimum of one real money wager in the month.

Each month a member has a certain lifecycle type. The member’s status will change on a monthly basis based on their previous and current month's activity. 
The statuses are:


    New		= First time they place a real money wager
    Retained	= Active in the prior calendar month and the current calendar month
    Unretained	= Active in the prior calendar month, but not active in the current calendar month
    Reactivated	= Not active in the prior calendar month, but active in the current calendar month
    Lapsed	= Not active in the prior calendar month or the current calendar month

### 3) Based on the REVENUE_ANALYSIS dataset above, build a RESTful web service that can be queried for:-

    •	the total win amount for a given member,
    •	the total wager amount for a given member, and
    •	the number of wagers placed by a given member.
  

## Setup before u  do anything :-

	1) I have worked it using pycharm tool and on windows machine.
		--> Install Python (better 3+)
		--> Pip install Flask
	2) Download this project ZIP and Extract till 'project_code' folder to one location (for e.g..  c:\project_code)
	
	3) Under this folder you  will see follwing  structure ,this is how u extract and keep it
	   ├── project_code
	         ├── custom_api
	         │    ├── __init__.py
	         │    └── member_stats_api.py
	         ├── db_refresh
	         │     ├── db
	         │     │   ├──gamesys.db
             ├     │	     └──DB_Setup
	         │     │		├──Calendar_Test_Data.csv
	         │     │                └──Revenue_Analysis_Test_Data.csv
	         ├     ├── __init__.py
	         │     ├── users_lifecycle_status_view_creation.py
	         │     └── db_table_utils.py
             │
	         └── __init__.py
	
	4) Sub folder (db_refresh):-
		a) users_lifecycle_status_view_creation.py 
			--> This Program Just Load CSV FILES to its tables as overwrite
			--> Database information is  next
		
		b) db_table_utils.py
			--> This  is a place  where i have defined database tables creation , drop , making an 
			     connection and other stuff.
			--> Here i have used SQLITE database , since its so cool , handy and so much light  which can 
			    easily be integrated in this  usecase.
			--> So what i have  done is i have created a Database 'gamesys.db' which is present in its 
			    sub folder 'db'.
			--> Within this database i have made 2 tables , 
			     one is REVENUE_ANALYSIS and other is CALENDAR
	
	4) Sub folder (custom_api):-
		a) member_stats_api.py
			--> Place  where i have  build an APP using Flask Library.
			--> In Here get_stats() function will decide what kind of request is been asked from API, 
                                   It will Prepare the request parameters to appropiate SQL Query which is dynamically generated based on parameters.
		
	
### TO  Run  the Webserver APP :-
	1) python member_stats_api.py 
    --> Once its running, go  to  browser and use the mentioned API to  get required data
    --> Refer file "game_customer_monthly_status/Solution/RESTful_Web_Service/README.md" for API information
		
	
