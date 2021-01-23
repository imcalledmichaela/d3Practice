let values = [-1.0, 2.1, 3.3, 0.4, 1.8, 2,5, 4.5, 5.3, 3.7, 4.6];
d3 = require("d3")
let check = [-1.0, 3.3, 5.3]
console.log(check)
var min = d3.min(values)
var max = d3.max(values)
var median = d3.median(values)
console.log(min)
console.log(max)
console.log(median)