from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import render, redirect

from django.views import View

# Create your views here.
from sessions_app.models import SessionTbl


class SetSessionView(View):
    def get(self, request):
        if 'counter' in request.session:
            request.session['counter'] += 1
        else:
            request.session['counter'] =0
        return HttpResponse(f'Thanks! counter is equal={request.session["counter"]}')

class ShowSessionView(View):
    def get(self, request):
        if 'counter' in request.session:
            request.session['counter'] += 1
            return HttpResponse(f'Thanks! counter is equal={request.session["counter"]}')
        else:
            return HttpResponse("There is no any counter")


class DeleteSessionView(View):
    def get(sef,request):
        pass
#         try:
#             if request.session[key]:
#                 del request.session[key]
#         except  KeyError:
#             pass
#         return HttpResponse("Deleted")

        # if 'counter' in request.session:
        #     del request.session['counter']
        #     return HttpResponse(f'Thanks! counter deleted')
        # else:
        #     return HttpResponse('There is no any counter'



class LoginView(View):
    def get(self, request):
        if 'loggedUser' not in request.session:
            return render(request, 'login_page.html')
        else:
            return HttpResponse(f'Hello here {request.session["loggedUser"]}')

    def post(self, request):
        name = request.POST.get('name')
        request.session['loggedUser'] = name
        return HttpResponse(f'So the second option {request.session["loggedUser"]}!')

class AddToSessionView(View):
    def get(self, request):
        return render(request, "add_to_session.html")

    def post(self, request):
        key = request.POST.get('key')
        value = request.POST.get('value')
        request.session[key] = value

        tbl_data = SessionTbl(key=key, value=value)
        tbl_data.save()
        return redirect("show_all_session")


class ShowAllSessionView(View):
    def get(self, request):
        tbl_data = SessionTbl.objects.all()
        return render(request, "table_data.html", {'tbl_data': tbl_data})

# class ShowAllSession2View(View):
#     def get(self, request):
#         # new_entry = SessionTbl(key=request.POST.get('key'), value=request.POST.get('value'))
#         # new_entry.save()
#         tbl_data = SessionTbl.objects.create(key=request.POST.get('key'), value=request.POST.get('value'))
#         return render(request, "table_data.html", {'tbl_data': tbl_data})

