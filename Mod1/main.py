"""
time: O(n log(n)) since we perform a sort
space: O(1) if we are allowed to sort in place O(n) if not due to needing to
create another structure to hold the sorted data
"""


def nonconstructible_change(coins):
    # always start by sorting the array
    coins.sort()

    """
    initialize a counter to check the for the allowable amount of change 
    allowed for each coin when adding it to the next
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

        """
        make sure to increment within the for-loop to go to the next coin
        """
        allowable_change += i

    """
    return the allowable amount of change from going to one coin to the next
    """
    return allowable_change + 1


print(nonconstructible_change([1, 2, 5]))