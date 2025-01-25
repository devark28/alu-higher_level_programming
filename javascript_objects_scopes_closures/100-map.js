#!/usr/bin/node
const list = require('')
module.exports = {
  converter: (base) => {
    return (num) => num.toString(base);
  }
};
