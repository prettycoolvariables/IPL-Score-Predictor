document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('nav a'); 

    links.forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault(); 
            const href = this.getAttribute('href'); 
            
            document.getElementById('main-content').style.opacity = 0;

            setTimeout(function() {
                window.location.href = href;
            }, 500); 
        });
    });
});