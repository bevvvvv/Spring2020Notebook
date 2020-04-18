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
conf = mocapJoints(mocapFnum,:,4);
%confidence values -> ignore frames without all 1 confidence

%% Camera Param Example
vue2
