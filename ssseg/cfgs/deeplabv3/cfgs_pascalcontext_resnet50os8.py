'''define the config file for pascalcontext and resnet50os8'''
from .base_cfg import *


# modify dataset config
DATASET_CFG = DATASET_CFG.copy()
DATASET_CFG['train'].update(
    {
        'type': 'pascalcontext',
        'rootdir': 'data/VOCdevkit/VOC2010/',
        'aug_opts': [('Resize', {'output_size': (520, 520), 'keep_ratio': True, 'scale_range': (0.5, 2.0)}),
                     ('RandomCrop', {'crop_size': (480, 480), 'one_category_max_ratio': 0.75}),
                     ('RandomFlip', {'flip_prob': 0.5}),
                     ('PhotoMetricDistortion', {}),
                     ('Normalize', {'mean': [123.675, 116.28, 103.53], 'std': [58.395, 57.12, 57.375]}),
                     ('ToTensor', {}),
                     ('Padding', {'output_size': (480, 480), 'data_type': 'tensor'}),]
    }
)
DATASET_CFG['test'].update(
    {
        'type': 'pascalcontext',
        'rootdir': 'data/VOCdevkit/VOC2010/',
        'aug_opts': [('Resize', {'output_size': (520, 520), 'keep_ratio': True, 'scale_range': None}),
                     ('Normalize', {'mean': [123.675, 116.28, 103.53], 'std': [58.395, 57.12, 57.375]}),
                     ('ToTensor', {}),]
    }
)
# modify dataloader config
DATALOADER_CFG = DATALOADER_CFG.copy()
# modify optimizer config
OPTIMIZER_CFG = OPTIMIZER_CFG.copy()
OPTIMIZER_CFG.update(
    {
        'type': 'sgd',
        'sgd': {
            'learning_rate': 0.004,
            'momentum': 0.9,
            'weight_decay': 1e-4,
        },
        'max_epochs': 260,
    }
)
# modify losses config
LOSSES_CFG = LOSSES_CFG.copy()
# modify model config
MODEL_CFG = MODEL_CFG.copy()
MODEL_CFG.update(
    {
        'num_classes': 60,
        'backbone': {
            'type': 'resnet50',
            'series': 'resnet',
            'pretrained': True,
            'outstride': 8,
            'use_stem': True,
            'selected_indices': (2, 3),
        },
        'aspp': {
            'in_channels': 2048,
            'out_channels': 512,
            'dilations': [1, 12, 24, 36],
        },
    }
)
# modify inference config
INFERENCE_CFG = INFERENCE_CFG.copy()
INFERENCE_CFG.update({
    'mode': 'slide',
    'opts': {
        'cropsize': (480, 480),
        'stride': (320, 320),
    }, 
    'tricks': {
        'multiscale': [1],
        'flip': False,
        'use_probs_before_resize': True,
    }
})
# modify common config
COMMON_CFG = COMMON_CFG.copy()
COMMON_CFG['train'].update(
    {
        'backupdir': 'deeplabv3_resnet50os8_pascalcontext_train',
        'logfilepath': 'deeplabv3_resnet50os8_pascalcontext_train/train.log',
    }
)
COMMON_CFG['test'].update(
    {
        'backupdir': 'deeplabv3_resnet50os8_pascalcontext_test',
        'logfilepath': 'deeplabv3_resnet50os8_pascalcontext_test/test.log',
        'resultsavepath': 'deeplabv3_resnet50os8_pascalcontext_test/deeplabv3_resnet50os8_pascalcontext_results.pkl'
    }
)