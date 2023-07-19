from pymongo import MongoClient
import subprocess

def server_status():
    try:
        subprocess.check_output(['sudo', 'service', 'mongod', 'start'])
    except:
        pass