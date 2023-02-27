document.addEventListener('DOMContentLoaded', () => {

    var instance = M.Carousel.init({
        fullWidth: true,
        indicators: true
      });
    
      // Or with jQuery    
      $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true
      });
    // Navegation Menu
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
 
    // Slider
    var elems = document.querySelectorAll('.slider');
    var instances = M.Slider.init(elems, {
        indicators: false,
        height: 500,
        duration: 500,
        interval:3000
    });

});