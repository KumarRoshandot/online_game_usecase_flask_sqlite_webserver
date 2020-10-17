# Instructions for API URL for Members Stats
http://hostname:port/gamesys/

### List of Parameters
    •	stats_oper (Possible Values are  ['total_win_amt','total_wager_amt','total_wager_count','refreshdb'] )
                      1) refreshdb :- This  will just load both Input CSV Files to its respective table as overwrite.
                      2) total_win_amt :- sum(WIN_AMOUNT)
                      3) total_wager_amt :- sum(WAGER_AMOUNT)
                      4) total_wager_count :- sum(NUMBER_OF_WAGERS)
                      
    •	member_id (Mandatory column value to be provided)
    •	game_id (Optional)
    •	month (Optional, but goes in combination with year parameter)
    •	year (Optional, but goes in combination with month parameter)


  #### Refresh Database tables , Load attached CSV files to its tables
    http://hostname:port/gamesys?stats_oper=refreshdb
    
  #### The total win amount for a given member
    •	http://hostname:port/gamesys?stats_oper=total_win_amt&member_id=1001
    •	http://hostname:port/gamesys?stats_oper=total_win_amt&member_id=1001&game_id=7499
    •	http://hostname:port/gamesys?stats_oper=total_win_amt&member_id=1001&year=2017&month=APRIL
    •	http://hostname:port/gamesys?stats_oper=total_win_amt&member_id=1001&year=2017&month=APRIL&game_id=7588
    
#### The total wager amount for a given member
    •	http://hostname:port/gamesys?stats_oper=total_wager_amt&member_id=1001
    •	http://hostname:port/gamesys?stats_oper=total_wager_amt&member_id=1001&game_id=7499
    •	http://hostname:port/gamesys?stats_oper=total_wager_amt&member_id=1001&year=2017&month=APRIL
    •	http://hostname:port/gamesys?stats_oper=total_wager_amt&member_id=1001&year=2017&month=APRIL&game_id=7588
    
#### The total wager count for a given member
    •	http://hostname:port/gamesys?stats_oper=total_wager_count&member_id=1001
    •	http://hostname:port/gamesys?stats_oper=total_wager_count&member_id=1001&game_id=7499
    •	http://hostname:port/gamesys?stats_oper=total_wager_count&member_id=1001&year=2017&month=APRIL
    •	http://hostname:port/gamesys?stats_oper=total_wager_count&member_id=1001&year=2017&month=APRIL&game_id=7588    
