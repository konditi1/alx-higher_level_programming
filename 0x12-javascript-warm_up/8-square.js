#!/usr/bin/node
const args = process.argv;
const parsedInt = parseInt(args[2]);
if (isNaN(parsedInt)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parsedInt; i++) {
    // this is the shortest
    // console.log('X'.repeat(parsedInt));
    for (let j = 0; j < parsedInt; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
