#!/usr/bin/node
const list = require('100-data.js');
module.exports = {
  converter: (base) => {
    return (num) => num.toString(base);
  }
};
