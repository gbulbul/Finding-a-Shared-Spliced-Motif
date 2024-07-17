# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 19:28:14 2024

@author: gbulb
"""
class class_for_longest_substring:
    def choose_min_len(dict_):
        return min(dict_.values())
    def find_longest_substring(dict_):
        longest_substring=''
        for value1 in dict_.values():
            for value2 in dict_.values():
                if value1!=value2:
                    for i in range(0,len(min_)-1,1):
                        if value1[i:i+1]==value2[i:i+1] and value2[i:i+1] not in longest_substring:
                           longest_substring+=value1[i:i+1]
                        elif value1[i:i+1]!=value2[i:i+1] and value2[i:i+1]+''+value1[i:i+1] not in longest_substring and value1[i:i+1]+''+value2[i:i+1] not in longest_substring:
                             longest_substring+=value1[i:i+1]+''+value2[i:i+1]
        return longest_substring
if __name__=="__main__":
    dict_={}
    dict_['Rosalind_23']='AACCTTGG'
    dict_['Rosalind_64']='ACACTGTGA'
    min_=class_for_longest_substring.choose_min_len(dict_)
    print(class_for_longest_substring.find_longest_substring(dict_))
                   
                
    
    