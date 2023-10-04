
function showMenu(){
    document.querySelector(".left").style.display = 'flex'
    document.querySelector('.left').style.display = 'flex'
    x = window.matchMedia("(max-width: 700px)")
    if (x.matches){
        document.querySelector('.left').style.width = 'fit-content'
        document.querySelector('.left').style.position = 'fixed'
    }
    document.querySelector('.left').style.zIndex = '30'
    document.querySelector('.container').style.display = 'flex'
}


function hideMenu(){
    document.querySelector('.left').style.display = 'none'
    document.querySelector('.right').style.width = '100%'
    document.querySelector('.right').style.display = 'flex'
    document.querySelector('.right').style.justifyContent = 'center'
    document.querySelector('.main').style.justifyContent = 'center'
}


function searchPlus(){
    reg = /^\+[0-9]+$/
    field = document.querySelector('#phone').value
    
    // if (field.indexOf('+') == -1 || field[0] != '+' || field.indexOf('+') != 0){
    if (field.match(reg)){
        document.querySelector('.error').style.display = 'none'
    }else{
        document.querySelector('.error').style.display = 'block'
        document.querySelector('.error').style.backgroundColor = 'white'
        document.querySelector('.error').style.padding = '7px'
        document.querySelector('.error').style.borderRadius = '3px'
        document.querySelector('.error').style.color = 'red'
    }
    if(field.length < 13){
        document.querySelector('.note').style.display = 'block'
        document.querySelector('.note').style.backgroundColor = 'white'
        document.querySelector('.note').style.padding = '5px'
        document.querySelector('.note').style.marginTop = '3px'
        document.querySelector('.note').style.borderRadius = '2px'
        document.querySelector('.note').style.color = 'green'
        return false;
    }else{
        document.querySelector('.note').style.display = 'none'
    }
}
