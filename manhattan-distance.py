__author__ = 'Burak Tekin'
__date__ = '05/12/2013'
__contact_ = 'iletisim@buraktekin.net / tknbrk@gmail.com'

import math
#********************************#
#                +---+---+---+   #
#                | 1 | 2 | 3 |   #
#                +---+---+---+   #
#   GOAL STATE:  | 4 | 5 | 6 |   #
#                +---+---+---+   #
#                | 7 | 8 |   |   #
#                +---+---+---+   #
#********************************#


# State examples for using Manhattan Distance

goal_state = [1, 2, 3,
              4, 5, 6,
              7, 8, 0]

initial_state = [1, 2, 5,
                 6, 8, 0,
                 7, 4, 3]

example_state = [0, 1, 2,
                 3, 4, 5,
                 6, 7, 8]

example_state1 = [1, 2, 7,
                  4, 5, 6,
                  3, 8, 0]

example_state2 = [1, 2, 4,
                  3, 5, 6,
                  7, 8, 0]

example_state3 = [0, 2, 3,
                  4, 5, 6,
                  7, 8, 1]

example_state4 = [0, 1, 4,
                  8, 7, 6,
                  2, 5, 3]


def manhattan_distance(current_state):
    distance = 0
    kalan = 0
    bolum = 0

    for i in current_state:
        position_difference = abs(goal_state.index(i) - current_state.index(i))
        if i is not 0:
            kalan = position_difference % 3
            bolum = position_difference / 3
            distance += kalan + int(math.floor(bolum))
            if abs(goal_state.index(i) % 3 - current_state.index(i) % 3) == 2 and position_difference % 3 == 1:
                distance += 2
            print "i: " + str(i) + " goal-index: " + str(goal_state.index(i)) + " current-index: " + str(current_state.index(i)) + " bolum: " + str(bolum) + ": kalan: " + str(kalan) + ": distance: " + str(distance)
    return distance

print "Manhattan distance is: " + str(manhattan_distance(goal_state))       # Result = 0
print "Manhattan distance is: " + str(manhattan_distance(initial_state))    # Result = 9
print "Manhattan distance is: " + str(manhattan_distance(example_state))    # Result = 12
print "Manhattan distance is: " + str(manhattan_distance(example_state1))   # Result = 8
print "Manhattan distance is: " + str(manhattan_distance(example_state2))   # Result = 6
print "Manhattan distance is: " + str(manhattan_distance(example_state3))   # Result = 4
print "Manhattan distance is: " + str(manhattan_distance(example_state4))   # Result = 14