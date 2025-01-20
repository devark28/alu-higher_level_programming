#!/usr/bin/node
if (process.argv.length - 1 === 0) {
    console.log('No argument');
} else if (process.argv.length - 1 === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
