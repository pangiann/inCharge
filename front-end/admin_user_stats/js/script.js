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
    var user_id = localStorage.getItem('user_id');
    document.getElementById('user').innerHTML = user_id;
    document.getElementById('user2').innerHTML = user_id;
    myHeaders.append("Authorization", "Bearer " + auth_token);

    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };
    var user_id = localStorage.getItem('user_id');

    fetch(base_url + "/admin/" + user_id + "/check_auth", requestOptions)
        .then(response => {
            
            if (response.status === 200) {
                return response.text();
            } else {
                throw new Error(response.status);
            }
        })
        .then(result => {
           load_users();
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
                //localStorage.removeItem('auth_token');
                //localStorage.removeItem('user_id');
                window.location.replace('../admin_profile');
            }
        });

}
function load_users() {
    var myHeaders = new Headers();
    var auth_token = localStorage.getItem('auth_token');
    var user_id = localStorage.getItem('user_id');

    myHeaders.append("Authorization", "Bearer " + auth_token);
    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };



  
    fetch(window.base_url + "/admin/" + user_id + "/users", requestOptions)
        .then(response => response.text())
        .then(result =>{
            //console.log(result)
            let json_obj = JSON.parse(result);
            var users_num = json_obj.users.length;
           // console.log(users_num);
            
            for (i = 0; i < users_num; i++) {
                var x = document.getElementById("selUser");
                var option = document.createElement("option");
                //console.log(json_obj.users[i].username)
                option.text = json_obj.users[i].username;
                option.value = json_obj.users[i].username;
                x.add(option);
            }
    
        })
        .catch(error => console.log('error', error));
}


async function getUserInfo() {
    var myHeaders = new Headers();
    var auth_token = localStorage.getItem('auth_token');
    myHeaders.append("Authorization", "Bearer " + auth_token);
    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };
    var user_id = localStorage.getItem('user_id');
    document.getElementById('user').innerHTML = user_id;
    document.getElementById('user2').innerHTML = user_id;
    var e = document.getElementById("selUser");
    var value = e.options[e.selectedIndex].value;
    var customer_id = e.options[e.selectedIndex].text;
    let myResult = await fetch(window.base_url + "/admin/" + user_id + "/" + customer_id + "/sub", requestOptions)
        .then(response => response.text())
        .then(result =>{
            //console.log(result)
           
            
            let json_obj = JSON.parse(result);
            const row = document.createElement('li');
            row.classList = "table-row";
            const content = `
            <tr class="table-header">
                <th class="col col-1">ID</th>
                <th class="col col-2">Name</th>
                <th class="col col-3">Email</th>
                <th class="col col-4">Address</th>
                <th class="col col-5">Phone</th>
                <th class="col col-6">Payment Status</th>
                <th class="col col-7">Cost</th>
            </tr>
            <tr class="table-row">
                <td class="col col-1" data-label="UserName">${json_obj.contract[0].username}</td>
                <td class="col col-2" data-label="Customer Name">${json_obj.contract[0].first_name + " " + json_obj.contract[0].last_name}</td>
                <td class="col col-3" data-label="Email">${json_obj.contract[0].email}</td>
                <td class="col col-4" data-label="Address">${json_obj.contract[0].address}</td>
                <td class="col col-5" data-label="Phone">${json_obj.contract[0].phone}</td>
                <td class="col col-6" data-label="Payment Status">${json_obj.contract[0].last_month_paid_bill + "/" + json_obj.contract[0].last_month_issued_bill}</td>
                <td class="col col-7" data-label="Cost">${json_obj.contract[0].cost}</td>
                
            </tr>
            `;
            let container = document.querySelector(".responsive-table");
            container.innerHTML = content;
            
            return customer_id;
            
    
        })
        .catch(error => console.log('error', error));
    loadInfo(myResult);
}
function loadInfo(customer_id) {
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
    fetch(window.base_url + "/admin/" + user_id + "/" + customer_id, requestOptions)
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
       
        var contract_info = user_info.contract_info;
        if (contract_info.length!=0) {
            document.getElementById("provider").innerHTML = contract_info[0].supplier;
            document.getElementById("points").innerHTML = contract_info[0].points;
            document.getElementById("cost").innerHTML = contract_info[0].price + "$";


        }
        
        var car_info = user_info.car_info;
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
            window.location.replace('../business-login');
        }
        else {
            alert("Bad request");
           
            window.location.replace('../business-login');
        }
    });
}
$(document).ready(function(){
 
    // Initialize select2
    $("#selUser").select2();
  
    // Read selected option
    $('#but_read').click(function(){
      var username = $('#selUser option:selected').text();
      var userid = $('#selUser').val();
  
      $('#result').html("id : " + userid + ", name : " + username);
  
    });
});

function logout() {
    localStorage.clear();

    window.location.replace('../business-login/');
}



  
