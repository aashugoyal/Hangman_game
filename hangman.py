import random
import string
word= 'blue green yellow black brown red'.split()
def chooseWord(word):
    return random.choice(word)
def isWordGuessed(secretWord, letterGuessed):
    """
       letterGuessed : the letter which we are guessing
       if all the letter which we are guessing is in secretWord
       then our function  return True otherwise False   
    """
    for x in range(len(secretWord)):
        counter=0
        if secretWord[x] in letterGuessed:
            counter+=1
        if counter == len(secretWord):
            return True
        else:
            return False
def getGuessedWord(secretWord, letterGuessed):
    '''
    if letter is correct then it is in the correct position
    '''
    value=''
    char=''
    for x in secretWord:
        if x in letterGuessed:
            value = x
        else:
            value='_'
        char=char+value
        return char
    '''
    currently working on it 
    12345678910
    '''
    
    

