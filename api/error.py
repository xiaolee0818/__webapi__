from . import api1


@api1.route("/error")
def error():
    return "<h1>fix it!</h1> "
