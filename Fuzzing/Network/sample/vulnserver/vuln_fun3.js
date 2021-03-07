//const threadId = Process.enumerateThreads()[0];
//Interceptor.attach(DebugSymbol.fromName("strncpy").address, {
Interceptor.attach(ptr('0x401808'), {
	onEnter: function(args) {
		console.log("func3 called " );
		
		var a = Memory.readByteArray(this.context.esp,4)
		var b = new Uint8Array(a);
		var str = "";

		for(var i = 0; i < b.length; i++) {
		    str += (b[i].toString(16) + " ");
		}
		console.log(str);
		//console.log('Context  : ' + JSON.stringify(this.context));
		//var trace = Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress);
        	//for (var j in trace)
            	//	console.log(trace[j]);


	},
onLeave: function (retval) {
	console.log('fun3 ret Context  : ' + JSON.stringify(this.context));
	var a = Memory.readByteArray(this.context.esp,4)
	var b = new Uint8Array(a);
	var str = "";

	for(var i = 0; i < b.length; i++) {
	    str += (b[i].toString(16) + " ");
	}
	console.log(str);
    }

});

