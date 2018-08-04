animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
 
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
 
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
 
    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    List = aDict.values()
    NUM = 0
    for n in List:
        NUM += len(n)
    return NUM
print(how_many(animals))