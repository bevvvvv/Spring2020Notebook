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
    disp(['l is ',num2str(a),'X + ',num2str(b),'Y + ',num2str(c)]);
    % Q1e - find p
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
    e = [0.2;0.1;f];
    F * e
end

function on_line=check_point(p, l)
    p_homo = p ./ p(3);
    if sum(p_homo.*l) == 0
        on_line = 1;
    else
        on_line = 0;
    end
end