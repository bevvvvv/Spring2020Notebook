function [H, rhoScale, thetaScale] = myHoughTransform(Im, threshold, rhoRes, thetaRes)
	% Performs Hough transform on edge magnitude image
    % Im - edge magnitude image
    % threshold - edge strength threshold
    % rhoRes - resolution along rho
    % thetaRes - resolution along theta
    % returns
    % H - hough transform accumulator
    % rhoScale - array of rho values in H (y value of H)
    % thetaScale - array of theta values in H (x value of H)
    
    % Threshold Im (only include values above threshold)
    Im_thresh = Im;
    Im_thresh(Im <= threshold) = 0;
    
    % instantiate variables
    thetaScale = floor((2 * pi) / thetaRes);
    thetaStep = (2 * pi) / (thetaScale -1);
    theta = 0:thetaStep:(2 * pi);
    rhoStop = (size(Im,1)^2 + size(Im,2)^2) ^ 0.5;
    rhoScale = rhoStop / rhoRes; % number of pixels
    H = zeros(2*rhoScale, thetaScale);
    
    % vote
    [y, x] = find(Im_thresh > 0);
    % each point - calculate hough line
    rho = zeros(size(x,1), thetaScale);
    for i = 1:size(x)
        rho(i,:) = x(i) .* cos(theta) +  y(i) .* sin(theta);
    end
    
    for i = 1:size(x,1)
        for j = 1:size(rho,2) % go through each theta
            rho_val = rho(i,j);
            rho_val = rho_val / rhoRes; % adjust for res
            rho_val = rho_val + rhoScale; % no negative
            rho_val = floor(rho_val);
            H(rho_val, j) = H(rho_val, j) + 1; % cast your vote!
        end
    end
    % normalize H
    max_vote = max(max(H));
    H = H ./ max_vote;
    rhoScale = 2 * rhoScale;
end
        
        