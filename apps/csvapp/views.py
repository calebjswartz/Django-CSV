from django.shortcuts import render
import csv, io
from django.contrib import messages
from csvapp.models import Biostats
import pandas as pd

# Create your views here.
def file_upload(request):
    template = 'upload.html'
    data = Biostats.objects.all()
    prompt = {
        'order': 'Order of the CSV should be name, sex, age, height, weight.',
        'Biostats': data
    }
    if request.method == "GET":
        return render(request, template, prompt)
    try:
        csv_file = request.FILES['file']
        #check that file is csv
        if not csv_file.name.endswith('csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE.')
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = Biostats.objects.update_or_create(
                name=column[0],
                sex=column[1],
                age=column[2],
                height=column[3],
                weight=column[4]
            )
        context = {}
        return render(request,template, context)
    except Exception as e:
        messages.error(request,"Unable to upload file. "+repr(e))
        return render(request, template, prompt)

def display(request):
    df = pd.DataFrame.from_records(Biostats.objects.all().values())
    df_html = df.to_html()
    context = {'loaded_data':df_html}
    return render(request, 'display.html', context)