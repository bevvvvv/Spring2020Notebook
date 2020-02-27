function [rhos, thetas] = myHoughLines(H, nLines)
    % Detect lines from hough transform
    % H - Hough transform accumulator
    % nLines - number of lines to return
    
    % NMS
    H_di = imdilate(H, [0 0 0 0 0 ; 0 0 1 0 0; 0 0 0 0 0]);
     
    % chose top peaks
    [~, indices] = sort(H_di(:), 'desc');
    [rhos, thetas] = ind2sub(size(H_di), indices(1:nLines));
end
        