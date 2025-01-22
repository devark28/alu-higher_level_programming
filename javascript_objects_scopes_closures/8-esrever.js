#!/usr/bin/node
module.exports = {
  esrever: (list) => {
    return list.reduceRight((acc, ele) => acc.push(ele), []);
  }
};
