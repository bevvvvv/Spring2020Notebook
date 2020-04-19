%% Clear and load
% clear existing variables
clear

% load mocapJoints data
load('Subject4-Session3-Take4_mocapJoints.mat');
% load vue2 structure
load('vue2CalibInfo.mat');
% load vue4 structure
load('vue4CalibInfo.mat');
% dims: frame X joint X coords

%% Point Extraction Example
mocapFnum = 1000; %mocap frame number 1000
x = mocapJoints(mocapFnum,:,1);
%array of 12 X coordinates
y = mocapJoints(mocapFnum,:,2);
% Y coordinates
z = mocapJoints(mocapFnum,:,3);
% Z coordinates
%conf = mocapJoints(mocapFnum,:,4);
%confidence values -> ignore frames without all 1 confidence

%% Camera Param Example
% vue2

%% Load mp4/check projection translation

%initialization of VideoReader for the vue video.
%YOU ONLY NEED TO DO THIS ONCE AT THE BEGINNING
filenamevue2mp4 = 'Subject4-Session3-24form-Full-Take4-Vue2.mp4';
vue2video = VideoReader(filenamevue2mp4);

%now we can read in the video for any mocap frame mocapFnum.
%the (50/100) factor is here to account for the difference in frame
%rates between video (50 fps) and mocap (100 fps).
vue2video.CurrentTime = (mocapFnum-1)*(50/100)/vue2video.FrameRate;
vid2Frame = readFrame(vue2video);
image(vid2Frame)

%% Test worldToImage
imageCoords = worldToImage([x; y; z], vue2);
hold on;
scatter(imageCoords(1,:), imageCoords(2,:), 5, 'red');

%% Test triangulate
imageCoords1 = worldToImage([x; y; z], vue2);
imageCoords2 = worldToImage([x; y; z], vue4);
worldCoords = triangulate(imageCoords1, imageCoords2,  vue2, vue4);
disp('Reconstruction error');
disp(averageL2([x; y; z], worldCoords));
