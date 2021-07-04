import connexion
import six

import os, sys
import stat
from swagger_server import util
import subprocess
from subprocess import Popen, PIPE
import sys

def get_copy_path(copy=None):  # noqa: E501
    """path

     # noqa: E501

    :param copy: 
    :type copy: str

    :rtype: None
    """
    print(copy)
    destination = "/Users/cwills/API-work/bucket-api/foo/"
    copyfolderlist = ["SIM_INPUT", "job_history", "PRICING_INPUT", "AGGREGATION_INPUT", "PROTOBUF_TRADES", "AGGREGATION_OUTPUT/results_pb/", "PRICING_OUPUT"]
    listlength  = len(copyfolderlist)
    for i in range(listlength):
        print(copyfolderlist[i])
        #cmd = 'gsutil -m -o \"GSUTIL:parallel_thread_count=1\" -o \"GSUTIL:sliced_object_download_max_components=60\"  cp -r gs://%s/%s /%s' % (bucket_path, copyfolderlist[i], destination)
        #cmd = 'gsutil -m -o \"GSUTIL:parallel_process_count=1\" -o \"GSUTIL:sliced_object_download_max_components=60\"  cp -r gs://%s/%s /%s' % (bucket_path, copyfolderlist[i], destination)
        cmd = 'gsutil cp -r gs://%s/%s /%s' % (copy, copyfolderlist[i], destination)
        subprocess.run(cmd, shell=True, close_fds=True)

    return True 


def get_list_path(query=None):  # noqa: E501
    """list

     # noqa: E501

    :param query: 
    :type query: str

    :rtype: None
    """
    filelist=[]

    dirs = os.listdir( query )
    for file in dirs:
         filelist.append(file)
    return(filelist)
