%% CMPEN 454
% PS4
% Joseph Sepich

disp('----------QUESTION 1-----------')
f = 100; % meters
real_h = 20; % meters
f_mm = f * 1000;
h_mm = real_h * 1000;
disp(h_mm * 15 / f_mm);
disp('millimeters');

%%
disp('----------QUESTION 2-----------')
f = 50; % mm
h_mm = 25;
f_m = 25 / 1000;
h_m = 50 / 1000;
person_h = 2; %meters
disp(person_h * f_m / h_m);
disp('meters');


%%
disp('----------QUESTION 4a-----------')
% To find a simple stero depth use the following equation
% d = (bf) / Z
% b is the baseline (offset of cameras)
% f is focal length
% Z is depth
% d is disparity of pixel (x - x')
f = 50; % pixels
b = 40; % cm
d = 25; % pixels
disp(b * f / d);
disp('centimeters');

disp('----------QUESTION 4b-----------')
f = 50; % pixels
b = 40; % cm
Z = 80; % cm
disp(b * f / Z);
disp('pixels');

disp('----------QUESTION 4c-----------')
f = 50; % pixels
b = 40; % cm
Z = 50; % cm
disp(b * f / Z);
disp('pixels');

disp('----------QUESTION 4d-----------')
f = 50; % pixels
b = 40; % cm
d = 1; % pixels
disp(b * f / d);
disp('centimeters');

disp('----------QUESTION 4e-----------')
disp('Say we use our previous focal length and baseline');
f = 50; % pixels
b = 40; % cm
%for d = 0:16
%    disp(b * f / d);
%end
disp('16 possible depths');

%%
disp('----------QUESTION 5a-----------')
f = 8; % mm
b_AB = 120; % mm
b_AC = 240; % mm

Z = 80; % mm
disp(b_AB * f / Z);
disp('millimeters');

disp('----------QUESTION 5b-----------')
Z = 80; % mm
disp(b_AC * f / Z);
disp('millimeters');

disp('----------QUESTION 5b-----------')
d = 0.004; % mm
disp((b_AC * f / d) / 1000); % larger baseline can measure larger distances
disp('meters');

%%
disp('----------QUESTION 11-----------')
S = [1, 0, 0, -10;
     0, 1, 0, -2;
     0, 0, 1, -5;
     0, 0, 0, 1];
theta = deg2rad(-90);
R = [0, -1, 0, 0;
        0, 0, 1, 0;
        -1, 0, 0, 0;
        0, 0, 0, 1];
disp('Essential Matrix data');
disp(S);
disp(R);

E = R * S;
world = [8; 6; 7; 1];
disp(E);
cam_coords = E * world;
disp(cam_coords);
f = 5; % mm
x = f * cam_coords(1) / cam_coords(3);
y = f * cam_coords(2) / cam_coords(3);
disp(x);
disp(y);

%%
disp('----------QUESTION 13-----------')
load cameraPmatrix.mat % loads Pmat
disp('Camera location');
disp(Pmat(:,4));
inv_Pmat = inv(Pmat);
z_axis = inv_Pmat * [0; 0; 1; 1];
z_axis = z_axis(1:3,:);
z_axis = z_axis / norm(z_axis);
disp(z_axis);

disp('U');
disp(Pmat(1,4) + z_axis(1,1) * 5);
disp('V');
disp(Pmat(2,4) + z_axis(2,1) * 5);
disp('W');
disp(Pmat(3,4) + z_axis(3,1) * 5);

