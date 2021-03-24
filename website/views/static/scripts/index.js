document.addEventListener("DOMContentLoaded", ()=>{
    fetch("/app/user")
    .then( (resp) =>{
        return resp.json()
    })
    .then( (json) =>{
        
        function createChild(content){
            const ul            = document.getElementById("user-data-ul")
            let li              = document.createElement("li");
            li.appendChild(document.createTextNode(content));
            ul.appendChild(li);

        }
        const div   = document.getElementById("data-div")
        div.innerHTML =""  
    
        const ul    = document.createElement("ul")
        ul.appendChild(document.createTextNode(""))
        ul.setAttribute("id","user-data-ul")
        div.appendChild(ul)

        const email         = json.email
        const name          = json.name

        createChild(email)
        createChild(name)

        div.style.visibility = "visible"
        
    })
});