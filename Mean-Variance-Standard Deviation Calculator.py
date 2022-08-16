import numpy as np

def calculations():
    list1 = []
    elements_of_list = int(input('enter number of elements in list: '))
    for i in range(0,elements_of_list):
        ele = int(input())
        list1.append(ele)
        
    ## TO GET A MIN
    numpy_array = np.array(list1)
    numpy_array = numpy_array.reshape(3, 3)
    min_axis0 = numpy_array.min(axis=0)
    min_axis0= min_axis0.tolist()
    min_axis1 = numpy_array.min(axis=1)
    min_axis1= min_axis1.tolist()
    min_f = min(list1)
    
##############################################################
    #TO GET A MAX
    numpy_array = np.array(list1)
    numpy_array = numpy_array.reshape(3, 3)
    max_axis0 = numpy_array.max(axis=0)
    max_axis0= max_axis0.tolist()
    max_axis1 = numpy_array.max(axis=1)
    max_axis1= max_axis1.tolist()
    max_f = max(list1)
#############################################################    
    # TO GET THE MEAN
    numpy_array = np.array(list1)
    numpy_array = numpy_array.reshape(3, 3)
    mean_axis0 = numpy_array.mean(axis=0)
    mean_axis0= mean_axis0.tolist()
    mean_axis1 = numpy_array.mean(axis=1)
    mean_axis1= mean_axis1.tolist()
    mean_f = np.array(list1)
    mean_f = np.mean(list1)
    mean_f = mean_f.tolist()
###############################################################
    # TO GET THE SUM
    numpy_array = np.array(list1)
    numpy_array = numpy_array.reshape(3, 3)
    sum_axis0 = numpy_array.sum(axis=0)
    sum_axis0= sum_axis0.tolist()
    sum_axis1 = numpy_array.sum(axis=1)
    sum_axis1= sum_axis1.tolist()
    sum_f= sum(list1)
###############################################################
    # TO GET THE variance
    numpy_array = np.array(list1)
    numpy_array = numpy_array.reshape(3, 3)
    var_axis0 = numpy_array.var(axis=0)
    var_axis0= var_axis0.tolist()
    var_axis1 = numpy_array.var(axis=1)
    var_axis1= var_axis1.tolist()
    var_f = np.array(list1)
    var_f = np.var(list1)    
    var_f = var_f.tolist()
###############################################################
    # TO GET THE Standard Deviation
    numpy_array = np.array(list1)
    numpy_array = numpy_array.reshape(3, 3)
    std_axis0 = numpy_array.std(axis=0)
    std_axis0= std_axis0.tolist()
    std_axis1 = numpy_array.std(axis=1)
    std_axis1= std_axis1.tolist()
    std_f = np.array(list1)
    std_f = np.std(list1)    
    std_f = std_f.tolist()    
###############################################################    
    
    dic_cal= {
        
        'min':[min_axis0,min_axis1,min_f],
        'max':[max_axis0,max_axis1,max_f],
        'mean':[mean_axis0,mean_axis1,mean_f],
        'sum': [sum_axis0,sum_axis1,sum_f],
        'var': [var_axis0,var_axis1,var_f],
        'standard deviation': [std_axis0,std_axis1,std_f],
    }
    print(dic_cal)

    return calculations


a = calculations()
