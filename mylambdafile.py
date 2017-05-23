# -*- coding: utf-8 -*-
"""
Created on Thu May 18 22:06:42 2017

@author: Veeramani Natarajan
"""

import sys

def mylambdafunction(event,context): 
    sys.path.append("./Lib/site-packages")
    import PyDictionary    
    dictionary=PyDictionary.PyDictionary()
    syn=dictionary.synonym('life')
    return (syn)