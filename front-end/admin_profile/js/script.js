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


function check_auth() {
    var myHeaders = new Headers();
    var auth_token = localStorage.getItem('auth_token');
    myHeaders.append("Authorization", "Bearer " + auth_token);

    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };
    var user_id = localStorage.getItem('user_id');

    fetch(window.base_url +"/admin/" + user_id + "/check_auth", requestOptions)
        .then(response => {
            
            if (response.status === 200) {
                return response.text();
            } else {
                throw new Error(response.status);
            }
        })
        .then(result => {
            getAdminInfo();
        })
        .catch(error => {
            console.log('error', error)
            if (error == "Error: 401" || error == "Error: 422" || error == "Error: 423") {
                alert('Not authorized');
                localStorage.clear();
                window.location.replace('../business-login');
            }
            else {
                alert("Bad request");
                
                window.location.replace('../business-login');
            }
        });

}
function getAdminInfo() {

    var myHeaders = new Headers();
    var auth_token = localStorage.getItem('auth_token');

    myHeaders.append("Authorization", "Bearer " + auth_token);
    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };
    var user_id = localStorage.getItem('user_id');
    console.log(user_id);
    fetch(window.base_url + "/admin/" + user_id, requestOptions)
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
        
        var admin_info = json_obj;
        console.log(admin_info.last_name)
        document.getElementById("user").innerHTML = admin_info.company;
        document.getElementById("user2").innerHTML = admin_info.company;

        document.getElementById("name").innerHTML = admin_info.last_name + " " + admin_info.first_name;
        document.getElementById("email").innerHTML = admin_info.email;
        document.getElementById("phone").innerHTML = admin_info.phone;
        document.getElementById("address").innerHTML = admin_info.address;

       

    
    
    
      })
      .catch(error => {
        console.log('error', error)
        if (error == "Error: 401" || error == "Error: 422" || error == "Error: 423") {
            alert('Not authorized');
            localStorage.removeItem('auth_token');
            localStorage.removeItem('user_id');
            window.location.replace('../business-login');
        }
        else {
            alert("Bad request");
            localStorage.removeItem('auth_token');
            localStorage.removeItem('user_id');
            window.location.replace('../business-login');
        }
    });
}


function logout() {
    localStorage.clear();

    window.location.replace('../business-login/');
}
