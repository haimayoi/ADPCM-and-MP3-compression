% 1. Read the audio file
[audio, fs] = audioread('group3.wav');  % Replace with your filename

% 2. If stereo, convert to mono
if size(audio, 2) == 2
    audio = mean(audio, 2);  % Average the two channels
end

% 3. Length and FFT
N = length(audio);
Y = fft(audio);             % Compute FFT
Y = Y(1:floor(N/2));        % Keep only positive frequencies
f = (0:N/2-1) * fs/N;       % Frequency axis

% 4. Compute magnitude spectrum (in dB)
mag = abs(Y);
mag_db = 20*log10(mag + eps);  % Use eps to avoid log(0)

% 5. Plot spectrum
figure;
plot(f, mag_db);
xlabel('Frequency (Hz)');
ylabel('Magnitude (dB)');
title('Magnitude Spectrum of Audio Signal');
grid on;
