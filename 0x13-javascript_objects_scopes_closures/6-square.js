#!/usr/bin/node

const square = require('./5-square');

class square extends square{
    charPrint(c){
        for (let index = 0; index < this.size; index++) {
            console.log(c === undefined ? 'X'.repeat(this.size): c.repeat(this.size))
        }
    }
}

