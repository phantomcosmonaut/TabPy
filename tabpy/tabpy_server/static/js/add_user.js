document.addEventListener("DOMContentLoaded", ready);

function ready(){

	var goodPassword = false;
	var pwd = document.getElementById("pwd");
	var postbtn = document.getElementById("post-btn");
	var pwdchecker = document.getElementById("pwd-checker");
	var result = document.getElementById("result-text");
	postbtn.disabled = true;
	var re = new RegExp(
		"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{6,})");

	pwd.onfocus = reTest
	pwd.onblur= function(){
		pwdchecker.style.display = "none";
	}
	pwd.addEventListener("keyup", reTest)

	function reTest(event){
		if(re.test(pwd.value)){
			postbtn.disabled = false;
			pwdchecker.style.display = "none";
		}
		else{
			postbtn.disabled = true;
			pwdchecker.style.display = "block";
		}
	}

	function pwdSubmission(){
		const url = window.location.href;
		const xhttp = new XMLHttpRequest();
		var username = document.getElementById("user").value;
		var password = document.getElementById("pwd").value;
		xhttp.open("POST", url);
		body = JSON.stringify({"username":username, "password":password});
		xhttp.send(body);
		xhttp.onreadystatechange = (response) => {
			if (xhttp.readyState == 4) {
				switch(xhttp.status){
					case 200:
						result.style.color = '#5cb85c';
						break;
					default:
						result.style.color = '#d9534f';
						break;
				}
			result.innerText = JSON.parse(xhttp.responseText)["message"];
			}
		}
	}

	postbtn.addEventListener("click", pwdSubmission)
}
