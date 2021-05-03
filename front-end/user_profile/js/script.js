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
function check_auth(auth_token) {
    var myHeaders = new Headers();
    
    myHeaders.append("Authorization", "Bearer " + auth_token);

    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };
    var user_id = localStorage.getItem('user_id');

    fetch(window.base_url +"/user/" + user_id + "/check_auth", requestOptions)
        .then(response => {
            
            if (response.status === 200) {
                return response.text();
            } else {
                throw new Error(response.status);
            }
        })
        .then(result => console.log(result))
        .catch(error => {
            console.log('error', error)
            if (error == "Error: 401" || error == "Error: 422" || error == "Error: 423") {
                alert('Not authorized');
                localStorage.removeItem('auth_token');
                localStorage.removeItem('user_id');
                window.location.replace('../login');
            }
            else {
                alert("Bad request");
                localStorage.removeItem('auth_token');
                localStorage.removeItem('user_id');
                window.location.replace('../login');
            }
        });

}

function getUserInfo() {

    var raw = "";
    var myHeaders = new Headers();
    var auth_token = localStorage.getItem('auth_token');
    check_auth(auth_token);
    myHeaders.append("Authorization", "Bearer " + auth_token);
    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };
    var user_id = localStorage.getItem('user_id');
    console.log(user_id);
    fetch(window.base_url + "/user/" + user_id, requestOptions)
    .then(response => {
        
        if (response.status === 200) {
            return response.text();
        } else {
            throw new Error(response.status);
        }
    })
    .then(result =>{
        console.log(result);
        let json_obj = JSON.parse(result);
        
        var user_info = json_obj.user_info;
        document.getElementById("user").innerHTML = user_info[0].username;
        document.getElementById("user2").innerHTML = user_info[0].username;

        document.getElementById("name").innerHTML = user_info[0].last_name + " " + user_info[0].first_name;
        document.getElementById("email").innerHTML = user_info[0].email;
        document.getElementById("phone").innerHTML = user_info[0].phone;
        document.getElementById("address").innerHTML = user_info[0].address;

        var contract_info = json_obj.contract_info;
        if (contract_info.length!=0) {
            document.getElementById("provider").innerHTML = contract_info[0].supplier;
            document.getElementById("points").innerHTML = contract_info[0].points;
            document.getElementById("cost").innerHTML = contract_info[0].price + "$";


        }
        else {
            document.getElementById("provider").innerHTML = "NO CONTRACT YET?";
            document.getElementById("provider_text").innerHTML = "Say goodbye to pay-as-you-go pricing and complex invoices. InCharge is the monthly subscription solution that makes car charging even easier. Hit the \
                    Subscribe button to check all the various contracts made \
                    by our partners and check what fits your preferences";
            
            var newNode = document.createElement('a');
            newNode.href = "../contracts/index.html"
            newNode.className = 'button';
            newNode.innerHTML = "SUBSCRIBE";
            document.getElementById('card-text').appendChild(newNode);
            stats = document.querySelector('.card-stats');
            stats.classList.add('closed');
        
        }
        var car_info = json_obj.car_info;
        document.getElementById("car_name").innerHTML = car_info[0].brand;
        document.getElementById("model").innerHTML = car_info[0].model;
        document.getElementById("capacitance").innerHTML = car_info[0].capacitance + " kWh";

    
    
    
      })
    .catch(error => {
        console.log('error', error)
        if (error == "Error: 401" || error == "Error: 422" || error == "Error: 423") {
            alert('Not authorized');
            localStorage.removeItem('auth_token');
            localStorage.removeItem('user_id');
            window.location.replace('../login');
        }
        else {
            alert("Bad request");
            localStorage.removeItem('auth_token');
            localStorage.removeItem('user_id');
            window.location.replace('../login');
        }
    });
}


function logout() {
    localStorage.clear();

    window.location.replace('../login/');
}