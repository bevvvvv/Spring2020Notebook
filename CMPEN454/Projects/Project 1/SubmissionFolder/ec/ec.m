clear;

directory     = './';    %the directory containing the images

%parameters
sigma     = 5;
threshold = 0.1;
rhoRes    = 2;
thetaRes  = pi/90;
nLines    = 50;
%end of parameters

imglist = dir(sprintf('%s/*.jpg', directory));

for i = 1:numel(imglist)
    
    %read in images%
    [path, imgname, dummy] = fileparts(imglist(i).name);
    img = imread(sprintf('%s/%s', directory, imglist(i).name));
    img = imresize(img, 0.25);
    
    if (ndims(img) == 3)
        img = rgb2gray(img);
    end
    
    img = double(img) / 255;
   
    %actual Hough line code function calls%  
    [Im] = myEdgeFilter(img, sigma);   
    [H,rhoScale,thetaScale] = myHoughTransform(Im, threshold, rhoRes, thetaRes);
    [rhos, thetas] = myHoughLines(H, nLines);
    lines = houghlines(Im>threshold, 180*(thetaScale/pi), rhoScale, [rhos,thetas],'FillGap',5,'MinLength',20);
    
    %everything below here just saves the outputs to files%
    fname = sprintf('%s/%s_01edge.png', directory, imgname);
    imwrite(sqrt(Im/max(Im(:))), fname);
    fname = sprintf('%s/%s_02threshold.png', directory, imgname);
    imwrite(Im > threshold, fname);
    fname = sprintf('%s/%s_03hough.png', directory, imgname);
    imwrite(H/max(H(:)), fname);
    fname = sprintf('%s/%s_04lines.png', directory, imgname);
    
    img2 = img;
    for j=1:numel(lines)
       img2 = drawLine(img2, lines(j).point1, lines(j).point2); 
    end     
    imwrite(img2, fname);
end