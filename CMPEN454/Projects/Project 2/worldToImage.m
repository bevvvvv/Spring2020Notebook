function [imageCoords] = worldToImage(worldCoords, cameraStruct)
%WORLDTOIMAGE Transform one or more world coordinate points to a 2D image
% point.
%   worldCooords - one or more 3D world coordinates
%   cameraStruct - camera calibration to project onto
camInfo = cameraStruct;
if nargin == 1
    % default to vue2
    camInfo = load('vue2CalibInfo.mat');
end

% x = P X_w
% make homogenous
worldCoords(4,:) = 1;
% convert
imageCoords = camInfo.Kmat * camInfo.Pmat * worldCoords;
% normalize
for i = 1:size(imageCoords, 2)
    imageCoords(1:2,i) = imageCoords(1:2,i) / imageCoords(3,i);
end
% remove "z"
imageCoords(3,:) = [];
imageCoords = floor(imageCoords);
end

