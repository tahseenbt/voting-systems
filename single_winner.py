# Name: Tahseen Bin Taj

from a3_helpers import *


def count_plurality(ballots):
    '''
    (list) -> (dict)
    Given a list containing candidates, the count for each candidate is returned in a dictionary
    >>> count_plurality(['LIBERAL', 'LIBERAL', 'NDP', 'LIBERAL'])
    {'LIBERAL': 3, 'NDP': 1}
    >>> count_plurality([])
    {}
    '''
    candidates = get_all_candidates(ballots)
    votes = {}
    for candidate in candidates:
        votes[candidate] = ballots.count(candidate)
    return votes

def count_approval(ballots):
    '''
    (list) -> (dict)
    Given a nested list containing candidates, return the votes each candidate got.
    >>> count_approval([ ['LIBERAL', 'NDP'], ['NDP'], ['NDP', 'GREEN', 'BLOC']] )
    {'LIBERAL': 1, 'NDP': 3, 'GREEN': 1, 'BLOC': 1}
    >>> count_approval([])
    {}
    '''
    flattened_ballots = flatten_lists(ballots)
    candidates = get_all_candidates(flattened_ballots)
    votes = {}
    for candidate in candidates:
        votes[candidate] = flattened_ballots.count(candidate)
    return votes

def count_rated(ballots):
    '''
    (list) -> (dict)
    Given a list of rated ballots, the sum of the scores of each candidate is returned.
    >>> count_rated([{'LIBERAL':5, 'NDP':2}, {'NDP':4, 'GREEN':5}])
    {'LIBERAL': 5, 'NDP': 6, 'GREEN': 5}
    >>> count_rated([])
    {}
    '''
    if len(ballots) != 0:
        total = ballots[0]
        for i in range(1,len(ballots)):
            total = add_dicts(total, ballots[i])
        return total
    return {}

def count_first_choices(ballots):
    '''
    (list) -> (dict)
    Given a nested ordered list in ascending priority, a dictionary is returned with the\
    winners of first choice.
    >>> pr_dict(count_first_choices([['NDP', 'LIBERAL'], ['GREEN', 'NDP'], ['NDP', 'BLOC']]))
    {'BLOC': 0, 'GREEN': 1, 'LIBERAL': 0, 'NDP': 2}
    >>> pr_dict(count_first_choices([[], ['NDP', 'LIBERAL'], ['GREEN', 'NDP'], ['NDP', 'BLOC']]))
    {'BLOC': 0, 'GREEN': 1, 'LIBERAL': 0, 'NDP': 2}
    >>> count_first_choices([])
    {}
    '''
    candidates = get_all_candidates(ballots)
    winners = []
    votes = {}
    for ballot in ballots:
        if len(ballot) != 0:
            winners.append(ballot[0])
    for candidate in candidates:
        votes[candidate] = winners.count(candidate)
    return votes


if __name__ == '__main__':
    doctest.testmod()
