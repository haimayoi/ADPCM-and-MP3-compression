import wave
from codec import encode_block, decode_block

# --- Đọc file WAV gốc ---
with wave.open("group3.wav", "rb") as wav_in:
    if wav_in.getsampwidth() != 2 or wav_in.getnchannels() != 1:
        raise ValueError("File WAV phải là 16-bit PCM mono.")
    framerate = wav_in.getframerate()
    pcm_data = wav_in.readframes(wav_in.getnframes())

# --- Encode PCM → ADPCM ---
adpcm_data = bytearray()
for i in range(0, len(pcm_data), 1010):
    block = pcm_data[i:i+1010]
    if len(block) < 1010:
        block += b'\x00' * (1010 - len(block))  # Padding nếu block cuối thiếu
    adpcm_data += encode_block(block)

with open("group3.adpcm", "wb") as f:
    f.write(adpcm_data)
print("Đã nén xong → group3.adpcm")

# --- Decode ADPCM → PCM ---
decoded_pcm = bytearray()
for i in range(0, len(adpcm_data), 256):
    block = adpcm_data[i:i+256]
    decoded_pcm += decode_block(block)

with wave.open("group3_decoded.wav", "wb") as wav_out:
    wav_out.setnchannels(1)
    wav_out.setsampwidth(2)
    wav_out.setframerate(framerate)
    wav_out.writeframes(decoded_pcm)
print(" Đã giải nén lại → group3_decoded.wav")
