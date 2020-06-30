from django.shortcuts import render
from CORE.models import UserNote, Note
from CORE.forms import NoteForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
	notes = Note.objects.all().order_by('date')
	form = NoteForm()
	return render(request, 'CORE/index.html', locals())

@csrf_exempt
def addNewNote(request):
	form = NoteForm(request.POST)

	if request.is_ajax() and form.is_valid():
		new_note = form.save(commit=False)
		new_note.save()
		return HttpResponse('done')

@csrf_exempt
def deleteNote(request):
	if request.is_ajax():
		Note.objects.filter(id=request.POST['id']).delete()
	return HttpResponse('done')

@csrf_exempt
def updateNote(request):

	if request.is_ajax():
		#import ipdb; ipdb.set_trace()
		note = get_object_or_404(Note, id=request.POST['id'])
		upt_form = NoteForm(request.POST, instance=note)

		if upt_form.is_valid():
			upt_form.save()
	return HttpResponse('done')