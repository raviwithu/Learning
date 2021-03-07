var mqtt_unpack_uint16_ptr = DebugSymbol.fromName("__mqtt_unpack_uint16").address;
//var mqtt_unpack_uint16_fun = new NativeFunction(mqtt_unpack_uint16_ptr, 'int', ['pointer']);
Interceptor.attach(mqtt_unpack_uint16_ptr, {
onEnter: function(args) {
console.log("mqtt_unpack_uint16 called");
console.log("Arg[1] -" + args[0].toInt32());
var b = new Uint8Array(args[0]);
var str = "";
for(var i = 0; i < b.length; i++) {
    str += (b[i].toString(16) + " ");
}
console.log(str);
},
onLeave: function (retval) {
    //console.log("mqtt_unpack_uint16 return value -" + retval);
    }
});
