const playButton = document.getElementById('playButton');
const audio = document.getElementById('audio');

// Función para aumentar el volumen gradualmente
function fadeIn(audioElement) {
    let volume = 0;
    audioElement.volume = volume;
    const interval = setInterval(() => {
        if (volume < 1) {
            volume += 0.01;
            audioElement.volume = volume;
        } else {
            clearInterval(interval);
        }
    }, 50);
}

// Función para disminuir el volumen gradualmente
function fadeOut(audioElement) {
    let volume = audioElement.volume; // Obtén el volumen actual
    const interval = setInterval(() => {
        if (volume > 0) {
            volume -= 0.01;
            audioElement.volume = volume;
        } else {
            audioElement.pause();
            audioElement.currentTime = 0;
            playButton.textContent = 'Reproducir Canción';
            clearInterval(interval);
        }
    }, 50);
}

playButton.addEventListener('click', () => {
    if (audio.paused) {
        audio.play();
        fadeIn(audio);
        playButton.textContent = 'Pausar Canción';
    } else {
        fadeOut(audio);
    }
});

// Disminuir volumen cuando la canción está por terminar
audio.addEventListener('timeupdate', () => {
    const remainingTime = audio.duration - audio.currentTime;
    if (remainingTime < 5) { // Ajusta el tiempo según prefieras
        fadeOut(audio);
    }
});