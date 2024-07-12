function validateForm() {
    var fields = ["name", "number", "email", "message"];
    var isValid = true;
 
    for (var i = 0; i < fields.length; i++) {
       var fieldValue = document.getElementById(fields[i]).value;
       if (fieldValue === "") {
          alert("Please fill in all the fields");
          return false;
 
       }
    }

    var email = document.getElementById('email').value;
    var mobile = document.getElementById('number').value;
    var emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/     ;
    var mobileRegex = /^[0-9]{10}$/;
 
    if (!emailRegex.test(email)) {
       alert("Please enter a email");
    }
    if  (!mobileRegex.test(number)){
       alert("Please enter number")
    }

 }
 
