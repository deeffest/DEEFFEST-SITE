document.getElementById('search').addEventListener('input', function(e) {
    var value = e.target.value.toLowerCase();
    var items = Array.from(document.querySelectorAll('.project, .news'));

    items.forEach(function(item) {
        var title = item.querySelector('.project-title, .news-title').textContent.toLowerCase();
        if (title.indexOf(value) === -1) {
            item.style.display = 'none';
        } else {
            item.style.display = 'flex';
        }
    });
});