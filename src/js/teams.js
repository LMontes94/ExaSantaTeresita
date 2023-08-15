const yearLinks = document.querySelectorAll(".year-link");
const teamList = document.getElementById("team-list");

yearLinks.forEach((yearLink) => {
    yearLink.addEventListener("click", (event) => {
        event.preventDefault();
        const selectedYear = event.target.getAttribute("data-year");
        // Aquí puedes usar JavaScript para cargar y mostrar la lista de equipos correspondiente al año seleccionado
        teamList.innerHTML = `<li class="list-group-item">Equipo 1 (${selectedYear})</li>
                                    <li class="list-group-item">Equipo 2 (${selectedYear})</li>
                                    <li class="list-group-item">Equipo 3 (${selectedYear})</li>`;
    });
});