# Name: Tahseen Bin Taj

from instant_run_off import *

################################################################################

def irv_to_stv_ballot(ballots, num_winners):
    '''
    (list), (int) -> (list)
    Replace each party in ranked ballots by the num_winners number of candidates.
    >>> irv_to_stv_ballot([['NDP', 'CPC'], ['GREEN']], 3)
    [['NDP0', 'NDP1', 'NDP2', 'CPC0', 'CPC1', 'CPC2'], ['GREEN0', 'GREEN1', 'GREEN2']]
    >>> irv_to_stv_ballot([],3)
    []
    '''
    new_ballots = []
    for ballot in ballots:
        temp = []
        for index in range(len(ballot)):
            for i in range(num_winners):
                temp.append(ballot[index]+str(i))
        new_ballots.append(temp)
    return new_ballots

################################################################################


def eliminate_n_ballots_for(ballots, to_eliminate, n):
    '''(lst, str) -> lst
    Remove n of the ballots in ballots where the first choice is for the candidate to_eliminate.

    Provided to students. Do not edit.

    >>> ballots = [['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'GREEN2', 'GREEN3'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['GREEN1'], 1)
    [['GREEN1', 'GREEN2', 'GREEN3'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['GREEN1'], 2)
    [['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['NDP3'], 2)
    [['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['NDP3'], 1)
    [['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'GREEN2', 'GREEN3'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['NDP3', 'GREEN1'], 5)
    [['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> b = [['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3']]
    >>> eliminate_n_ballots_for(b, ['GREEN1'], 2)
    [['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3']]
    '''
    quota = n
    new_ballots = []
    elims = 0
    for i,b in enumerate(ballots):
        if (elims >= quota) or  (len(b) > 0 and b[0] not in to_eliminate):
            new_ballots.append(b)
        else:
            elims += 1
    return new_ballots



def stv_vote_results(ballots, num_winners):
    '''(lst of list, int) -> dict

    From the ballots, elect num_winners many candidates using Single-Transferable Vote
    with Droop Quota. Return how many votes each candidate has at the end of all transfers.
    
    Provided to students. Do not edit.

    >>> random.seed(3) # make the random tie-break consistent
    >>> g = ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1']
    >>> n = ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3']
    >>> pr_dict(stv_vote_results([g]*5 + [n]*3, 4))
    {'BLOC1': 0, 'GREEN1': 2, 'GREEN2': 2, 'GREEN3': 0, 'NDP1': 2, 'NDP2': 2, 'NDP3': 0}
    >>> random.seed(1)
    >>> pr_dict(stv_vote_results([g]*5 + [n]*3, 4))
    {'BLOC1': 0, 'GREEN1': 2, 'GREEN2': 2, 'GREEN3': 0, 'NDP1': 2, 'NDP2': 0, 'NDP3': 0}
    >>> green = ['GREEN', 'NDP', 'BLOC', 'LIBERAL', 'CPC']
    >>> ndp = ['NDP', 'GREEN', 'BLOC', 'LIBERAL', 'CPC']
    >>> liberal = ['LIBERAL', 'CPC', 'GREEN', 'NDP', 'BLOC']
    >>> cpc = ['CPC', 'NDP', 'LIBERAL', 'BLOC', 'GREEN']
    >>> bloc = ['BLOC', 'NDP', 'GREEN', 'CPC', 'LIBERAL']
    >>> pr_dict(stv_vote_results([green]*10 + [ndp]*20 + [liberal]*15 + [cpc]*30 + [bloc]*25, 2))
    {'BLOC': 32, 'CPC': 34, 'GREEN': 0, 'LIBERAL': 0, 'NDP': 34}
    >>> pr_dict(stv_vote_results([green]*10 + [ndp]*20 + [liberal]*15 + [cpc]*30 + [bloc]*25, 3))
    {'BLOC': 26, 'CPC': 26, 'GREEN': 0, 'LIBERAL': 22, 'NDP': 26}
    '''
    quota = votes_needed_to_win(ballots, num_winners)

    to_eliminate = []
    result = {}
    final_result = {}

    for i in range(num_winners):
        # start off with quasi-IRV

        result = count_first_choices(ballots)

        while (not has_votes_needed(result, quota)) and len(result) > 0:
            to_eliminate.append( last_place(result) ) 
            ballots = eliminate_candidate(ballots, to_eliminate)
            result = count_first_choices(ballots)

        # but now with the winner, reallocate ballots above quota and keep going
        winner = get_winner(result)
        if winner:
            final_result[winner] = quota # winner only needs quota many votes
            ballots = eliminate_n_ballots_for(ballots, final_result.keys(), quota)
            ballots = eliminate_candidate(ballots, final_result.keys())
            result = count_first_choices(ballots)

    # remember the candidates we eliminated, their count should be 0
    for candidate in to_eliminate:
        final_result[candidate] = 0
    final_result.update(result)
    return final_result


################################################################################


def count_stv(ballots, num_winners):
    '''
    (list), (int) -> (dict)
    Returns how many candidates from each party won the election.
    >>> random.seed(3) # make the random tie-break consistent
    >>> g = ['GREEN', 'NDP', 'BLOC']
    >>> n = ['NDP', 'GREEN', 'BLOC']
    >>> pr_dict(count_stv([g]*5 + [n]*3, 4))
    {'BLOC': 0, 'GREEN': 3, 'NDP': 1}
    >>> count_stv([],4)
    {}
    '''
    parties = get_all_candidates(ballots)
    ret = {}
    converted_to_stv = irv_to_stv_ballot(ballots, num_winners)
    results = stv_vote_results(converted_to_stv, num_winners)
    quota = votes_needed_to_win(ballots, num_winners)
    for party in parties:
        ret[party] = 0
        for key in results:
            if party in key and results[key] == quota:
                ret[party] += 1
    return ret

################################################################################


def count_SL(results, num_winners):
    '''
    (list), (int) -> (dict)
    Given a list of plurality votes result and the number of winners, how many seats are won by \
    each party is returned
    >>> results = ['A']*100000 + ['B']*80000 + ['C']*30000 + ['D']*20000
    >>> pr_dict(count_SL(results, 8))
    {'A': 3, 'B': 3, 'C': 1, 'D': 1}
    >>> count_SL([], 3)
    {}
    '''
    if len(results) != 0:
        count = count_plurality(results)
        quotient = count_plurality(results)
        seats = {}
        for party in get_all_candidates(results):
            seats[party] = 0
        while sum(seats.values()) != num_winners:
            winner = get_winner(quotient)
            seats[winner] += 1
            quotient[winner] = count[winner]/(2*seats[winner]+1)
        return seats
    return {}
################################################################################


if __name__ == '__main__':
    doctest.testmod()
