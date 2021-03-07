const threadId = Process.enumerateThreads()[0];
Interceptor.attach(ptr("0x004061ac"), {
	onEnter: function(args) {
		console.log("Connection Handler called " );
		
		//var trace = Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress);
        	//for (var j in trace)
            	//	console.log(trace[j]);


	},
onLeave: function (retval) {
	console.log('Context  : ' + JSON.stringify(this.context));
    }

});

