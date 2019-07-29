 /* get date for default value*/
   
 let today = new Date().toISOString().substr(0, 10);
 //document.querySelector("#date").value = today;
 
 //Prepare date values for function

 var validdate = new Date(today);
 var day = validdate.getDate();
 if (day>30 || day==30){
         validdate.setMonth(validdate.getMonth()+1);
         validdate.setDate(2);
 } else{
         validdate.setDate(day+2);
 }
 document.querySelector("#date").value = validdate.toISOString().substr(0,10);


 
 /* Pricing module*/

 var totalp=0, suggestp=0;
 function pricing_calculation(){
     var gal=document.getElementById("gallon").value;
     gallon = Number(gal); //change string into number
     var dateform = document.getElementById("date").value;
     var datedata = new Date(dateform);
     var month = 1+ datedata.getMonth(); //the getMonth run fron 0->11
     var current_p = 1.5;
     var location_f, history_f, gallon_f, company_f, fluctuation_f, margin, suggested_price, total_price;
     var temp = "{{ client.state }}";
     if (temp =="TX"){
         location_f =0.02;
     } else {
         location_f=0.04;
     }
     temp = {{clientHistory}};
     if (temp ==0){
         history_f = 0;
     } else {
         history_f =0.01;
     }
     if ((+gallon)>1000){
         gallon_f = 0.02;
     } else {
         gallon_f =0.03;
     }
     if (month>5 && month<9){
         fluctuation_f = 0.04;
     } else {
         fluctuation_f = 0.03;
     } 
     company_f = 0.1;
     margin = current_p*(location_f-history_f+gallon_f+company_f+fluctuation_f);
     suggested_price = current_p + margin;
     total_price = (+gallon) * suggested_price;
     suggested_price= Math.round(suggested_price*100)/100;
     total_price = Math.round(total_price*100)/100;
     document.getElementById("suggestprice").value = Number(suggested_price);
     document.getElementById("totalprice").value = Number(total_price); 
     enableSubmit(); 
 }

 //For buttons
 //for submit button
 function enableSubmit() {
         document.getElementById('gallon').readOnly = true;
         document.getElementById('date').readOnly = true;
         document.getElementById("submitbutton").disabled = false;
     }
 
 //for set_price button
 function checkGallon(){
     var entergallon = Number(document.getElementById("gallon").value);
    
     if (entergallon >0){           
         document.getElementById('get_price').disabled= false;
     } else {
         document.getElementById('get_price').disabled = true; 
     }
 }
 function checkDateBeforePrice(){
     var enterdate = document.getElementById("date").value;
     enterdate= new Date(enterdate);
     if (enterdate<validdate ){
             document.getElementById('reminderDate').innerHTML="Please choose at least 2 days later from today for time delivery";
         } else {   
             document.getElementById('reminderDate').innerHTML="";   
             pricing_calculation();        
         }
 }
 function validateEnter(){
     checkGallon();
 }

 function setPrice(){
     checkDateBeforePrice();
 }