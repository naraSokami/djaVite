import os
import shutil
import time
import re

### TODO ###
# 
# 

def mkdirIfNot(path, v=False):
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        if v == True:
            print(f'dir {path} already exists /_/')


def mkFileIfNot(path, v=False):
    if not os.path.exists(path):
        f = open(path, 'x')
    else:
        if v == True:
            print(f'file {path} already exists /_/')


def getApps():
    return [path for path in os.listdir('.') if os.path.isdir(path)]


def addApp(name, v=True):
    if not name in getApps():
        os.system(f'python manage.py startapp {name}')
    else:
        if v == True:
            print(f'app {name} already exists /_/')


def removeApp(name):
    shutil.rmtree(name)


def getLines(path):
    with open(path) as f:
        return f.readlines()


def strInFile(str, path):
    with open(path) as f:
        content = f.read()

        if str in content:
            return True
        else:
            return False


def lastImportIndex(path):
    last = 0
    lines = getLines(path)

    for i in range(len(lines)):
        if 'import' in lines[i]:
            last = i
        else:
            if not lines[i] == '\n':
                break
    return last
    

def use(path, importStr, v=False):
    i = lastImportIndex(path) + 1
    lines = getLines(path)
    lines = lines[:i] + [importStr + '\n'] + lines[i:]
    print(lines)

    if not strInFile(importStr, path):
        with open(path, "w") as f:
            f.write("".join(lines))
    else:
        if v == True:
            print(f'import "{importStr}" already used by file "{path}" /_/')


def addLines(path, lines, i):
    lines = getLines(path)
    lines = lines[:i] + lines + lines[i:]
    with open(path, 'w') as f:
        f.write("".join())


class Env:
    def __init__(self, v=False):
        self.v = v
        mkFileIfNot('.djaenv')

    
    def getEnvs(self):
        envs = {}
        lines = getLines('.djaenv')

        for i in range(len(lines)):
            match = re.match(r'([A-Z_]+)=(.+)', lines[i])
            
            if re.match:
                envs[match.group(1)] = match.group(2)
            
        return envs


    def getEnv(self, name):
        envs = self.getEnvs()
        if name in envs:
            return envs[name]
        else:
            if self.v == True:
                print(f'env "{name}" not found /_/')
            return -1


    def setEnv(self, name, value):
        """
            If env found set value of env and return 0
            If env not found create env and return 1 
        """
        rv = 0
        envs = self.getEnvs()
        if not name in envs:
            rv = 1

        envs[name] = value
        with open(".djaenv", "w") as f:
            f.write("\n".join([f'{k}={envs[k]}' for k in envs]))
        
        return rv


env = Env()
print(env.setEnv('MAIN_AP', 'testing...'))




def addView(name, app):
    # in app/views.py
    use(f'{app}/views.py', 'from django.http import HttpResponse')

    # in app/urls.py
    mkFileIfNot(f'{app}/urls.py')
    use(f'{app}/urls.py', 'from . import views')
    use(f'{app}/urls.py', 'from django.urls import path')

    # in mainApp/urls.py
    if not strInFile("from django.urls import path"):
        use(f'{MAIN_APP}/urls.py', "from django.urls import include, path")
    else:
        re.sub(r"from django\.urls import include, path")

# addView("test", "pastek")