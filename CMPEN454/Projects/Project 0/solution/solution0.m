% Joseph Sepich
% Jan 21, 2020
function ps1()
    %%
    disp('------------QUESTION 1-----------------')
    % This question is all about filter matching (1D intensity graph)
    % There is a filter description and an output image
    % 1. Gaussian filter sigma = 3 will have smoothing effect (same mode) D
    % 2. Gaussian filter sigma = 6 will smooth more (same mode) -> F
    % 3. Finite difference filter  will be derivative -> B
    % 4. Derivative of Gaussian - edges are modes -> 
    % 5. Second Derivative of Gaussian is LaPlace - edges are zeros ->
    
    %%
    disp('------------QUESTION 2-----------------')
    % Filter matching images
    % 1. Gaussian sigma 10 - smoothing -> C
    % 2. Derivative of gaussian in x - modes at vertical edges -> E
    % 3. Derivative of gaussian in y - modes at horizontal edges -> D
    % 4. Second Derivative of gaussian in x - zeros at vertical edges -> F
    % 5. LaPlacian of Gaussian - edges are outlined bright -> A
    % 6. Harris Corner (R) - __ -> B
    
    %%
    disp('------------QUESTION 3-----------------')
    % Cascaded Gaussian function
    % Recall that you add varaince of two convuluated gaussians
    disp('G ^ 1 - should be 1')
    n = 1;
    disp(cascaded_gaussian(n));
    disp('G ^ 2')
    n = 2;
    disp(cascaded_gaussian(n));
    disp('G ^ 3')
    n = 3;
    disp(cascaded_gaussian(n));
    disp('G ^ 4')
    n = 4;
    disp(cascaded_gaussian(n));
    disp('G ^ 5')
    n = 5;
    disp(cascaded_gaussian(n));
    disp('G ^ 100')
    n = 100;
    disp(cascaded_gaussian(n));
end

function result=cascaded_gaussian(n)
    result = n ^ 0.5;
end