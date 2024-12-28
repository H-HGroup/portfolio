const adminStatus = document.querySelector('.admin_status');
const sendMassageButton = document.querySelector('.send_icon');
const massegeText = document.querySelector('.text');
let number = document.querySelector('.number');
let userName = document.querySelector('.name');
let sendInfoButton = document.querySelector('.send-info-button');
let userInfo = document.querySelector('.user-info');



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
        // add admin to local storage
        localStorage.setItem('admin',JSON.stringify(data.admin));

        if (JSON.parse(localStorage.getItem('admin'))==='offline') {
            adminStatus.firstElementChild.innerHTML = 'sorry, admin is offline. We will respond soon.'
        }
         else {
           adminStatus.firstElementChild.innerHTML = `you are connected to ${data.admin}`
            
        }
    })
    
}
 

// send button action
sendInfoButton.addEventListener('click',()=>{
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
    
    if (JSON.parse(localStorage.getItem('admin'))==='offline') {
        adminStatus.firstElementChild.innerHTML = 'sorry, admin is offline. We will respond soon.'
    }
     else {
       adminStatus.firstElementChild.innerHTML = `you are connected to ${JSON.parse(localStorage.getItem('admin'))}`
        
    }
}
userInfoRemover();


///// end connection /////


/////////// send massage ////////////////

sendMassageButton.addEventListener('click',()=>{
    if(localStorage.getItem('user') && massegeText.value.length > 0){
            fetch('http://127.0.0.1:8000/SendMassage/', {
                method:'POST',
                headers:{
                    'Connect-Type':'application/json',
                    'X-CSRFToken' : csrftoken,
                },
                body: JSON.stringify({  
                    msg: massegeText.value,  
                    senderName: JSON.parse(localStorage.getItem('user'))[0].username,
                    senderNumber: JSON.parse(localStorage.getItem('user'))[0].usernumber,  
                    reciver: JSON.parse(localStorage.getItem('admin'))  
                }),          
            })
            .then (res=>res.json())
            .then (data=>{
                console.log(data);
            })
    }
})
