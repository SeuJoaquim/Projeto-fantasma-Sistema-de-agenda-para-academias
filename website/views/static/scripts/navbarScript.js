function hasToken(){
    let cookieArr = document.cookie.split(";");
    
    for (const cookie of cookieArr) {
        let nameValue = cookie.split("=")
        console.log(nameValue[0])
        console.log(nameValue[1])
        if (nameValue[0].trim() === "token"){
            console.log("has cookie")
            return nameValue[1]
        } 
    }
    return false
}

document.addEventListener("DOMContentLoaded", ()=>{
    const token = hasToken();
    console.log(token)

    if(token){
        const login = document.getElementById("Login");
        const signUp = document.getElementById("signUp");
        login.remove()
        signUp.remove()
    }
    else{
        const logout = document.getElementById("Logout");
        logout.remove()
    }
}); 