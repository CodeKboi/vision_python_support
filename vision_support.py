#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:02:13 2024

@author: kevin
"""


import time 
import os

def m2s(filebase="C:/"):
    '''
    This function generates a Start.txt file and causes the task
    to proceed with the execution.
    The function is used in conjunction with the File Start/Abort
    TASK in the Vision 5.0. Set up the task in the current test
    defintion (CTD) to use this command. 
    This is used for external signaling.

    Parameters
    ----------
    filebase : TYPE, optional
        Filepath,refer to the task instructions. The default is "C:/".

    Returns
    -------
    None.

    '''
    f = open(filebase+"DataSets/StartTest/Start.txt","w")
    f.close()
def abort(filebase="C:/"):
    '''
    This function generates a Abort.txt file and causes the task
    to abort the execution.
    The function is used in conjunction with the File Start/Abort
    TASK in the Vision 5.0. Set up the task in the current test
    defintion (CTD) to use this command. 
    This is used for external signaling.

    Parameters
    ----------
    filebase : TYPE, optional
        Filepath,refer to the task instructions. The default is "C:/".

    Returns
    -------
    None.

    '''
    f = open(filebase+"DataSets/StartTest/Abort.txt","w")
    f.close()
def clear_last_run(filebase="C:/"):
    '''
    Clears the directory C:/DataSets/StartTest/ by default
    Preferably run at the start of the script

    Parameters
    ----------
    filebase : TYPE, optional
        Filepath,refer to the task instructions. The default is "C:/".

    Returns
    -------
    None.

    '''
    directory = filebase+"DataSets/StartTest/"
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                # Delete file
                os.remove(file_path)
                
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")
    
def s2m(file_path,sleep_time=1):
    '''
    The task generates a specified *.txt file. This function can be used
    to detect the file and wait depending on the configuration in the 
    Vision Software
    The function is used in conjunction with the Signal Task - Write
    TASK in the Vision 5.0. Set up the task in the current test
    defintion (CTD) to use this command. 
    This is used for external signaling.

    Parameters
    ----------
    file_path : TYPE
        File Path as specified in the Task Definition.
    sleep_time : TYPE, optional
        Wait time for the file. The default is 1.

    Returns
    -------
    None.

    '''
    while not os.path.exists(file_path):
        time.sleep(sleep_time)
    print("s_ack received")
    os.remove(file_path)
    
def file_write(file_path,V,t):
    '''
    Writes the file for the custom file in the hysteresis task.
    Make sure the unit of the time array is in seconds
    The input is taken in milliseconds and the function
    adjusts it appropriately

    Parameters
    ----------
    file_path : TYPE
        File Path as specified in the Task Definition.
    V : TYPE
        Voltage Wavform to be written.
    t : TYPE
        Time array for the waveform.
        
    Raises
    ------
    RuntimeError
        Sampling rate is too high or too many points.
        Ensure sampling rate is lesser than 1MHz and points lesser than 32000
        
    Returns
    -------
    None.

    '''
    dt = t[2]-t[1]
    if dt < 1e-6:
        raise RuntimeError("Sampling is too high. Must be >= 1 microsecond")
    if len(t) >32e3:
        raise RuntimeError("Too many points. Max 32000")
    with open(file_path,"w") as f:
        f.write(str(len(t))+"\n")
        f.write(str(1e3*(dt))+"\n")
        for j in V:
            f.write(str(j)+"\n")
