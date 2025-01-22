#!/usr/bin/node
module.exports = {
  logMe: (item) => {
    return list.reduceRight((acc, ele) => acc.concat(ele), []);
  }
};
