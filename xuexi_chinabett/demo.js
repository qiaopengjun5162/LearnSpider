// nodejs 运行 JS 代码
function func(arg) {
    return arg + ' hello';
}

var name = process.argv[2]
var data = func(name);
console.log(data)