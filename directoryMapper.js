function doit(el,ev){
    var x = el.nextElementSibling;

    if(x.style.display==='none'){
        x.style.display='inline';
    }
    else{
        x.style.display='none';
    }
}

function popFolders(){
    const buttonWords = ["Pop Go the Folders!","Fold 'Em Up!"];

    var folderCollection = document.querySelectorAll("div.folder");
    var folderBttn = document.querySelector('button#folder-button');

    if(folderBttn.textContent == buttonWords[0]){
        openFolderStr = "";

        folderCollection.forEach(function(el){
            if(el.style.display != "none"){
                openFolderStr += (el.dataset.addy+",,;");
                console.log(el);
                console.log(el.dataset.addy);
            };
            el.style.display = "inline";
        });
        folderBttn.dataset.openFolders = openFolderStr;
        folderBttn.innerHTML = buttonWords[1];
    }
    else{
        openFolderArr = folderBttn.dataset.openFolders.split(",,;");
        console.log(openFolderArr);

        folderCollection.forEach(function(el){
            if(!(el.dataset.addy in openFolderArr)){
                el.style.display = "none";
            }
            else{
                console.log("notOpen: "+el.dataset.addy);
            }
        });
        delete folderBttn.dataset.openFolders;
        folderBttn.innerHTML = buttonWords[0];
    }
}

function colorDZ(crayon){
    var dzEl = document.querySelector("div.drop-zone");
    dzEl.style.backgroundColor = crayon;
}

function allowDrop(ev){
    ev.preventDefault();
}

function drag(ev){
    ev.dataTransfer.setData("text/plain",ev.target.dataset.addy);
}

function showAddy(ev){
    var address = ev.dataTransfer.getData("text/plain");
    var firstCol = document.querySelector("div.column1");

    if(document.querySelector("div.link-display")){
        var newDiv = document.querySelector("div.link-display");
        var fileLink = newDiv.querySelector("a");
    }
    else {
        var newDiv = document.createElement("div");
        newDiv.className = "link-display";

        var fileLink = document.createElement("a");
        fileLink.target = "_blank";

        newDiv.appendChild(fileLink);
        firstCol.insertBefore(newDiv,document.querySelector("div.directory-map"));
    }

    fileLink.innerText = address;
    fileLink.href = address;
    //window.open('file:///'+address);

    colorDZ("#5f88f8");
}