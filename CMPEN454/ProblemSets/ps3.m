% Joseph Sepich
% Feb 21, 2020
function ps3()
    %%
    disp('------------QUESTION 1-----------------')
    % Homogeneous Coordinates
    % recall [x, y] hetero to homo is [ax, ay, a]
    % line: ax + by + c = 0
    % http://www.maths.lth.se/matematiklth/personal/calle/datorseende13/notes/forelas2.pdf
    
    % Q1a
    l = [1, 2, 1];
    p = [-3, 1, 1];
    if check_point(p,l)
        disp('P is on line l (Q1a)');
    else
        disp('P is not on line l (Q1a)');
    end
    % Q1b
    p = [6, -3, 1];
    if check_point(p,l)
        disp('P is on line l (Q1b)');
    else
        disp('P is not on line l (Q1b)');
    end
    % Q1c
    l = [1, 2, 0];
    p = [-2 * l(2), 2 * l(1), l(1) + l(2)];
    if check_point(p,l)
        disp('P is on line l (Q1c)');
    else
        disp('P is not on line 1 (Q1c)');
    end
    % Q1d - find l
    p1 = [6, 10, 1];
    p2 = [-2, 2, 1];
    z = (p2(2) - p1(2)) / (p2(1) - p1(1));
    a = -1 * z;
    b = 1;
    c = z * p1(1) * p1(1);
    a = a / a;
    b = b / a;
    c = c / a;
    % THIS CALC WAS WRONG
    l1 = [2, 4, -10];
    l2 = [-1, 2, 1];
    l1_normalized = [(-1 * l1(1) / l1(2)), (-1 * l1(3) / l1(2))];
    l2_normalized = [(-1 * l2(1) / l2(2)), (-1 * l2(3) / l2(2))];
    x = (l2_normalized(2) - l1_normalized(2)) / (l1_normalized(1) - l2_normalized(1));
    y = l1_normalized(1) * x + l1_normalized(2);
    disp(['P is (',num2str(x),',',num2str(y),')']);
    
    %%
    disp('------------QUESTION 2-----------------')
    % Fundamental Matrix
    
    F = [-1, 2, 0;
         0, 10, -1;
         -10, 0, 2];
    
    % Q2a - find left epipole (prime is right)
    % recall Fe = 0
    f = 1;
    e_A = [-10;2;f];
    e_B = [-1;2;f];
    e_C = [0;-5;f];
    e_D = [0.2;0.1;f];
    disp(F * e_D);
    disp('D is left epipole (Q2a)');
    
    % Q2b - find right epipole (prime is right)
    % recall e''F = 0
    disp(e_A' * F);
    disp('A is right epipole (Q2b)');
    
    % Q2c - find epipolar line in right
    % recall l' = Fx
    p = [0;0;1];
    disp(F * p);
    disp('C is the line in the right image (Q2c)');
    
    % Q2D - find epipolar line in left
    % recall l = F'x'
    disp(F'*p);
    disp('D is the line in the left image (Q2d)');
    
    % Q2e - do any points match (right is prime)
    % recall x''Fx = 0
    x = [0; 0; f];
    x_prime_A = [100, 2, f];
    x_prime_B = [10, 2, f];
    x_prime_C = [1, 2, f];
    disp(x_prime_A * F * x);
    disp(x_prime_B * F * x);
    disp(x_prime_C * F * x);
    disp('All of the above might be correspondences (D Q2e)')
    
    %%
    disp('------------QUESTION 3-----------------')
    % Stereo Calculations
    % Q3a - Find Essential matrix
    % cameras are only translated 12 cm in x
    % R = I, t = [12, 0, 0];
    % E = ES, S = [0, -Tz, Ty; Tz 0 -Tx; -Ty Tx 0]
    R = [1, 0, 0;
        0, 1, 0;
        0, 0, 1];
    S = [0, 0, 0;
        0, 0 -12;
        0, 12, 0];
    E = R * S;
    disp(E);
    disp('Above is the E (Q3a)');
    
    % Q3b - same as previous with rotation
    % Rotation along y axis
    beta = deg2rad(90);
    R = [cos(beta), 0, sin(beta);
        0, 1, 0;
        -sin(beta), 0, cos(beta)];
    S = [0, 0, 0;
        0, 0 -12;
        0, 12, 0];
    E = R * S;
    disp(E);
    disp('Above is the new E (Q3b)');
    
    %%
    disp('------------QUESTION 4-----------------')
    % Stereo rect
    % Q4a - same as 3b format
    % two rotations - -90 deg around V(y), -90 deg around U(x)
    theta = deg2rad(-90);
    R_y = [cos(theta), 0, sin(theta);
        0, 1, 0;
        -sin(theta), 0, cos(theta)];
    R_x = [1, 0, 0;
        0, cos(theta), -sin(theta);
        0, sin(theta), cos(theta)];
    R = R_x * R_y;
    S = [0, -2, 12;
        2, 0 -6;
        -12, 6, 0];
    E = R * S;
    disp(R);
    disp(S);
    disp('Q4a E = RS');
    
    % Q4b - find epipoles
    E = R * S;
    [U,S,V] = svd(E);
    e = V(:,3);
    e = e ./ e(3);
    e_prime = [(1/6) (-1/2) 1];
    disp(e);
    disp(e_prime);
    disp('Q4b e and e prime');
end

function on_line=check_point(p, l)
    p_homo = p ./ p(3);
    if sum(p_homo.*l) == 0
        on_line = 1;
    else
        on_line = 0;
    end
end