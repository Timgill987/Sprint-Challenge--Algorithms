'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    #Must not contain loops
    #must only run a comparison once through the string
    #must ignore capital letters
        #if word startswith('th')
            #count +=1
        #return count
    count = 0
    if len(word) < 2:
        return count
    elif word.startswith('th'):
        count += 1
    return count + count_th(word[1:])
