    /* get date for default value*/
   
    let today = new Date().toISOString().substr(0, 10);
    document.querySelector("#date").value = today;
    
    /* Pricing module*/
    document.getElementById("#suggestprice").value= Number;
    document.getElementById("#totalprice").value = Number;
    var totalp=0, suggestp=0;
    //document.getElementById("#get_price").onclick = pricing_calculation;
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
        //suggestp = suggested_price;
        document.getElementById("totalprice").value = Number(total_price);
        //totalp = total_price;
    }
    
    
    
   /* function checkform()
        {
            var f = document.forms["form1"].elements;
            var cansubmit = true;
    
            for (var i = 0; i < f.length; i++) {
                if (f[i].value.length == 0) cansubmit = false;
            }
    
            if (cansubmit) {
                document.getElementById('#submitbutton').disabled = !cansubmit;            
            }
        }
*/