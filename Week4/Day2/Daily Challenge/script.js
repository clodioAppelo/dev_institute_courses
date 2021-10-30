let todisplay = ``
	let longest = array.reduce((a, b)=>{
			return a.length > b.length ? a.length : b.length;
		}
	);
	while (todisplay.length<longest+5) {todisplay+="*"}
	todisplay+='\n';
	for (let index = 0; index < array.length; index++) {
		let toadd = ""
		toadd+='