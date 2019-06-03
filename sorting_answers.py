#!/usr/bin/python3

# x y r

import numpy as np

from detecting_circles import detectCircles

def sortingAnswers(data):
  sortedYs = np.array(sorted(data, key=lambda circle: (circle[1])))
  dividedYs = np.split(sortedYs, 25)
  # print(dividedYs)

  # TODO: Check if we need to sort by Xs
  sortedXs = []
  for row in dividedYs:
    sortedXs.append(np.array(sorted(row, key=lambda row: (row[0]))))
  print(sortedXs)

  dictionary = {"mcq": {}, "true_false": {}}

  for idx, row in enumerate(sortedXs): # Change this to sortedXs
    dictionary["mcq"][idx+1] = row[0:6]
    dictionary["mcq"][idx+26] = row[6:12]

    dictionary["true_false"][idx+1] = row[12:14]

  # print(dictionary)
  return dictionary

if __name__ == '__main__':
  data = detectCircles("./exampapper.jpeg")
  sortingAnswers(data)

