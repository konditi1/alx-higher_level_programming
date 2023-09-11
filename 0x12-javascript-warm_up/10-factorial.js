#!/usr/bin/node
function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
const args = process.argv;
const parsedInt = parseInt(args[2]);
if (isNaN(parsedInt)) {
  console.log(1);
} else {
  console.log(factorial(parsedInt));
}
