import execjs

js_string = """
const jsdom = require("jsdom");
const {JSDOM} = jsdom;

const html = `<!DOCTYPE html><p>Hello world</p>`;
const dom = new JSDOM(html, {
    url: "https://www.toutiao.com",
    referrer: "https://example.com/",
    contentType: "text/html"
});
document = dom.window.document;

window = global;
Object.assign(global, {
    location: {
        hash: "",
        host: "user.qunar.com",
        hostname: "user.qunar.com",
        href: "https://user.qunar.com/passport/login.jsp",
        origin: "https://user.qunar.com",
        pathname: "/",
        port: "",
        protocol: "https:",
        search: "",
    },

});

function func(arg) {
  
    return arg + '666' + document.location.hostname;
}

"""
JS = execjs.compile(js_string)

sign = JS.call("func", "qiao")
print(sign)
# return arg + '666' + document.location.hostname + window.navigator.userAgent;