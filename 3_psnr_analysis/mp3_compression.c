#include <stdio.h>
#include <stdlib.h>
#include <lame/lame.h>

int main() {
    lame_global_flags *gfp = lame_init();
    if (gfp == NULL) {
        fprintf(stderr, "Failed to initialize LAME encoder\n");
        return 1;
    }

    // Set LAME parameters
    lame_set_num_channels(gfp, 1);       // Mono
    lame_set_in_samplerate(gfp, 44100);  // 44.1 kHz
    lame_set_brate(gfp, 128);            // 128 kbps
    lame_set_mode(gfp, MONO);            // MONO mode
    lame_set_quality(gfp, 2);            // Quality setting

    // Initialize the encoder
    if (lame_init_params(gfp) < 0) {
        fprintf(stderr, "Failed to initialize LAME parameters\n");
        lame_close(gfp);
        return 1;
    }

    FILE *wav_file = fopen("group3.wav", "rb");
    if (wav_file == NULL) {
        perror("Failed to open WAV file");
        lame_close(gfp);
        return 1;
    }

    // Skip WAV header (44 bytes)
    fseek(wav_file, 44, SEEK_SET);

    FILE *mp3_file = fopen("compressed_mp3.mp3", "wb");
    if (mp3_file == NULL) {
        perror("Failed to open MP3 file");
        fclose(wav_file);
        lame_close(gfp);
        return 1;
    }

    const int PCM_SIZE = 8192;
    const int MP3_SIZE = 8192;
    short pcm_buffer[PCM_SIZE];
    unsigned char mp3_buffer[MP3_SIZE];
    int read, write;

    do {
        // Read PCM data (16-bit signed mono)
        read = fread(pcm_buffer, sizeof(short), PCM_SIZE, wav_file);

        if (read == 0) {
            // Encode the remaining data
            write = lame_encode_flush(gfp, mp3_buffer, MP3_SIZE);
        } else {
            // Encode mono PCM to MP3
            write = lame_encode_buffer(gfp, pcm_buffer, NULL, read, mp3_buffer, MP3_SIZE);
        }

        // Write MP3 data
        fwrite(mp3_buffer, write, 1, mp3_file);

    } while (read != 0);

    fclose(wav_file);
    fclose(mp3_file);
    lame_close(gfp);

    printf("Compression complete. Output: compressed_mp3.mp3\n");

    return 0;
}
