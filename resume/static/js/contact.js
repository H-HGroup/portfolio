let number = document.querySelector('.number');
let userName = document.querySelector('.name');
let sendButton = document.querySelector('.send-info-button');
let userInfo = document.querySelector('.user-info')





//connection

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
        localStorage.setItem('user',JSON.stringify(array));
    })
    
}


sendButton.addEventListener('click',()=>{
    nameValue = userName.value;
    numerValue = number.value;
    array.push({'username':nameValue, 'usernumber':numerValue})
    userName.value = "";
    number.value = "";


    connection(numerValue, nameValue)
    
})


let userInfoRemover = () =>{
    if(localStorage.getItem('user')){
        userInfo.remove()
    }
}
userInfoRemover();





