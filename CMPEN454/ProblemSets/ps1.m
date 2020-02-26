% Joseph Sepich
% Jan 21, 2020
function ps1()
    %%
    % Problem 1
    % Function
    disp('------------QUESTION 1-----------------')
    function out = z(x, y)
        out = x^2 + 2 * y^2 - 6 * x - 8 * y + 20;
    end
    
    % Question 1: Gradients
    % 1a x,y=1,1 gradient is (-4,-4)
    % 1b x,y=1,2 gradient is (-4,0) which is less magnitude
    % 1c x,y=3,2 gradient is (0,0)
    % 1d what is (3,2) gradient?
    [Y, X] = ndgrid(0:0.01:4, 1:0.01:5);
    Z = arrayfun(@(y,x) z(x,y), Y, X);
    surf(X, Y, Z, 'edgecolor', 'none');
    
    %%
    % Question 2: Convulation/Correlation
    % 2a Compute Convolution
    disp('------------ QUESTION 2-----------------')
    disp('First derivative convulution')
    pixels = [40, 50, 60, 80, 80, 80, 30];
    filter = [1, 0, -1];
    convu = zeros(1,5);
    for pixel = 1:length(pixels)
        if pixel == 1
            continue
        elseif pixel == length(pixels)
            break
        end
        convu(pixel-1) = sum(filter .* flip(pixels(pixel-1:pixel+1)));
    end
    disp(convu)
    
    % 2b would answer be different with cross correlation?
    disp('First derivative cross correlation')
    crossCorr = zeros(1,5);
    for pixel = 1:length(pixels)
        if pixel == 1
            continue
        elseif pixel == length(pixels)
            break
        end
        crossCorr(pixel-1) = sum(filter .* pixels(pixel-1:pixel+1));
    end
    disp(crossCorr)
    
    % 2c new filter
    disp('Laplace convulution')
    filter = [1 -2 1];
    convu = zeros(1,5);
    for pixel = 1:length(pixels)
        if pixel == 1
            continue
        elseif pixel == length(pixels)
            break
        end
        convu(pixel-1) = sum(filter .* flip(pixels(pixel-1:pixel+1)));
    end
    disp(convu)
    
    % 2d would previous be different with cross?
    disp('Laplace cross correlation')
    crossCorr = zeros(1,5);
    for pixel = 1:length(pixels)
        if pixel == 1
            continue
        elseif pixel == length(pixels)
            break
        end
        crossCorr(pixel-1) = sum(filter .* pixels(pixel-1:pixel+1));
    end
    disp(crossCorr)
    
    %%
    disp('------------ QUESTION 2E-----------------')
    disp('Zero padding Laplace')
    pixels = [0, 40, 50, 60, 80, 80, 80, 30, 0];
    filter = [1 -2 1];
    convu = zeros(1,5);
    for pixel = 2:length(pixels)
        if pixel == length(pixels)
            break
        end
        convu(pixel-1) = sum(filter .* pixels(pixel-1:pixel+1));
    end
    disp(convu)
    
    % Replication
    disp('Replication padding Laplace')
    pixels = [40, 40, 50, 60, 80, 80, 80, 30, 30];
    crossCorr = zeros(1,5);
    for pixel = 2:length(pixels)
        if pixel == length(pixels)
            break
        end
        crossCorr(pixel-1) = sum(filter .* pixels(pixel-1:pixel+1));
    end
    disp(crossCorr)
    
    % Reflection
    disp('Reflection Padding LaPlace')
    pixels = [40, 40, 50, 60, 80, 80, 80, 30, 30];
    convu = zeros(1,5);
    for pixel = 2:length(pixels)
        if pixel == length(pixels)
            break
        end
        convu(pixel-1) = sum(filter .* pixels(pixel-1:pixel+1));
    end
    disp(convu)
    
    % Wraparound
    disp('Wraparound Padding LaPlace')
    pixels = [30, 40, 50, 60, 80, 80, 80, 30, 40];
    crossCorr = zeros(1,5);
    for pixel = 2:length(pixels)
        if pixel == length(pixels)
            break
        end
        crossCorr(pixel-1) = sum(filter .* pixels(pixel-1:pixel+1));
    end
    disp(crossCorr)
    
    %%
    disp('------------ QUESTION 3-----------------')
    % 2D  Convolution
    disp('2D Convulution')
    filter_f = [1,-1,-1; 1,2,-1; 1,1,1];
    row_length = length(filter_f(:,1));
    col_length = length(filter_f(1,:));
    diff_r = (row_length - 1) / 2;
    diff_c = (col_length - 1) / 2;
    image_h = [0,0,0,0,0,0;
               0,2,2,2,3,0;
               0,2,1,3,3,0;
               0,2,2,1,2,0;
               0,1,3,2,2,0;
               0,0,0,0,0,0];
    convu = zeros(4,4);
    for r = 2:(length(image_h(1,:))-diff_r)
        for c = 2:(length(image_h(:,1))-diff_c)
            image_elem = image_h(r-diff_r:r+diff_r,c-diff_c:c+diff_c);
            filter = flipud(fliplr(filter_f));
            convu(r-1, c-1) = sum(sum(filter .* image_elem));
        end
    end
    disp(convu)
    
    %%
    disp('------------ QUESTION 4-----------------')
    % Computing Gradients
    % Problem: Used cross correlation with filter [1/2, 0, -1/2] instead of
    % convolution
    
    % 4a: The computed gradient is perpendicular to correct
    % False, the convuluted gradient will be parallel, but in the opposite
    % direction as the correlated gradient (left versus right)
    filter_r = [0.5, 0, -0.5];
    filter_c = [1;1;1];
    filter_2d = filter_c * filter_r;
    disp('Filter in 2D (Cross)');
    disp(filter_2d);
    disp('Filter in 2D (Convulution)');
    disp(flipud(fliplr(filter_2d)));
    
    % 4b - will point downhill instaed of uphill
    % true, the opposite direction
    
    % 4c - still have same local min/max
    % true, magnitude should remain the same
    
    % 4d - still have same magnitude
    % true
    
    %%
    disp('------------ QUESTION 5-----------------')
    % Use convulution, but wrong values
    % 5a - Computed gradient will be perpendicular
    disp('Right value filter')
    convu = zeros(4,4);
    for r = 2:(length(image_h(1,:))-diff_r)
        for c = 2:(length(image_h(:,1))-diff_c)
            image_elem = image_h(r-diff_r:r+diff_r,c-diff_c:c+diff_c);
            filter = flipud(fliplr(filter_2d));
            convu(r-1, c-1) = sum(sum(filter .* image_elem));
        end
    end
    disp(convu)
    filter_r2 = [1, 0, -1];
    filter_2d2 = filter_c * filter_r2 ;
    disp('Wrong value gradient filter');
    convu = zeros(4,4);
    for r = 2:(length(image_h(1,:))-diff_r)
        for c = 2:(length(image_h(:,1))-diff_c)
            image_elem = image_h(r-diff_r:r+diff_r,c-diff_c:c+diff_c);
            filter = flipud(fliplr(filter_2d2));
            convu(r-1, c-1) = sum(sum(filter .* image_elem));
        end
    end
    disp(convu)
end