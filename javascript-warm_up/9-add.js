#!/usr/bin/node
if (Number.isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  const num1 = Number(process.argv[2]).toFixed(0);
  const num2 = Number(process.argv[3]).toFixed(0);
  console.log(add());
}

function add(a, b) {
  return a + b;
}
