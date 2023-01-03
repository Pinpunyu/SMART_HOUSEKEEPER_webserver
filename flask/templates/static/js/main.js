
function showform(num){
	
    let menu = document.getElementById('inputform');
    let result = document.getElementById('result_text');
	
	result.innerHTML = '';
	
    switch(num){
		
		case '1':
			menu.innerHTML='<div class="form-group"><label class="lab-text"for="exampleInputEmail1">User name</label><input required name="username" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter User name"></div><button type="submit" class="btn btn-primary">Submit</button>';			
			break;
			
		case '2':			
			menu.innerHTML='<div class="form-group"><label class="lab-text"for="exampleInputEmail1">User name</label><input required name="username" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter User name"></div><div class="form-group"><label class="lab-text"for="exampleInputEmail1">Item name</label><input required name="itemname" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter Item name"></div><button type="submit" class="btn btn-primary">Submit</button>';
			break;
		
		case '3':			
			menu.innerHTML='<div class="form-group"><label class="lab-text"for="exampleInputEmail1">User name</label><input required name="username" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter User name"></div><div class="form-group"><label class="lab-text"for="exampleInputEmail1">Remote Control name</label><input required name="remotecontrolname" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter Remote Control name"></div><button type="submit" class="btn btn-primary">Submit</button>';
			break;
		
		default:
			break;
    }
}


