const btnHamburger = document.querySelector('#btnHamburger');
const header = document.querySelector('.header');
const overlay = document.querySelector('.overlay');
const fadeElems = document.querySelectorAll('.has-fade-menu');
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


function onload() {
    var user_id = localStorage.getItem('user_id');

    document.getElementById('user').innerHTML = user_id;
    document.getElementById('user2').innerHTML = user_id;
    getUserInfo();
    
    var x = document.getElementById("time");
    x.checked=true;
    openTimeOptions();

}
function openBatteryOptions() {
    var x = document.getElementById("battery");

    if (document.getElementById("timeCheck").checked) {
        document.getElementById("timeCheck").checked = false;
        var y = document.getElementById("time");
        y.classList.remove('open');
        y.classList.remove('fade-in');
        y.classList.add('fade-out');

    }
    if (x.classList.contains ('open')) {
      x.classList.remove('open');
      x.classList.remove('fade-in');
      x.classList.add('fade-out');
    } 
    else {
        x.classList.add('open');
        x.classList.remove('fade-out');
        x.classList.add('fade-in');
    }
}
function openTimeOptions() {
    var x = document.getElementById("time");
    if (document.getElementById("batCheck").checked) {
        document.getElementById("batCheck").checked = false;
        var y = document.getElementById("battery");
        y.classList.remove('open');
        y.classList.remove('fade-in');
        y.classList.add('fade-out');
    }

    if (x.classList.contains ('open')) {
      x.classList.remove('open');
      x.classList.remove('fade-in');
      x.classList.add('fade-out');
    } 
    else {
        x.classList.add('open');
        x.classList.remove('fade-out');
        x.classList.add('fade-in');
       
    }
}

function checkValidTime() {
    var h = document.getElementById('h');
    var m = document.getElementById('m');

    var proceed_button = document.getElementById('cont');
    var but = document.getElementById('but');
    if (h.value == null || m.value == null ||   !h.checkValidity() || !m.checkValidity() ) {
      
        
        proceed_button.style.pointerEvents="none";  
        but.style.backgroundColor="gray"; 
    }
    if (h.checkValidity() && m.checkValidity() ) {
      
        
        proceed_button.style.pointerEvents="auto";  
        but.style.backgroundColor="#fab90a"; 
    }
    
}


function checkValidBat() {
    var s = document.getElementById('st')
    var e = document.getElementById('e');

    

    var proceed_button = document.getElementById('cont2');
    var but = document.getElementById('but2');
    
    if (st.value == null || e.value == null || parseInt(e.value) <= parseInt(st.value) ||  !st.checkValidity() || !e.checkValidity() ) {
      
        
        proceed_button.style.pointerEvents="none";  
        but.style.backgroundColor="gray"; 
    }
    if (e.checkValidity() && st.checkValidity() && parseInt(e.value) > parseInt(st.value)) {
      
        
        proceed_button.style.pointerEvents="auto";  
        but.style.backgroundColor="#fab90a"; 
    }
    
}
function getUserInfo() {

    var raw = "";
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
       
        var contract_info = json_obj.contract_info;
        if (contract_info.length != 0) {
            localStorage.setItem('contract', 1);


        }
        else {
            localStorage.setItem('contract', 0);
        
        }
      
    
    
    
    
    })
    .catch(error => {
        console.log('error', error)
        if (error == "Error: 401" || error == "Error: 422" || error == "Error: 423") {
            alert('Not authorized');
            localStorage.clear();

            window.location.replace('../login');
        }
        else {
            alert("Bad request");
            
            window.location.replace('../login');
        }
    });
}
function calculateTimeCost() {
    var myHeaders = new Headers();
    point_id = localStorage.getItem('point_id');
    var auth_token = localStorage.getItem('auth_token');
    myHeaders.append("Authorization", "Bearer " + auth_token);
    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };
    hours = document.getElementById('h').value;
    minutes = document.getElementById('m').value;
    duration = hours + ":" + minutes + ":" + "00";
    var user_id = localStorage.getItem("user_id");
    fetch( window.base_url + "/user/" + user_id + "/" + point_id + "/" + duration + "/calculate", requestOptions)
    .then(response => {
        
        if (response.status === 200) {
            return response.text();
        } else {
            throw new Error(response.status);
        }
    })
    .then(result => {
        let json_obj = JSON.parse(result);
        localStorage.setItem('cost', json_obj.cost);
        let contract = localStorage.getItem('contract');
        localStorage.setItem('energy', json_obj.energy);
        localStorage.setItem('duration', json_obj.time);
        localStorage.setItem('points', json_obj.points);

        if (contract == 1) {
            window.location.replace('../charging_payment/');

        }
        else {
            window.location.replace('../pay/');

        }
    })
    .catch(error => {
        if (error == "Error: 401" || error == "Error: 422" || error == "Error: 423") {
            alert('Not authorized');
            localStorage.clear();


            window.location.replace('../login');
        }
        else {
            alert("Bad request");
           
            window.location.replace('../charging');
        }
    });
}

function calculateBatteryCost() {
    var myHeaders = new Headers();
    let point_id = localStorage.getItem('point_id');
    var auth_token = localStorage.getItem('auth_token');
    myHeaders.append("Authorization", "Bearer " + auth_token);
    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };
    start = document.getElementById('st').value;
    end = document.getElementById('e').value;
    var user_id = localStorage.getItem("user_id");
    fetch(base_url + "/user/" + user_id + "/" + point_id + "/" + start + "/" + end + "/calculate", requestOptions)
    .then(response => {
        
        if (response.status === 200) {
            return response.text();
        } else {
            throw new Error(response.status);
        }
    })
    .then(result => {
        let json_obj = JSON.parse(result);
        localStorage.setItem('cost', json_obj.cost);
        let contract = localStorage.getItem('contract');
        localStorage.setItem('energy', json_obj.energy);
        localStorage.setItem('time', json_obj.time);
        localStorage.setItem('points', json_obj.points);

        if (contract == 1) {
            window.location.replace('../charging_payment/');

        }
        else {
            window.location.replace('../pay/');

        }    })
    .catch(error => {
        console.log('error', error)
        if (error == "Error: 401" || error == "Error: 422" || error == "Error: 423") {
            alert('Not authorized');
            localStorage.clear();
            window.location.replace('../login');
        }
        else {
            alert("Bad request");
           
            window.location.replace('../charging');
        }
    });
}
function logout() {
    localStorage.clear();

    window.location.replace('../login/');
}