const loginShow = document.querySelector('.login-show');
const modalBg = document.querySelector('.modal-bg');
const loginClose = document.querySelector('.close-modal');

loginShow.addEventListener('click',(e)=>{
    modalBg.style.display='flex';
});

loginClose.addEventListener('click',(e)=>{
    modalBg.style.display='none';
});
