from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import Context
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ArchiveIndexView, DetailView, CreateView, DeleteView 
# from xhtml2pdf import pisa             # import python module
from accounts.models import User, Trainee

"""def index(request):
    return HttpResponse("Hello World.")

def detail(request, roster_id):
    return HttpResponse("You're looking at poll %s." % roster_id)

def results(request, roster_id):
    return HttpResponse("You're looking at the results of poll %s." % roster_id)

def vote(request, roster_id):
    return HttpResponse("You're voting on poll %s." % roster_id)

# Define your data
sourceHtml = "<html><body><p>To PDF or not to PDF<p></body></html>"
outputFilename = "test.pdf"

# Utility function
def convertHtmlToPdf(sourceHtml, outputFilename):
    # open output file for writing (truncated binary)
    resultFile = open(outputFilename, "w+b")

    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
            sourceHtml,                # the HTML to convert
            dest=resultFile)           # file handle to recieve result

    # close output file
    resultFile.close()                 # close output file

    # return True on success and False on errors
    return pisaStatus.err

# Main program
if __name__=="__main__":
    pisa.showLogging()
    convertHtmlToPdf(sourceHtml, outputFilename)
"""


