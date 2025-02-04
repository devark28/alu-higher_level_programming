#!/usr/bin/node
const [, , URL] = process.argv;
require('request')(URL, (err, res, body) => {
  // console.log(JSON.parse(body));
  console.log(JSON.parse(body).reduce((acc, usr) => {
    console.log(acc);
    if(acc[usr?.userId] && usr.complete){
      acc[usr?.userId] += 1;
    }else{
      acc[usr?.userId] = 1;
    }
    return acc;
    // return {
    //   [usr?.userId]: (acc[usr?.userId] || 0) + 1,
    //   [usr?.userId]: acc[usr?.userId] ? acc[usr?.userId] + 1 : 1,
    //   ...acc
    // };
  }, {}));
});
