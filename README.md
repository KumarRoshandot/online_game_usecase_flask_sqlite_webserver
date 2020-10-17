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
This view should give their lifecycle status for that month, and if the member has lapsed, it should show a rolling count of the number of months since they were last active.

Active means that the member has made a minimum of one real money wager in the month.

Each month a member has a certain lifecycle type. The member’s status will change on a monthly basis based on their previous and current month's activity. The statuses are:


    New		= First time they place a real money wager
    Retained	= Active in the prior calendar month and the current calendar month
    Unretained	= Active in the prior calendar month, but not active in the current calendar month
    Reactivated	= Not active in the prior calendar month, but active in the current calendar month
    Lapsed	= Not active in the prior calendar month or the current calendar month

### 3) Based on the REVENUE_ANALYSIS dataset above, build a RESTful web service that can be queried for:-

    •	the total win amount for a given member,
    •	the total wager amount for a given member, and
    •	the number of wagers placed by a given member.
  

#### Your solution should also meet the following requirements:
    •	All responses should be in JSON format.
    •	Each RESTful endpoint should accept an optional parameter for calculating the totals for a specific month, 
        and an optional parameter for a specific game type.
    •	The web service can be built using either Java or Python. 
        Ideally, we would like it to be provided with a build and dependency manager, such as Maven, 
        with all dependencies accessible through publicly available repositories. 
        Otherwise, please package all dependencies in your solution. Regardless of the option, 
        please provide instructions for building and deploying the application in a README.md file.
    •	You are not limited to any particular framework and 
        we don't expect any data to persist beyond the lifespan of the server.
    •	Where possible, you should write tests for the application.
