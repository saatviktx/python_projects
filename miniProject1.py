# =============================================================
# 🐍 Python Fundamentals Assessment — Section 3: Mini Project
# =============================================================

# REQUIREMENTS CHECKLIST (cross off as you use them):
# [YES] Variables — store meaningful data in named variables
# [YES] Data types — use at least int, str, and bool naturally
# [YES] Input/Output — use input() and print()
# [YES] Type conversion — convert at least once e.g. int(input(...))
# [YES] String methods — at least one e.g. .strip() .upper() .lower()
# [YES] f-strings — format at least one print statement
# [YES] Conditionals — at least one if/elif/else block
# [YES] Lists — create and manipulate at least one list
# [ ] Loop — at least one for or while loop
# [YES] Function — define and call at least one function using def

# -------------------------------------------------------------
# IDEAS (pick one or come up with your own):
# - Simple quiz game
# - Basic calculator with a menu
# - Number guessing game
# - Shopping list manager
# - Student grade checker
# -------------------------------------------------------------

# RULES:
# - Flag anything you're unsure about with a comment
# - Think it through before you type
# - Have fun with it

# YOUR CODE BELOW:
def stmtPrint(blank):
    print(f'Here\'s your {blank} playlist: {playlist}')

playlist = []
stmtPrint('empty')

songChoose = bool(input('Would you like to add a song to your playlist (True/False)? '))

while songChoose == True:
    song1 = input('What song would you like to add? ').strip()
    playlist.append(song1)
    stmtPrint('updated')
    songChoose = bool(input('Would you like to add a song to your playlist (True/False)? '))
stmtPrint('final') #IM STUCK ON THIS. IM DONE FOR TODAY...

feedback = input('Would you like to leave feedback (Y/N)? ')
if feedback == 'Y' or feedback == 'y':
    pplFeedback = input('Enter feedback: ')
    print('Thanks for sharing! Have a great week ahead!')
else:
    print('Got it. Thanks for using our service!')

review = float(input('How would you rate this service from a scale of 1-5? '))
if review < 3:
    print('We\'re sorry for any issues caused...')
elif review > 3 and review <= 5:
    print('We appreciate your feedback! We\'re glad you liked our service!!!')
else:
    while review > 5:
        review = float(input('How would you rate this service from a scale of 1-5? '))
        if review <= 5:
            if review < 3:
                print('We\'re sorry for any issues caused...')
            elif review > 3 and review <= 5:
                print('We appreciate your feedback! We\'re glad you liked our service!!!')




