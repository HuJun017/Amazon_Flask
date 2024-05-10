function getProdotto(ID){
    //dichiarazioni delle varibili (le due pagine principali)
    let mainPage = document.getElementById('mainPage');
    let informationPage = document.getElementById('informationPage');


    //variabili
    let IDValue = document.querySelector('.ID');
    let NomeValue = document.querySelector('.Nome');
    let PrezzoValue = document.querySelector('.Prezzo');
    let QuantitaValue = document.querySelector('.Quantita');
    let CategoriaValue = document.querySelector('.Categoria');

    //pacco di informazioni
    console.log(ID);
    /*{
        ID: IDValue,
        Nome: NomeValue,
        Prezzo: PrezzoValue,
        Quantita: QuantitaValue,
        Categoria: CategoriaValue
    }*/

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
