#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

// Check if the correct number of arguments is provided
if (args.length !== 5) {
  console.error('Usage: node myScript.js sourceFile1 sourceFile2 destinationFile');
  process.exit(1); // Exit with an error code
}

const sourceFile1 = args[2];
const sourceFile2 = args[3];
const destinationFile = args[4];

// Read the content of the first source file
fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error('Error reading the first source file:', err);
    process.exit(1); // Exit with an error code
  }

  // Read the content of the second source file
  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error('Error reading the second source file:', err);
      process.exit(1); // Exit with an error code
    }

    // Concatenate the content of the two source files
    const concatenatedContent = data1 + data2;

    // Write the concatenated content to the destination file
    fs.writeFile(destinationFile, concatenatedContent, (err) => {
      if (err) {
        console.error('Error writing to the destination file:', err);
        process.exit(1); // Exit with an error code
      }
    });
  });
});
