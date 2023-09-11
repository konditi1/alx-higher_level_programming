#!/usr/bin/node
// Remove the first two arguments (interpreter and script name)
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  // convert the arguments into integers and remove dublicate using set
  const uniqueIntegers = [...new Set(args.map(args => parseInt(args)))];
  // Sort the unique integers in descending order
  const sortedIntegers = uniqueIntegers.sort((a, b) => b - a);
  // The second biggest integer will be at index 1 (index 0 is the largest)
  console.log(sortedIntegers[1]);
}
