from django.shortcuts import render, redirect, get_object_or_404
from .models import Study
from .forms import StudyForm

def study_list_view(request):
    studies = Study.objects.all()
    return render(request, 'studies/study_list.html', {'studies': studies})

def add_study_view(request):
    if request.method == 'POST':
        form = StudyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('study_list')
    else:
        form = StudyForm()
    return render(request, 'studies/add_study.html', {'form': form})

def view_study_view(request, pk):
    study = get_object_or_404(Study, pk=pk)
    return render(request, 'studies/view_study.html', {'study': study})

def edit_study_view(request, pk):
    study = get_object_or_404(Study, pk=pk)
    if request.method == 'POST':
        form = StudyForm(request.POST, instance=study)
        if form.is_valid():
            form.save()
            return redirect('study_list')
    else:
        form = StudyForm(instance=study)
    return render(request, 'studies/edit_study.html', {'form': form})

def delete_study_view(request):
    if request.method == 'POST':
        ids_to_delete = request.POST.getlist('delete_ids')
        if ids_to_delete:
            Study.objects.filter(id__in=ids_to_delete).delete()
    return redirect('study_list')