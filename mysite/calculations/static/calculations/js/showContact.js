//////////////////////////////////  Scroll to contacts  /////////////////////////////////

const contactLink = document.querySelector('#contact_link');
const footer = document.querySelector('footer');

contactLink.addEventListener('click', function(event) {
    footer.scrollIntoView({block: "center", behavior: "smooth"});
    event.preventDefault();
})
