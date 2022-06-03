from pydub import AudioSegment
from pydub.playback import play

# Function for playing audiosegments 
def play_segment(s, audiofile):
    start = int(s[1]*1000-300)
    end = int(s[2]*1000+300)
    audio = AudioSegment.from_file(audiofile)
    audio_piece = audio[start:end] 
    play(audio_piece)