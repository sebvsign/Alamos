const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    //toggle del nav
    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active');
    });

    //animacion de los links
    navLinks.forEach((link, nav) => {
        link.style.animation = 'navLinkFade 0.5 ease forwards ${ nav / 7 + 2}s';
    });
}

navSlide();


