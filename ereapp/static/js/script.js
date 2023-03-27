let i=[0];
let images=[]
let time=3000;

images[0]="./static/images/hero.jpg"
images[1]="./static/images/hero1.jpg"
images[2]="./static/images/hero2.jpg"
images[3]="./static/images/hero3.jpg"
images[4]="./static/images/hero4.jpg"

function changeImg(){
    if(i<images.length){
        document.slide.src=images[i]
        i++
    }else{i=0}
setTimeout("changeImg()", time);
}
window.onload=changeImg;

function checker(event){
    var pswd = document.getElementById("c_pwd").value
    var confirmation = document.getElementById("pwd").value
    if(pswd != confirmation){
        alert("Both passwords must match!")
        event.preventDefault()
    }
}


function checker2(event){
    var pswd = document.getElementById("pswd2").value
    var confirmation = document.getElementById("pswd1").value
    if(pswd != confirmation){
        alert("Both passwords must match!")
        event.preventDefault()
    }
}



$(document).ready(function(){

    $('.logo').click(function(){
        window.location.href = '/';
    });
    $('.login').click(function(){
        window.location.href = '/login';
    });

    $('.signup').click(function(){
        window.location.href = '/signup';
    });

    $('.abt').click(function(){
        window.location.href = '/about';
    });

    $('.tour').click(function(){
        window.location.href = '/tours';
    });

    $('.fb').click(function(){
        window.location.href = 'facebook.com/erekereng';
    });

    $('.ig').click(function(){
        window.location.href = 'instagram.com/erekereng';
    });

    $('.twi').click(function(){
        window.location.href = 'twitter.com/erekereng';
    });

    $('.tour').click(function(){
        window.location.href = '/tours';
    });

});
