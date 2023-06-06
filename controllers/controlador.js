let botones = document.querySelectorAll(".generar-boton");
botones.forEach(function(boton) {
    boton.addEventListener("click", function(evento){
        evento.preventDefault();
        let reporte = document.getElementById("reporte");
        reporte.classList.remove("d-none");
        // Obtén el ID del panel objetivo desde el atributo data-bs-target
        let panelId = boton.getAttribute("data-bs-target");
        // Obtén el iframe dentro del panel y establece la URL del archivo correspondiente
        let iframe = document.querySelector(`${panelId} iframe`);
        iframe.src = `./tables/${panelId.substring(1)}.html`;
    });
});
