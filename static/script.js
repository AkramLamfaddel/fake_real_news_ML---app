async function predict() {
    const text = document.getElementById("newsText").value;
    const response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    });
    const data = await response.json();
    document.getElementById("result").innerText = data.prediction;
}
