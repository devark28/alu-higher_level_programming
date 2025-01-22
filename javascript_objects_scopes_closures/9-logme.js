#!/usr/bin/node
module.exports = {
  logMe: () => {
    return list.reduceRight((acc, ele) => acc.concat(ele), []);
  }
};
