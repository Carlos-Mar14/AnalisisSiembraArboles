let boton = document.getElementById("generarBoton")

boton.addEventListener("click", function(evento){
    evento.preventDefault()
    let reporte = document.getElementById("reporte")
    reporte.classList.remove("d-none")
})
