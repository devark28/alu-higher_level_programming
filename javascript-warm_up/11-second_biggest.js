#!/usr/bin/node
function getArgs() {
  const scriptArgs = process.argv.slice(2);
  return scriptArgs.length === 0 ? undefined : scriptArgs;
}

function getSecondLargest(elements = []) {
  if (elements.length <= 1) {
    return 0;
  }
  let nums = elements.map(Number);
  return nums.sort((a, b) => a - b).at(1);
}

console.log(getSecondLargest(getArgs()));
