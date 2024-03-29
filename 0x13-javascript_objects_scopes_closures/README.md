# Resources

<b>Read or watch:</b>

* [JavaScript object basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)
* [Object-oriented JavaScript (read all examples!)](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
* [Class - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
* [super - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
* [extends - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
* [Object prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
* [Inheritance in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
* [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
* [this/self](https://alistapart.com/article/getoutbindingsituations/)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

# Tasks

## 0. Rectangle #0

### File: [0-rectangle.js](0-rectangle.js) | [0-main.js](0-main.js)

<b>Write an empty class `Rectangle` that defines a rectangle:</b>

* You must use the `class` notation for defining your class

```
guillaume@ubuntu:~/0x13$ cat 0-main.js
#!/usr/bin/node
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);

guillaume@ubuntu:~/0x13$ ./0-main.js
Rectangle {}
[Class: Rectangle]
guillaume@ubuntu:~/0x13$ 
```
   
## 1. Rectangle #1

### File: [1-rectangle.js](1-rectangle.js) | [1-main.js](1-main.js)

<b>Write a class `Rectangle` that defines a rectangle:</b>

* You must use the class notation for defining your class
* The constructor must take 2 arguments `w` and `h`
* Initialize the instance attribute `width` with the value of `w`
* Initialize the instance attribute `height` with the value of `h`

```
guillaume@ubuntu:~/0x13$ cat 1-main.js
#!/usr/bin/node
const Rectangle = require('./1-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

guillaume@ubuntu:~/0x13$ ./1-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
guillaume@ubuntu:~/0x13$ 
```
   
## 2. Rectangle #2

### File: [2-rectangle.js](2-rectangle.js) | [2-main.js](2-main.js)

<b>Write a class `Rectangle` that defines a rectangle:</b>

* You must use the class notation for defining your class
* The constructor must take 2 arguments `w` and `h`
* Initialize the instance attribute `width` with the value of `w`
* Initialize the instance attribute `height` with the value of `h`
* If `w` or `h` is equal to 0 or not a positive integer, create an empty object

```
guillaume@ubuntu:~/0x13$ cat 2-main.js
#!/usr/bin/node
const Rectangle = require('./2-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

const r4 = new Rectangle(2, 0);
console.log(r4);
console.log(r4.width);
console.log(r4.height);

guillaume@ubuntu:~/0x13$ ./2-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
guillaume@ubuntu:~/0x13$ 
```
   
3. Rectangle #3

### File: [3-rectangle.js](3-rectangle.js) | [3-main.js](3-main.js)

<b>Write a class `Rectangle` that defines a rectangle:</b>

You must use the `class` notation for defining your class
The constructor must take 2 arguments: `w` and `h`
Initialize the instance attribute `width` with the value of `w`
Initialize the instance attribute `height` with the value of `h`
If `w` or `h` is equal to 0 or not a positive integer, create an empty object
Create an instance method called `print()` that prints the rectangle using the character `X`

```
guillaume@ubuntu:~/0x13$ cat 3-main.js
#!/usr/bin/node
const Rectangle = require('./3-rectangle');

const r1 = new Rectangle(2, 3);
r1.print();

const r2 = new Rectangle(10, 5);
r2.print();

guillaume@ubuntu:~/0x13$ ./3-main.js
XX
XX
XX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
guillaume@ubuntu:~/0x13$ 
```
   
## 4. Rectangle #4

### File: [4-main.js](4-main.js) | [4-rectangle.js](4-rectangle.js)

<b>Write a class `Rectangle` that defines a rectangle:</b>

* You must use the `class` notation for defining your class
* The constructor must take 2 arguments: `w` and `h`
* Initialize the instance attribute `width` with the value of `w`
* Initialize the instance attribute `height` with the value of `h`
* If `w` or `h` is equal to 0 or not a positive integer, create an empty object
* Create an instance method called `print()` that prints the rectangle using the character X
* Create an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle
* Create an instance method called `double()` that multiples the `width` and the `height` of the rectangle by 2

```
guillaume@ubuntu:~/0x13$ cat 4-main.js
#!/usr/bin/node
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(2, 3);
console.log('Normal:');
r1.print();

console.log('Double:');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();

guillaume@ubuntu:~/0x13$ ./4-main.js
Normal:
XX
XX
XX
Double:
XXXX
XXXX
XXXX
XXXX
XXXX
XXXX
Rotate:
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x13$ 
```
   
## 5. Square #0

### File: [5-square.js](5-square.js) | [5-main.js](5-main.js)

<b>Write a class `Square` that defines a square and inherits from `Rectangle` of `4-rectangle.js`:</b>

* You must use the `class` notation for defining your class and `extends`
* The constructor must take 1 argument: size
* The constructor of `Rectangle` must be called (by using `super()`)

```
guillaume@ubuntu:~/0x13$ cat 5-main.js
#!/usr/bin/node
const Square = require('./5-square');

const s1 = new Square(4);
s1.print();
s1.double();
s1.print();

guillaume@ubuntu:~/0x13$ ./5-main.js
XXXX
XXXX
XXXX
XXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
guillaume@ubuntu:~/0x13$ 
```
   
## 6. Square #1

### File: [6-square.js](6-square.js) | [6-main.js](6-main.js)

<b>Write a class `Square` that defines a square and inherits from `Square` of `5-square.js`:</b>

* You must use the class notation for defining your `class` and `extends`
* Create an instance method called `charPrint(c)` that prints the rectangle using the character c
If `c` is `undefined`, use the character `X`

```
guillaume@ubuntu:~/0x13$ cat 6-main.js
#!/usr/bin/node
const Square = require('./6-square');

const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');

guillaume@ubuntu:~/0x13$ ./6-main.js
XXXX
XXXX
XXXX
XXXX
CCCC
CCCC
CCCC
CCCC
guillaume@ubuntu:~/0x13$ 
```
   
## 7. Occurrences

### File: [7-occurrences.js](7-occurrences.js) | [7-main.js](7-main.js)

<b>Write a function that returns the number of occurrences in a list:</b>

* Prototype: `exports.nbOccurences = function (list, searchElement)`

```
guillaume@ubuntu:~/0x13$ cat 7-main.js
#!/usr/bin/node
const nbOccurences = require('./7-occurrences').nbOccurences;

console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nbOccurences(["S", 12, "c", "S", "School", 8], "S"));

guillaume@ubuntu:~/0x13$ ./7-main.js
1
4
2
guillaume@ubuntu:~/0x13$ 
```
   
## 8. Esrever

### File: [8-esrever.js](8-esrever.js) | [8-main.js](8-main.js)

<b>Write a function that returns the reversed version of a list:</b>

* Prototype: `exports.esrever = function (list)`
* You are not allow to use the built-in method `reverse`

```
guillaume@ubuntu:~/0x13$ cat 8-main.js
#!/usr/bin/node
const esrever = require('./8-esrever').esrever;

console.log(esrever([1, 2, 3, 4, 5]));
console.log(esrever(["School", 89, { id: 12 }, "String"]));

guillaume@ubuntu:~/0x13$ ./8-main.js
[ 5, 4, 3, 2, 1 ]
[ 'String', { id: 12 }, 89, 'School' ]
guillaume@ubuntu:~/0x13$ 
```
   
## 9. Log me

### File: [9-logme.js](9-logme.js) | [9-main.js](9-main.js)

<b>Write a function that prints the number of arguments already printed and the new argument value. (see example below)</b>

* Prototype: `exports.logMe = function (item)`
* Output format: `<number arguments already printed>: <current argument value>`

```
guillaume@ubuntu:~/0x13$ cat 9-main.js
#!/usr/bin/node
const logMe = require('./9-logme').logMe;

logMe("Hello");
logMe("Best");
logMe("School");

guillaume@ubuntu:~/0x13$ ./9-main.js
0: Hello
1: Best
2: School
guillaume@ubuntu:~/0x13$ 
```
   
## 10. Number conversion

### File: [10-converter.js](10-converter.js) | [10-main.js](10-main.js)

<b>Write a function that converts a number from base 10 to another base passed as argument:</b>

* Prototype: `exports.converter = function (base)`
* You are not allowed to import any file
* You are not allowed to declare any new variable (`var`, `let`, etc..)

```
guillaume@ubuntu:~/0x13$ cat 10-main.js
#!/usr/bin/node
const converter = require('./10-converter').converter;

let myConverter = converter(10);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));


myConverter = converter(16);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));

guillaume@ubuntu:~/0x13$ ./10-main.js
2
12
89
2
c
59
guillaume@ubuntu:~/0x13$ 
```