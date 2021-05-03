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
    document.getElementById('user').innerHTML = user_id;
    document.getElementById('user2').innerHTML = user_id;

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
      
var first_year;
var last_year;
var tot_num_arr = [];
var sum_cost_per_month_arr = [];
var sum_cost_per_year_arr = [];
var tot_years_num_arr = [];

//second chart - function needs a unique name   
function drawChart2() {

    const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"
    ]; 
    var auth_token = localStorage.getItem('auth_token');
    check_auth(auth_token);
    var user_id = localStorage.getItem('user_id');
    var myHeaders = new Headers();
    myHeaders.append("Authorization", "Bearer " + auth_token);


    var requestOptions = {
      method: 'GET',
      headers: myHeaders,
      redirect: 'follow'
    };

    
    fetch(base_url + "/user/" + user_id + "/SessionsPerDate/2014-01-01/2021-03-31", requestOptions)
      .then(response => response.text())
      .then(result => {
            console.log(result);
            json_obj = JSON.parse(result);
            //console.log(json_obj);
            sum_costs = json_obj.sum_costs;
            //console.log(sum_costs);
            years_costs = json_obj.years_costs;

            tot_num = json_obj.tot_num;

            tot_years_num = json_obj.tot_years_num;
            years = sum_costs.length;
            first_year = json_obj.first_year;
            last_year = json_obj.last_year;

            // add all years options in html
            for (i = 0; i <= last_year-first_year; i++) {
                    var x = document.getElementById("years");
                    var option = document.createElement("option");
                    option.text = json_obj.first_year + i;
                    x.add(option);
            }
            // create array for monthly costs/number of sessions in appropriate form in order to use it in google charts
            for (i = first_year; i <= last_year; i++) {
                tot_num_arr.push([["Month", "Number of Charges"]]);
                sum_cost_per_month_arr.push([["Month", "Cost"]]);
                for (j = 0; j < 12; j++) {
                    var cost_month = [monthNames[j], sum_costs[i-first_year][j]];
                    var times_month = [monthNames[j], tot_num[i-first_year][j]]
                    sum_cost_per_month_arr[i-first_year].push(cost_month);
                    tot_num_arr[i-first_year].push(times_month);
                }
            }


            sum_cost_per_year_arr = [["Year", "Cost"]];
            tot_years_num_arr = [["Year", "Number of Charges"]];
            for (i = 0; i < years_costs.length; i++) {
                sum_cost_per_year_arr.push([(first_year + i).toString(), years_costs[i]]);
                tot_years_num_arr.push([(first_year + i).toString(), tot_years_num[i]]);
            }
            changeChart();

          //console.log(arr);

      })
      .catch(error => console.log('error', error));
       
  
   
  }
    
function changeChart() {

  year = document.getElementById("years").value;
  option2 = document.getElementById("years_way").value;
  console.log(option2);

    
    
  
  if (option2 == "cost") {
    let chart =  {
        title: 'Company Performance',
        subtitle: 'Sales, Expenses, and Profit: 2014-2017',
    };
    let avg_id = 'mo_year';
    let avg_string = "$/year";
    let chart_id = "piechart";
    drawChart(sum_cost_per_year_arr, chart, avg_id, avg_string, chart_id);
  
    avg_id = 'mo_month';
    avg_string = "$/month";
    chart_id = "div_chart";
    drawChart(sum_cost_per_month_arr[year-first_year], chart, avg_id, avg_string, chart_id);
  }
  else {
    let chart =  {
        title: 'Company Performance',
        subtitle: 'Sales, Expenses, and Profit: 2014-2017',
    };
    let avg_id = 'mo_year';
    let avg_string = "/year";
    let chart_id = "piechart";
    drawChart(tot_years_num_arr, chart, avg_id, avg_string, chart_id);
    chart =  {
        title: 'Company Performance',
        subtitle: 'Sales, Expenses, and Profit: 2014-2017',
    };
    avg_id = 'mo_month';
    avg_string = "/month";
    chart_id = "div_chart";
    drawChart(tot_num_arr[year-first_year], chart, avg_id, avg_string, chart_id);

  }


}  
function drawChart(arr_of_data, chart_opt, avg_id, avg_string, chart_id) {
    var total = 0;
    for(var i = 1; i < arr_of_data.length; i++) {
        total += arr_of_data[i][1];
    }
    var avg = total / arr_of_data.length;
    document.getElementById(avg_id).innerHTML = avg.toFixed(2) + avg_string;
    data = google.visualization.arrayToDataTable(arr_of_data);
    var options = {
        chart: chart_opt,
        vAxis: {minValue: 0},
        colors: ['#f0af00']
        
    };
    var chart = new google.visualization.ColumnChart(document.getElementById(chart_id));
    chart.draw(data, options);


}

$(window).resize(function(){
        changeChart();
});

function logout() {
    localStorage.clear();

    window.location.replace('../login/');
}