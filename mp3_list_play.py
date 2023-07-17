import board, time, busio, storage
import glob 
import random
from audiomp3 import MP3Decoder
from audiopwmio import PWMAudioOut as AudioOut

##### These are GLOBALS, which are usually not required #####


audio = AudioOut(board.GP22)
path = "sounds/"
filename = "1.mp3"
mp3_file = open(path + filename, "rb")
decoder = MP3Decoder(mp3_file)



MAX_AUDIO_PLAY_TIME_S = 100
###############################################


def play_mp3(mp3_filename):
    decoder.file = open(path + mp3_filename, "rb")
    audio.play(decoder)
    start_music = time.time()
    while audio.playing:
        # Chaning this to prevent infinite loop
        music_duration = time.time()-start_music
        if music_duration > MAX_AUDIO_PLAY_TIME_S:
            break
        else:
            # continue jumps to the next iteration of a loop. Pass does something very specific and not great.
            continue
    
def what_range_does(end_range):
    print(f"when given range({end_range}), the function will iterate through the following")
    for i in range(end_range):
        print(i)
    return


    
    
def main():
    # Add logic to wait for event/button/trigger

    keep_playing = True
    # you sure this is correct? your first file is 0.mp3?
    # to see what it does uncomment the next line
    # what_range_does(5)
    
    sound_names = [f"{x}.mp3" for x in range(5)]
    while keep_playing :
        # figure out what will cause the music to stop and set keep_playing = False when it is reached
        play_mp3(random.choice(sound_names))
    
    
    
           
if __name__ == "__main__":
    main()
