
    let index = 0;
    const slides = document.querySelector(".slides");
    const totalSlides = slides.querySelectorAll("img").length;

    function showSlide() {
        slides.style.transform = `translateX(-${index * window.innerWidth}px)`;
    }

    function nextSlide() {
        index = (index + 1) % totalSlides;
        showSlide();
    }

    setInterval(nextSlide, 3000);
    window.addEventListener("resize", showSlide);


