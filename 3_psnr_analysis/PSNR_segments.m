function PSNR_segments(original_file, adpcm_file, mp3_file)
    % Read audio files
    [x_org, fs_org] = audioread(original_file);
    [x_adpcm, fs_adpcm] = audioread(adpcm_file);
    [x_mp3, fs_mp3] = audioread(mp3_file);

    % Resample if needed
    if fs_adpcm ~= fs_org
        x_adpcm = resample(x_adpcm, fs_org, fs_adpcm);
    end
    if fs_mp3 ~= fs_org
        x_mp3 = resample(x_mp3, fs_org, fs_mp3);
    end

    % Convert stereo to mono if needed
    if size(x_org,2) == 2
        x_org = mean(x_org, 2);
    end
    if size(x_adpcm,2) == 2
        x_adpcm = mean(x_adpcm, 2);
    end
    if size(x_mp3,2) == 2
        x_mp3 = mean(x_mp3, 2);
    end

    % Normalize amplitudes
    x_org = x_org / max(abs(x_org));
    x_adpcm = x_adpcm / max(abs(x_adpcm));
    x_mp3 = x_mp3 / max(abs(x_mp3));

    % Match signal lengths
    min_len = min([length(x_org), length(x_adpcm), length(x_mp3)]);
    x_org = x_org(1:min_len);
    x_adpcm = x_adpcm(1:min_len);
    x_mp3 = x_mp3(1:min_len);

    % Compute PSNR for each 1-second segment
    segment_len = fs_org;  % 1 second per segment
    num_segments = floor(min_len / segment_len);
    psnr_adpcm = zeros(1, num_segments);
    psnr_mp3 = zeros(1, num_segments);

    for i = 1:num_segments
        idx_start = (i - 1) * segment_len + 1;
        idx_end = i * segment_len;

        seg_org = x_org(idx_start:idx_end);
        seg_adpcm = x_adpcm(idx_start:idx_end);
        seg_mp3 = x_mp3(idx_start:idx_end);

        psnr_adpcm(i) = calc_psnr(seg_org, seg_adpcm);
        psnr_mp3(i) = calc_psnr(seg_org, seg_mp3);
    end

    % Plot the results
    figure;
    p1 = plot(1:num_segments, psnr_adpcm, '-o', 'DisplayName', 'ADPCM');
    hold on;
    p2 = plot(1:num_segments, psnr_mp3, '-x', 'DisplayName', 'MP3');
    
    % Set colors for the plots
    p1.Color = [135 206 235] / 255;  % Skyblue
    p2.Color = [255 165 0] / 255;    % Orange
    
    title('PSNR per 1-second Segment');
    xlabel('Time (seconds)');
    ylabel('PSNR (dB)');
    legend show;
    grid on;
end

function psnr_val = calc_psnr(ref, test)
    mse = mean((ref - test).^2);
    if mse == 0
        psnr_val = Inf;
    else
        psnr_val = 10 * log10(1 / mse);
    end
end
