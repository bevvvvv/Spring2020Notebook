function [l2avg] = averageL2(coords1,coords2)
%AVERAGEL2 computes average L2 distance between input vectors
%   Detailed explanation goes here
diff = coords2 - coords1;
square = diff .^ 2; % elementwise square
totals = sum(square);
l2avg = mean(totals);
end

