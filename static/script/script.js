// Change @media screens max-width 430px

function handleTabletChange(mediaQuery) {

    if (mediaQuery.matches) {
        document.getElementById('responsive').innerHTML = `
        <div class="col-sm-12 text-center card-body ml-5">
            <div class="row w-50 mx-5 d-flex align-items-center justify-content-center card h-25"><a>&nbsp; &nbsp; Copies/ Diaries<i class="fa-solid fa-book mx-3"></i></a></div>
            <div class="row w-50 mx-5 d-flex align-items-center justify-content-center card"><a>Pencils<i class="fa-solid fa-pencil mx-3"></i></a></div>
            <div class="row w-50 mx-5 d-flex align-items-center justify-content-center card"><a>Stationary<img src="/media/stationary.png" style="height:20px;width:30px;padding-left:10px;"></a></div>
            <div class="row w-50 mx-5 d-flex align-items-center justify-content-center card"><a>Lunch Boxes<i class="fa-solid fa-box mx-3"></i></a></div>
            <div class="row w-50 mx-5 d-flex align-items-center justify-content-center card"><a>Bags<img src="/media/bag.jpg" style="height:100px; width:120px;"></a></div>
            <div class="row w-50 mx-5 d-flex align-items-center justify-content-center card"><a>Pencil Cases<img src="/media/pencil-case.png" style="height:20px;width:30px;padding-left:10px;"></a></div>
            <div class="row w-50 mx-5 d-flex align-items-center justify-content-center card"><a>All Products<i class="fa-solid fa-bag-shopping fa-lg mx-3"></i></a></div>
            <div class="row w-50 mx-5 d-flex align-items-center justify-content-center card"><a>Art Suplies<i class="fa-solid fa-paintbrush mx-3"></i></a></div>
            <div class="row w-50 mx-5 d-flex align-items-center justify-content-center card h-25"><a>Folders<img src="/media/folder.png" style="height:30px;width:30px;padding-left:10px;"></a></div>
    </div>`
    }
}

let mediaQuery = window.matchMedia('(max-width: 430px)');
handleTabletChange(mediaQuery);
mediaQuery.addEventListener("change", () => {
    this.handleTabletChange();
});