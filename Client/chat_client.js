var websocket = null;
var ws_protocol = null;
var ws_host = null;
var ws_port = null;


function onConnectClick() {
    let protocol = document.getElementById("protocol").value;
    let host = document.getElementById("host").value;
    let port = document.getElementById("port").value;

    openChatConnection(protocol, host, port);
}

function onDisconnectClick() {
    websocket.close();
}


function openChatConnection(protocol, host, port) {
    let websocketURL = protocol + "://" + host + ":" + port;

    console.log("Opening connection to chat server at " + websocketURL);

    try {
        websocket = new WebSocket(websocketURL);

        websocket.onopen = function (openEvent) {
            console.log("Chat server on: " + JSON.stringify(openEvent, null, 4));

            document.getElementById("bntSent").disabled = false;
            document.getElementById("bntConnect").disabled = true;
            document.getElementById("bntDisconnect").disabled = false;
        };

        websocket.onclose = function (closeEvent) {
            console.log("Chat Server off: " + JSON.stringify(closeEvent, null, 4));

            document.getElementById("bntSent").disabled = true;
            document.getElementById("bntConnect").disabled = false;
            document.getElementById("bntDisconnect").disabled = true;
        };

        websocket.onerror = function (errorEvent) {
            console.log("Chat Server Error: " + JSON.stringify(errorEvent, null, 4));
        };

        websocket.onmessage = function (messageEvent) {
            let message = messageEvent.data;
            console.log("Message Received: " + message);

            if (message.indexOf("error") > 0) {
                document.getElementById("incomingMessage").value += "error: " + message + "\r\n";
            }

            else {
                document.getElementById("incomingMessage").value += "message: " + message + "\r\n";
            }
        };
    } catch (e) {
        console.log(e)
    }
}


function onSendClick() {
    if (websocket.readyState !== WebSocket.OPEN) {
        console.log("Chat Server is not open: " + websocket.readyState);
        return -1;
    }

    let message = document.getElementById("message").value;

    websocket.send(message);
}
