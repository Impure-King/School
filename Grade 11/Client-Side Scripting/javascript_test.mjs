import {solve} from "numjs";
nj = require("numjs");
x = nj.array([1, 2, 3]);
y = nj.array([[1],
              [4],
              [9]])
design_matrix = function(x) {
    array = nj.concatenate([nj.ones((3)), x, nj.multiply(x, x)]);
    array = array.reshape(3, 3);
    array = nj.transpose(array);
    return array;
}
const X = design_matrix(x)
console.log(X);

calculate_theta = function(X, y) {
    return solve(X, y);
}
console.log(calculate_theta(X, y))