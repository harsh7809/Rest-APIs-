
const URL = 'http://127.0.0.1:8000/api1/per';

let btn= document.querySelector("#but");
let div = document.querySelector("#cont");

btn.addEventListener('click', ()=>{
    
    getdata();
    
});


const getdata = async() =>{
    
    let response = await fetch(URL);   
  //  console.log(response);        
    let data = await response.json();
    for (let i=0; i<data.length; i++) {
    div.innerHTML += `Name: ${data[i]['name']}, Age: ${data[i]['age']}<br>`;
    
    };
    

   
}; 

