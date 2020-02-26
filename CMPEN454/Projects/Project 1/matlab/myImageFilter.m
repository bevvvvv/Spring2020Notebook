function [img1] = myImageFilter(img0, h)
    % Returns a convulved image img1, using img0 and h
    % Makes use of Matlabs padding function (padarray)
    % img0 - greyscale image
    % h - odd sized filter kernel

    % Recall convolution is cross correlation with flipped image
    % across both axes

    % flip image
    flip_img = rot90(img0,2);

    % pad image
    pad_size_row = idivide(size(h,1),2);
    pad_size_col = idivide(size(h,2),2);
    flip_img = padarray(flip_img, [pad_size_row pad_size_col], 'replicate');

    img_rows = size(img0,1);
    img_cols = size(img0,2);
    img1 = zeros(img_rows, img_cols); % create output as zeroes
    % perform convolution
    for pixel_row = (pad_size_row+1):(img_rows-pad_size_row)
        for pixel_col = (pad_size_col+1):(img_cols-pad_size_col)
            img_kern = flip_img(pixel_row - pad_size_row:pixel_row + pad_size_row, pixel_col - pad_size_col:pixel_col + pad_size_col);
            img1(pixel_row, pixel_col) = sum(img_kern .* h);
        end
    end
end