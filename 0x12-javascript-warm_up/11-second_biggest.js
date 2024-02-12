#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const max = Math.max(...args);
  let secMax = 0;
  args.forEach(num => {
    if (max > num && num > secMax) {
      secMax = num;
    }
  });
  console.log(secMax);
}
