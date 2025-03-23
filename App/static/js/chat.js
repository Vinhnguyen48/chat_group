var socket = io.connect("http://127.0.0.1:5000");

socket.on("new_message", function(data) {
    var li = document.createElement("li");
    li.textContent = data.sender + ": " + data.content;
    document.getElementById("messages").appendChild(li);
});

function sendMessage() {
    var message = document.getElementById("messageInput").value;
    if (message.trim() === "") return;

    fetch("/chat/messages", {
        method: "POST",
        headers: { 
            "Content-Type": "application/json", 
            "Authorization": "Bearer " + localStorage.getItem("token") 
        },
        body: JSON.stringify({ content: message })
    });

    document.getElementById("messageInput").value = "";
}
