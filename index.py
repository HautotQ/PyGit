from js import document

def on_click(event):
    document.body.innerHTML += "<p>✅ Bouton cliqué depuis Python !</p>"

document.getElementById("btn").addEventListener("click", on_click)
