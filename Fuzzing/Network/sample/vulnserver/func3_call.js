var fun3Fun = ptr('0x401808');
var st = Memory.allocUtf8String('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA');

var f = new NativeFunction(fun3Fun, 'void', ['pointer']);

try{
	f(st);

}
catch(err){
	console.log(err);
}

