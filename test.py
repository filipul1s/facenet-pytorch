#--------------------------------------------#
#   该部分代码只用于看网络结构，并非测试代码
#--------------------------------------------#
from nets.facenet import Facenet
from torchsummary import summary

if __name__ == "__main__":
    model = Facenet(num_classes=10575).train().cuda()
    summary(model,(3,160,160))