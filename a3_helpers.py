# Name: Tahseen Bin Taj

import doctest
import random

def flatten_lists(nested):
    '''
    (list) -> (list)
    A nested list is converted to a single list.
    >>> flatten_lists([[0], [1,2], 3])
    [0, 1, 2, 3]
    >>> flatten_lists([[0], [1,2], [3]])
    [0, 1, 2, 3]
    >>> nested = [[0,1], [1,2,3], [3]]
    >>> flatten_lists(nested)
    [0, 1, 1, 2, 3, 3]
    >>> nested
    [[0, 1], [1, 2, 3], [3]]
    '''
    ret = []
    for element in nested:
        if type(element) == list:
            for value in element:
                ret.append(value)
        else:
            ret.append(element)
    return ret

def flatten_dict(d):
    '''
    (dict) -> (list)
    A dictionary is converted to list containing the keys repeated by the value
    >>> flatten_dict({'LIBERAL': 5, 'NDP': 2})
    ['LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'NDP', 'NDP']
    >>> d = {'LIBERAL': 2, 'NDP': 1}
    >>> flatten_dict(d)
    ['LIBERAL', 'LIBERAL', 'NDP']
    >>> d
    {'LIBERAL': 2, 'NDP': 1}
    >>> flatten_dict({'LIBERAL': 0, 'NDP': 0})
    []
    '''
    ret = []
    for key in d:
        for i in range(d[key]):
            ret.append(key)
    return ret

def add_dicts(d1, d2):
    '''
    (dict), (dict) -> (dict)
    Returns a new dictionary with the sum of input dictionaries.
    >>> add_dicts({'a': 5, 'b': 2, 'd': -1}, {'a': 7, 'b': 1, 'c': 5})
    {'a': 12, 'b': 3, 'd': -1, 'c': 5}
    >>> a = {'a': 2, 'c': 1, 'b': 5}
    >>> b = {'b': 2, 'c': 6, 'd': 7}
    >>> add_dicts(a, b)
    {'a': 2, 'c': 7, 'b': 7, 'd': 7}
    >>> a
    {'a': 2, 'c': 1, 'b': 5}
    >>> b
    {'b': 2, 'c': 6, 'd': 7}
    >>> add_dicts({'a': 1}, {'b': 2, 'c': 3, 'd': 4, 'e': 5})
    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    '''
    new_dict = {}
    for key in d1:
        new_dict[key] = d1[key]
    for key in d2:
        if key in new_dict:
            new_dict[key] += d2[key]
        else:
            new_dict[key] = d2[key]
    return new_dict

def get_all_candidates(ballots):
    '''
    (list) -> (list)
    >>> get_all_candidates([{'GREEN':3, 'NDP':5}, {'NDP':2, 'LIBERAL':4}, ['CPC', 'NDP'], 'BLOC'])
    ['GREEN', 'NDP', 'LIBERAL', 'CPC', 'BLOC']
    >>> get_all_candidates([['GREEN', 'NDP'], ['NDP', 'LIBERAL'], ['CPC', 'NDP'], 'BLOC'])
    ['GREEN', 'NDP', 'LIBERAL', 'CPC', 'BLOC']
    >>> get_all_candidates(['GREEN', 'NDP', 'NDP', 'LIBERAL', 'CPC', 'NDP', 'BLOC'])
    ['GREEN', 'NDP', 'LIBERAL', 'CPC', 'BLOC']
    '''
    ret = []
    for i,c in enumerate(ballots):
        if type(c) == dict:
	        ballots[i] = flatten_dict(c)
    ballots = flatten_lists(ballots)
    for ballot in ballots:
        if ballot not in ret:
            ret.append(ballot)
    return ret
###################################################### winner/loser

def get_candidate_by_place(result, func):
    '''
    (dict), (function) -> (str)
    Given a dictionary and a function, the function is applied to the dictionary and returns the key.
    >>> result = {'LIBERAL':4, 'NDP':5, 'CPC':6, 'GREEN':7}
    >>> get_candidate_by_place(result, max)
    'GREEN'
    >>> result = {'LIBERAL':4, 'NDP':6, 'CPC':6, 'GREEN':4}
    >>> random.seed(0)
    >>> get_candidate_by_place(result, min)
    'GREEN'
    >>> random.seed(1)
    >>> get_candidate_by_place(result, min)
    'LIBERAL'
    >>> get_candidate_by_place({}, max)
    ''
    '''
    if len(result) != 0 :
        output = func(result.values())
        ret = []
        for key in result:
            if result[key] == output:
                ret.append(key)
        return ret[random.randint(0,len(ret)-1)]
    else:
        return ''


def get_winner(result):
    '''
    (dict) -> (str)
    This function returns the key with the highest value. In case of a tie, it's broken randomly.
    >>> get_winner({'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 0})
    'NDP'
    >>> get_winner({'NDP': 2})
    'NDP'
    >>> get_winner({'NDP': 3, 'GREEN': 4, 'LIBERAL': 0, 'BLOC': 0})
    'GREEN'
    '''
    return get_candidate_by_place(result, max)

def last_place(result):
    '''
    (dict) -> (str)
    This function returns the key with the lowest value. In case of a tie, it's broken randomly.
    >>> last_place({'NDP': 2, 'GREEN': 1, 'LIBERAL': 1, 'BLOC': 0})
    'BLOC'
    >>> random.seed(0)
    >>> last_place({'LIBERAL':4, 'NDP':6, 'CPC':6, 'GREEN':4})
    'GREEN'
    >>> random.seed(1)
    >>> last_place({'LIBERAL':4, 'NDP':6, 'CPC':6, 'GREEN':4})
    'LIBERAL'
    '''
    return get_candidate_by_place(result, min)

###################################################### testing help

def pr_dict(d):
    '''(dict) -> None
    Print d in a consistent fashion (sorted by key).
    Provided to students. Do not edit.
    >>> pr_dict({'a':1, 'b':2, 'c':3})
    {'a': 1, 'b': 2, 'c': 3}
    '''
    l = []
    for k in sorted(d):
        l.append( "'" + k + "'" + ": " + str(d[k]) )
    print('{' + ", ".join(l) + '}')


if __name__ == '__main__':
    doctest.testmod()
