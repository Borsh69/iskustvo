function getCSRFToken() {
    const name = 'csrftoken';
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith(name + '=')) {
            return cookie.substring(name.length + 1);
        }
    }
    return null;
}

function sendComment(index) {
    var text = document.getElementById('commentArea').value;
    const csrftoken = getCSRFToken();
    $.ajax({
        type: "POST",
        url: "/post_comment/",
        data: {
            'text': text,
            'index': index,
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        },
        success: function(data) {
            console.log(data);
        }
    });
}