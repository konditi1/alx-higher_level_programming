#!/usr/bin/node
const args = process.argv;
const parsedInt = parseInt(args[2]);
if (isNaN(parsedInt)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parsedInt; i++) {
    console.log('C is fun');
  }
}
