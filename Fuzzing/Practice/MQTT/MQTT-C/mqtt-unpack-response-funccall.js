Process.setExceptionHandler(function (details) {
    console.log(JSON.stringify(details));
    console.log(details.address.sub(moduleBase));
});


var module_name = "mqtt";
var offset = '0x11316';
var funFun = ptr(Module.findBaseAddress(module_name)).add(offset);
//var f = new NativeFunction(funFun, 'ssize_t', ['pointer', 'int64', 'size_t']);
var f = new NativeFunction(funFun, 'pointer',['pointer','pointer','pointer']);
Interceptor.attach(funFun, {
	onEnter: function(args) {
			var ret_val = f(args[0],args[1],args[2]);
			console.log("mqtt_unpack_response called");
			console.log("ret_val - " + ret_val.toInt32())
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
		    console.log("return value -" + retval.toInt32())
		    }
});
