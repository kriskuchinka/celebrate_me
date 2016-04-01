var form = document.getElementById("sign_up_form");

// JQuery function to pull value from a cookie and save to variable
// Copied from https://docs.djangoproject.com/en/1.9/ref/csrf/
function getCookie(name) {
   var cookieValue = null;
   if (document.cookie && document.cookie != '') {
       var cookies = document.cookie.split(';');
       for (var i = 0; i < cookies.length; i++) {
           var cookie = jQuery.trim(cookies[i]);
           // Does this cookie string begin with the name we want?
           if (cookie.substring(0, name.length + 1) == (name + '=')) {
               cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
               break;
           }
       }
   }
   return cookieValue;
}

// Searches for value of CSRF Cookie and saves to variable.
// Copied from https://docs.djangoproject.com/en/1.9/ref/csrf/
var csrftoken = getCookie('csrftoken');

// Function to test the menthod of a request.
// Copied from https://docs.djangoproject.com/en/1.9/ref/csrf/
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// Changes how future AJAX calls will behave.  Sets a default.
// Copied from https://docs.djangoproject.com/en/1.9/ref/csrf/
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


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
    	data: {username: username, email: email, password: password},
    	method: "POST",
    	success: function(result) {
        	alert(result);
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


