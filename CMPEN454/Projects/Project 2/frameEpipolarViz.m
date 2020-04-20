function [] = frameEpipolarViz(cam1Coords,cam2Coords,frameNum,cam1,cam2,mp41Path,mp42Path)
%FRAMEEPIPOLARVIZ Creates epipolar geometry images from two mocap cameras.
%   cam1Coords - mocap point coordinates in image from cam 1
%   cam2Coords - mocap point coordinates in image from cam 2
%   frameNum - mocap data frame number to render
%   cam1 - camera 1 calibration struct
%   cam2 - camera 2 calibration struct
%   mp41Path - path to cam 1 mp4 file (to grab image)
%   mp42Path - path to cam 2 mp4 file (to grab image)

% start by calculating epipole
% epipole is location of projection of other camera onto image plane
e = worldToImage(cam2.position', cam1);
e_prime = worldToImage(cam1.position', cam2);

% load images
cam1video = VideoReader(mp41Path);
cam2video = VideoReader(mp42Path);

cam1video.CurrentTime = (frameNum-1)*(50/100)/cam1video.FrameRate;
vid2Frame1 = readFrame(cam1video);

cam2video.CurrentTime = (frameNum-1)*(50/100)/cam2video.FrameRate;
vid2Frame2 = readFrame(cam2video);

xVal = linspace(0,size(vid2Frame1,2),size(vid2Frame1,2));
lines1 = zeros(size(cam1Coords,2),size(vid2Frame1,2));
lines2 = zeros(size(cam1Coords,2),size(vid2Frame1,2));

% calculate epipolar lines for each image
for i = 1:size(cam1Coords,2)
    lines1(i,:) = ((cam1Coords(2,i) - e(2)) / (cam1Coords(1,i) - e(1)) .* (xVal - e(1))) + e(2);
    lines2(i,:) = ((cam2Coords(2,i) - e_prime(2)) / (cam2Coords(1,i) - e_prime(1)) .* (xVal - e_prime(1))) + e_prime(2);
end

colors = 'ymcrgbw';
% plot lines
figure(1)
image(vid2Frame1)
hold on;
for i = 1:size(cam1Coords,2)
    color = mod(i,size(colors,2)) + 1;
    plot(xVal, lines1(i,:), 'Color', colors(color));
    scatter(cam1Coords(1,i), cam1Coords(2,i), 20, colors(color), 'filled');
end
    
hold off;
figure(2)
image(vid2Frame2)
hold on;
for i = 1:size(cam2Coords,2)
    color = mod(i,size(colors,2)) + 1;
    plot(xVal, lines2(i,:), 'Color', colors(color));
    scatter(cam2Coords(1,i), cam2Coords(2,i), 20, colors(color), 'filled');
end
end

