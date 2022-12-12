// Change @media screens max-width 430px

function handleTabletChange(mediaQuery) {

    if (mediaQuery.matches) {
        document.getElementById('responsive').innerHTML = `
        <div class="col-sm-12 text-center card-body ml-5">
            <div class="row w-50 mx-5 d-flex align-items-center justify-content-center card">1</div>
            <div class="row w-50 mx-5 d-flex align-items-center justify-content-center card">2</div>
            <div class="row w-50 mx-5 d-flex align-items-center justify-content-center card">3</div>
            <div class="row w-50 mx-5 d-flex align-items-center justify-content-center card">4</div>
            <div class="row w-50 mx-5 d-flex align-items-center justify-content-center card">5</div>
            <div class="row w-50 mx-5 d-flex align-items-center justify-content-center card">6</div>
            <div class="row w-50 mx-5 d-flex align-items-center justify-content-center card">7</div>
            <div class="row w-50 mx-5 d-flex align-items-center justify-content-center card">8</div>
            <div class="row w-50 mx-5 d-flex align-items-center justify-content-center card">9</div>
    </div>`
    }
}

let mediaQuery = window.matchMedia('(max-width: 430px)');
handleTabletChange(mediaQuery);
mediaQuery.addEventListener("change", () => {
    this.handleTabletChange();
});