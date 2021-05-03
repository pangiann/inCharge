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

    fetch(window.base_url +"/admin/" + user_id + "/check_auth", requestOptions)
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
function load_subs() {
    var myHeaders = new Headers();
    var auth_token = localStorage.getItem('auth_token');
    check_auth(auth_token);
    console.log(auth_token);
    myHeaders.append("Authorization", "Bearer " + auth_token);
    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };
    var user_id = localStorage.getItem('user_id');
    document.getElementById('user').innerHTML = user_id;
    document.getElementById('user2').innerHTML = user_id;
    fetch(window.base_url + "/admin/" + user_id + "/subs", requestOptions)
        .then(response => response.text())
        .then(result =>{
            //console.log(result)
            let json_obj = JSON.parse(result);
            var subs_num = json_obj.sessions.length;
            for (i = 0; i < subs_num; i++) {
                const row = document.createElement('tr');
                row.classList = "table-row";
                const content = `
                <tr class="table-row">
                    <td class="col col-1" data-label="UserName">${json_obj.sessions[i].username}</td>
                    <td class="col col-2" data-label="Customer Name">${json_obj.sessions[i].first_name + " " + json_obj.sessions[i].last_name}</td>
                    <td class="col col-3" data-label="Email">${json_obj.sessions[i].email}</td>
                    <td class="col col-4" data-label="Address">${json_obj.sessions[i].address}</td>
                    <td class="col col-5" data-label="Phone">${json_obj.sessions[i].phone}</td>
                    <td class="col col-6" data-label="Payment Status">${json_obj.sessions[i].last_month_paid_bill + "/" + json_obj.sessions[i].last_month_issued_bill}</td>
                    <td class="col col-7" data-label="Cost">${json_obj.sessions[i].cost}</td>
                    <td class="col col-8" data-label="Check">
                        <input type="checkbox" name="check" id="${json_obj.sessions[i].username}"/>
                    </td>
                </tr>
                `;
                let container = document.querySelector(".responsive-table");
                container.innerHTML += content;
            }
    
        })
        .catch(error => console.log('error', error));

}

async function issue_api(customer_id) {
    var myHeaders = new Headers();
    var auth_token = localStorage.getItem('auth_token');
    var user_id = localStorage.getItem('user_id');
    myHeaders.append("Authorization", "Bearer " + auth_token);
    var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        redirect: 'follow'
    };
    console.log(user_id);
    let result = await fetch(window.base_url + "/admin/" + user_id + "/" + customer_id + "/issue", requestOptions)
        .then(response => {
        
            if (response.status === 200) {
                return response.text();
            } else {
                throw new Error(response.status);
            }
        })
        .then(result => {
            json_obj = JSON.parse(result);
            //console.log(json_obj.msg);
            return json_obj.msg;
            //window.location.replace('../subscriptions');
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
                
                window.location.replace('../admin_profile');
            }
        });
    return result;
}


async function issue() {
    var checkboxes = document.getElementsByName("check");
    
    

    // loop over them all
    for (var i=0; i<checkboxes.length; i++) {
       // And stick the checked ones onto an array...
       if (checkboxes[i].checked) {
            var customer_id = checkboxes[i].id;
            let result = await issue_api(customer_id);
            console.log(result);
            

           
       }
    }
    window.location.replace('../subscriptions');
}
  
function logout() {
    localStorage.clear();

    window.location.replace('../business-login/');
}
