import urllib

from . import http, dict, errors

noresponse = "Couldn't contact the API right now..."


def eightball():
    r = http.get("/8ball")
    return dict.JsonDict({
        "text": r["response"],
        "image": r["url"]
    })


def img():
    try:
        return http.get("/img/random")["url"]
    except Exception as e:
        raise errors.NothingFound(noresponse)

def catboy():
    try:
        return http.get("/img/catboy")["url"]
    except Exception as e:
        raise errors.NothingFound(noresponse)

def yaoi():
    try:
        return http.get("/img/yaoi")["url"]
    except Exception as e:
        raise errors.NothingFound(noresponse)


def response():
    try:
        return http.get("/catboy")["response"]
    except Exception as e:
        raise errors.NothingFound(noresponse)
