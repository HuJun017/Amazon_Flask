function getProdotto(Nome) {
    let mainPage = document.getElementById('mainPage');
    let infoPage = document.getElementById('infoPage');
    console.log(Nome);
    mainPage.style.display = 'none';
    infoPage.style.display = 'block';
    fetch('https://3245-hujun017-amazonflask-sf0izuh99hp.ws-eu111.gitpod.io/elenco', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({NomeProdotto: Nome}),
    }).then((response) => response.json())
    .then((data) => {
        console.log(data);
    })
}
