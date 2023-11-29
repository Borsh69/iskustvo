function getCookie(name) {
    let matches = document.cookie.match(new RegExp(
      "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
    }

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
    var myCookies = getCookie("In_Account")
    if (myCookies == "True"){
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
                document.getElementById('commentArea').value = "";
                var replace = document.getElementById('commentSection');
                replace.innerHTML = '';
                replace.innerHTML = data;
            }
        });
    }
    else {
        window.location.replace("/login/");
    }
    
}