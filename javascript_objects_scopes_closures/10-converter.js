#!/usr/bin/node
let count = 0;
module.exports = {
  converter: (base) => {
    return (num) => num.toString(base);
  }
};
