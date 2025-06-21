import time
# from datetime import datetime, time
from django.http import HttpResponseForbidden
#
# class LogIPMiddleware:
#
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         ip = request.META.get('REMOTE_ADDR', 'Nomalum IP')
#         # print(request.META
#         for k,v in request.META.items():
#             print(f"{k}------{v}")
#         now = datetime.datetime.now()
#         print(f"[ {now} ] So'rov IP: {ip}")
#         response = self.get_response(request)
#         return response

#
# class Middleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         now = datetime.now().time()
#         start_time = time(8, 0, 0)
#         end_time = time(19,0,0)
#         if not(start_time<=now<=end_time):
#             return HttpResponseForbidden("Sait 08:00 dan 18:00 gacha ishlaydi")
#         response =self.get_response(request)
#         return response
def get_client_id(request):
    x_forwarded_for=request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        print(x_forwarded_for)
        ip = x_forwarded_for.split(',')[0]
        print(ip)
    else:
        ip=request.META.get('REMOTE_ADDR')
    return ip

class RequestCount:
    def __init__(self, get_response):
        self.get_response = get_response
        self.request = {}

    def __call__(self, request):
        ip = get_client_id(request)
        now = time.time()
        if ip not in self.request:
            self.request[ip]=[]
        self.request[ip]=[t for t in self.request[ip] if (now-t)<10]
        if len(self.request[ip])>=5:
            return HttpResponseForbidden("Siz juda ko'p so'rov yubordingiz 10 sekuntda faqat 5 marta jo'natish mumkin")
        self.request[ip].append(now)
        response=self.get_response(request)
        return response

