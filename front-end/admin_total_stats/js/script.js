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


function checkAuth() {
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

    fetch(base_url +"/admin/" + user_id  + "/check_auth", requestOptions)
        .then(response => {
            
            if (response.status === 200) {
                return response.text();
            } else {
                throw new Error(response.status);
            }
        })
        .then(result => {
             loadStations();
        
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
    localStorage.removeItem('auth_token');
    localStorage.removeItem('user_id');
    window.location.replace('../business-login/');
}

function loadStations() {
    let x = document.getElementById('stations');
    let option = document.createElement("option");
    option.text = "All";
    x.add(option);
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
      };
      
    fetch(base_url + "/stations", requestOptions)
        .then(response => {
                
            if (response.status === 200) {
                return response.text();
            } else {
                throw new Error(response.status);
            }
        })
        .then(result => {
            let json_obj = JSON.parse(result);
            let stations_len = json_obj.stations.length;
            for (i = 0; i < stations_len; i++) {
                let x = document.getElementById('stations');
                let option = document.createElement("option");
                option.text = json_obj.stations[i].station_no;
                x.add(option);
            }
            loadPoints("All");
            
        })
        .catch(error => {
            console.log('error', error);
            alert(error);
            window.location.replace('../admin_profile');
        });
    
    
        

}
function stationChanged() {
    let station_id = document.getElementById('stations').value;
    loadPoints(station_id);
    //prepareChart();
    
}
function loadPoints(station_id) {
    var myHeaders = new Headers();
    var auth_token = localStorage.getItem('auth_token');
    var user_id = localStorage.getItem('user_id');
    myHeaders.append("Authorization", "Bearer " + auth_token);

    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };
    let x = document.getElementById('points');
    x.length = 0;
    let option = document.createElement("option");
    option.text = "All";
    x.add(option);
    console.log(station_id);
    if (station_id == "All") {
        console.log("komple");
        api_string = "/admin/" + user_id + "/points";
    }
    else {
        api_string = "/admin/" + user_id + "/" + station_id + "/points";
    }
    fetch(base_url + api_string, requestOptions)
        .then(response => {
                
            if (response.status === 200) {
                return response.text();
            } else {
                throw new Error(response.status);
            }
        })
        .then(result => {
            let json_obj = JSON.parse(result);
            let points_len = json_obj.points.length;
            for (i = 0; i < points_len; i++) {
                let x = document.getElementById('points');
                let option = document.createElement("option");
                option.text = json_obj.points[i].point_id;
                x.add(option);
            }
            document.getElementById('points').value = "All";
            prepareChart();
        })
        .catch(error => {
            console.log('error', error);
            alert(error);
            window.location.replace('../admin_total_stats');
            
        });
    
    

}

var monthToNumber = {
    "Jan": 1,  "Feb": 2,  "Mar" : 3,  "Apr" : 4,  "May" : 5,  "Jun" : 6,
    "Jul": 7,  "Aug": 8,  "Sept" : 9,  "Oct" : 10, "Nov" : 11, "Dec" : 12
}

var first_year;
var last_year;

var sum_costs_per_day_arr = [];
var tot_num_per_day_arr = [];
var tot_energy_per_day_arr = [];
var sum_costs_per_month_arr = [];
var tot_num_per_month_arr = [];
var tot_energy_per_month_arr = [];

var years_costs_arr= [];
var tot_years_num_arr = [];
var tot_years_energy_arr = [];


