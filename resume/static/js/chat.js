const onlineStatus = document.querySelector('.online-status');

onlineStatus.addEventListener('click',()=>{
    onlineStatus.firstElementChild.classList.toggle('online');
    if (onlineStatus.lastElementChild.innerHTML === 'online'){
        onlineStatus.lastElementChild.innerHTML='offline';
    }
    else{
        onlineStatus.lastElementChild.innerHTML='online';
    };
    
})


