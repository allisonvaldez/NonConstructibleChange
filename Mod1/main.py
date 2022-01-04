"""
time: O(n log(n)) since we perform a sort
space: O(1) if we are allowed to sort in place O(n) if not due to needing to
create another structure to hold the sorted data
"""


def nonconstructible_change(coins):
    # always start by sorting the array
    coins.sort()

    """
    initialize a counter for the allowable amount of change allowed for each 
    coin
    """
    allowable_change = 0

    """
    create a for-loop that iterates over the array of coins controlling for 
    the condition of NOT having a a coin greater than the amount of allowable 
    change
    """
    for i in coins:
        if i > allowable_change + 1:
            return allowable_change + 1


print(nonconstructible_change(f"the minimum amount {[1, 1, 1, 1, 1]}"))
