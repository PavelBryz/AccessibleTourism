function activateMenuToggle(){
    Array.from($('nav div')).forEach( el => el.classList.toggle('active'));
    $('nav > a')[0].classList.toggle('active')
}
function toggleSize(){
    if ($(':root')[0].style.getPropertyValue('--fs') === '' || $(':root')[0].style.getPropertyValue('--fs') === '1'){
	$(':root')[0].style.setProperty('--fs', '1.5');
} else {$(':root')[0].style.setProperty('--fs', '1');}
}