from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from datetime import datetime
import urllib
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.

def contact(request):
    form = ContactForm()
    return render(request , 'name.html' , {'form':form}) 



def result(request):

    LEGACY_DATE_STRING = '%Y-%m-%d+%H:%M:%S'
    EXT_MEDIA_DATE_STRING = '%Y-%m-%d+%H:%M:%S.%f'
  
    result = "https://netsync.unl.edu/feeds/apps/"
    

    if(request.method == 'POST'):
      
        form = ContactForm(request.POST)
        
        if form.is_valid():
            print('true')
            mediaSource = form.cleaned_data['mediaSource']

            if(mediaSource == '-1'):
                val1 = ""

            else:
                a = dict(ContactForm.FIRST_CHOICES)
        
                val1 = a.get(mediaSource) + "/"


        
            
           
           
            #print('post {}'.format(mediaSource))
            contain = form.cleaned_data['contain']
            if(contain == '-1'):
                val2 = ""

            else:         
                b = dict(ContactForm.CONTAIN_CHOICES)
                val2 =  b.get(contain)  + "/"

       

            

            category = form.cleaned_data['category']
            if(category == '-1'):
               val3 = ""
               
            else:
               c = dict(ContactForm.SERIES_CAT_CHOICE)
               x1 = c.get(category)
               my_encoded_stringx1 = urllib.parse.quote_plus(x1)
               store_x1= my_encoded_stringx1.replace("%" , "&")
               store_x11 = store_x1.replace("26" , "")

               val3 = store_x11  + "/"
            

          
          
            

            netSeries = form.cleaned_data['netSeries']
            if(netSeries == '-1'):
                val4 = ""
            else:
                d = dict(ContactForm.NET_SERIES)
                x2 = d.get(netSeries) 
                my_encoded_string2 = urllib.parse.quote_plus(x2)
                store_x2= my_encoded_string2.replace("%" , "&")
                store_x22 = store_x2.replace("26" , "")

                val4 =  store_x22 + "/"
               
                

           

            netCategories = form.cleaned_data['netCategories']
            if(netCategories == "-1"): 
                val5 = ""  
            else:
                e = dict(ContactForm.NET_CATEGORIES)

                x3 = e.get(netCategories)

                #val5 = e.get(netCategories) + "/"
                my_encoded_string3 = urllib.parse.quote_plus(x3)
                store_x3 = my_encoded_string3.replace("%" , "&")
                store_x33 = store_x3.replace("26" , "")


                val5 =  store_x33 + "/"

                
               # converting the strin to get rid of & character
            

            externalVideoSeries = form.cleaned_data['externalVideoSeries']
            if(externalVideoSeries == "-1"):
                val6 = ""
            else:
                f = dict(ContactForm.EXTERNAL_VIDEOS)
                x4 = f.get(externalVideoSeries)

                my_encoded_string4 = urllib.parse.quote_plus(x4)
                store_x4 = my_encoded_string4.replace("%" , "&")
                store_x44 = store_x4.replace("26" , "")

                val6 = store_x44 + "/"

             
            

            externalAudioSeries = form.cleaned_data['externalAudioSeries']
            if(externalAudioSeries == "-1"):
                val7 = ""
            else:
                
                g = dict(ContactForm.EXTERNAL_AUDIOS)
                x5 = g.get(externalAudioSeries) 

                my_encoded_string5 = urllib.parse.quote_plus(x5)
                store_x5 = my_encoded_string5.replace("%" , "&")
                store_x55 = store_x5.replace("26" , "")

                val7 = store_x55 + "/"
                 

            
          
            

            date = form.cleaned_data['date']
            if(date == '-1'):
                val8 = ""
            else:
                f = dict(ContactForm.DATE_CHOICES)
                val8 = f.get(date)  + "/"


            both = form.cleaned_data['both']
            if(both == "-1"):
                val9 = ""
            else:
                h = dict(ContactForm.BOTH)
                x6 = h.get(both)

                my_encoded_string4 = urllib.parse.quote_plus(x6)
                store_x6 = my_encoded_string4.replace("%" , "&")
                store_x66 = store_x6.replace("26" , "")

                val9 = store_x66 + "/"


               

              
          


       
         

            number = form.cleaned_data['number']
            strNumber = str(number) + "/"

            

            print("dddddd")

            before = form.cleaned_data['before']
            after = form.cleaned_data['after']

            print(before)




            before1 = ""
            after1 = ""


            if(before is not None):
                before1 = datetime.strftime(before, LEGACY_DATE_STRING) + "/"
                after1 = ""
            else:
                before1 = ""

            if(after is not None):
                after1 = datetime.strftime(after, LEGACY_DATE_STRING) +  "/"
            else:
                after1 = ""

           


            x = "https://netsync.unl.edu/feeds/apps/"

            
        

            if(mediaSource  == '0' and category != '-1' and date !='-1'):
               
                if(contain == '-1'):
                    result = result + val1 + "media/" + val4  + val9 + val5+ val8 + before1 + after1 + strNumber
                else:
                    result = result + val1 + "media/" + val4 + val9  + val2 + val8 + before1 + after1 + strNumber
            

            elif(mediaSource == '0' and category!='-1' and date == '-1'):
                if(contain == '-1'):
                    result = result + val1 + "media/" + val4  + val9 + val5+ val8 + strNumber

                else:
                    result = result + val1 + "media/" + val4  + val9 + val5+ val2 + strNumber
  
            elif(mediaSource == '1' and date !='-1' and contain!='-1'):

                if(before is not None):
                    start = datetime.strftime(before, EXT_MEDIA_DATE_STRING) + "/"
                else:
                    start = ""


                if(after is not None):
                    end = datetime.strftime(after, EXT_MEDIA_DATE_STRING) + "/"

                else:
                    end = ""


                


                result = result + val1 + "media/" + val4  + val9 + val5+ val8 + start + end + strNumber 

               
            elif(mediaSource  == '1' and contain !='-1'):

                if(contain == '0' and externalAudioSeries !='-1'):
                    result = result + val1 + "media/" + val7+ val2+ strNumber
                elif(contain == '1' and externalVideoSeries != '-1'):
                    result = result + val1 + "media/" + val6+ val2+ strNumber
                
                elif(contain == '2' and both!='-1'):
                    result = result + val1 + "media/"  + val9+ val2+ strNumber
                else:
                    result = result + val1 + val4 + val9 + val5 + val6 + val7 +  val2 +"series/"

                



            elif(date == '-1'):

                result = result + val1 + val4 + val9 + val5 + val6 + val7 +  val2 +"series/"




            
            






            

            



            
        return render(request , 'display.html' , {'result':result}) 


    else:
        print("not done")
        form = ContactForm()
        return render(request , 'name.html' , {'form':form}) 
    