function prepareChart() {

    const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"
    ]; 
    
    var auth_token = localStorage.getItem('auth_token');
    var user_id = localStorage.getItem('user_id');
    
    var myHeaders = new Headers();
    myHeaders.append("Authorization", "Bearer " + auth_token);


    var requestOptions = {
      method: 'GET',
      headers: myHeaders,
      redirect: 'follow'
    };
    var station = document.getElementById('stations').value;
    var point = document.getElementById('points').value;

    var sdate = document.getElementById('sdate').value;
    var edate = document.getElementById('edate').value;
    console.log(point);
    console.log(station);
   
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();

    today = yyyy + '-' + mm + '-' + dd;
    // BE CAREFUL WHEN WE REACH 2100 (BECAUSE WE MADE A GREAT APP) 
    // WE HAVE TO CHANGE EDATE VALUE
    if (!sdate) {
        sdate = "2000-01-01";
    }
    if (!edate) {
        edate = today;
    }
    
    if (station == "All" && (point == "All" || point == "")) {
        api_string = "/SessionsPerProvider/" + sdate + "/" + edate;
    }
    else if (point == "All") {
        api_string = "/SessionsPerStation/" + station + "/"  + sdate + "/" + edate; 
    }
    else {
        api_string = "/SessionsPerPoint/" + point + "/" + sdate + "/" + edate;
    }
    fetch(base_url + "/admin/" + user_id + api_string, requestOptions)
        .then(response => {
            
            if (response.status === 200) {
                return response.text();
            } else {
                throw new Error(response.status);
            }
        })
        
      .then(result => {
            //console.log(result);
            json_obj = JSON.parse(result);
            //console.log(json_obj);
            sum_costs_per_day = json_obj.sum_costs_per_day;
            //console.log(sum_costs);
            sum_costs_per_month = json_obj.sum_costs_per_month;

            tot_num_per_day = json_obj.tot_num_per_day;
            tot_num_per_month = json_obj.tot_num_per_month;

            tot_energy_per_day = json_obj.tot_energy_per_day;
            tot_energy_per_month = json_obj.tot_energy_per_month;

            
            first_year = json_obj.first_year;
            last_year = json_obj.last_year;
            sum_costs_per_day_arr.length = 0;
            tot_num_per_day_arr.length = 0;
            tot_energy_per_day_arr.length = 0;
            sum_costs_per_month_arr.length = 0;
            tot_num_per_month_arr.length = 0;
            tot_energy_per_month_arr.length = 0;

            years_costs_arr.length = 0;
            tot_years_num_arr.length = 0;
            tot_years_energy_arr.length = 0;
            let years = document.getElementById('years');
            years.length = 0;
            for (i = 0; i <= last_year-first_year; i++) {
                    let x = document.getElementById("years");
                    let option = document.createElement("option");
                    option.text = json_obj.first_year + i;
                    x.add(option);
            }
            for (i = first_year; i <= last_year; i++) {
                sum_costs_per_day_arr.push([]);
                tot_num_per_day_arr.push([]);
                tot_energy_per_day_arr.push([]);


                for (j = 0; j < 12; j++) {
                    sum_costs_per_day_arr[i-first_year].push([["Day", "Cost"]]);
                    tot_num_per_day_arr[i-first_year].push([["Day", "Number of Charges"]]);
                    tot_energy_per_day_arr[i-first_year].push([["Day", "Energy"]]);


                    for (k = 0; k < 31; k++) {
                        let cost_day = [(k+1).toString() + "/" + (j+1).toString(), sum_costs_per_day[i-first_year][j][k]];
                        sum_costs_per_day_arr[i-first_year][j].push(cost_day);
                        let num_day = [(k+1).toString() + "/" + (j+1).toString(), tot_num_per_day[i-first_year][j][k]];
                        tot_num_per_day_arr[i-first_year][j].push(num_day);
                        let energy_day = [(k+1).toString() + "/" + (j+1).toString(), tot_energy_per_day[i-first_year][j][k]];
                        tot_energy_per_day_arr[i-first_year][j].push(energy_day);

                    }
                }

              
            }
            //console.log(sum_costs_per_day_arr[0][0]);
            for (i = first_year; i <= last_year; i++) {
                tot_num_per_month_arr.push([["Month", "Number of Charges"]]);
                sum_costs_per_month_arr.push([["Month", "Cost"]]);
                tot_energy_per_month_arr.push([["Month", "Energy"]]);
                for (j = 0; j < 12; j++) {
                    let cost_month = [monthNames[j], sum_costs_per_month[i-first_year][j]];
                    let times_month = [monthNames[j], tot_num_per_month[i-first_year][j]];
                    let energy_month = [monthNames[j], tot_energy_per_month[i-first_year][j]];
                    sum_costs_per_month_arr[i-first_year].push(cost_month);
                    tot_num_per_month_arr[i-first_year].push(times_month);
                    tot_energy_per_month_arr[i-first_year].push(energy_month);
                }
            }


            years_costs = json_obj.years_costs;
            tot_years_num = json_obj.tot_years_num;
            tot_years_energy = json_obj.tot_years_energy;
           
            years_costs_arr = [["Year", "Cost"]];
            tot_years_num_arr = [["Year", "Number of Charges"]];
            tot_years_energy_arr = [["Year", "Energy"]];
            for (i = 0; i < years_costs.length; i++) {
                years_costs_arr.push([(first_year + i).toString(), years_costs[i]]);
                tot_years_num_arr.push([(first_year + i).toString(), tot_years_num[i]]);
                tot_years_energy_arr.push([(first_year + i).toString(), tot_years_energy[i]]);
            }

            changeChart();

          //console.log(arr);

      })
      .catch(error => {
          console.log('error', error);
          window.location.replace('../admin_profile');
      });
       
  
   
  }
    
