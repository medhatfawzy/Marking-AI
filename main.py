import cv2
import sys
import json

from detecting_circles import detectCircles
from sorting_answers import sortingAnswers
from marking import marking

if __name__ == '__main__':
  filename = sys.argv[1]

  # Read image as gray-scale
  img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
  # Cropping:
  # img = img[round(img.shape[0]/9):img.shape[0], 0:img.shape[1]]
  img = img[round(img.shape[0]/8):img.shape[0], 0:img.shape[1]]
  # Binarization
  ret, thresh = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)

  circles_data = detectCircles(thresh)
  answers_dictionary = sortingAnswers(circles_data)
  print(json.dumps(marking(answers_dictionary, thresh), indent=4))
