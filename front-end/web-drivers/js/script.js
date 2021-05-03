const btnHamburger = document.querySelector('#btnHamburger');
const header = document.querySelector('.header');
const overlay = document.querySelector('.overlay');
const fadeElems = document.querySelectorAll('.has-fade');
const body = document.querySelector('body');
document.querySelector('#btnHamburger').addEventListener('click', function(){
    console.log('open hamburger');

    if (header.classList.contains('open')) { // close hamburger menu
        body.classList.remove('noscroll');

        header.classList.remove('open');
        fadeElems.forEach(function(element){
            element.classList.remove('fade-in');
            element.classList.add('fade-out');
        })
   
    }
    else { // open hamburger menu
        body.classList.add('noscroll');

        header.classList.add('open');
        fadeElems.forEach(function(element){
            element.classList.remove('fade-out');
            element.classList.add('fade-in');
        })
        

    }

});