function [worldCoords] = triangulate(imageCoords1,imageCoords2, cam1, cam2)
%TRIANGULATE Recovers 3D scene points from 2D image plane coordinates.
%   imageCoords1 - image coordinates from cam 1
%   imageCoords2 - image coordinates from cam 2
%   cam1 - camera 1 calibration struct
%   cam2 - camera 2 calibration struct
camInfo1 = cam1;
camInfo2 = cam2;
if nargin == 2
    camInfo1 = load('vue2CalibInfo.mat');
elseif nargin == 3
    camInfo2 = load('vue4CalibInfo.mat');
end
P = camInfo1.Kmat * camInfo1.Pmat;
P_prime = camInfo2.Kmat * camInfo2.Pmat;
x = imageCoords1(1,:);
y = imageCoords1(2,:);
x_prime = imageCoords2(1,:);
y_prime = imageCoords2(2,:);

worldCoords = zeros(3, size(imageCoords1,2));

for i = 1:size(imageCoords1,2)
    A = [y(i) * P(3,:) - P(2,:);
        P(1,:) - x(i) * P(3,:); 
        y_prime(i) * P_prime(3,:) - P_prime(2,:);
        P_prime(1,:) - x_prime(i) * P_prime(3,:)];

    % solve SVD SX = 0
    [U, S, V] = svd(A);
    worldCoords(:,i) = V(1:3,4) / V(4,4);
end

end

