// by Alexander Nikolskiy

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

process.stdin.setEncoding('utf8');
rl.on('line', readLine);

function readLine(line) {
    console.log(fib(parseInt(line, 10)));
    process.exit();
}

function fib(n) {
    // write your code here
    var dict = [];
    dict[0] = 0;
    dict[1] = 1;
    for(var i = 2; i<=n; i++){
        dict[i] = dict[n-1] + dict[n-2];
    }
}

module.exports = fib;
