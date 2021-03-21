
const myForm = document.getElementById("signUp-form");


function loadMessages(obj){
    
    function insertInList(text){
        let field       = document.getElementById("alert-list")
        let li          = document.createElement("li");

        li.appendChild(document.createTextNode(text['message']));
        if (text.category === "error"){
            li.setAttribute("class","error")
        } 
        else{
            li.setAttribute("class","success")
        }
        
        field.appendChild(li);
    }
    const div   = document.getElementById("alert-div")
    div.innerHTML =""  

    const ul    = document.createElement("ul")
    ul.appendChild(document.createTextNode(""))
    ul.setAttribute("id","alert-list")
    div.appendChild(ul)

    const messages  = obj.messages;
    for (message of messages) {
        insertInList(message)
    }
    div.style.visibility = "visible"

    
    
}

function login(formData){
    const email         = formData.get("email");
    const password      = formData.get("password1");
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
            alert("Tente novamente")
        }
    });
}

myForm.addEventListener("submit", (form)=> {
    form.preventDefault();
    const formData = new FormData(myForm)

    fetch("/auth/signUp", {
        method: 'post',
        body: formData
    }).then( (resp) =>{
        return resp.json();
    }).then( (json)=> {
        const messages  = json.messages;

        let formIsValid = true
        for (message of messages){
            if (message.category === "error"){
                formIsValid = false
            }
        }
        if (formIsValid){
            login(formData)
        }else{
            loadMessages(json);
        }
    });
});
