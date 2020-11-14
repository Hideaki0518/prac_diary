from django.views import generic
from .forms import InquiryForm


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'


class InquiryViews(generic.FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
