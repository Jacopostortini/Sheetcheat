function createCookie(key, value, expiration){
    let cookie = escape(key)+"="+escape(value)+";"
    if(expiration!=null){
        cookie += "expires="+expiration+";"
    }
    document.cookie = cookie
}

function getCookie(name){
    let key = name+"="
    let cookies = document.cookie.split(';');
    	for (let i = 0; i < cookies.length; i++) {
    		let cookie = cookies[i];
    		while (cookie.charAt(0) === ' ') {
                cookie = cookie.substring(1, cookie.length);
            }
    		if (cookie.indexOf(key) === 0) {
                return cookie.substring(key.length, cookie.length);
            }
    	}
    	return null;
}

function deleteCookie(key){
    createCookie(key, "", -1)
}