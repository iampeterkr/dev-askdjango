# dojo/views.py
import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from askdjango import settings


def mysum(request, numbers):
    # request: HttpRequest
    print(numbers)
    result=sum(map(lambda s: int(s or 0), numbers.split("/")))
    print(result)
    return HttpResponse(result)


def hello(request, name, age):
    print(name, age)
    result="안녕하세요 {}, {} 살입니다.".format(name,age)
    return HttpResponse(result)


def post_list1(request):
    name="공유"
    return HttpResponse('''
        <h1> POST_LIST1 </h1>
        <p> {name} </p>
        <p> Post list 1 입니다. </p>
    '''.format(name=name))


def post_list2(request):
    name="공유"
    result=render(request, 'dojo/post_list.html',{'name':name} )

    return result


def post_list3(request):
    return JsonResponse(
        {
            'message':"JsonResponse 응답입니다.",
            'item':['python', '장고', 'aws'],
        }, json_dumps_params={'ensure_ascii':False}
        )


def excel_download(request):
    
   # filepath='/Users/peterLee/dev/askdjango/5w-hw.xlsx'
#    filepath=os.path.join(settings.BASE_DIR, '5w-hw.xlsx')
    filepath=os.path.join(settings.BASE_DIR, '5w-hw.xlsx')
    filename=os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel') # 필요한 응답헤더 세팅
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response