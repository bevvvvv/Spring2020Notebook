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



