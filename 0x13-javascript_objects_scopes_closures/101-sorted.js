#!/usr/bin/node
const { dict } = require('./101-data.js');
// Create an empty dictionary to store the result
const resultDict = {};

// Iterate through the original dictionary's properties
for (const userId in dict) {
  const occurrence = dict[userId];

  // Check if the occurrence count is already a key in the result dictionary
  if (resultDict[occurrence]) {
    resultDict[occurrence].push(userId);
  } else {
    // If not, create a new key with an array containing the user id
    resultDict[occurrence] = [userId];
  }
}

// Print the result dictionary
console.log(resultDict);
