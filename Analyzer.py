import cv2 as cv
import numpy as np

class FrameAnalyzer:
    def __init__(self, edge_accuracy, number_of_led) -> None:
        self.frame = None
        self.frame_x, self.frame_y = None, None
        self.edge_accuracy = edge_accuracy
        self.number_of_led = number_of_led


    def analyze_frame(self, frame):
        if frame is not None:
            self.frame = frame
            self.frame_y, self.frame_x = self.frame.shape[0:2]
            edgeList = self.extract_edges_from_frame()
            edgesFrame = cv.hconcat(edgeList)
            return self.extract_color_from_frame(edgesFrame)
        else:
            return None


    def extract_edges_from_frame(self):
        limit = self.edge_accuracy

        edgeA = self.frame[self.frame_y - limit:]
        edgeC = cv.rotate(self.frame[:limit], cv.ROTATE_180)    
        edgeB = cv.rotate(self.frame[:, self.frame_x-limit:], cv.ROTATE_90_CLOCKWISE)
        edgeD = cv.rotate(self.frame[:, :limit], cv.ROTATE_90_COUNTERCLOCKWISE)
        return [edgeA, edgeB, edgeC, edgeD]


    def extract_color_from_frame(self, frame):
        listOfColours = list()
        avg_color_for_col = np.average(frame, axis=0)

        pixel_for_led = frame.shape[1]//self.number_of_led
        uncovered_pixels= frame.shape[1]%self.number_of_led

        """
        print(f"TOTAL PIXEL {frame.shape[1]}")
        print(f"PIXEL FOR LED {pixel_for_led}")
        print(f"UNCOVERED PIXELS {uncovered_pixels}")
        print(f"FROM {self.number_of_led-uncovered_pixels}* LED ADDING ONE PIXEL")
        """

        i=0
        for iter, start_x in enumerate([n for cont, n in enumerate(range(0, frame.shape[1]+1, pixel_for_led)) if cont < self.number_of_led]):
            if iter == self.number_of_led-uncovered_pixels-1:
                pixel_for_led += 1
            if iter > self.number_of_led-uncovered_pixels:
                i+=1
            
            segment = avg_color_for_col[start_x+i:start_x+i+pixel_for_led]
            color = np.median(segment, axis=0)
            listOfColours.append(color)
        
        # The listOfColours is a list of BGR values
        return listOfColours


class SoundAnalyzer:
    pass