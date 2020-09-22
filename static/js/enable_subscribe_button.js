function planSelect(name, price, priceId) {
    var inputs = document.getElementsByTagName('input');

    for(var i = 0; i<inputs.length; i++){
        inputs[i].checked = false;
        if(inputs[i].name== name){

            inputs[i].checked = true;
        }
    }

    var n = document.getElementById('plan');
    var p = document.getElementById('price');
    var pid = document.getElementById('priceId');
    n.innerHTML = name;
    p.innerHTML = price;
    pid.innerHTML = priceId;
    document.getElementById("submit").disabled = false;
}