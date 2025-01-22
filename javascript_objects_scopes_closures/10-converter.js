#!/usr/bin/node
let count = 0;
module.exports = {
  converter: (base) => {
    console.log(`${count++}: ${item}`);
  }
};
