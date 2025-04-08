function startListening() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-IN';
    recognition.start();

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        document.getElementById('query').value = transcript;
    }

    recognition.onerror = function(event) {
        alert('Voice recognition error: ' + event.error);
    }
}
