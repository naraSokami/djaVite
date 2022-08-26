import os, shutil



def mkdirIfNot(path, v=False):
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        if v == True:
            print(f'dir {path} already exists /_/')


def mkFileIfNot(path, v=False):
    """
        return 0 if file created else return -1
    """
    if not os.path.exists(path):
        f = open(path, 'x')
        return 0
    else:
        if v == True:
            print(f'file {path} already exists /_/')
        return -1


def getApps():
    return [path for path in os.listdir('.') if os.path.isdir(path)]


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


def templated(path, templatePath):
    templateContent = ""

    with open(f'{os.path.dirname(__file__)}/templates/{templatePath}', 'r') as f:
        templateContent = f.read()

    with open(path, 'w') as f:
        f.write(templateContent)