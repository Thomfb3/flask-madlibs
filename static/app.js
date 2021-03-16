const madlibForm = document.getElementById("madlib-form");
const submit = document.getElementById("submit");
const madlibInputList = document.querySelectorAll(".form-control")

let madlibInputarray = [];
let sufficientInput = false;

madlibForm.addEventListener("change", function(e) {
    madlibInputarray = [];
    madlibInputList.forEach((input) => madlibInputarray.push(input.value))
    sufficientInput = madlibInputarray.every((word) => word.length >= 3)
})


submit.addEventListener("click", function(e) {    
    if(!sufficientInput) {
       e.preventDefault();
       alert("Words must be at 3 letters long!");
    }
})
