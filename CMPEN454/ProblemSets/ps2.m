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
    % 4. Derivative of Gaussian - edges are modes -> C
    % 5. Second Derivative of Gaussian is LaPlace - edges are zeros -> E
    
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
    
    %%
    disp('------------QUESTION 4-----------------')
    f = [-1, -2, -1;
        0, 0, 0;
        1, 2, 1];
    g = [0, 0, 0;
        0, 9, 9;
        0, 9, 9];
    
    % Q9 part B
    disp('SSD Score between f and g:')
    SSD = 0;
    for r = 1:3
        for c = 1:3
            SSD = SSD + (g(r, c) - f(r, c)) ^ 2;
        end
    end
    disp(SSD);
    
    % Q10 part C and Q8 part a
    raw = 0;
    denom_f = 0;
    denom_g = 0;
    f_mean = mean(mean(f));
    g_mean = mean(mean(g));
    for r = 1:3
        for c = 1:3
            raw = raw + (f(r,c) - f_mean) * (g(r, c) - g_mean);
            denom_f = denom_f + (f(r, c) - f_mean) ^ 2;
            denom_g = denom_g + (g(r, c) - g_mean) ^ 2;
        end
    end
    row = raw / (denom_f * denom_g) ^ 0.5;
    disp('Raw correlation? between f and g:')
    disp(raw);
    disp('Normalize Correlation between f and g:');
    disp(row);
    
    % Q11 part D
    % f can be written as a seperable filter
    disp('F as a seperable filter')
    part1 = [-1 0 1]';
    part2 = [1 2 1];
    disp(part1);
    disp(part2);
    disp('Vector multiplication results in:')
    disp(part1 * part2)
    
    % Q12 part E
    % g can be written as a seperable filter
    disp('G as a seperable filter')
    part1 = [0 1 1]';
    part2 = [0 9 9];
    disp(part1);
    disp(part2);
    disp('Vector multiplication results in:')
    disp(part1 * part2)
end

function result=cascaded_gaussian(n)
    result = n ^ 0.5; % since gaussian is sigma=1 in our case
end