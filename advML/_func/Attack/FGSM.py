from advML.function import advML_deep_package
def FGSM(model,input,lable,epsilon):
    if(advML_deep_package == 'pytorch'):
        from torch.nn import Module
        from torch import Tensor
        assert isinstance(model,Module),'Model should be a child-class of Module'
        assert isinstance(input,Tensor),'Input should be a Tensor'
        assert isinstance(lable,Tensor),'Lable should be a Tensor'
        return FGSM_pytorch(model,input,lable,epsilon)
    return

def FGSM_pytorch(model,input,lable,epsilon):
    import torch.nn as nn
    import torch
    #import torch.clamp as clamp
    input.requires_grad = True
    predict = model(input)
    criterion = nn.CrossEntropyLoss()
    loss = criterion(predict,lable)
    model.zero_grad()
    loss.backward()
    grad = input.grad.data
    perturbed_input = input + epsilon*(grad.sign())
    perturbed_input = torch.clamp(perturbed_input,0,1)
    return perturbed_input

