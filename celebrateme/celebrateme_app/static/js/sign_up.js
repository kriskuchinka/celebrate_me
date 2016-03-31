

var form = document.getElementById("sign_up_form");

// Check to ensure that external JS is connected to intended page
function externalJs() {
	console.log("Your external JS is connected properly.");
} // End of start funtion
externalJs();

form.noValidate = true;

form.addEventListener("submit", gatherInfo);

function createUser(username, email, password) {
    $.ajax({
    	url: "create_user",
    	method: "POST",
    	success: function(result) {
        	alert(data);
    	}
	});	
}


function gatherInfo(event) {
	event.preventDefault();
	var username = form.username.value;
	var email = form.email.value;
	var password = form.password.value;
	console.log(username, email, password);
	createUser(username, email, password);
}


