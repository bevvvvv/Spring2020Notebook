function [img1] = myEdgeFilter(img0, sigma)
    % Returns an edge magnitude img1
    % img0 - grayscale image
    % sigma - Standard Deviation of gaussian smoothing kernel

    % Create Gaussian kernel
    hsize = 2 * ceil(3 * sigma) + 1;
    h = fspecial('gaussian', hsize, sigma);

    % Use myImageFilter to convolve img0 with gaussian kernel
    smooth_img = myImageFilter(img0, h);

    % imgx - gradient in x direction (Sobel filter)
    sobel = [1 0 -1;
             2 0 -2;
             1 0 -1];
    imgx = myImageFilter(smooth_img, sobel);

    % imgy - gradient in y direction (Sobel filter)
    sobel = [1 2 1;
             0 0 0;
             -1 -2 -1];
    imgy = myImageFilter(smooth_img, sobel);

    % magnitude of gradient - sqrt(x^2 + y^2)
    img_max = (imgx .^2 + imgy .^ 2) .^ 0.5;
    img1 = img_max;

    % NMS
    % vector angle -> atan(y/x) (range is -90 to 90)
    thetas = rad2deg(atan(imgy ./ imgx));
    for row = 1:size(img1,1)
        for col = 1:size(img1,2)
            angle = thetas(row, col);
            if angle < 0
                angle = angle * -1;
            end
            if angle < 22.5 % 0 degree mapping
               if (col > 1 && img_max(row, col-1) > img_max(row, col)) || ...
                   (col < size(img1,2) && img_max(row, col+1) > img_max(row, col))
                   img1(row,col) = 0;
               end
            elseif angle < 67.5 % 45 degree mapping
               if (row > 1 && col < size(img1,2) && img_max(row -1, col+1) > img_max(row, col)) ||  ...
                       (row < size(img1,1) && col > 1 && img_max(row+1, col-1) > img_max(row, col))
                   img1(row,col) = 0;
               end
            elseif angle < 112.5 % 90 degree mapping
                if (row > 1 && img_max(row-1, col) > img_max(row, col)) || ...
                        (row < size(img1,1) && img_max(row+1, col) > img_max(row, col))
                   img1(row,col) = 0;
               end
            else % 135 degree mapping
                if (row < size(img1,1) && col > 1 && img_max(row+1, col-1) > img_max(row, col)) || ...
                        (row > 1 && col < size(img1,2) && img_max(row-1, col+1) > img_max(row, col))
                   img1(row,col) = 0;
               end
            end
        end
    end
end
    
                
        
        
