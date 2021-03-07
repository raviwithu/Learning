var mqtt_unpack_uint16_ptr = DebugSymbol.fromName("mqtt_unpack_fixed_header").address;
//var mqtt_unpack_uint16_fun = new NativeFunction(mqtt_unpack_uint16_ptr, 'int', ['pointer']);
Interceptor.attach(mqtt_unpack_uint16_ptr, {
onEnter: function(args) {
console.log("mqtt_unpack_fixed_header called");
console.log("Arg[1] -" + args[0].toInt32());
var a = Memory.readByteArray(args[1],args[2].toInt32());
var b = new Uint8Array(args[0]);
var str = "";
for(var i = 0; i < b.length; i++) {
    str += (b[i].toString(16) + " ");
}
console.log(str);
},
onLeave: function (args) {
	console.log("mqtt_unpack_uint16 return value -" + args[0]);
	//var a = Memory.readByteArray(args[0],args[2].toInt32());
	//var b = new Uint8Array(a);
	//for(var i = 0; i < b.length; i++) {
    	//	str += (b[i].toString(16) + " ");
	//}
	//console.log(str);

    }
});
