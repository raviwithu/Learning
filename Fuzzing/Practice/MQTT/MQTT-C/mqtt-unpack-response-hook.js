var module_name = "mqtt";
var offset = '0x11316';
//var funFun = ptr(Module.findBaseAddress(module_name)).add(offset);
var funFun = DebugSymbol.fromName("mqtt_unpack_response").address;
//var f = new NativeFunction(funFun, 'int', ['pointer']);
Interceptor.attach(funFun, {
onEnter: function(args) {
console.log("mqtt_unpack_response called");
//console.log("Size - " + args[2]);
//console.log("Buffer data - " + Memory.readByteArray(args[1],args[2].toInt32()));
var a = Memory.readByteArray(args[1],args[2].toInt32());
var b = new Uint8Array(a);
var str = "";

for(var i = 0; i < b.length; i++) {
    str += (b[i].toString(16) + " ");
}
console.log(str);
},
onLeave: function (retval) {
    console.log("return value -" + retval)
    }
});
