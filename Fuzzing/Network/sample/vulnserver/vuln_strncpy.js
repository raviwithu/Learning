const threadId = Process.enumerateThreads()[0];
//Interceptor.attach(DebugSymbol.fromName("strncpy").address, {
Interceptor.attach(ptr('0x77c59b70'), {
	onEnter: function(args) {
		console.log("Connection Handler called " );
		
		console.log('Context  : ' + JSON.stringify(this.context));
		//var trace = Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress);
        	//for (var j in trace)
            	//	console.log(trace[j]);


	},
onLeave: function (retval) {
	console.log('Context  : ' + JSON.stringify(this.context));
    }

});

