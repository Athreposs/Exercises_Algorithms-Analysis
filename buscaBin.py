# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 21:18:02 2022

@author: PICHAU
"""

class BuscaBin:
    
    """Initializing the variables that will appear and be used on the other methods of this algorithm"""
    
    def __init__(self, vector, key, start, end):
        
        self.vector = vector
        
        self.key = key
        
        self.start = start
        
        self.end = end
        
        
    def busca(self):
        
        """Here is the search algorithm for the binary search.
        
        This method is getting the index of the numbers in the created vector and comparing the value of 
        
        the inputed key to the lower and upper halves of the vector."""
        
        self.start= 0 #informing that the vector will start on the first position
        
        self.end= len(self.vector) # the maximum position will have the size of the vector
        
        while self.start <= self.end: #informing that the operation will continue until the whole vector is searched
            
            middle = (self.start + self.end) // 2 #the middle is defined as the sum of the updated start and end of the vector divided by two

            if self.key not in self.vector: #case where the informed key is not in the vector
                
                print(f'A chave informada {self.key} não está inserida dentro do vector \n')
                
                break
            
            else:
            
                if self.key == self.vector[middle]: #case when the key is found
                    
                    return middle #returning the key position on the vector when it is found
                
                
                if self.key > self.vector[middle]: #key value higher than the mid-point
                    
                    self.start = middle + 1 #increasing the start position and updating the 'middle value' that will be used on the comparison made
                    
                    return self.start
                    
                else: #key value lower than the mid-point
                
                    self.end = middle - 1 #Descreasing the end position and updating the 'middle value' that will be used on the comparison made
                    
                    return self.end
                
                return middle #returning the updated 'middle position'
        
    def printValues(self):
        
        """This method prints the results"""
        
        print("\n")
        
        print(f'Binário: A chave {self.key} foi encontrada')
        
