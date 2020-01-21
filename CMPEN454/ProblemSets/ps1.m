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
    disp('Second derivative convulution')
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
    disp('Second derivative cross correlation')
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
    % Border handling methods
    % Zero padding
    
    % Replication
    
    % Reflection
    
    % Wraparound

end