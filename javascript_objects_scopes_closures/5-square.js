#!/usr/bin/node
const Rectangle = require('javascript_objects_scopes_closures/4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Rectangle;
