import os
import re
from utils import getLines, mkFileIfNot


INIT_ENVS = {
    "DJA_PATH": os.path.dirname(__file__)
}


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

ENV = Env()

for k, v in INIT_ENVS.items():
    ENV.setEnv(k, v)