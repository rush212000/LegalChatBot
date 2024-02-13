document.addEventListener("DOMContentLoaded", function() {
    const sendMessageButton = document.getElementById("send-btn"); // The ID for your send button
    const userInputField = document.getElementById("user-input"); // The ID for your input field
    const messagesContainer = document.getElementById("messages"); // The ID for the container where messages are displayed

    sendMessageButton.addEventListener("click", function() {
        const userMessage = userInputField.value;
        if (userMessage.trim() !== "") {
            displayMessage(userMessage, "user");
            fetch('/process_input', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({message: userMessage}),
            })
            .then(response => response.json())
            .then(data => {
                displayMessage(data.response, "bot");
            })
            .catch((error) => {
                console.error('Error:', error);
            });

            userInputField.value = ""; // Clear input field after sending
        }
    });

    function displayMessage(message, sender) {
        const messageElement = document.createElement("div");
        if (sender === "user") {
            messageElement.classList.add("user-message");
        } else {
            messageElement.classList.add("bot-message");
        }
        messageElement.textContent = message;
        messagesContainer.appendChild(messageElement);
        messagesContainer.scrollTop = messagesContainer.scrollHeight; // Scroll to the bottom
    }
});
