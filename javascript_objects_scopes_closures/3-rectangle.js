#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = '';
    let i = 0;
    for (i = 0; i < this.width; i++) {
      row += 'X';
    }
    for (i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}
module.exports = Rectangle;
