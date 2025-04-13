import random
import librosa
from mido import MidiFile, MidiTrack, Message, MetaMessage, bpm2tempo

# === CONFIG ===
audio_path = "group3.wav"  
output_file = "jazz.mid"
ticks_per_beat = 480
bpm = 65 

# === LOAD AUDIO AND MATCH LENGTH ===
y, sr = librosa.load(audio_path)
duration_sec = librosa.get_duration(y=y, sr=sr)
beats_total = int((bpm / 60) * duration_sec)
bars = beats_total // 4
total_beats = bars * 4

# === JAZZ CONTENT ===
melody_phrases = [[72, 74], [76, 74, 72], [72], [74, 76]]
chords = [[60, 64, 67], [62, 65, 69], [59, 63, 67], [60, 64, 69]] * (bars // 4)
bass_roots = [36, 38, 35, 36] * (bars // 4)  # Acoustic bass range
ride_cymbal = 51  # GM percussion note for ride
pad_chords = [[60, 67], [62, 69], [59, 67], [60, 67]] * (bars // 4)


mid = MidiFile(ticks_per_beat=ticks_per_beat)

#  Piano Melody (channel 0) 
melody_track = MidiTrack()
melody_track.append(MetaMessage('track_name', name='Acoustic Grand Piano', time=0))
melody_track.append(MetaMessage('instrument_name', name='Piano Melody', time=0))
melody_track.append(MetaMessage('set_tempo', tempo=bpm2tempo(bpm)))
melody_track.append(Message('program_change', program=0, channel=0, time=0))

melody_time = 0
beat = 0
while beat < total_beats:
    if random.random() < 0.5:
        phrase = random.choice(melody_phrases)
        for note in phrase:
            vel = random.randint(35, 45)
            melody_track.append(Message('note_on', note=note, velocity=vel, time=melody_time, channel=0))
            melody_track.append(Message('note_off', note=note, velocity=vel, time=int(ticks_per_beat * 1.2), channel=0))
            melody_time = 0  # reset after first note
        rest = int(ticks_per_beat * random.uniform(1.0, 3.0))
        melody_time = rest
        beat += len(phrase) + rest / ticks_per_beat
    else:
        rest = int(ticks_per_beat * random.uniform(2.0, 4.0))
        melody_time = rest
        beat += rest / ticks_per_beat
if melody_time > 0:
    melody_track.append(Message('note_on', note=0, velocity=0, time=melody_time, channel=0))
mid.tracks.append(melody_track)

#  Piano Chords (channel 1) 
chord_track = MidiTrack()
chord_track.append(MetaMessage('track_name', name='Acoustic Grand Piano', time=0))
chord_track.append(MetaMessage('instrument_name', name='Piano Chords', time=0))
chord_track.append(Message('program_change', program=0, channel=1, time=0))
for chord in chords:
    for i, note in enumerate(chord):
        chord_track.append(Message('note_on', note=note, velocity=50, time=0 if i > 0 else 0, channel=1))
    for i, note in enumerate(chord):
        chord_track.append(Message('note_off', note=note, velocity=50, time=int(ticks_per_beat * 4) if i == 0 else 0, channel=1))
mid.tracks.append(chord_track)

#  Acoustic Bass (channel 2) 
bass_track = MidiTrack()
bass_track.append(MetaMessage('track_name', name='Acoustic Bass', time=0))
bass_track.append(MetaMessage('instrument_name', name='Acoustic Bass', time=0))
bass_track.append(Message('program_change', program=32, channel=2, time=0))
for root in bass_roots:
    pattern = [root, root + 3, root + 5, root + 2]
    for i, note in enumerate(pattern):
        bass_track.append(Message('note_on', note=note, velocity=60, time=0 if i == 0 else 0, channel=2))
        bass_track.append(Message('note_off', note=note, velocity=60, time=ticks_per_beat, channel=2))
mid.tracks.append(bass_track)

#  Drums (channel 9) 
drum_track = MidiTrack()
drum_track.append(MetaMessage('track_name', name='Standard Drum Kit', time=0))
drum_track.append(MetaMessage('instrument_name', name='Drums', time=0))
drum_track.append(Message('program_change', program=0, channel=9, time=0))
for b in range(total_beats):
    if b % 2 == 1:
        drum_track.append(Message('note_on', note=ride_cymbal, velocity=40, time=0, channel=9))
        drum_track.append(Message('note_off', note=ride_cymbal, velocity=40, time=int(ticks_per_beat * 0.6), channel=9))
    else:
        drum_track.append(Message('note_on', note=0, velocity=0, time=int(ticks_per_beat), channel=9))
mid.tracks.append(drum_track)

#  Pad (channel 3) 
pad_track = MidiTrack()
pad_track.append(MetaMessage('track_name', name='String Ensemble 1', time=0))
pad_track.append(MetaMessage('instrument_name', name='String Pad', time=0))
pad_track.append(Message('program_change', program=48, channel=3, time=0))
for chord in pad_chords:
    for i, note in enumerate(chord):
        pad_track.append(Message('note_on', note=note + 12, velocity=15, time=0 if i > 0 else 0, channel=3))
    for i, note in enumerate(chord):
        pad_track.append(Message('note_off', note=note + 12, velocity=15, time=int(ticks_per_beat * 4) if i == 0 else 0, channel=3))
mid.tracks.append(pad_track)

# save
mid.save(output_file)
print(f" full jazz combo saved as: {output_file}")
