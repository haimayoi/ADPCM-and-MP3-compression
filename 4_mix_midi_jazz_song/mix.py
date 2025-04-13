from pydub import AudioSegment
import subprocess
import os

def mix_audio(wav1, wav2, output_file="final_mix.wav", gain_db=20):
    audio1 = AudioSegment.from_file(wav1)
    audio2 = AudioSegment.from_file(wav2).apply_gain(gain_db)  # tăng âm lượng MIDI

    mixed = audio1.overlay(audio2)
    mixed.export(output_file, format="wav")
    print(f"✅ Mixed audio saved to: {output_file}")

def convert_midi_to_wav(midi_file, output_wav, soundfont_path):
    """Chuyển đổi file MIDI sang WAV sử dụng FluidSynth"""
    # Kiểm tra xem file soundfont có tồn tại không
    if not os.path.exists(soundfont_path):
        print(f"❌ Không tìm thấy file soundfont tại: {soundfont_path}")
        return False
        
    cmd = f'fluidsynth -ni "{soundfont_path}" "{midi_file}" -F "{output_wav}" -r 44100'
    print(f"Đang chạy lệnh: {cmd}")
    result = subprocess.run(cmd, shell=True)
    
    if os.path.exists(output_wav) and os.path.getsize(output_wav) > 0:
        print(f"✅ Chuyển đổi thành công! File WAV đã được tạo: {output_wav}")
        return True
    else:
        print("❌ Chuyển đổi thất bại. Lỗi khi chạy FluidSynth.")
        return False

if __name__ == "__main__":
    # Các đường dẫn file
    original_wav = "group3.wav"    # đổi tên file ghi âm của bạn
    midi_file = "jazz.mid"
    midi_wav = "jazz.wav"           # sẽ tạo ra từ MIDI
    
    # Đường dẫn đến file soundfont - thay đổi cho đúng
    # Thay đổi đường dẫn tới file soundfont trên Ubuntu
    # soundfont_path = "/usr/share/sounds/sf2/FluidR3_GM.sf2"
    soundfont_path = r"FluidR3_GM.sf2"
    
    # Kiểm tra nếu người dùng đã sao chép file vào thư mục hiện tại
    if os.path.exists("FluidR3_GM.sf2"):
        soundfont_path = "FluidR3_GM.sf2"
        print("Đã tìm thấy file soundfont trong thư mục hiện tại.")
    
    print("\n🎵 Đang chuyển đổi MIDI sang WAV...")
    success = convert_midi_to_wav(midi_file, midi_wav, soundfont_path)
    
    if success:
        # Bước 2: Mix 2 file WAV lại
        if os.path.exists(original_wav):
            input("\n👉 Nhấn Enter để tiếp tục mix hai file WAV...")
            mix_audio(original_wav, midi_wav, "jazz_mix.wav", gain_db=20)
        else:
            print(f"❌ Không tìm thấy file ghi âm: {original_wav}")
    else:
        print("Vui lòng kiểm tra đường dẫn đến file soundfont hoặc sao chép file FluidR3_GM.sf2 vào thư mục hiện tại.")