import cv2 as cv

from Analyzer import FrameAnalyzer
        
frame = cv.imread("PyAmbilight\prova.jpg")
fa = FrameAnalyzer(edge_accuracy=50, number_of_led=180)

for pixel in fa.analyze_frame(frame):
    print(pixel)
