#!/usr/bin/node
function getNumberArgs() {
  const scriptArgs = process.argv.slice(2);
  return scriptArgs.length === 0 ? undefined : scriptArgs;
}


