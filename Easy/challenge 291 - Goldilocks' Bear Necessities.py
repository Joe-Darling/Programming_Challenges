"""
Challenge: Goldilocks' Bear Necessities

Description:
Once upon a time, there lived an adventurous little girl called Goldilocks. She explored the world with abandon, having
a lot of fun. During her latest foray into the woods, she found another bear home -- though this one is home to many
more bears. Having learned from her previous experiences, Goldilocks knows that trial and error is not an efficient way
of finding the right chair and porridge to help herself to.

The task falls to you: given descriptions of Goldilocks' needs and of the available porridge/chairs at the dinner table,
tell Goldilocks which chair to sit in so the chair does not break, and the porridge is at an edible temperature.

The input begins with a line specifying Goldilocks' weight (as an integer in arbitrary weight-units) and the maximum
temperature of porridge she will tolerate (again as an arbitrary-unit integer). This line is then followed by some
number of lines, specifying a chair's weight capacity, and the temperature of the porridge in front of it.
Sample input:
100 80
30 50
130 75
90 60
150 85
120 70
200 200
110 100
Interpreting this, Goldilocks has a weight of 100 and a maximum porridge temperature of 80. The first seat at the table
has a chair with a capacity of 30 and a portion of porridge with the temperature of 50. The second has a capacity of 130
and temperature of 60, etc.

Seats #2 and #5 have both good enough chairs to not collapse under Goldilocks, and porridge that is cool enough for her
to eat.

Bonus:
No Bonus

Results:
Success!
Standard: Took about 18 minutes
"""


def main():
    seats = ""
    with open("D:\\Files\Python Projects\DailyProgrammer\Files\Goldilocks'.txt", "r") as f:
        goldi_weight, goldi_max_temp = f.readline().strip("\n").split(" ")
        goldi_weight = int(goldi_weight)
        goldi_max_temp = int(goldi_max_temp)
        x = 1
        for line in f:
            line = line.strip("\n")
            seat_weight = int(line.split(" ")[0])
            seat_temp = int(line.split(" ")[1])
            if seat_weight >= goldi_weight and seat_temp <= goldi_max_temp:
                seats += str(x) + " "
            x += 1

    print(seats)

main()