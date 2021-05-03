function getSelectedOption(sel) {
    var opt;
    for ( var i = 0, len = sel.options.length; i < len; i++ ) {
        opt = sel.options[i];
        if ( opt.selected === true ) {
            break;
        }
    }
    return opt;
}

function loadCars() {


    var requestOptions = {
      method: 'GET',
      redirect: 'follow'
    };
    
    fetch(window.base_url +"/car/brands", requestOptions)
      .then(response => response.text())
      .then(result =>  {          
            console.log(result);
            let json_obj = JSON.parse(result);
            var car_len =  json_obj.brands.length;
            for (i = 0; i < car_len; i++) {
                var x = document.getElementById("f1");
                var option = document.createElement("option");
                option.text = json_obj.brands[i].brand;
               
                x.add(option);
            }

      })      
      .catch(error => console.log('error', error));



}

function loadModel() {
  var sel_brand = document.getElementById('f1');
  var brand = getSelectedOption(sel_brand);
  var sel_model = document.getElementById('f2');
  sel_model.length = 0;
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

 

  var requestOptions = {
    method: 'GET',
    headers: myHeaders,
    redirect: 'follow'
  };

  fetch(window.base_url +"/car/" + brand.text + "/models", requestOptions)
    .then(response => response.text())
    .then(result =>  {          
        console.log(result);
        let json_obj = JSON.parse(result);
        var car_len =  json_obj.models.length;
        for (i = 0; i < car_len; i++) {
            var y = document.getElementById("f2");
            var option2 = document.createElement("option");
            option2.text = json_obj.models[i].model;
            y.add(option2);
        }

    })      
    .catch(error => console.log('error', error));

}



function check_auth(auth_token) {
    var myHeaders = new Headers();
    
    myHeaders.append("Authorization", "Bearer " + auth_token);

    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };
    var user_id = localStorage.getItem('user_id');

    fetch(window.base_url + "/user/" + user_id + "/check_auth", requestOptions)
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
    console.log(auth_token);
    myHeaders.append("Authorization", "Bearer " + auth_token);
    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };
    var user_id = localStorage.getItem('user_id');
    console.log(user_id);
    fetch(window.base_url +"/user/" + user_id, requestOptions)
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
        document.getElementById("username").innerHTML = user_info[0].username;
        document.getElementById("name").value = user_info[0].last_name + " " + user_info[0].first_name;
        document.getElementById("email").value = user_info[0].email;
        document.getElementById("phone").value = user_info[0].phone;
        document.getElementById("address").value = user_info[0].address;

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
        document.getElementById("b1").text = car_info[0].brand;
        document.getElementById("m1").text = car_info[0].model;
        loadCars();
    
    
    
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


function updateUser() {
    var myHeaders = new Headers();
    var auth_token = localStorage.getItem('auth_token');
    check_auth(auth_token);
    console.log(auth_token);
    myHeaders.append("Authorization", "Bearer " + auth_token);
    var user_id = localStorage.getItem('user_id');
    console.log(user_id);
    myHeaders.append("Content-Type", "application/json");
    new_name  = document.getElementById("name").value; 
    new_email = document.getElementById("email").value;
    new_phone = document.getElementById("phone").value;
    new_address = document.getElementById("address").value;
    var sel_brand = document.getElementById('f1');
    var brand = getSelectedOption(sel_brand).text;
    var sel_model = document.getElementById('f2');
    var model = getSelectedOption(sel_model).text;
    split_name = new_name.split(' ');
    first_name = split_name[0];
    last_name = split_name[1];
    split_address = new_address.split(',');
    city = split_address[0];
    street = split_address[1];
    postal_code = split_address[2];
    split_street =  street.split(' ');
    // HERE WE HAVE TO BE VERY CAREFUL, AFTER SPLITTING ADDRESS IN 3 PARTS WITH COMMAS
    // SECOND VALUE (STREET) STARTS WITH A SPACE, SO WHEN WE SPLIT STREET WITH SPACES 
    // AT INDEX 0 WILL BE NULL VALUE, AT INDEX 1 STARTS WE HAVE STREET NAME, AND THEN STREET NUMBER

    var raw = JSON.stringify({
        "first_name": first_name, 
        "last_name": last_name, 
        "phone": parseInt(new_phone),
        "car_brand": brand, 
        "car_model": model, 
        "city": city,
        "street_name": split_street[1] + " " + split_street[2],
        "street_number": parseInt(split_street[3]),
        "postal_code": parseInt(postal_code)
    });

    var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch(window.base_url + "/user/" + user_id, requestOptions)
    .then(response => {
        
        if (response.status === 200) {
            return response.text();
        } else {
            throw new Error(response.status);
        }
    })
    .then(result => {
        console.log(result);
        window.location.replace('../user_profile');
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
            
            window.location.replace('../update_user_profile');
        }
    });


}