
import  time

class test():
    def __init__(self):
        self.NUM_TEST = 15
        self.fieldnames = [None] * self.NUM_TEST    #fieldnames associating with outputs of each test
        self.fieldnames[0] = ['n', 'zeroes count', 'ones count', 'abs(ones-zeroes)', 'p-value', 'success']
        self.fieldnames[1] = ['n','chi_sq','p-value', 'success']
        self.fieldnames[2] = ['n', 'zeroes count', 'ones count', 'one_prop', 'vobs','p-value', 'success']
        self.fieldnames[3] = ['n', 'chi_sq','p-value', 'success']
        self.fieldnames[4] = ['n', 'M', 'Q', 'N', 'FM', "FMM", 'chi_sq', 'p-value', 'success']
        self.fieldnames[5] = ['n', 'N0', 'N1', 'd','p-value', 'success']
        self.fieldnames[6] = ['n', 'mu', 'sigma', 'chi_sq','p-value', 'success']
        self.fieldnames[7] = ['n', 'template', 'M', 'N', 'K', 'model', 'v', 'lambda', 'eta', 'chi_sq','p-value', 'success']
        self.fieldnames[8] = ['n', '#blocks', 'L', 'K', 'Q', 'sigma', 'p-value', 'success']
        self.fieldnames[9] = ['n', 'M', 'N', 'K', 'v', 'mu', 'chi_sq', 'p-value', 'success']
        self.fieldnames[10] = ['n', 'psi_sq_m', 'psi_sq_mm1', 'psi_sq_mm2', 'delta1', 'delta2', 'p1', 'p2', 'p_average', 'success']
        self.fieldnames[11] = ['n', 'appen_m', 'chi_sq', 'p-value', 'success']
        self.fieldnames[12] = ['n', 'p_forward', 'p_backward', 'success']
        self.fieldnames[13] = ['n', 'J', 'chi_sq', 'p-value', 'p_average', 'success']
        self.fieldnames[14] = ['n', 'J', 'count', 'p-value', 'p_average','success']

        self.testlist= [
                        'monobit_test',
                        'frequency_within_block_test',
                        'runs_test',
                        'longest_run_ones_in_a_block_test',
                        'binary_matrix_rank_test',
                        'dft_test',
                        'non_overlapping_template_matching_test',
                        'overlapping_template_matching_test',
                        'maurers_universal_test',
                        'linear_complexity_test',
                        'serial_test',
                        'approximate_entropy_test',
                        'cumulative_sums_test',
                        'random_excursion_test',
                        'random_excursion_variant_test'
                        ]

    
    def run_test(self,sequence):
         self.P_values = {}
         self.sucess = {}
         
         for i in range(self.NUM_TEST):
                        
                        
                        if i<9:

                            self.testFile = __import__("0"+str(i+1)+"_"+self.testlist[i])
                        else:
                            self.testFile = __import__(str(i+1)+"_"+self.testlist[i])
                    
                
                
                        x = self.testFile.test(sequence,len(sequence))
                        self.P_values[self.testlist[i]] = x[len(x)-2]
                        self.sucess[self.testlist[i]] = x[len(x)-1]
                
         p_vals1 = 0
         p_vals2 = 0

         for i in self.testlist:
            if self.sucess[i] == True:
                 
                 p_vals1 = p_vals1 + self.P_values[i]
            # else:
            #      p_vals = p_vals + self.P_values[i]/2
    




         return (1-p_vals1/15)
                 
            
         
            

    

if __name__ == '__main__':
    test = test()
    sequence = ''
    with open('hybrid.txt','r') as f:
         i = 10
         for line in f:
             if len(sequence) <= 2056032 :
                  if i <20:
                       pass
                  i+=1
                  
                  sequence += line[:-1]

    t0 = time.time()
        
    print(len(sequence))
    
    print(test.run_test(sequence))
    t1 = time.time()

    print(test.P_values)
    print(test.sucess)
    print("time cost: ",t1-t0)

    print("test is over !!!!")

     






              
              


        