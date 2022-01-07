import cv2 as cv
import numpy as np
import time

from Analyzer import FrameAnalyzer

def resize_frame(frameList, scale_percent):
    frameListResized = list()

    for img in frameList:
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        frameListResized.append(cv.resize(img, dim))

    return frameListResized
        
frame = cv.imread("prova.jpg")
fa = FrameAnalyzer(edge_accuracy=50, number_of_led=180)
print(fa.analyze_frame(frame))





"""
    borderList = extract_edges_from_frame(frame, 50)
    borderListResized = resize_frame(borderList, 50)
    ultimateFrame = cv.hconcat(borderListResized)

    #cv.imwrite(str(i)+"B.png", ultimateFrame)


    listOfColours = metodo1(ultimateFrame, 180)
    #met2 = metodo2(ultimateFrame, 180)

    list_of_pixel_colored = list()
    for color in listOfColours:
        list_of_pixel_colored.append(np.array([[[color[0], color[1], color[2]],
                                                [color[0], color[1], color[2]]],
                                                
                                                [[color[0], color[1], color[2]],
                                                 [color[0], color[1], color[2]]],
                                                 
                                                 [[color[0], color[1], color[2]],
                                                 [color[0], color[1], color[2]]],
                                                 
                                                 [[color[0], color[1], color[2]],
                                                 [color[0], color[1], color[2]]],
                                                 
                                                 [[color[0], color[1], color[2]],
                                                 [color[0], color[1], color[2]]],
                                                 
                                                 [[color[0], color[1], color[2]],
                                                 [color[0], color[1], color[2]]],
                                                 
                                                 [[color[0], color[1], color[2]],
                                                 [color[0], color[1], color[2]]]]))

    list_of_pixel_colored = resize_frame(list_of_pixel_colored, 100)
    led_strip_color = cv.hconcat(list_of_pixel_colored)

    cv.imwrite("Video/"+str(i)+".png", led_strip_color)
    #frameA = cv.resize(frame, (400, 300))
    #ultimateFrameA = cv.resize(ultimateFrame, (400, 300))
    #led_strip_colorA = cv.resize(led_strip_color, (400, 300))
    #video = np.concatenate((led_strip_colorA, frameA), 0)
    #cv.imshow("Prova",led_strip_color)
    #time.sleep(2)
    print()
    if cv.waitKey(1) == ord("q"):              
        break
"""