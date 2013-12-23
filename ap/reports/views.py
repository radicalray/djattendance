from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext
from django_tables2   import RequestConfig
from accounts.models import Trainee
from reports.tables import TraineeTable

def index(request):
    return HttpResponse("test")
    
def table(request):
	queryset = Trainee.objects.all()
	table = TraineeTable(queryset)
	RequestConfig(request).configure(table)
	return render_to_response("trainees.html", {"table": table}, context_instance=RequestContext(request))