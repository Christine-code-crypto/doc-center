// alert("Docs center")
// watchers
let fileAvailable = null;

// global variables
const date = new Date();

// add loader animation during navigation and on page load
const loadingContainer = document.querySelector("#loading_container");
const spinner = document.querySelector("#spinner");

// listen to the load event
window.addEventListener("load", () => {
    loadingContainer.style.display="none";
})

// get current year and append it to the copyright text
let copyright = document.querySelector("#copyright");
const year = date.getFullYear();
copyright.append(year);

// test search button
const searchButton = document.querySelector("#searchButton");
searchButton.addEventListener("click", () => {
    console.log("you clicked me")
})

// preview files
const fileInput = document.querySelector("#fileInput");
const filePreview = document.querySelector("#filePreview");
// listen for change event on fileInput
fileInput.onchange = (event) => {
    const file = event.target.files[0];
    if(file) fileAvailable = file;
    console.log(file);
    if(file){
        // show filePreview
        filePreview.style.display = "block";
        // hide fileInput
        fileInput.style.display = "none";
        filePreview.src = URL.createObjectURL(file);
    }else{
        // hide filePreview
        filePreview.style.display = "none"
        // show fileInput
        fileInput.style.display = "block";
    }
}

// show document details
const showDocumentDetails = document.querySelectorAll("#openModal")
const closeModal = document.querySelector("#closeModal")
const documentModal = document.querySelector("#showDocumentDetails")
const modalContent = document.querySelector("#modalContent");
const modalInfo = document.querySelector("#modalInfo");
const popUp = document.querySelector("#popUp");

closeModal.addEventListener("click", () => {
    // hide modal
    console.log("close modal")
    documentModal.style.display = "none";
})


showDocumentDetails.forEach(button => button.addEventListener("click", () => {
      const modalInfo = button.parentNode.childNodes[11];
      console.log(button.parentNode.childNodes[11]);

      // fill the modal
    //   modalContent.querySelector("#documentImage").src = modalInfo.children[0].textContent; // image
    //   modalContent.querySelector("#documentName").textContent = modalInfo.children[1].textContent; // name
    //   modalContent.querySelector("#documentCategory").textContent = modalInfo.children[2].textContent; // name
    //   modalContent.querySelector("#documentDescription").textContent = modalInfo.children[3].textContent; // name
    //   modalContent.querySelector("#documentCreatedAt").textContent = modalInfo.children[4].textContent; // name

    //   alert("view document " );
        documentModal.style.display = "block";
        popUp.style.display = "block";
      })
);

// mark book as returned or not using checkbox
const returnedCheckbox = document.querySelector("#returned");
const returnedForm = document.querySelector("#returnForm")
returnedCheckbox.addEventListener("change", () => {
    returnedForm.submit();
})