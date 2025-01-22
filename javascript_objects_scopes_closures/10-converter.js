#!/usr/bin/node
let count = 0;
module.exports = {
  converter: (item) => {
    console.log(`${count++}: ${item}`);
  }
};
