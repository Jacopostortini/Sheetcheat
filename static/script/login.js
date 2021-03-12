function login_popup(){
    document.getElementById("login_popup").style.display = "flex"
    document.getElementById("popup_background_filter").style.display = "flex"    
}

function login(){
    var email = $("#email_input").val()
    var pwd = $("#password_input").val()
    var jdata = {
        mail: email,
        password: pwd
    }
    $.ajax({    
        url: BASE_URL+"login",
        type: 'post',
        data: JSON.stringify(jdata),
        contentType: "application/json; charset=utf-8",
        dataType: 'json',
        success: function (data) {
            console.log(data)
            close_login_popup()
            Username = data["username"]
            createCookie("Username", data["username"], null)
            createCookie("AccessToken", data["access_token"], null)
            createCookie("RefreshToken", data["refresh_token"], null)
            createCookie("LoggedIn", "True", null)
            changeLoginStatus()
        },
        error: function(jq){
            console.log("Error "+jq.status+", "+jq.statusText)
        }
    });
}

function close_login_popup(){
    document.getElementById("login_popup").style.display = "none"
    document.getElementById("popup_background_filter").style.display = "none" 
}

function changeLoginStatus(){
    if(Boolean(getCookie("LoggedIn"))){
        // document.getElementById("login_button").style.display = "none"
        // document.getElementById("signup_button").style.display = "none"
        // document.getElementById("username_label").style.display = "block"
        // document.getElementsByClassName("user_icon")[0].style.display = "block"
        // document.getElementById("username_label").innerHTML = getCookie("Username")
        $("#login_button").hide()
        $("#signup_button").hide()
        $("#username_label").show()
        $(".user_icon").show()
        $("username_label").html = getCookie("Username")
    } else{
        // document.getElementById("login_button").style.display = "block"
        // document.getElementById("signup_button").style.display = "block"
        // document.getElementById("username_label").style.display = "none"
        // document.getElementsByClassName("user_icon")[0].style.display = "none"
        $("#login_button").show()
        $("#signup_button").show()
        $("#username_label").hide()
        $(".user_icon").hide()
    }
}