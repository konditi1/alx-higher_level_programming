#!/usr/bin/node

// Define the repeat function using the specified prototype
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Export the callMeMoby function so that it's visible from outside
module.exports.callMeMoby = callMeMoby;
