function PSNR(original_file, compressed_file, mp3_file)
    % Read audio files
    [x_org, fs_orig] = audioread(original_file);
    [x_adpcm, fs_adpcm] = audioread(compressed_file);
    [x_mp3, fs_mp3] = audioread(mp3_file);

    % Resample if needed
    if fs_adpcm ~= fs_orig
        x_adpcm = resample(x_adpcm, fs_orig, fs_adpcm);
    end
    if fs_mp3 ~= fs_orig
        x_mp3 = resample(x_mp3, fs_orig, fs_mp3);
    end

    % Convert stereo to mono
    if size(x_org,2) == 2
        x_org = mean(x_org, 2);
    end
    if size(x_adpcm,2) == 2
        x_adpcm = mean(x_adpcm, 2);
    end
    if size(x_mp3,2) == 2
        x_mp3 = mean(x_mp3, 2);
    end

    % Normalize amplitudes (optional)
    x_org = x_org / max(abs(x_org));
    x_adpcm = x_adpcm / max(abs(x_adpcm));
    x_mp3 = x_mp3 / max(abs(x_mp3));

    % Match signal lengths
    min_len = min([length(x_org), length(x_adpcm), length(x_mp3)]);
    x_org = x_org(1:min_len);
    x_adpcm = x_adpcm(1:min_len);
    x_mp3 = x_mp3(1:min_len);

    % Compute PSNR values
    psnr_adpcm = calc_psnr(x_org, x_adpcm);
    psnr_mp3 = calc_psnr(x_org, x_mp3);

    % Display results
    fprintf('PSNR (ADPCM): %.2f dB\n', psnr_adpcm);
    fprintf('PSNR (MP3): %.2f dB\n', psnr_mp3);

    % Plot bar chart with colors
    figure;
    b = bar([psnr_adpcm, psnr_mp3], 'FaceColor', 'flat');
    b.CData(1,:) = [135 206 235] / 255;  % Skyblue
    b.CData(2,:) = [255 165 0] / 255;    % Orange

    set(gca, 'XTickLabel', {'ADPCM', 'MP3'});
    ylabel('PSNR (dB)');
    title('PSNR Comparison Between Codecs');
    grid on;
end

function psnr_val = calc_psnr(ref, test)
    mse = mean((ref - test).^2);
    if mse == 0
        psnr_val = Inf;
    else
        psnr_val = 10 * log10(1 / mse); % Reference is normalized to [-1,1]
    end
end
