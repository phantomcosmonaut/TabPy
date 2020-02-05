document.addEventListener("DOMContentLoaded", ready);

function ready(){
	var goodPassword = false;
	var pwd = document.getElementById("pwd");
	var postbtn = document.getElementById("post-btn");
	var pwdchecker = document.getElementById("pwd-checker");
	postbtn.disabled = true;
	var re = new RegExp(
		"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{6,})");

	pwd.onfocus = function(){
		pwdchecker.style.display = "block";
	}
	pwd.onblur= function(){
		pwdchecker.style.display = "none";
	}
	pwd.addEventListener("keyup", function(event){
		if(re.test(pwd.value)){
			postbtn.disabled = false;
			pwdchecker.style.display = "none";
		}
		else{
			postbtn.disabled = true;
			pwdchecker.style.display = "block";
		}
	})
}
