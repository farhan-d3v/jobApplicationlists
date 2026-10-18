from django.shortcuts import get_object_or_404, render,redirect

from applications.forms import JobApplicationForm
from applications.models import JobApplication

def company_list(request):
    company = JobApplication.objects.all()

    return render(
        request,
        "company/company_list.html",
        {"company":company}
    )
def add_application(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("company_list")
    else:
        form = JobApplicationForm()

    return render(
        request,
        "company/application_form.html",
        {"form": form}
    )

def edit_application(request, application_id):
    application = get_object_or_404(JobApplication,id = application_id )

    if request.method == "POST":
        form = JobApplicationForm(request.POST,instance=application)
        if form.is_valid():
            form.save()
            return redirect("company_list")
    else:
        form = JobApplicationForm(instance=application)
    return render(
        request,
        "company/application_form.html",
                {"form": form}
            )

def delete_application(request, application_id):
    application = get_object_or_404(
        JobApplication, id=application_id
    )

    if request.method == "POST":
        application.delete()
        return redirect("company_list")

    return render(
        request,
        "company/confirm_delete.html",
        {"application": application}
    )