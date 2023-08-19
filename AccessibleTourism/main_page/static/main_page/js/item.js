function playaudio() {
    a = document.getElementById("idAudio");
    $('#pause, #stop').removeClass('hidden')
    a.play();
}
function pauseaudio() {
    a = document.getElementById("idAudio");
    a.pause();
}
function stopaudio() {
    a = document.getElementById("idAudio");
    $('#pause, #stop').addClass('hidden')
    a.pause();
    a.currentTime = 0;
}