function changeChart() {

  year = document.getElementById("years").value;
  month = document.getElementById("month").value;
  option = document.getElementById("way").value;
  //option2 = document.getElementById("years_way").value;
  //console.log(option2);
  if (month == "All") {
        if (option=="cost") {
            let chart =  {
                title: 'Company Performance',
                subtitle: 'Sales, Expenses, and Profit: 2014-2017',
            };
            let avg_id = 'mo_month';
            let avg_string = "$/month";
            let chart_id = "div_chart";
            drawChart(sum_costs_per_month_arr[year-first_year], chart, avg_id, avg_string, chart_id);
            
        }
        else if (option=="NumOfCharges") {
            let chart =  {
                title: 'Company Performance',
                subtitle: 'Sales, Expenses, and Profit: 2014-2017',
            };
            let avg_id = 'mo_month';
            let avg_string = "/month";
            let chart_id = "div_chart";
            drawChart(tot_num_per_month_arr[year-first_year], chart, avg_id, avg_string, chart_id);

        }
        else {
            let chart =  {
                title: 'Company Performance',
                subtitle: 'Sales, Expenses, and Profit: 2014-2017',
            };
            let avg_id = 'mo_month';
            let avg_string = "/month";
            let chart_id = "div_chart";
            drawChart(tot_energy_per_month_arr[year-first_year], chart, avg_id, avg_string, chart_id);


        }
  }
  else {
        if (option=="cost") {
            let chart =  {
                title: 'Company Performance',
                subtitle: 'Sales, Expenses, and Profit: 2014-2017',
            };
            let avg_id = 'mo_month';
            let avg_string = "/day";
            let chart_id = "div_chart";
            drawChart(sum_costs_per_day_arr[year-first_year][monthToNumber[month]-1], chart, avg_id, avg_string, chart_id);

        }
        else if (option=="NumOfCharges") {
            let chart =  {
                title: 'Company Performance',
                subtitle: 'Sales, Expenses, and Profit: 2014-2017',
            };
            let avg_id = 'mo_month';
            let avg_string = "/day";
            let chart_id = "div_chart";
            drawChart(tot_num_per_day_arr[year-first_year][monthToNumber[month]-1], chart, avg_id, avg_string, chart_id);

        }
        else {
            let chart =  {
                title: 'Company Performance',
                subtitle: 'Sales, Expenses, and Profit: 2014-2017',
            };
            let avg_id = 'mo_month';
            let avg_string = "/day";
            let chart_id = "div_chart";
            drawChart(tot_energy_per_day_arr[year-first_year][monthToNumber[month]-1], chart, avg_id, avg_string, chart_id);


        }

  }
  if (option == "cost") {
      let chart =  {
          title: 'Company Performance',
          subtitle: 'Sales, Expenses, and Profit: 2014-2017',
      };
      let avg_id = 'mo_year';
      let avg_string = "$/year";
      let chart_id = "piechart";
      drawChart(years_costs_arr, chart, avg_id, avg_string, chart_id);

  }
  else if (option == "NumOfCharges") {
      let chart =  {
          title: 'Company Performance',
          subtitle: 'Sales, Expenses, and Profit: 2014-2017',
      };
      let avg_id = 'mo_year';
      let avg_string = "/year";
      let chart_id = "piechart";
      drawChart(tot_years_num_arr, chart, avg_id, avg_string, chart_id);


  }
  else {
      let chart =  {
          title: 'Company Performance',
          subtitle: 'Sales, Expenses, and Profit: 2014-2017',
      };
      let avg_id = 'mo_year';
      let avg_string = "/year";
      let chart_id = "piechart";
      drawChart(tot_years_energy_arr, chart, avg_id, avg_string, chart_id);


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
        colors: ['#2d314d']

    };
    var chart = new google.visualization.ColumnChart(document.getElementById(chart_id));
    chart.draw(data, options);


}
$(window).resize(function(){
        changeChart();
});

function logout() {
    localStorage.clear();

    window.location.replace('../business-login/');
}