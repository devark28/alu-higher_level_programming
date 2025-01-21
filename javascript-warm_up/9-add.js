#!/usr/bin/node
if (Number.isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  const n1 = Number(process.argv[2]);
  const n2 = Number(process.argv[3]);
  console.log(add(n1, n2));
}

function add(a, b) {
  return a + b;
}
