# -*- coding: utf-8 -*-
from workflow import Workflow3 # Alfred-Workflow: https://www.deanishe.net/alfred-workflow/index.html
import sys

def main(wf):
    try:
        query = wf.args[0]
        
        subtitle_vertical = "Press 'Enter' and copy to clipboard vertically"
        result_str_v = sequential_strings_creator(query, '\n')
        wf.add_item(title=result_str_v, subtitle=subtitle_vertical, arg=result_str_v, valid=True)   
                
        subtitle = "Press 'Enter' and copy to clipboard horizontally"
        result_str_h = sequential_strings_creator(query, ' ')
        wf.add_item(title=result_str_h, subtitle=subtitle, arg=result_str_h, valid=True)
        
    except:
        wf.add_item("Invalid input. format: strings {number-number} strings")
    
    wf.send_feedback() 
    
def sequential_strings_creator(query, join_string):
    """
    This function generates a series of sequential strings 
    It supports the sequence of either integer or one-digit float
    
    :param query: input from alfred workflow input, expects curly braces work as discriminators 
    :type query: string
    :param join_string: string that seperates the sequentail strings
    :type join_string: string
    
    :rtype result: string
    """
    str_before_num = query[:query.index('{')]
    str_after_num = query[query.index('}')+1:]
    num_range = query[query.index('{')+1 : query.index('}')]
    open_num = num_range[:num_range.index('-')]
    close_num = num_range[num_range.index('-')+1:]
    
    if isint(open_num) & isint(close_num):
        num_list = range(int(open_num), int(close_num)+1, 1)
    elif isfloat(open_num) & isfloat(close_num):
        # don't use numpy.arange here: favors other users who don't have numpy package
        num_list = [0.1 * x for x in range(int(float(open_num)*10), int(float(close_num)*10)+1, 1)]
        num_list = [round(i,1) for i in num_list] # prevent numerical precision problem 
    else:
        raise Exception
    
    result_list = [str_before_num + str(i) + str_after_num for i in num_list]
    result =  join_string.join(result_list)
    
    return result

def isfloat(x):
    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True

def isint(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b

if __name__ == '__main__':
    wf = Workflow3() # create a workflow3 boject
    sys.exit(wf.run(main)) # run