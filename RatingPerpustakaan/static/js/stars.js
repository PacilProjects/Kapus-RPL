const one = document.getElementById("first")
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

const handleSelect = (selection) => {
    switch(selection){
        case 'first':{
            one.classList.add('checked')
            two.classList.remove('checked')
            three.classList.remove('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            return
        }
        case 'second':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.remove('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            return
        }
        case 'third':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            return
        }
        case 'fourth':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.add('checked')
            five.classList.remove('checked')
            return
        }
        case 'fifth':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.add('checked')
            five.classList.add('checked')
            return
        }
    }
}
const handleClick = (selection) => {
    switch(selection){
        case 'first':{
            one.classList.add('clicked')
            two.classList.remove('clicked')
            three.classList.remove('clicked')
            four.classList.remove('clicked')
            five.classList.remove('clicked')
            return
        }
        case 'second':{
            one.classList.add('clicked')
            two.classList.add('clicked')
            three.classList.remove('clicked')
            four.classList.remove('clicked')
            five.classList.remove('clicked')
            return
        }
        case 'third':{
            one.classList.add('clicked')
            two.classList.add('clicked')
            three.classList.add('clicked')
            four.classList.remove('clicked')
            five.classList.remove('clicked')
            return
        }
        case 'fourth':{
            one.classList.add('clicked')
            two.classList.add('clicked')
            three.classList.add('clicked')
            four.classList.add('clicked')
            five.classList.remove('clicked')
            return
        }
        case 'fifth':{
            one.classList.add('clicked')
            two.classList.add('clicked')
            three.classList.add('clicked')
            four.classList.add('clicked')
            five.classList.add('clicked')
            return
        }
    }
}
const handleOut = (selection) => {
    switch(selection){
        case 'first':{
            one.classList.remove('checked')
            return
        }
        case 'second':{
            one.classList.remove('checked')
            two.classList.remove('checked')
            return
        }
        case 'third':{
            one.classList.remove('checked')
            two.classList.remove('checked')
            three.classList.remove('checked')
            return
        }
        case 'fourth':{
            one.classList.remove('checked')
            two.classList.remove('checked')
            three.classList.remove('checked')
            four.classList.remove('checked')
            return
        }
        case 'fifth':{
            one.classList.remove('checked')
            two.classList.remove('checked')
            three.classList.remove('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            return
        }
    }
}
const arr = [one,two,three,four,five]
// arr.forEach(item => item.addEventListener('click', (event)=> {
//     ['mouseover','mouseout','click'].forEach
//     handleClick(event.target.id)
// }))
arr.forEach(function (item1){
    ['mouseover','mouseout','click'].forEach(function (item2){
        if(item2 === "click"){
            item1.addEventListener('click', (event) =>{
                handleClick(event.target.id)
            })
        }
        if(item2 === "mouseover"){
            item1.addEventListener('mouseover', (event) =>{
                handleSelect(event.target.id)
            })
        }
        if(item2 === "mouseout"){
            item1.addEventListener('mouseout', (event) =>{
                handleOut(event.target.id)
            })
        }
    })
})



