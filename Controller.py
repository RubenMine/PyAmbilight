from rpi_ws281x import Color
import _rpi_ws281x as ws

class LEDController:
    def __init__(self, n_led, gpio, brightness, channel, freq, dma_num, invert) -> None:
        self.leds = None
        self.channel = None

        self.NUMBER_OF_LED = n_led
        self.LED_GPIO = gpio
        self.LED_BRIGHTNESS = brightness
        self.LED_CHANNEL = channel
        self.LED_FREQ_HZ = freq
        self.LED_DMA_NUM = dma_num
        self.LED_INVERT = invert

    def initializes_leds(self):
        self.leds = ws.new_ws2811_t()

        for channum in range(2):
            channel = ws.ws2811_channel_get(self.leds, channum)
            ws.ws2811_channel_t_count_set(channel, 0)
            ws.ws2811_channel_t_gpionum_set(channel, 0)
            ws.ws2811_channel_t_invert_set(channel, 0)
            ws.ws2811_channel_t_brightness_set(channel, 0)

        self.channel = ws.ws2811_channel_get(self.leds, self.LED_CHANNEL)

        ws.ws2811_channel_t_count_set(self.channel, self.NUMBER_OF_LED)
        ws.ws2811_channel_t_gpionum_set(self.channel, self.LED_GPIO)
        ws.ws2811_channel_t_invert_set(self.channel, self.LED_INVERT)
        ws.ws2811_channel_t_brightness_set(self.channel, self.LED_BRIGHTNESS)

        ws.ws2811_t_freq_set(self.leds, self.LED_FREQ_HZ)
        ws.ws2811_t_dmanum_set(self.leds, self.LED_DMA_NUM)

        return ws.ws2811_init(self.leds)

    def set_colors(self, colors):
        for i, color in enumerate(colors):
            c = Color(color[1], color[0], color[2])
            ws.ws2811_led_set(self.channel, i, int(c))
        ws.ws2811_render(self.leds)

    def clear(self):
        c = Color(0, 0, 0)
        for i in range(self.NUMBER_OF_LED):
            ws.ws2811_led_set(self.channel, i, int(c))
        ws.ws2811_render(self.leds)