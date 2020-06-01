# Name: Tahseen Bin Taj

from single_winner import *

################################################################################

def votes_needed_to_win(ballots, num_winners):
    '''
    (list), (int) -> (int)
    Given a list of ballots, return the number of votes needed to win.
    >>> votes_needed_to_win([{'CPC':3, 'NDP':5}, {'NDP':2, 'CPC':4}, {'CPC':3, 'NDP':5}], 1)
    2
    >>> votes_needed_to_win(['g']*20, 2)
    7
    '''
    return (int(len(ballots)/(num_winners+1))+1)

def has_votes_needed(result, votes_needed):
    '''
    (dict), (int) -> (bool)
    Checks whether the given result has a candidate with the required votes.
    >>> has_votes_needed({'NDP': 4, 'LIBERAL': 3}, 4)
    True
    >>> has_votes_needed({}, 2)
    False
    >>> has_votes_needed({'NDP': 5, 'LIBERAL': 3}, 4)
    True
    '''
    votes = result.values()
    for vote in votes:
        if vote >= votes_needed:
            return True
    return False

################################################################################


def eliminate_candidate(ballots, to_eliminate):
    '''
    (list), (list) -> (list)
    Given a list and another which contains the candidates to eliminate, a new list excluding them is returned.
    >>> l1 = [['NDP', 'LIBERAL'], ['GREEN', 'NDP'], ['NDP', 'BLOC']]
    >>> l2 = ['NDP', 'LIBERAL']
    >>> eliminate_candidate(l1, l2)
    [[], ['GREEN'], ['BLOC']]
    >>> l1
    [['NDP', 'LIBERAL'], ['GREEN', 'NDP'], ['NDP', 'BLOC']]
    >>> l2
    ['NDP', 'LIBERAL']
    >>> eliminate_candidate([],[])
    []
    '''
    ret = []
    for ballot in ballots:
        temp_list = []
        for candidate in ballot:
            if candidate not in to_eliminate:
                temp_list.append(candidate)
        ret.append(temp_list)
    return ret

################################################################################


def count_irv(ballots):
    '''
    (list) -> (dict)
    Given a list of ballots, the result of the votes is given as per counting the irv.
    >>> pr_dict(count_irv([['NDP'], ['GREEN', 'NDP', 'BLOC'], ['LIBERAL','NDP'], ['LIBERAL'], ['NDP', 'GREEN'], ['BLOC', 'GREEN', 'NDP'], ['BLOC', 'CPC'], ['LIBERAL', 'GREEN'], ['NDP']]))
    {'BLOC': 0, 'CPC': 0, 'GREEN': 0, 'LIBERAL': 3, 'NDP': 5}
    >>> count_irv([])
    {}
    '''
    if len(ballots) != 0:
        new_ballots = ballots
        raw = count_first_choices(ballots)
        votes_needed = (votes_needed_to_win(ballots, 1))
        has_votes = (has_votes_needed(raw, votes_needed))
        while not has_votes:
            new_ballots = eliminate_candidate(new_ballots, last_place(raw))
            raw = count_first_choices(new_ballots)
            has_votes = (has_votes_needed(raw, votes_needed))
        for key in get_all_candidates(ballots):
            if key not in raw:
                raw[key] = 0
        return raw
    return {}

################################################################################

if __name__ == '__main__':
    doctest.testmod()
