from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib import messages
from rest_framework.parsers import JSONParser
from . models import Status
from . serializers import StatusSerializers
import pickle
import joblib
# from sklearn.externals import joblib
import json
import numpy as np
import pandas as pd
from sklearn import preprocessing
from . forms import StatusForm



# Create your views here.

class StatusView(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializers
    

def ohevalue(df):
    ohe_col = joblib.load(r"D:\Data_Science_env\Data_Science\Mobiloitte\sales_classifier\ohecols.joblib")
    cat_columns = ['Country','Month', 'Lead_Type', 'Company_Size', 'Leads_Priority','Lead_Source','Market_Place_Subsource','Platform']
    df_preprocessed = pd.get_dummies(df, columns= cat_columns)
    newdict = {}
    for i in ohe_col:
        if i in df_preprocessed.columns:
            newdict[i] = df_preprocessed[i].values

        else:
            newdict[i] = 0
    newdf = pd.DataFrame(newdict)
    return newdf           





def winloss(unit):
    try:
        mdl = joblib.load(r"D:\Data_Science_env\Data_Science\Mobiloitte\sales_classifier\classifier_model.joblib")
        # mydata=pd.read_csv(r'D:\Data_Science_env\Data_Science\Mobiloitte\x_test.csv')
        # mydata = request.data
        # mydata = pd.get_dummies(mydata, drop_first= True)
        # unit = np.array(list(mydata.values()))
        # unit = unit.reshape(1, -1)
        scalers = joblib.load(r"D:\Data_Science_env\Data_Science\Mobiloitte\sales_classifier\scalers.joblib")
        x = scalers.transform(unit)
        y_pred = mdl.predict(x)
        y_pred = (y_pred > 0.6)
        new_df = pd.DataFrame(y_pred, columns= ['Status'])
        new_df = new_df.replace({True : 'Won', False : 'Lost'})
        return ('{}'.format(new_df))
        # return ('{}'.format(new_df))



    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)    



def myform(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            Month = form.cleaned_data['Month']
            Lead_Type = form.cleaned_data['Lead_Type']
            Leads_Priority = form.cleaned_data['Leads_Priority']
            Lead_Source = form.cleaned_data['Lead_Source']
            Market_Place_Subsource = form.cleaned_data['Market_Place_Subsource']
            Country = form.cleaned_data['Country']
            Business_Potential = form.cleaned_data['Business_Potential']
            Company_Size = form.cleaned_data['Company_Size']
            Platform = form.cleaned_data['Platform']
            # print(Month, Lead_Type, Lead_Priority, Lead_Source, Market_Place_Subsource, Country, Business_Potential, Company_Size, Platform)
            mydict = (request.POST).dict()
            df = pd.DataFrame(mydict, index = [0])
            answer = winloss(ohevalue(df))
      
            messages.success(request, '{}'.format(answer))
            # return render(request, '{}'.format(answer))
            # print(ohevalue(df))

    
    form = StatusForm()

    return render(request, 'myform.html', {'form' : form})