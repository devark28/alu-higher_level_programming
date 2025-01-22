#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      console.log(`${c.repeat(this.width)}\n`.repeat(this.height));
    } else {
      super.print();
    }
  }
}
module.exports = Square;
