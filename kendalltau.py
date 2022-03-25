def kendall_tau(perm1, perm2):
    """
    Compute the Kendall Tau distance between two rankings of the numbers
    from 0 to N-1

    Parameters
    ----------
    perm1: list
        A permutation of the elements 0, 1, ..., N-1
    perm2:
        A permutation of the elements 0, 1, ..., N-1
    
    Returns
    -------
    The Kendall-Tau distance, or the number of discordant pairs between
    the two rankings
    """
    ## TODO: Fill this in
    return 0

# This example should have 7 discordant pairs
perm1 = [0, 4, 3, 1, 2]
perm2 = [1, 4, 2, 3, 0]
print(kendall_tau(perm1, perm2))
