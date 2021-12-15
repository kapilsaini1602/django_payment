from django.utils.deprecation import MiddlewareMixin
from paytm_integ.models import OrderDetails
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


class CheckStatus(MiddlewareMixin):

    # def process_request(self, request):
    #     print(request.body)
    #     print(request.path)
    #     obj = OrderDetails.objects.all()
    #     print(obj)
    #
    #     return None

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path == '/':
            return redirect("https://227c-223-178-209-150.ngrok.io/pay")
        return None



    # def process_exception(self, request, exception):
    #     if exception:
    #         return redirect("https://0589-223-178-209-150.ngrok.io/pay")
    #     else:
    #         print("..")



    # def process_response(self, request, response):
    #     print('processing response')



# process_request: called before django determines which view should handle request.
# process_view: called before django know which view to call but before triggerning actual view of url.
# process_exception: Handles the exception caused by views.
