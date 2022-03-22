

class BuscaSeq:
    
    
    """ Initializing the holders that will receive the valuues in the following methods"""
    
    def __init__(self, vector, chave, condition):
        
        self.vector = vector
        
        self.chave = chave
        
        self.condition = condition
        
           
    def busca_chave(self):
        
        """Starting the sequential search algorithm"""
        
        
        while self.condition == False: #Until the condition is fulfilled, the loop remains
        
            
            if self.chave not in self.vector: #forcing condition when the key inputed is not in the informed vector
                
                print(f'A chave informada {self.chave}, não está contida no vetor gerado. \n')
                
                break
                
            else: #general case
                
                for i in range(len(self.vector)): #for all positions on the vector, the search will happen until the key is found
                    
                    if self.vector[i] == self.chave: #stop condition
                        
                        print(f'Sequencial: A chave {self.chave} foi encontrada')
                        
                        break
                        
                        
                self.condition= True


