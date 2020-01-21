% Joseph Sepich
% Jan 21, 2020
function ps1()
    % Problem 1
    % Function
    function out = z(x, y)
        out = x^2 + 2 * y^2 - 6 * x - 8 * y + 20;
    end

    % 1a x,y=1,1 gradient is (-4,-4)
    % 1b x,y=1,2 gradient is (-4,0) which is less magnitude
    % 1c x,y=3,2 gradient is (0,0)
    % 1d what is (3,2) gradient?
    X = -4:0.5:4;
    Y = -4:0.5:4;
    Z = zeros(length(X), length(Y));
    for x = 1:length(X)
        for y = 1:length(Y)
            Z(x, y) = z(x,y);
        end
    end
    surf(X, Y, Z);

end