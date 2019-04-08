from advML.function import advML_deep_package
import torch.nn as nn
import torch

def BIGS(model,input,lable,epsilon,times):
    if(advML_deep_package == 'pytorch'):
        from torch.nn import Module
        from torch import Tensor
        assert isinstance(model,Module),'Model should be a child-class of Module'
        assert isinstance(input,Tensor),'Input should be a Tensor'
        assert isinstance(lable,Tensor),'Lable should be a Tensor'
        return BIGS_pytorch(model,input,lable,epsilon,times)
    else:
        assert 0>1,"The deep package is unsupported!"

def BIGS_pytorch(model,input,lable,epsilon,times):
    perturbed_input = input
    for i in range(times):
        perturbed_input.requires_grad = True
        predict = model(perturbed_input)
        criterion = nn.CrossEntropyLoss()
        loss = criterion(predict,lable)
        model.zero_grad()
        loss.backward()
        with torch.no_grad():
            perturbed = 0.01 * (perturbed_input.grad.data.sign())
            perturbed_input = Clip(perturbed_input,perturbed_input+perturbed,epsilon)
    return perturbed_input


def Clip(original,input,epsilon):
    input = torch.where(input>original-epsilon,input,original)
    input = torch.where(input<original+epsilon,input,original)
    return torch.clamp(input,0,1)
