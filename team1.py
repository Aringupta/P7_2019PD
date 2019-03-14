####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'team1' # Only 10 chars displayed.
strategy_name = 'Change My Mind'
strategy_description = 'Collude until they betray, then betray'
    
def move(my_history, their_history, my_score, their_score):
    if 'b' in their_history:
        return 'b'
    else:
        return 'c'

