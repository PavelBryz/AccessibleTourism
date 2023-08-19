function activateMenuToggle(){
    Array.from($('nav div')).forEach( el => el.classList.toggle('active'));
    $('nav > a')[0].classList.toggle('active')
}