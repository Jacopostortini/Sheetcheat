function signup(){
    var email = $("#email_input").val()
    var name = $("#username_input").val()
    var pwd = $("#password_input").val()
    var jdata = {
        mail: email,
        username: name,
        password: pwd
    }
    if(email!="" && name!="" && pwd!=""){
        $("#fill_in_all").hide()
        $.ajax({    
            url: BASE_URL+"register",
            type: 'post',
            data: JSON.stringify(jdata),
            contentType: "application/json; charset=utf-8",
            dataType: 'json',
            success: function (data) {
                console.log(data)
                window.location.href = "/"
                alert("Account created successfully, check your emails to confirm your registration and get started")
            },
            error: function(jq, status, message){
                console.log("An error occured: Error "+status+", "+message)
            }
        });
    } else{
        $("#fill_in_all").show()
    }
}

document.onkeypress = function(){
    if(event.keyCode==13){
        signup()
    }
}