# The Minion Game : Kevin and Stuart want to play the 'The Minion Game'.
# Game Rules:
''' Both players are given the same string, S.  Both players have to make substrings using the letters of the string S.
    Stuart has to make words starting with consonants.  Kevin has to make words starting with vowels. 
    The game ends when both players have made all possible substrings. '''
# Scoring
''' A player gets +1 point for each occurrence of the substring in the string S.    '''
# For Example:
''' String = BANANA
    Kevin's vowel beginning word = ANA
    Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.   '''
    # Kevin                     Stuart
'''    A        3                   B       1
       AN       2                   N       2
       ANA      2                   BA      1
       ANAN     1                   NA      2
       ANANA    1                   BAN     1
                                    NAN     1
                                    BANA    1 
                                    NANA    1
                                    BANAN   1
                                    BANANA  1   '''
# Input
''' BANANA  '''
# Output
''' Stuart 12   '''


def minion_game(string):
    # consonants = list
    vowels = 'AEIOU'
    StuartScore = 0
    KevinScore = 0
    for i in range(len(string)):
        if string[i] in vowels:
            KevinScore += len(string)-i
        else:
            StuartScore += len(string)-i
            
    if KevinScore > StuartScore:
        print('Kevin', KevinScore)
    elif KevinScore < StuartScore:
        print('Stuart', StuartScore)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)