const hamburger=document.querySelector(".hamburger");
const navvy=document.querySelector(".navvy");
const right=document.querySelector(".right");


hamburger.addEventListener("click",()=>{
    hamburger.classList.toggle("active");
    navvy.classList.toggle("active");
    right.style.display=="flex"?right.style.display="none":right.style.display="flex";
})

document.querySelectorAll("nav-link").forEach(n => n.addEventListener("click",()=>{
    hamburger.classList.remove("active");
    navvy.classList.remove("active");

    
}))