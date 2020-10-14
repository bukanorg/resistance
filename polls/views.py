from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def store_cookie(request, cookie):
    response = HttpResponse('blah')
    response.set_cookie('cokie', cookie)
    return response


def get_cookie(request):
    value = request.COOKIES.get('cokie')
    if value is not None:
        return HttpResponse("cookie %s" % value)
    else:
        return HttpResponse("no cookie")
