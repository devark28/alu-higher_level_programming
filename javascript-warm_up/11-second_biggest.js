#!/usr/bin/node
function getArgs() {
  const scriptArgs = process.argv.slice(2);
  return scriptArgs.length === 0 ? undefined : scriptArgs;
}

function getSecondLargest(elements = []) {
  return elements.map(Number).toSorted((a, b) => a - b).at(1) ?? 0
}

console.log(getSecondLargest(getArgs()));
