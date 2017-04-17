# dojo/views_cvb.py
import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from askdjango import settings
from django.views.generic import View, TemplateView


class PostListView1(View):

    def get(self, request):
        name="공유"
        html=self.get_template_string().format(name=name)
        return HttpResponse(html)


    def get_template_string(self):
        return '''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p> Class View list 1 </p>
        <p> cvb 여러분의 파이썬&장고 페이스메이커가 되겠습니다.</p>'''

post_list1 = PostListView1.as_view()



class PostListView2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name']="클래스 TemplateView 공유"
        return context

post_list2 = PostListView2.as_view()


class PostListView3(View):

    def get(self, request):
        return JsonResponse(self.get_data(),
                            json_dumps_params={'ensure_ascii':False}
        )
    def get_data(self):
        return {
            'message':"JsonResponse 응답입니다.",
            'item':['python', '장고', 'aws'],
        }
post_list3 = PostListView3.as_view()


class ExcelDownloadView(View):
    filepath = '/Users/peterLee/dev/askdjango/5w-hw.xlsx'

    def get(self, request):

        filename = os.path.basename(self.filepath)

        with open(self.filepath, 'rb') as f:

            response = HttpResponse(f, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)

            return response

