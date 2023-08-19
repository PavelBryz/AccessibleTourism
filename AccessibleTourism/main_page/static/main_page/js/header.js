function activateMenuToggle(){
    Array.from($('nav div')).forEach( el => el.classList.toggle('active'));
    $('nav > a')[0].classList.toggle('active')
}
function toggleSize(){
    if ($('*')[0].style.getPropertyValue('font-size') === ''){
	$('*')[0].style.setProperty('font-size', '1.5rem');
} else {$('*')[0].style.removeProperty('font-size');}
}