#!/usr/bin/node
if (Number.isNaN(Number(process.argv[2]))) {
  console.log(process.argv);
} else {
  console.log(Number(process.argv[2]));
}