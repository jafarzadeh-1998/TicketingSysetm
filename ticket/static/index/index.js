console.clear();
const loginBtn =  document.querySelector('#login');
const signupBtn = document.querySelector('#signup');

function slideUp(){
  if(this.id == 'signup')
  {
    const parent = this.parentElement;
    const sibling = parent.nextElementSibling;
    parent.classList.remove('slide-up');
    sibling.classList.add('slide-up');
  } else 
  {
    const parent = this.parentElement.parentElement;
    const sibling = parent.previousElementSibling;
    parent.classList.remove('slide-up');
    sibling.classList.add('slide-up');
  }
}

loginBtn.addEventListener('click', slideUp);
signupBtn.addEventListener('click', slideUp);