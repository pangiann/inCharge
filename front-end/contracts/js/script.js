const btnHamburger = document.querySelector('#btnHamburger');
const header = document.querySelector('.header');
const overlay = document.querySelector('.overlay');
const fadeElems = document.querySelectorAll('.has-fade');
const body = document.querySelector('body');
document.querySelector('#btnHamburger').addEventListener('click', function(){
    console.log('open hamburger');

    if (header.classList.contains('open')) { // close hamburger menu
        body.classList.remove('noscroll');
        header.classList.remove('open');
        fadeElems.forEach(function(element){
            element.classList.remove('fade-in');
            element.classList.add('fade-out');
        })

    }
    else { // open hamburger menu
        body.classList.add('noscroll');
        header.classList.add('open');
        fadeElems.forEach(function(element){
            element.classList.remove('fade-out');
            element.classList.add('fade-in');
        })


    }

});


function show_contracts() {
    var user_id = localStorage.getItem('user_id');
    document.getElementById('user').innerHTML = user_id;
    document.getElementById('user2').innerHTML = user_id;
    var myHeaders = new Headers();
    //var auth_token = localStorage.getItem('auth_token');

    //myHeaders.append("Authorization", "Bearer " + auth_token);
    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };

    fetch(base_url + "/contracts", requestOptions)
    .then(response => {
        
        if (response.status === 200) {
            return response.text();
        } else {
            throw new Error(response.status);
        }
    })
    .then(result => {
        console.log(result)
        let json_obj = JSON.parse(result);
        var contracts_num = json_obj.contracts.length;
        for (i = 0; i < contracts_num; i++) {
            const card = document.createElement('a');
            card.classList = "choice__item";
            const content = `
            <a href="#" class="choice__item">
                <div class="choice__circle">
                    <div class="choice__top">
                        ${json_obj.contracts[i].distributor}
                    </div>
                    <div class="choice__price">
                        ${json_obj.contracts[i].price}$/month
                           
                    </div>
                    
                </div>
        
                <div class="choice__text">
                    <div class="choice__title">
                        Provider Info
                    </div>
                    <div class="choice__description">
                        <p> ${json_obj.contracts[i].email}</p>
                        <p> ${json_obj.contracts[i].phone}</p>
                        <p>www.elpedison.com</p>
                    </div>
                </div>
                <div class="choice__button">
                    <div class="button" id="${i}" onClick="subscribe('${json_obj.contracts[i].distributor}')">SUBSCRIBE</div>
                </div> 
            </a>       
            `;
            let container = document.querySelector(".choice__grid");
            container.innerHTML += content;
        }

    })
    .catch(error => {
        if (error == "Error: 401" || error == "Error: 422" || error == "Error: 423") {
            alert('Not authorized');
            localStorage.removeItem('auth_token');
            localStorage.removeItem('user_id');
            window.location.replace('../login');
        }
        else {
            console.log('error', error);
            window.location.replace('../user_profile');
        }
    });
}

function subscribe(distributor) {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var auth_token = localStorage.getItem('auth_token');
    var user_id = localStorage.getItem('user_id');

    console.log(auth_token);
    myHeaders.append("Authorization", "Bearer " + auth_token);
    var raw = JSON.stringify({"distributor": distributor});

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch(window.base_url + "/user/" + user_id + "/NewContract", requestOptions)
    .then(response => {
        if (response.status === 200) {
            console.log('You\'ve subscribed successfully'); 
            alert("Successful subscription"); 
            window.location.replace("../user_profile/"); 
            return response.json();
        } else {
            throw new Error(response.status);
        }
    })
    .then(result => { 
        console.log(result);
       
    })
    .catch(error => {
        if (error == "Error: 401" || error == "Error: 422" || error == "Error: 423") {
            alert('Not authorized');
            localStorage.removeItem('auth_token');
            localStorage.removeItem('user_id');
            window.location.replace('../login');
        }
        else {
            console.log('Failed to get info of customer', error); 
            alert("Failed to get contracts"); 
            window.location.replace("../user_profile/index.html");
        }
    });
    //
}


function logout() {
    localStorage.clear();

    window.location.replace('../login/');
}