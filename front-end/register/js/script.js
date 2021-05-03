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


var strength = {
    0: "Worst ☹",
    1: "Bad ☹",
    2: "Weak ☹",
    3: "Good ☺",
    4: "Strong ☻"
}

var password = document.getElementById('password');
//var meter = document.getElementById('password-strength-meter');
var text = document.getElementById('password-strength-text');

password.addEventListener('input', function()
{
    var val = password.value;
    var result = zxcvbn(val);

    // Update the password strength meter
    //meter.value = result.score;

    // Update the text indicator
    if(val !== "") {
        text.innerHTML = "Strength: " + "<strong>" + strength[result.score] + "</strong>" + "<span class='feedback'>" + result.feedback.warning + " " + result.feedback.suggestions + "</span";
    }
    else {
        text.innerHTML = "";
}
});

function validateEmail(email) {

    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

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

// get selected option in sel (reference obtained above)


function loadCars() {

    var requestOptions = {
      method: 'GET',
      redirect: 'follow'
    };
    
    fetch(base_url + "/car/brands", requestOptions)
      .then(response => response.text())
      .then(result =>  {          
            //console.log(result);
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

  fetch(base_url + "/car/" + brand.text + "/models", requestOptions)
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
function userRegister() {


  
  var lastname = document.getElementById('lname').value;
  var firstname = document.getElementById('fname').value;
  var password = document.getElementById('password').value;
  var email = document.getElementById('email').value;
  var phone = document.getElementById('phone').value;
  var username = document.getElementById('username').value;
  var city = document.getElementById('city').value;
  var street = document.getElementById('street').value;
  var street_num = document.getElementById('street_num').value;
  var postal = document.getElementById('postal').value;
  
  var sel_brand = document.getElementById('f1');
  var brand = getSelectedOption(sel_brand);
  console.log(brand.text);

  var sel_model = document.getElementById('f2');
  var model = getSelectedOption(sel_model);
  console.log(model.text);

  var pass_strength = zxcvbn(password);
  integer = /^[0-9]+$/;
  
  var birth_date = document.getElementById('date').value;

  if (pass_strength <= 2) {
    alert("Insert a better password for your safety :))")
  }
  if (lastname == "" || firstname == "" || email == "" || phone == "" || username == "" || !integer.test(phone)) {
      alert("Not valid input");
      window.location.replace('../register')
  }
 
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/x-www-form-urlencoded");
  
  var urlencoded = new URLSearchParams();
  urlencoded.append("username", username);
  urlencoded.append("password", password);
  urlencoded.append("car_brand", brand.text);
  urlencoded.append("car_model", model.text);
  urlencoded.append("first_name", firstname);
  urlencoded.append("last_name", lastname);
  urlencoded.append("email", email);
  urlencoded.append("birth_date", birth_date);
  urlencoded.append("phone", phone);
  urlencoded.append("city", city);
  urlencoded.append("street_name", street);
  urlencoded.append("street_number", street_num);
  urlencoded.append("postal_code", postal);
  
  var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: urlencoded,
    redirect: 'follow'
  };
  
  fetch(window.base_url + "/user/create", requestOptions)
    .then(response => {
            
        if (response.status === 200) {
            return response.text();
        } else {
            throw new Error(response.status);
        }
    })
    .then(result => {
        console.log(result);
        window.location.replace('../login');
    })
    .catch(error => {
        console.log('error', error);
        window.location.replace('../register');
    });


}

function validName() {
    fname = document.getElementById("fname");
    console.log(fname);

}