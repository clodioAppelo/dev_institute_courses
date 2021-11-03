
// Create a new HTML file

// Create a banner saying "The sales end in 10min ! " . Style the banner and make it visible to the user after 5 sec.

// const banner  = document.querySelector(`#banner`)
// let timeOut = setTimeout(() => {
//     banner.style.display="block"
// }, 5000);

// clearTimeout(timeOut)

// timeOut = setTimeout(() => {
//     banner.style.display="block"
// }, 7000);


//-------------------------------------------------------------------------------------------


// const timerSpan  = document.querySelector(`#timer`)
// let timer = 10
// let interval = setInterval(() => {
//     timer--
//     timerSpan.textContent = timer
//     // if(timer===0){
//     //     clearInterval(interval)
//     // }
// }, 1000);


//------------------------------------------------------------------------------------------
// let incrementXYPostion = 0
// const redCube = document.querySelector("#red")
// let incrementInterval= ()=>{let currentInterval  = setInterval(() => {
//     redCube.style.top=`${incrementXYPostion}px`
//     redCube.style.left=`${incrementXYPostion}px`
//     incrementXYPostion+=50
//     if(incrementXYPostion==500){
//         clearInterval(currentInterval)
//         incrementXYPostion = 0
//     }
// }, 500)};
// let starter = document.querySelector(`#starter`)
// starter.addEventListener('click', incrementInterval);