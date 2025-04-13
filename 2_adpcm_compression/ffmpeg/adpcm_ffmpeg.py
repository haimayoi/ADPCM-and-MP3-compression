import subprocess
import os

def compress_to_adpcm(input_file, output_file):
    if not os.path.isfile(input_file):
        print("Input file not found")
        return

    try:
        # Lệnh FFmpeg
        command = [
            'ffmpeg',
            '-y',  # Ghi đè nếu output_file tồn tại
            '-i', input_file,
            '-acodec', 'adpcm_ima_wav',  # Codec ADPCM
            output_file
        ]
        subprocess.run(command, check=True)
        print(f"Successfully compressed: {output_file}")
    except subprocess.CalledProcessError as e:
        print("Error running FFmpeg:", e)

# --- Ví dụ sử dụng ---
compress_to_adpcm("group3.wav", "compressed_ffmpeg.wav")
