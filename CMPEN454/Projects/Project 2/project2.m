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
mp4Path = ['Subject4-Session3-24form-Full-Take4-Vue2.mp4'; 'Subject4-Session3-24form-Full-Take4-Vue4.mp4'];

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
filenamevue2mp4 = mp4Path(1,:);
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
hold off;

%% Test triangulate
imageCoords1 = worldToImage([x; y; z], vue2);
imageCoords2 = worldToImage([x; y; z], vue4);
worldCoords = triangulate(imageCoords1, imageCoords2,  vue2, vue4);
disp('Reconstruction error');
disp(mean(L2([x; y; z], worldCoords)));

%% Epipolar Geometry
frameEpipolarViz(imageCoords1, imageCoords2, mocapFnum, vue2, vue4, mp4Path(1,:), mp4Path(2,:));

    
%% Quantitative Eval

% Calculate L2 error for each pair
% load data for all frames with confidence of 1
x = zeros(1,size(mocapJoints,2));
y = zeros(1,size(mocapJoints,2));
z = zeros(1,size(mocapJoints,2));
totalError = zeros(1);
for frame = 1:size(mocapJoints,1)
    if sum(mocapJoints(mocapFnum,:,4)) == 12
        x(frame,:) = mocapJoints(mocapFnum,:,1);
        y(frame,:) = mocapJoints(mocapFnum,:,2);
        z(frame,:) = mocapJoints(mocapFnum,:,3);
    end
    worldCoords = [x(frame); y(frame); z(frame)];
    imageCoords1 = worldToImage(worldCoords, vue2);
    imageCoords2 = worldToImage(worldCoords, vue4);
    recovered = triangulate(imageCoords1, imageCoords2, vue2, vue4);
    totalError(frame) = sum(L2(recovered, worldCoords));
end

% each joint stats
for i = 1:size(mocapJoints,2)
    worldCoords = [x(:,i)'; y(:,i)'; z(:,i)'];
    imageCoords1 = worldToImage(worldCoords, vue2);
    imageCoords2 = worldToImage(worldCoords, vue4);
    recovered = triangulate(imageCoords1, imageCoords2, vue2, vue4);
    values = L2(recovered, worldCoords);
    fprintf('Joint: %d\n',i);
    fprintf('Mean: %d\n',mean(values));
    fprintf('Stdev: %d\n',std(values));
    fprintf('Minimum: %d\n',min(values));
    fprintf('Median: %d\n',median(values));
    fprintf('Maximum: %d\n\n',max(values));
end

% all joint stats
worldCoords = [reshape(x(:,:),1,[]); reshape(y(:,:),1,[]); reshape(z(:,:),1,[])];
imageCoords1 = worldToImage(worldCoords, vue2);
imageCoords2 = worldToImage(worldCoords, vue4);
recovered = triangulate(imageCoords1, imageCoords2, vue2, vue4);
values = L2(recovered, worldCoords);
disp('Entire dataset L2 error stats');
fprintf('Mean: %d\n',mean(values));
fprintf('Stdev: %d\n',std(values));
fprintf('Minimum: %d\n',min(values));
fprintf('Median: %d\n',median(values));
fprintf('Maximum: %d\n\n',max(values));

figure(3)
plot(1:1:size(mocapJoints,1), totalError);

%% Qualitative Eval
% one input 3D skeleton
figure(4)
mocapFnum = 1000; %mocap frame number 1000
x = mocapJoints(mocapFnum,:,1);
y = mocapJoints(mocapFnum,:,2);
z = mocapJoints(mocapFnum,:,3);
skel = [x; y; z];
skel = constructSkeleton(skel);
plot3(skel(1,:), skel(2,:), skel(3,:));

% min error, max error indicies 2D plots

% one output 3D skeleton
worldCoords = [x; y; z];
imageCoords1 = worldToImage(worldCoords, vue2);
imageCoords2 = worldToImage(worldCoords, vue4);
recovered = triangulate(imageCoords1, imageCoords2, vue2, vue4);
skel = constructSkeleton(recovered);
figure(5)
plot3(skel(1,:), skel(2,:), skel(3,:));
