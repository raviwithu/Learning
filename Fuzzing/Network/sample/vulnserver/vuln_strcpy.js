console.log(DebugSymbol.fromName("strcpy").address);
//Interceptor.attach(ptr(DebugSymbol.fromName("strcpy").address), {
Interceptor.attach(ptr('0x77c56780'), {
	onEnter: function(args) {
		console.log("strcpy called " );
	        console.log("strcpy args[0] addr - " + args[0]);	
	        //console.log("strcpy args[1] addr - " + args[1]);	
		console.log('Context  : ' + JSON.stringify(this.context));
		//var trace = Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress);
        	//for (var j in trace)
            	//	console.log(trace[j]);


	},
onLeave: function (retval) {
	console.log('Context  : ' + JSON.stringify(this.context));
	//var a = Memory.readByteArray(ptr('0xd1f9c4'),4)
	//var a = Memory.readByteArray(ptr('0x039ef9c4'),4)
        //        var b = new Uint8Array(a);
        //        var str = "";

          //      for(var i = 0; i < b.length; i++) {
         //        str += (b[i].toString(16) + " ");
         //       }
         //       console.log(str);

    }

});

