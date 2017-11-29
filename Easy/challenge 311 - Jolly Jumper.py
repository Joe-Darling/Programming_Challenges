"""
Challenge: Jolly Jumper:

Description:
A sequence of n > 0 integers is called a jolly jumper if the absolute values of the differences between successive
elements take on all possible values through n - 1 (which may include negative numbers). For instance, 1 4 2 3
is a jolly jumper, because the absolute differences are 3, 2, and 1, respectively. The definition implies that any
sequence of a single integer is a jolly jumper. Write a program to determine whether each of a number of sequences is a
jolly jumper

Result:
Success!
Standard: Took about 8 minutes
"""


def jolly_jumper(lst):
    num = lst[0]
    lst.remove(lst[0])

    jumps = []
    for x in range(1, num):
        jumps.append(x)

    ind = 0
    while ind != len(lst) - 1:
        ans = abs(lst[ind] - lst[ind+1])
        if ans in jumps:
            jumps.remove(ans)
            ind += 1
        else:
            return False
    return True

lst = [5, 1, 4, 2, -1, 6]
print(jolly_jumper(lst))