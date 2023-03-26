


var x =document.getElementById("login");
var y =document.getElementById("register");
var z =document.getElementById("btn");


var email = document.getElementById('email').value;
var password = document.getElementById('password').value;
var passwordConfirm = document.getElementById('passwordConfirm').value;

function register(){
    x.style.left = "-400px";
    y.style.left = "50px";
    z.style.left = "110px";

}
function login(){
    x.style.left = "50px";
    y.style.left = "450px";
    z.style.left = "0";

}
function forgot(){
    window.location.href = '/forgot';
}

function checkreg(){
    window.location.href = "/";
    alert("Chenging was successful");
   
    if(password = passwordConfirm){//запрос имеил с сервера
        alert("Chenging was successful");
        
            
    }
        //запрос на сервер хз как 
}

function backtomain(){
    window.location.href = "/main";
}
function addzan(){
    window.location.href = "/addzan";

}
function addfood(){
    window.location.href = "/addfood";
}


