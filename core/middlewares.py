from django.utils.deprecation import MiddlewareMixin
import time
from core.models import Log

class LogMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if not '/admin/' in request.get_full_path():
            self.start_time = time.time()

    def process_response(self, request, response):
        if not '/admin/' in request.get_full_path():
            self.execution_time = time.time() - self.start_time
            log = Log(path=request.path, method=request.method, start_time=self.start_time, time=self.execution_time)  
            log.save()
        return response

