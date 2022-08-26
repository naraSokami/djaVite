from app import App


### TODO ###
# 
# 



app = App('pastek')
app.addTemplate('index')




# def addView(name, app):
#     # in app/views.py
#     use(f'{app}/views.py', 'from django.http import HttpResponse')

#     # in app/urls.py
#     mkFileIfNot(f'{app}/urls.py')
#     use(f'{app}/urls.py', 'from . import views')
#     use(f'{app}/urls.py', 'from django.urls import path')

#     # in mainApp/urls.py
#     if not strInFile("from django.urls import path"):
#         use(f'{MAIN_APP}/urls.py', "from django.urls import include, path")
#     else:
#         re.sub(r"from django\.urls import include, path")

# addView("test", "pastek")