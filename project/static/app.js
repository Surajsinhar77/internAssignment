
const signup = document.getElementById('signupform');

function cheakingPassword(){
    const pass1 = signup.password1.value;
    const pass2 = signup.password2.value;
    const getag = document.getElementById('matchingresult');
    if(pass1 == pass2){
        getag.innerText = 'Password and Confirm Password Match';
        getag.style.color = 'green';
        getag.style.display ='block';
        if(pass1.length < 7){
            const verpass = document.getElementById('verifypass');
            verpass.style.display = 'block';
            verpass.innerText = 'Weak Password';
            verpass.style.color = 'orange';
        }else{
            const verpass = document.getElementById('verifypass');
            verpass.style.display = 'block';
            verpass.innerText = 'Strong Password';
            verpass.style.color = 'green';
        }
    }else{
        getag.innerText = 'Password and Confirm Password Unmatch';
        getag.style.color = 'Red';
    }
}