from django.shortcuts import render, redirect
from .forms import MultipleFileUploadForm
from .models import MultipleFileUpload
from django.contrib import messages
import json
import PyPDF2
from django.db.models import Q

def index(request):
    return render(request, 'uploads.html')

def upload_files(request):
    if request.method == 'POST':
        form = MultipleFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            for file in request.FILES.getlist('files'):
                title = file.name  

               
                if file.name.endswith('.pdf'):
                    content = extract_text_from_pdf(file)
                else:
                    content = file.read().decode('utf-8')  # Read text file content

                
                position_index = generate_positional_index(content)

               
                MultipleFileUpload.objects.create(title=title, content=content, position_index=position_index)
            messages.success(request, 'Files uploaded successfully!')
            form = MultipleFileUploadForm()
            return render(request, 'search.html')  
    else:
        form = MultipleFileUploadForm()

    files = MultipleFileUpload.objects.all() 
    return render(request, 'uploads.html', {'form': form, 'files': files})

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()
    return text

def generate_positional_index(content):
    words = content.split()
    index = {}
    for position, word in enumerate(words):
        if word in index:
            index[word].append(position)
        else:
            index[word] = [position]
    return index

def search_files(request):
    query = request.GET.get('query', '')
    search_terms = [term.strip() for term in query.split(';') if term.strip()] 

    
    q_objects = Q()
    for term in search_terms:
        q_objects |= Q(content__icontains=term) | Q(title__icontains=term)
    files_matching_query = MultipleFileUpload.objects.filter(q_objects)

    return render(request, 'search.html', {'query': query, 'files': files_matching_query})
