let number = document.querySelector('.number');
let userName = document.querySelector('.name');
let sendButton = document.querySelector('.send-info-button');
let userInfo = document.querySelector('.user-info')



/////////// connection //////////////


// ajax code fron django document
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

 
array=[];

// send username and user number to backend
function connection(name, number) {
    fetch('http://127.0.0.1:8000/ConnectionToAdmin/', {
        method:'POST',
        headers:{
            'Connect-Type':'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body:JSON.stringify({'userName':name, 'userNumber': number}),

    })
    .then (res=>res.json())
    .then (data=>{
        console.log(data);
        userInfo.remove();
        // add username and usernumber to local storage
        localStorage.setItem('user',JSON.stringify(array));
    })
    
}

// send button action
sendButton.addEventListener('click',()=>{
    nameValue = userName.value;
    numerValue = number.value;
    array.push({'username':nameValue, 'usernumber':numerValue})
    userName.value = "";
    number.value = "";


    connection(numerValue, nameValue)
   
})

// remove userInfo box even after refresh
let userInfoRemover = () =>{
    if(localStorage.getItem('user')){
        userInfo.remove()
    }
}
userInfoRemover();


/////////// end connection //////////////


