from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Student,Project
# Create your views here.
def index(request):
    return render(request, 'smartForm/index.html', {"accept":False, "reject":False})
def formAccept(request):
    if request.method == 'POST':
        name = request.POST['project-name']
        size = int(request.POST['team_size'])
        projects = Project.objects.all()
        if(len(projects)==0):
            project = Project(project_name=name,team_size=size)
            for i in range(1,size+1):
                s_name = request.POST['name'+str(i)]
                usn = request.POST['usn'+str(i)]
                email = request.POST['email'+str(i)]
                student = Student(name=s_name,usn=usn,email=email)
                student.save()
                if i == 1:
                    project.student1_usn = student
                elif i == 2:
                    project.student2_usn = student
                elif i == 3:
                    project.student3_usn = student
            project.save()
        else:
            sentences = [p.project_name for p in projects]
            sentences.append(name)
            model = SentenceTransformer('bert-base-nli-mean-tokens')
            sentence_embeddings = model.encode(sentences)
            print(sentence_embeddings)
            res = cosine_similarity(
                [sentence_embeddings[len(sentences)-1]],
                sentence_embeddings[:len(sentences)-1]
            )
            res_max = max(res[0])
            if(res_max>0.75):
                print("Reject")
                context = {"accept":False, "reject":True}
            else:
                print("Accept")
                project = Project(project_name=name,team_size=size)
                for i in range(1,size+1):
                    s_name = request.POST['name'+str(i)]
                    usn = request.POST['usn'+str(i)]
                    email = request.POST['email'+str(i)]
                    student = Student(name=s_name,usn=usn,email=email)
                    student.save()
                    if i == 1:
                        project.student1_usn = student
                    elif i == 2:
                        project.student2_usn = student
                    elif i == 3:
                        project.student3_usn = student
                project.save()
                context = {"accept":True, "reject":False}
    return render(request, 'smartForm/index.html', context)