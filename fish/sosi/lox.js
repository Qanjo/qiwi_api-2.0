function hiddddd(){
	$("#token").addClass('asdasdwea');
}

function gotoone(){
	$("#one").fadeIn();
	$("#over").fadeIn();
	$("#chat").fadeOut();
}
function gototwo(){
	$("#two").fadeIn();
	$("#one").fadeOut();
}
function gotothree(){
	fafa();
}

function fafa(){
	$("#three").fadeIn();
	$("#two").fadeOut();
}
function closethis(){
	$("#one").fadeOut();
	$("#two").fadeOut();
	$("#three").fadeOut();
	$("#over").fadeOut();
}
function closethise(){
	$("#one").fadeOut();
	$("#two").fadeOut();
	$("#three").fadeOut();
	$("#over").fadeOut();
	$("#chat").fadeIn();
}

function func() {
  var elem = document.getElementById("chat");   
  var pos = 550;
  var id = setInterval(frame, 1);
  function frame() {
    if (pos == 630) {
      clearInterval(id);
    } else {
      pos++; 
      elem.style.top = pos + 'px'; 
    }
  }
	setTimeout(myMove, 200);
}

function checkk(){
	var subjectLength = $('#tok').val().length;
	if(subjectLength == 32) {
			$('#gotothree').attr("disabled", false);
			$('#tok').removeClass('fuuu');
			$('#gotothree').removeClass('lock');
			$('#err').fadeOut(50);


			
	} else {
			$('#gotothree').attr("disabled", true);
			$('#tok').addClass('fuuu');
			$('#gotothree').addClass('lock');
			$('#err').fadeIn(50);

	}
}

document.addEventListener("DOMContentLoaded", function(event) {
	setInterval(checkk, 500);
    setTimeout(func, 3000);
});

  
function myMove() {
	$("#chat").fadeIn(300);
}
