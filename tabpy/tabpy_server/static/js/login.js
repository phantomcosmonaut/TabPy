document.addEventListener("DOMContentLoaded", ready);

function ready(){
	const url = window.location.href;
	const xhttp = new XMLHttpRequest();

	function pwdSubmission(event){
		var result = document.getElementById("result-text");
		var username = document.getElementById("user").value;
		var password = document.getElementById("pwd").value;
		xhttp.open("POST", url);
		body = JSON.stringify({"username":username, "password":password});
		xhttp.send(body);
		xhttp.onreadystatechange = (response) => {
			if (xhttp.readyState == 4 && xhttp.status !== 200) {
				result.style.color = '#d9534f';
			result.innerText = JSON.parse(xhttp.responseText)["message"];
			}
		}
	}
	var postbtn = document.getElementById("post-btn");
	postbtn.addEventListener("click", pwdSubmission);
}
