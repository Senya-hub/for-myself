//console.log("test")

let userName = "sergei"; //глобальныя переменная
const age = 52;
let boo = true;


//Выборка элементов
const header = document.querySelector(".header"); // усли id то ставим решетку
const headers = document.getElementById("header");
const navLinks = document.querySelectorAll(".nav-link"); 
const testBtn = document.querySelector("#testBtn");

userName = "Сергей";
//name = "sergei";
//age = 52;

console.log(userName, age);
console.log(typeof userName, typeof age, typeof boo, typeof header);
console.log(header, headers);
console.log(navLinks);

function sayHello() {
    let message = "Hello JavaScript"; //локальная переменная
    console.log(message);
}

sayHello(); // вызываем функцию

function simpleMath(a, b) {
    let result = a + b;    //локальная переменная
    return result;        // выводим локальую переменную из функции для использования в дальнейшем
}

let sum = simpleMath(121, 232); //т.к. использовали return, результат будет в названии функции
console.log(sum);

// события

window.addEventListener("scroll", function() {
    //console.log("scrolled");
    // let scrollPos = window.scrollY;

    // if(scrollPos > 0) {
    //     header.classList.add('red');
    // } else {
    //     header.classList.remove('red');
    checkScroll();
    }

    //console.log(scrollPos);
    //header.classList.add('red'); //наша переменная header, записанная выше
});

document.addEventListener("DOMContentLoaded", function() {
    // let scrollPos = window.scrollY;

    // if(scrollPos > 0) {
    //     header.classList.add('red');
    // } else {
    //     header.classList.remove('red');
    // }
    checkScroll();
});

function checkScroll () {
    let scrollPos = window.scrollY;

    if(scrollPos > 0) {
        header.classList.add('red');
    } else {
        header.classList.remove('red');
    }
}

// testBtn.addEventListener("click", function() {
//    console.log('clicked')
// });

//navLinks.addEventListener("click", function() {

//)};

for(let navItem of navLinks) {
    navItem.addEventListener("click", function() {
        console.log(navItem.text);
    });
};