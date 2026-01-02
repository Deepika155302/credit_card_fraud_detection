function checkFraud() {

    let time = document.getElementById("time").value;
    let amount = document.getElementById("amount").value;
    let type = document.getElementById("type").value;
    let online = document.getElementById("online").value;

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            data: [time, amount, type, online]
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText =
            "Result: " + data.result;
    });
}

// Random transaction generator
function randomTransaction() {

    document.getElementById("time").value =
        Math.floor(Math.random() * 100000);

    document.getElementById("amount").value =
        Math.floor(Math.random() * 10000);

    document.getElementById("type").value =
        Math.floor(Math.random() * 3);

    document.getElementById("online").value =
        Math.floor(Math.random() * 2);
}


