function hello() {
    console.log("hello22")
}


function saveCookieCheckboxState(doc, elementId, cookieId) {
    const checkbox = doc.getElementById(elementId);
    if (checkbox == null) {
        return
    }

    if (checkbox.checked) {
        doc.cookie = cookieId + '=checked';
    } else {
        doc.cookie = cookieId + '=unchecked';
    }
}

function loadCookieCheckboxState(doc, elementId, cookieId) {
    const checkbox = doc.getElementById(elementId);
    if (checkbox == null) {
        return;
    }
    const checkboxState = getCookie(doc, cookieId);
    if (checkboxState === 'checked') {
        checkbox.checked = true;
    } else {
        checkbox.checked = false;
    }
}

function getCookie(doc, name) {
    const cookies = doc.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith(name + '=')) {
            return cookie.substring(name.length + 1);
        }
    }
    return '';
}
