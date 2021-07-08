import pandas as pd
from difflib import ndiff

def lev_dis(str_1, str_2):
    """
        The Levenshtein distance is a string metric for measuring the difference between two sequences.
        It is calculated as the minimum number of single-character edits necessary to transform one string into another
    """
    distance = 0
    buffer_removed = buffer_added = 0
    for x in ndiff(str_1, str_2):
        code = x[0]
        # Code ? is ignored as it does not translate to any modification
        if code == ' ':
            distance += max(buffer_removed, buffer_added)
            buffer_removed = buffer_added = 0
        elif code == '-':
            buffer_removed += 1
        elif code == '+':
            buffer_added += 1
    distance += max(buffer_removed, buffer_added)
    return distance


if __name__=='__main__':
    data=pd.read_csv('20210103_hundenamen.csv')['HUNDENAME']
    final=[]
    for i in data:
    	if lev_dis("Luca",i)==1:
    		if i not in final:
    			final.append(i)
    
    print(final)

