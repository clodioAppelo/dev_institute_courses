
		function frame(str){
			let lines = str.split('\n')
			// get length of longest line:
			let max_length = Math.max(...lines.map(l => l.length))
			let border = '*'.repeat(max_length + 4)
		
			let ret =  border + "\n"
			// make inner lines padded to length:
			ret += lines.reduce((s,l) => s+=`* ${l.padEnd(max_length)} *\n`, "")
			ret += border
			return ret
		}
		
		console.log(frame('Hello world in a frame'))
		// console.log(frame('A longer string with more words'))
		// console.log(frame('A longer string with more words\nand more lines\nwrapped into a nice box.'))