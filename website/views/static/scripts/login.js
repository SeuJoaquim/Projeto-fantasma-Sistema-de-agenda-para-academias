const myForm = document.getElementById("login-form");


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


myForm.addEventListener("submit", (form)=> {
    form.preventDefault();
    const formData = new FormData(myForm)

    fetch("/auth/confirmacao", {
        method: 'post',
        body: formData
    }).then( (resp) =>{
        return resp.json();
    }).then( (json)=> {
        loadMessages(json);
    }).cath((e)=>{
        console.log(e);
    });

});
