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

    fetch(window.base_url +"/user/" + user_id + "/check_auth", requestOptions)
        .then(response => {
            
            if (response.status === 200) {
                return response.text();
            } else {
                throw new Error(response.status);
            }
        })
        .then(result => {
            getUserInfo();
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

var add_minutes =  function (dt, minutes) {
    return new Date(dt.getTime() + minutes*60000);
}


function checkout() {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    let username = localStorage.getItem('user_id');
    let point_id = localStorage.getItem('point_id');
    let cost = localStorage.getItem('cost');
    let energy = localStorage.getItem('energy');
    let duration = localStorage.getItem('duration');
    let points = localStorage.getItem('points');
    var today = new Date();
    let today_time = today.toLocaleTimeString();
    let time_start_string = today_time.split(" ");
    let time_start = time_start_string[0];
    
    new_date = add_minutes(today, duration);
    let time_string = new_date.toLocaleTimeString();
    let time_end_string = time_string.split(" ");
    let time_end = time_end_string[0];
    console.log(time_string);
    console.log(time_end_string);
    console.log(time_end);

    var raw = JSON.stringify({
        "username": username,
        "point_id": point_id,
        "protocol": "High",
        "charging_type": "Contract",
        "points":  parseInt(points),
        "time_start": time_start,
        "time_end":time_end,
        "cost":cost,
        "energy": energy
    });

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch(base_url + "/charging_session", requestOptions)
    .then(response => {
        
        if (response.status === 200) {
            return response.text();
        } else {
            throw new Error(response.status);
        }
    })
    .then(result => {
        localStorage.removeItem('cost');
        localStorage.removeItem('energy');
        localStorage.removeItem('duartion');
        localStorage.removeItem('points');
        localStorage.removeItem('point_id');
        window.location.replace('../user_profile')
    })
    .catch(error => {
        if (error == "Error: 401" || error == "Error: 422" || error == "Error: 423") {
            alert('Not authorized');
            localStorage.clear();


            window.location.replace('../login');
        }
        else {
            alert("Bad request");
            localStorage.removeItem('cost');
            localStorage.removeItem('energy');
            localStorage.removeItem('duartion');
            localStorage.removeItem('points');
            localStorage.removeItem('point_id');

           
            window.location.replace('../charging');
        }
    });

}

function getUserInfo() {

    let cost = localStorage.getItem('cost');
    var tot_cost = document.getElementById('total_cost');
    tot_cost.innerHTML = cost + "$";
    var user_id = localStorage.getItem('user_id');
    document.getElementById('user').innerHTML = user_id;
    document.getElementById('user2').innerHTML = user_id;
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
        if (contract_info.length!=0) {
            document.getElementById("provider").innerHTML = contract_info[0].supplier;
            document.getElementById("points").innerHTML = contract_info[0].points;
            document.getElementById("cost").innerHTML = contract_info[0].price + "$";


        }
        else {
            window.location.replace('../pay');
        
        }
      

    
    
    
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

