import cv2 as cv
from Analyzer import FrameAnalyzer
from Controller import LEDController
import time

NUMBER_OF_LED = 100
EDGE_ACCURACY = 50
LED_CHANNEL = 0
LED_FREQ_HZ = 800000        
LED_DMA_NUM = 10            
LED_GPIO = 18               
LED_BRIGHTNESS = 255        
LED_INVERT = 0


fa = FrameAnalyzer(edge_accuracy=EDGE_ACCURACY, number_of_led=NUMBER_OF_LED)
strip = LEDController(n_led=NUMBER_OF_LED, gpio=LED_GPIO, brightness=LED_BRIGHTNESS, channel=LED_CHANNEL,
                      freq=LED_FREQ_HZ, dma_num=LED_DMA_NUM, invert=LED_INVERT).initializes_leds()

cap = cv.VideoCapture()
ret = True
while(ret):
    ret, frame = cap.read()

    start = time.time()

    colors = fa.analyze_frame(frame)
    strip.set_colors(colors)

    end = time.time()
    print(f"Execution Time: {end-start}")

strip.clear(strip)

