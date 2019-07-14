function pricing(){
    var gallon=document.getElementById("gallon").value;
    var dateform = document.getElementById("date").value;
    var timePeriod = datetime.datetime.strptime(dateform,"%Y-%m-%d");
    var month = timePeriod.month;
    var current_p = 1.5;
    var location_f, history_f, gallon_f, company_f, fluctuation_f, margin, suggested_price, total_price;
    if (client.state=="TX"){
        location_f =0.02;
    } else {
        location_f=0.04;
    }
    if (clientHistory.count()==0){
        history_f = 0;
    } else {
        history_f =0.01;
    }
    if (gallon>1000){
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
    total_price = gallon * suggested_price;
    document.getElementById("suggestprice").innerHTML = suggested_price;
    document.getElementById("totalprice").innerHTML = total_price;
}