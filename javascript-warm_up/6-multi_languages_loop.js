#!/usr/bin/node
let strs = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let curr = null;
while (curr = strs.shift()) {
  console.log(curr);
}
