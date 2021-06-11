var answer, wrongButton, rightButton;
function feedback(){
  answer = document.forms["form"]["user_answer"].value;
  if (answer != "correct"){
    wrongButton = document.getElementById(answer);
    wrongButton.classList.remove("btn-outline-info");
    wrongButton.classList.add("btn-danger");
  }
  rightButton = document.getElementById("right");
  rightButton.classList.remove("btn-outline-info");
  rightButton.classList.add("btn-success");
}