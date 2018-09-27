let websocket = null;
let ws_protocol = null;
let ws_host = null;
let ws_port = null;


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


// https://webbjocke.com/javascript-web-encryption-and-hashing-with-the-crypto-api/
// Example to work from, change when a better understanding is had

async function genEncryptionKey(password, mode, length) {
    let algo = {
        name: 'PBKDF2',
        hash: 'SHA-256',
        salt: new TextEncoder().encode('a-unique-salt'),
        iterations: 1000
    };
    let derived = {name: mode, length: length};
    let encoded = new TextEncoder().encode(password);
    let key = await crypto.subtle.importKey('raw', encoded, {name: 'PBKDF2'}, false, ['deriveKey']);

    return crypto.subtle.deriveKey(algo, key, derived, false, ['encrypt', 'decrypt']);
}


async function encrypt(text, password, mode, length, ivLength) {
    let algo = {
        name: mode,
        length: length,
        iv: crypto.getRandomValues(new Uint8Array(ivLength))
    };
    let key = await genEncryptionKey(password, mode, length);
    let encoded = new TextEncoder().encode(text);

    return {
        cipherText: await crypto.subtle.encrypt(algo, key, encoded),
        iv: algo.iv
    };
}


function onSendClick() {
    if (websocket.readyState !== WebSocket.OPEN) {
        console.log("Chat Server is not open: " + websocket.readyState);
        return -1;
    }

    let message = document.getElementById("message").value;
    // Defunct encryption - likely not to implement
    // TODO: delete later if not using client encryption
    // let pwd = "password";
    // message = await encrypt(message, pwd, 'AES-GCM', 256, 12).then(encrypted => {
    //     console.log(encrypted);
    //     return encrypted.cipherText;
    // });

    websocket.send(message);
}

// encrypt('Secret text', 'password', 'AES-GCM', 256, 12).then(encrypted => {
//     console.log(encrypted); // { cipherText: ArrayBuffer, iv: Uint8Array }
// });
