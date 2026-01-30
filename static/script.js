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

function copyToTextarea(button) {
    // Trouver le texte dans le parent .news-example
    const parent = button.parentElement;
    const text = parent.querySelector('p:nth-of-type(2)').innerText;

    // Copier dans la textarea
    const textarea = document.getElementById('newsText');
    textarea.value = text;

    // Optionnel : message visuel
    button.innerText = 'Copied!';
    setTimeout(() => { button.innerText = 'Copy'; }, 1500);
}
