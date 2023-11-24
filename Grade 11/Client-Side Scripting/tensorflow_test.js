const nj = require("numjs");
const tf = require("@tensorflow/tfjs");

let array = nj.array([1, 2, 3]);
let array1 = tf.tensor2d([1, 2, 3], [3, 1]);
let array2 = tf.transpose(tf.concat([tf.ones(array1.shape),array1, tf.mul(array1, array1)], 1))
console.log(array);
console.log(array1);
console.log(array2.as2D());