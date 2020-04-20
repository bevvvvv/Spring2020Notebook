function skel = constructSkeleton(coordinates)
%CONSTRUCTSKELETON Summary of this function goes here
%   Detailed explanation goes here
% add midpoints
skel = coordinates;
x = skel(1,:);
y = skel(2,:);
z = skel(3,:);
skel(:,13) = [mean([x(1),x(4)]);mean([y(1),y(4)]);mean([z(1),z(4)])];
skel(:,14) = [mean([x(7),x(10)]);mean([y(7),y(10)]);mean([z(7),z(10)])];
temp = skel;
skel(:,1) = temp(:,3);
skel(:,3) = temp(:,1);
skel(:,4) = temp(:,13);
skel(:,5) = temp(:,14);
skel(:,6) = temp(:,7);
skel(:,7) = temp(:,8);
skel(:,8) = temp(:,9);
skel(:,9) = temp(:,8);
skel(:,10) = temp(:,7);
skel(:,11) = temp(:,10);
skel(:,12) = temp(:,11);
skel(:,13) = temp(:,12);
skel(:,14) = temp(:,11);
skel(:,15) = temp(:,10);
skel(:,16) = temp(:,14);
skel(:,17) = temp(:,13);
skel(:,18) = temp(:,4);
skel(:,19) = temp(:,5);
skel(:,20) = temp(:,6);
end

