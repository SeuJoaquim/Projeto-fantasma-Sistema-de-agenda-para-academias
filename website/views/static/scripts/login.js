const myForm = document.getElementById("login-form");

function login(formData){
    const email         = formData.get("email");
    const password      = formData.get("password");
    let headers = new Headers();
    headers.set('Authorization', 'Basic ' + btoa(`${email}:${password}`))
    fetch("/auth/login", {
        method: 'post',
        headers: headers
    }).then( (resp) =>{
        return resp.json();
    }).then( (json)=> {
        const token = json.token;
        if (token){
            document.cookie = `token=${token}; expires=${json.exp}`;
            const url = `/app`
            window.location.href = url;
        }
        else{
            alert(json.message)
            alert("Tente novamente")
        }
    });
}

myForm.addEventListener("submit", (form)=> {
    form.preventDefault();
    const formData      = new FormData(myForm)
    login(formData);
});
