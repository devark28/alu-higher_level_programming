#!/usr/bin/node
function getArgs() {
  const scriptArgs = process.argv.slice(2);
  return scriptArgs.length === 0 ? undefined : scriptArgs;
}

function getSecondLargest(elements = []) {
  if (arguments.length <= 1) {
    return 0;
  }
  return elements.map(Number).toSorted((a, b) => a - b).at(1);
}

console.log(getSecondLargest(getArgs()));
