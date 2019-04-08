def FGSM(model,input,lable,epsilon=0.05):
    from advML._func.Attack.FGSM import FGSM
    return FGSM(model,input,lable,epsilon)

def BIGS(model,input,lable,epsilon=0.05,times=10):
    from advML._func.Attack.BIGS import BIGS
    return BIGS(model,input,lable,epsilon,times)
