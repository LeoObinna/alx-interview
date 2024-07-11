#!/usr/bin/python3
'''Minimum Operations python3 challenge'''

def minOperations(n):
    '''
    Calculates the minimum number of operations needed to achieve exactly n 'H' characters in the file.
    
    An operation can be either "Copy All" or "Paste". The goal is to use the fewest number of operations
    to reach exactly n 'H' characters starting with one 'H'.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations needed to achieve n 'H' characters. 
             If n is impossible to achieve, returns 0.
    '''
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    # Loop until n is reduced to 1
    while n > 1:
        # While n is divisible by the current factor
        while n % factor == 0:
            # Add the factor to the operations count
            operations += factor
            # Reduce n by dividing it by the factor
            n //= factor
        # Move to the next factor
        factor += 1

    return operations
