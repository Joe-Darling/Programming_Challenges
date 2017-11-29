"""
Challenge: Rack Management 1

Description:
Given a sorted list of distinct integers, write a function that returns whether there are two integers in
the list that add up to 0. For example, you would return true if both -14435 and 14435 are in the list,
because -14435 + 14435 = 0. Also return true if 0 appears in the list.

Result:
Success!
Standard: Took about 7 minutes.
"""

import random


def subset_sum(lst):
    if len(lst) == 0:
        return False

    front_ind = 0
    back_ind = len(lst) - 1
    front = lst[front_ind]
    back = lst[back_ind]
    while front <= 0 <= back:
        if front == 0 or back == 0:
            return True
        if abs(front) == back:
            print(back)
            return True
        else:
            if abs(front) > back:
                front_ind += 1
                front = lst[front_ind]
            else:
                back_ind -= 1
                back = lst[back_ind]
    return False

lst = []
for x in range(40):
    lst.append(random.randint(-1000, 1000))
lst.sort()
print(lst)
print(subset_sum(lst))