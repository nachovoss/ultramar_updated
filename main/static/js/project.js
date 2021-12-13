(function(){

    const btnErase=document.querySelectorAll(".btnErase");

    btnErase.forEach(btn=>{
        btn.addEventListener('click',(e)=> {
            const confirmacion=confirm('Are you sure?');
            if(!confirmacion){
            e.preventDefault();
            }
        });
    });
})();


