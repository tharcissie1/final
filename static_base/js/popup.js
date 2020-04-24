
const username = document.getElementById('id_username');
username.classList.add('form-control');

// const email = document.getElementById('id_email');
// email.classList.add('form-control');


const password1 = document.getElementById('id_password1');
password1.classList.add('form-control');

const password2 = document.getElementById('id_password2');
password2.classList.add('form-control');
password2.style.marginBottom = '25px';


const signupTitle = document.getElementById('signupTitle');
signupTitle.style.color = 'white';





const mysignup = document.getElementById('mysignup');

// const btnSignUp = document.getElementById('myBtnSignup');
// btnSignUp.addEventListener('click', function(){

//     mysignup.style.display = 'block';
// })


const myclose = document.getElementById('myclose');
myclose.addEventListener('click', function(){

    mysignup.style.display = 'none';
})


window.onclick = function(event) {
    if (event.target == mysignup) {
        mysignup.style.display = "none";
    }
  }