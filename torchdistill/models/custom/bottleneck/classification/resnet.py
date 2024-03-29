from collections import OrderedDict

from torch import nn
from torchvision.models import resnet50, resnet101, resnet152

from ..base import BottleneckBase
from ..registry import get_bottleneck_processor
from ....registry import register_model, register_model


@register_model
class Bottleneck4ResNet(BottleneckBase):
    """
    Head Network Distillation: Splitting Distilled Deep Neural Networks for Resource-constrained Edge Computing Systems
    """
    def __init__(self, bottleneck_channel=12, bottleneck_idx=7, compressor=None, decompressor=None):
        modules = [
            nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, bottleneck_channel, kernel_size=2, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(bottleneck_channel),
            nn.ReLU(inplace=True),
            nn.Conv2d(bottleneck_channel, 512, kernel_size=2, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, kernel_size=2, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, kernel_size=2, stride=1, bias=False),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, kernel_size=2, stride=1, bias=False),
            nn.AvgPool2d(kernel_size=2, stride=1)
        ]
        encoder = nn.Sequential(*modules[:bottleneck_idx])
        decoder = nn.Sequential(*modules[bottleneck_idx:])
        super().__init__(encoder=encoder, decoder=decoder, compressor=compressor, decompressor=decompressor)


@register_model
class CustomResNet(nn.Sequential):
    def __init__(self, bottleneck, short_module_names, org_resnet):
        module_dict = OrderedDict()
        module_dict['bottleneck'] = bottleneck
        short_module_set = set(short_module_names)
        for child_name, child_module in org_resnet.named_children():
            if child_name in short_module_set:
                if child_name == 'fc':
                    module_dict['flatten'] = nn.Flatten(1)
                module_dict[child_name] = child_module

        super().__init__(module_dict)


@register_model
def custom_resnet50(bottleneck_channel=12, bottleneck_idx=7, compressor=None, decompressor=None,
                    short_module_names=None, **kwargs):
    if short_module_names is None:
        short_module_names = ['layer3', 'layer4', 'avgpool', 'fc']

    if compressor is not None:
        compressor = get_bottleneck_processor(compressor['key'], **compressor['kwargs'])

    if decompressor is not None:
        decompressor = get_bottleneck_processor(decompressor['key'], **decompressor['kwargs'])

    bottleneck = Bottleneck4ResNet(bottleneck_channel, bottleneck_idx, compressor, decompressor)
    org_model = resnet50(**kwargs)
    return CustomResNet(bottleneck, short_module_names, org_model)


@register_model
def custom_resnet101(bottleneck_channel=12, bottleneck_idx=7, compressor=None, decompressor=None,
                     short_module_names=None, **kwargs):
    if short_module_names is None:
        short_module_names = ['layer3', 'layer4', 'avgpool', 'fc']

    if compressor is not None:
        compressor = get_bottleneck_processor(compressor['key'], **compressor['kwargs'])

    if decompressor is not None:
        decompressor = get_bottleneck_processor(decompressor['key'], **decompressor['kwargs'])

    bottleneck = Bottleneck4ResNet(bottleneck_channel, bottleneck_idx, compressor, decompressor)
    org_model = resnet101(**kwargs)
    return CustomResNet(bottleneck, short_module_names, org_model)


@register_model
def custom_resnet152(bottleneck_channel=12, bottleneck_idx=7, compressor=None, decompressor=None,
                     short_module_names=None, **kwargs):
    if short_module_names is None:
        short_module_names = ['layer3', 'layer4', 'avgpool', 'fc']

    if compressor is not None:
        compressor = get_bottleneck_processor(compressor['key'], **compressor['kwargs'])

    if decompressor is not None:
        decompressor = get_bottleneck_processor(decompressor['key'], **decompressor['kwargs'])

    bottleneck = Bottleneck4ResNet(bottleneck_channel, bottleneck_idx, compressor, decompressor)
    org_model = resnet152(**kwargs)
    return CustomResNet(bottleneck, short_module_names, org_model)
