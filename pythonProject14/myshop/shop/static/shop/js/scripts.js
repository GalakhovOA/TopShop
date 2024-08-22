
document.addEventListener('DOMContentLoaded', function () {
    const cartButtons = document.querySelectorAll('.btn');

    cartButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            const url = this.getAttribute('href');
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    alert('Product added to cart!');
                });
        });
    });
});
