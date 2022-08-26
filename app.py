import os
import re
import shutil
from env import ENV
from utils import getApps, lastImportIndex, mkFileIfNot, mkdirIfNot, templated


class App:
    def __init__(self, name, v=True):
        self.name = name
        self.v = v

        if not self.name in getApps():
            os.system(f'python manage.py startapp {self.name}')
            if v == True:
                print(f'app {self.name} created |_|')
        else:
            if v == True:
                print(f'app {self.name} already exists /_/')


    def addTemplate(self, templateName, ext="html"):
        mkdirIfNot('templates')
        mkdirIfNot(f'templates/{self.name}')
        templatedPath = f'templates/{self.name}/{templateName}.{ext}'
        
        if mkFileIfNot(templatedPath) == 0:
            templated(templatedPath, "html/base-template.html")
        else:
            if self.v == True:
                print('temlpate "{templatePath}" already exists /_/')


    def getModels(self):
        with open(f'{self.name}/models.py') as f:
            matches = re.findall(r'class +([A-z]+)(?= *\((?:models.)?Model\) *\:)', f.read())
            return matches


    def addModel(self, name):
        i = lastImportIndex()
        


    def remove(self):
        try:
            shutil.rmtree(self.name)
            if self.v == True:
                print(f'app {self.name} succesfully removed |_|')

        except:
            if self.v == True:
                print(f'failed to remove app {self.name} X_X')
            return -1
