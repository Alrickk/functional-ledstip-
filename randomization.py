# circuitpython code for mp3
import time, board, digitalio, neopixel, random
from audiomp3 import MP3Decoder
from audiopwmio import PWMAudioOut as AudioOut


#strip brightness
strip = neopixel.NeoPixel(board.GP19, 60)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)


#Set up button
button = digitalio.DigitalInOut(board.GP16)
button.direction = digitalio.Direction.INPUT

songs = ['city1', 'driving1', 'city2', 'driving2', 'city3']


led_1 = digitalio.DigitalInOut(board.GP3)
led_2 = digitalio.DigitalInOut(board.GP6)
led_3 = digitalio.DigitalInOut(board.GP9)
led_4 = digitalio.DigitalInOut(board.GP11)
led_5 = digitalio.DigitalInOut(board.GP4)
led_6 = digitalio.DigitalInOut(board.GP5)
led_7 = digitalio.DigitalInOut(board.GP7)
led_8 = digitalio.DigitalInOut(board.GP13)

# Set send vs listen
led_1.direction = digitalio.Direction.OUTPUT
led_2.direction = digitalio.Direction.OUTPUT
led_3.direction = digitalio.Direction.OUTPUT
led_4.direction = digitalio.Direction.OUTPUT
led_5.direction = digitalio.Direction.OUTPUT
led_6.direction = digitalio.Direction.OUTPUT
led_7.direction = digitalio.Direction.OUTPUT
led_8.direction = digitalio.Direction.OUTPUT

ledlist = [led_1,led_2,led_3,led_4,led_5,led_6,led_7,led_8]

# ledlist = [x.value = False for x in ledlist]
audio = AudioOut(board.GP22)
path = "sounds/"
#filename and mp3 decoder
filename = "city1.mp3"
mp3_file = open(path + filename, "rb")
decoder = MP3Decoder(mp3_file)

def play_mp3(filename):
    decoder.file = open(path + filename, "rb")
    audio.play(decoder)
    while audio.playing:
        #run while the audio plays
       
         for idx, light in enumerate(ledlist):
            ledlist[idx].value = True
            time.sleep(0.001)
            for light in ledlist:
                light.value = False
            time.sleep(0.001)
        #led strip speedrun to seizure
            strip.fill(GREEN)
            time.sleep(0.03)
            strip.fill(BLUE)
            time.sleep(0.03)
            strip.fill(WHITE)
            time.sleep(0.03)
            strip.fill(OFF)
           
           
        
    else:
        for idx, light in enumerate(ledlist):
            ledlist[idx].value = False
           
           
       
           
       
       
        pass
    #file selection
while True:
    filename2=""
    if button.value:
        filename2 = random.choice(songs)
    play_mp3(filename2)
    print(filename2)
