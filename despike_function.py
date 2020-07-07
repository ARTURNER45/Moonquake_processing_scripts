#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import scipy as sp
import numpy as np

def despike_step1(y,m,kernel_size,threshold):
    med_filt_tr = sp.signal.medfilt(abs(y), kernel_size=kernel_size)
    fivemedian = 5 * med_filt_tr
    #spikes = abs(y) > fivemedian
    spikes = abs((y - med_filt_tr)) > threshold
    y_out = y.copy() # So we don’t overwrite y
    for i in np.arange(len(spikes)):
        if int(spikes[i]) != 0: # If we have an spike in position i
            if i >= (len(spikes) - kernel_size):
                w = np.arange(i-m,len(spikes))
                w2 = w[spikes[w] == 0]
                y_out[i] = np.mean(y[w2])
        
            elif i <= kernel_size:
                w = np.arange(0,i+1+m)
                w2 = w[spikes[w] == 0]
                y_out[i] = np.mean(y[w2])
            
            else:
                w = np.arange(i-m,i+1+m) # we select 2 m + 1 points around our spike
                w2 = w[spikes[w] == 0] # From such interval, we choose the ones which are not spikes
                y_out[i] = np.mean(y[w2]) # and we average their values
    return y_out,fivemedian


def despike_step2(y,m,kernel_size):
    med_filt_tr = sp.signal.medfilt(abs(y), kernel_size=kernel_size)
    fivemedian = 5 * med_filt_tr 
    spikes = abs(y) > fivemedian
    y_out = y.copy() # So we don’t overwrite y 
    for i in np.arange(len(spikes)):
        if int(spikes[i]) != 0: # If we have an spike in position i
            if i >= (len(spikes) - kernel_size):
                w = np.arange(i-m,len(spikes))
                w2 = w[spikes[w] == 0] 
                y_out[i] = np.mean(y[w2])
            
            elif i <= kernel_size:
                w = np.arange(0,i+1+m)
                w2 = w[spikes[w] == 0] 
                y_out[i] = np.mean(y[w2])
                
            else:
                w = np.arange(i-m,i+1+m) # we select 2 m + 1 points around our spike
                w2 = w[spikes[w] == 0] # From such interval, we choose the ones which are not spikes
                y_out[i] = np.mean(y[w2]) # and we average their values
    return y_out,fivemedian

