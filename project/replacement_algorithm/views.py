from django.shortcuts import render
from .forms import AlgorithmForm

# Create your views here.

def FIFO(nts):   # first in first out
    
    return 'fifo' , nts

def LRU(nts):   # least recently used
      
    return "lru"

def LFU(nts):   # least frequently used
    
    return "lfu" 

def MFU(nts):   # most frequently used
    
    return "mfu"

    

def home(request):
    form = AlgorithmForm()
    return render(request,'home.html',{'form': form})  # home.html is in templates folder of replacement_algorithm app folder 

def processing(request):
    
    if request.method == 'POST':
        form = AlgorithmForm(request.POST)
        
        if form.is_valid():
            
            x = request.POST['numbers']
            algorithm = request.POST['algorithm']
            z = x.split() # split string into list of strings
            map_object = map(int, z) # convert string to int
            
            list_of_integers = list(map_object)
            print(algorithm)
            
            if algorithm == 'FIFO':
                result = FIFO(list_of_integers)
            elif algorithm == 'LRU':
                result = LRU(list_of_integers)
            elif algorithm == 'LFU':
                result = LFU(list_of_integers)
            else:
                result = MFU(list_of_integers)
        return render(request,'processing.html',{'result': result}) 
           
        
        # return render(request,'processing.html')  # processing.html is in templates folder of replacement_algorithm app folder
    