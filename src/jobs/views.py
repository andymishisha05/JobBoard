from django.shortcuts import render
from .models import Job


# Create your views here.


def job_list(request):
    jobs_list = Job.objects.all()
    print(jobs_list)
    context = {"jobs": jobs_list}
    return render(request, "jobs.html", context)


def job_details(request, id):
    job = Job.objects.get(id=id)
    context = {"job": job}
    return render(request,"job_details.html",context)
    pass

