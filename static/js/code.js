function getProdotto(){
    //dichiarazioni delle varibili
    let mainPage = document.getElementById('mainPage');
    let informationPage = document.getElementById('informationPage');
    let prodotto = 

    //fetch delle informazioni
    fetch('https://3245-hujun017-flasklogin-iwzllonrxe7.ws-eu111.gitpod.io/elenco', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(prodotto)
    })
    //ricevimento delle informazioni
    .then(response => response.json())
    .then(data => {
        //visualizzo data
        console.log(data);
    })
    //in caso di errore
    .catch(error => {
        console.error('Si è verificato un errore:', error);
    });
}
