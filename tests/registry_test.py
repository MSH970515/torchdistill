from unittest import TestCase

from torchdistill.core.interfaces.registry import register_forward_proc_func, get_forward_proc_func, \
    register_pre_epoch_proc_func, register_pre_forward_proc_func, register_post_forward_proc_func, \
    register_post_epoch_proc_func, get_pre_epoch_proc_func, get_pre_forward_proc_func, get_post_forward_proc_func, \
    get_post_epoch_proc_func
from torchdistill.datasets.registry import register_dataset, register_collate_func, register_sample_loader, \
    register_batch_sampler, register_transform, register_dataset_wrapper, \
    DATASET_DICT, COLLATE_FUNC_DICT, SAMPLE_LOADER_DICT, BATCH_SAMPLER_DICT, \
    TRANSFORM_DICT, DATASET_WRAPPER_DICT
from torchdistill.losses.registry import register_high_level_loss, HIGH_LEVEL_LOSS_DICT, register_loss_wrapper, \
    register_mid_level_loss, LOSS_WRAPPER_DICT, MIDDLE_LEVEL_LOSS_DICT, register_func2extract_model_output, \
    FUNC2EXTRACT_MODEL_OUTPUT_DICT
from torchdistill.models.registry import register_adaptation_module, ADAPTATION_MODULE_DICT, \
    register_model, MODEL_DICT, register_auxiliary_model_wrapper, AUXILIARY_MODEL_WRAPPER_DICT
from torchdistill.optim.registry import register_optimizer, register_scheduler, OPTIM_DICT, SCHEDULER_DICT


class RegistryTest(TestCase):
    def test_register_dataset(self):
        @register_dataset
        class TestDataset0(object):
            def __init__(self):
                self.name = 'test0'

        assert DATASET_DICT['TestDataset0'] == TestDataset0

        @register_dataset()
        class TestDataset1(object):
            def __init__(self):
                self.name = 'test1'

        assert DATASET_DICT['TestDataset1'] == TestDataset1
        random_name = 'custom_test_dataset_name2'

        @register_dataset(key=random_name)
        class TestDataset2(object):
            def __init__(self):
                self.name = 'test2'

        assert DATASET_DICT[random_name] == TestDataset2

    def test_register_forward_proc_func(self):
        @register_forward_proc_func
        def test_forward_proc0(model, batch):
            return model(batch)

        assert get_forward_proc_func('test_forward_proc0') == test_forward_proc0

        @register_forward_proc_func()
        def test_forward_proc1(model, batch):
            return model(batch)

        assert get_forward_proc_func('test_forward_proc1') == test_forward_proc1
        random_name = 'custom_forward_proc_name2'

        @register_forward_proc_func(key=random_name)
        def test_forward_proc2(model, batch, label):
            return model(batch, label)

        assert get_forward_proc_func(random_name) == test_forward_proc2

    def test_register_collate_func(self):
        @register_collate_func
        def test_collate0(batch, label):
            return batch, label

        assert COLLATE_FUNC_DICT['test_collate0'] == test_collate0

        @register_collate_func()
        def test_collate1(batch, label):
            return batch, label

        assert COLLATE_FUNC_DICT['test_collate1'] == test_collate1
        random_name = 'custom_collate_name2'

        @register_collate_func(key=random_name)
        def test_collate2(batch, label):
            return batch, label

        assert COLLATE_FUNC_DICT[random_name] == test_collate2

    def test_register_sample_loader(self):
        @register_sample_loader
        class TestSampleLoader0(object):
            def __init__(self):
                self.name = 'test0'

        assert SAMPLE_LOADER_DICT['TestSampleLoader0'] == TestSampleLoader0

        @register_sample_loader()
        class TestSampleLoader1(object):
            def __init__(self):
                self.name = 'test1'

        assert SAMPLE_LOADER_DICT['TestSampleLoader1'] == TestSampleLoader1
        random_name = 'custom_sample_loader_name2'

        @register_sample_loader(key=random_name)
        class TestSampleLoader2(object):
            def __init__(self):
                self.name = 'test2'

        assert SAMPLE_LOADER_DICT[random_name] == TestSampleLoader2

    def test_register_sampler(self):
        @register_batch_sampler
        class TestBatchSampler0(object):
            def __init__(self):
                self.name = 'test0'

        assert BATCH_SAMPLER_DICT['TestBatchSampler0'] == TestBatchSampler0

        @register_batch_sampler()
        class TestBatchSampler1(object):
            def __init__(self):
                self.name = 'test1'

        assert BATCH_SAMPLER_DICT['TestBatchSampler1'] == TestBatchSampler1
        random_name = 'custom_batch_sampler_class_name2'

        @register_batch_sampler(key=random_name)
        class TestBatchSampler2(object):
            def __init__(self):
                self.name = 'test2'

        assert BATCH_SAMPLER_DICT[random_name] == TestBatchSampler2

    def test_register_transform(self):
        @register_transform()
        class TestTransform0(object):
            def __init__(self):
                self.name = 'test0'

        assert TRANSFORM_DICT['TestTransform0'] == TestTransform0

        @register_transform()
        class TestTransform1(object):
            def __init__(self):
                self.name = 'test1'

        assert TRANSFORM_DICT['TestTransform1'] == TestTransform1
        random_name = 'custom_transform_class_name2'

        @register_transform(key=random_name)
        class TestTransform2(object):
            def __init__(self):
                self.name = 'test2'

        assert TRANSFORM_DICT[random_name] == TestTransform2

    def test_register_dataset_wrapper(self):
        @register_dataset_wrapper
        class TestDatasetWrapper0(object):
            def __init__(self):
                self.name = 'test0'

        assert DATASET_WRAPPER_DICT['TestDatasetWrapper0'] == TestDatasetWrapper0

        @register_dataset_wrapper()
        class TestDatasetWrapper1(object):
            def __init__(self):
                self.name = 'test1'

        assert DATASET_WRAPPER_DICT['TestDatasetWrapper1'] == TestDatasetWrapper1
        random_name = 'custom_dataset_wrapper_class_name2'

        @register_dataset_wrapper(key=random_name)
        class TestDatasetWrapper2(object):
            def __init__(self):
                self.name = 'test2'

        assert DATASET_WRAPPER_DICT[random_name] == TestDatasetWrapper2

    def test_register_high_level_loss_class(self):
        @register_high_level_loss
        class TestCustomLoss0(object):
            def __init__(self):
                self.name = 'test0'

        assert HIGH_LEVEL_LOSS_DICT['TestCustomLoss0'] == TestCustomLoss0

        @register_high_level_loss()
        class TestCustomLoss1(object):
            def __init__(self):
                self.name = 'test1'

        assert HIGH_LEVEL_LOSS_DICT['TestCustomLoss1'] == TestCustomLoss1
        random_name = 'custom_loss_class_name2'

        @register_high_level_loss(key=random_name)
        class TestCustomLoss2(object):
            def __init__(self):
                self.name = 'test2'

        assert HIGH_LEVEL_LOSS_DICT[random_name] == TestCustomLoss2

    def test_register_loss_wrapper_class(self):
        @register_loss_wrapper
        class TestLossWrapper0(object):
            def __init__(self):
                self.name = 'test0'

        assert LOSS_WRAPPER_DICT['TestLossWrapper0'] == TestLossWrapper0

        @register_loss_wrapper()
        class TestLossWrapper1(object):
            def __init__(self):
                self.name = 'test1'

        assert LOSS_WRAPPER_DICT['TestLossWrapper1'] == TestLossWrapper1
        random_name = 'custom_loss_wrapper_class_name2'

        @register_loss_wrapper(key=random_name)
        class TestLossWrapper2(object):
            def __init__(self):
                self.name = 'test2'

        assert LOSS_WRAPPER_DICT[random_name] == TestLossWrapper2

    def test_register_mid_level_loss(self):
        @register_mid_level_loss
        class TestMiddleLevelLoss0(object):
            def __init__(self):
                self.name = 'test0'

        assert MIDDLE_LEVEL_LOSS_DICT['TestMiddleLevelLoss0'] == TestMiddleLevelLoss0

        @register_mid_level_loss()
        class TestMiddleLevelLoss1(object):
            def __init__(self):
                self.name = 'test1'

        assert MIDDLE_LEVEL_LOSS_DICT['TestMiddleLevelLoss1'] == TestMiddleLevelLoss1
        random_name = 'custom_mid_level_loss_class_name2'

        @register_mid_level_loss(key=random_name)
        class TestMiddleLevelLoss2(object):
            def __init__(self):
                self.name = 'test2'

        assert MIDDLE_LEVEL_LOSS_DICT[random_name] == TestMiddleLevelLoss2

    def test_func2extract_model_output(self):
        @register_func2extract_model_output
        def test_func2extract_model_output0():
            pass

        assert FUNC2EXTRACT_MODEL_OUTPUT_DICT['test_func2extract_model_output0'] == test_func2extract_model_output0

        @register_func2extract_model_output()
        def test_func2extract_model_output1():
            pass

        assert FUNC2EXTRACT_MODEL_OUTPUT_DICT['test_func2extract_model_output1'] == test_func2extract_model_output1
        random_name = 'custom_func2extract_org_output_name2'

        @register_func2extract_model_output(key=random_name)
        def test_func2extract_model_output2():
            pass

        assert FUNC2EXTRACT_MODEL_OUTPUT_DICT[random_name] == test_func2extract_model_output2

    def test_register_optimizer(self):
        @register_optimizer
        class TestOptimizer0(object):
            def __init__(self):
                self.name = 'test0'

        assert OPTIM_DICT['TestOptimizer0'] == TestOptimizer0

        @register_optimizer()
        class TestOptimizer1(object):
            def __init__(self):
                self.name = 'test1'

        assert OPTIM_DICT['TestOptimizer1'] == TestOptimizer1
        random_name = 'custom_optimizer_class_name2'

        @register_optimizer(key=random_name)
        class TestOptimizer2(object):
            def __init__(self):
                self.name = 'test2'

        assert OPTIM_DICT[random_name] == TestOptimizer2

    def test_register_scheduler(self):
        @register_scheduler
        class TestScheduler0(object):
            def __init__(self):
                self.name = 'test0'

        assert SCHEDULER_DICT['TestScheduler0'] == TestScheduler0

        @register_scheduler()
        class TestScheduler1(object):
            def __init__(self):
                self.name = 'test1'

        assert SCHEDULER_DICT['TestScheduler1'] == TestScheduler1
        random_name = 'custom_scheduler_class_name2'

        @register_scheduler(key=random_name)
        class TestScheduler2(object):
            def __init__(self):
                self.name = 'test2'

        assert SCHEDULER_DICT[random_name] == TestScheduler2

    def test_register_adaptation_module(self):
        @register_adaptation_module
        class TestAdaptationModule0(object):
            def __init__(self):
                self.name = 'test0'

        assert ADAPTATION_MODULE_DICT['TestAdaptationModule0'] == TestAdaptationModule0

        @register_adaptation_module()
        class TestAdaptationModule1(object):
            def __init__(self):
                self.name = 'test1'

        assert ADAPTATION_MODULE_DICT['TestAdaptationModule1'] == TestAdaptationModule1
        random_name = 'custom_adaptation_module_class_name2'

        @register_adaptation_module(key=random_name)
        class TestAdaptationModule2(object):
            def __init__(self):
                self.name = 'test2'

        assert ADAPTATION_MODULE_DICT[random_name] == TestAdaptationModule2

    def test_register_model(self):
        @register_model
        class TestModel0(object):
            def __init__(self):
                self.name = 'test0'

        assert MODEL_DICT['TestModel0'] == TestModel0

        @register_model()
        class TestModel1(object):
            def __init__(self):
                self.name = 'test1'

        assert MODEL_DICT['TestModel1'] == TestModel1
        random_name = 'custom_model_class_name2'

        @register_model(key=random_name)
        class TestModel2(object):
            def __init__(self):
                self.name = 'test2'

        assert MODEL_DICT[random_name] == TestModel2

    def test_register_auxiliary_model_wrapper(self):
        @register_auxiliary_model_wrapper
        class TestAuxiliaryModelWrapper0(object):
            def __init__(self):
                self.name = 'test0'

        assert AUXILIARY_MODEL_WRAPPER_DICT['TestAuxiliaryModelWrapper0'] == TestAuxiliaryModelWrapper0

        @register_auxiliary_model_wrapper()
        class TestAuxiliaryModelWrapper1(object):
            def __init__(self):
                self.name = 'test1'

        assert AUXILIARY_MODEL_WRAPPER_DICT['TestAuxiliaryModelWrapper1'] == TestAuxiliaryModelWrapper1
        random_name = 'custom_auxiliary_model_wrapper_class_name2'

        @register_auxiliary_model_wrapper(key=random_name)
        class TestAuxiliaryModelWrapper2(object):
            def __init__(self):
                self.name = 'test2'

        assert AUXILIARY_MODEL_WRAPPER_DICT[random_name] == TestAuxiliaryModelWrapper2

    def test_register_pre_epoch_proc_func(self):
        @register_pre_epoch_proc_func
        def test_pre_epoch_proc_func0():
            pass

        assert get_pre_epoch_proc_func('test_pre_epoch_proc_func0') == test_pre_epoch_proc_func0

        @register_pre_epoch_proc_func()
        def test_pre_epoch_proc_func1():
            pass

        assert get_pre_epoch_proc_func('test_pre_epoch_proc_func1') == test_pre_epoch_proc_func1
        random_name = 'custom_pre_epoch_proc_func_name2'

        @register_pre_epoch_proc_func(key=random_name)
        def test_pre_epoch_proc_func2():
            pass

        assert get_pre_epoch_proc_func(random_name) == test_pre_epoch_proc_func2

    def test_register_pre_forward_proc_func(self):
        @register_pre_forward_proc_func
        def test_pre_forward_proc_func0():
            pass

        assert get_pre_forward_proc_func('test_pre_forward_proc_func0') == test_pre_forward_proc_func0

        @register_pre_forward_proc_func()
        def test_pre_forward_proc_func1():
            pass

        assert get_pre_forward_proc_func('test_pre_forward_proc_func1') == test_pre_forward_proc_func1
        random_name = 'custom_pre_forward_proc_func_name2'

        @register_pre_forward_proc_func(key=random_name)
        def test_pre_forward_proc_func2():
            pass

        assert get_pre_forward_proc_func(random_name) == test_pre_forward_proc_func2

    def test_register_post_forward_proc_func(self):
        @register_post_forward_proc_func
        def test_post_forward_proc_func0():
            pass

        assert get_post_forward_proc_func('test_post_forward_proc_func0') == test_post_forward_proc_func0

        @register_post_forward_proc_func()
        def test_post_forward_proc_func1():
            pass

        assert get_post_forward_proc_func('test_post_forward_proc_func1') == test_post_forward_proc_func1
        random_name = 'custom_post_forward_proc_func_name2'

        @register_post_forward_proc_func(key=random_name)
        def test_post_forward_proc_func2():
            pass

        assert get_post_forward_proc_func(random_name) == test_post_forward_proc_func2

    def test_register_post_epoch_proc_func(self):
        @register_post_epoch_proc_func
        def test_post_epoch_proc_func0():
            pass

        assert get_post_epoch_proc_func('test_post_epoch_proc_func0') == test_post_epoch_proc_func0

        @register_post_epoch_proc_func()
        def test_post_epoch_proc_func1():
            pass

        assert get_post_epoch_proc_func('test_post_epoch_proc_func1') == test_post_epoch_proc_func1
        random_name = 'custom_post_epoch_proc_func_name2'

        @register_post_epoch_proc_func(key=random_name)
        def test_post_epoch_proc_func2():
            pass

        assert get_post_epoch_proc_func(random_name) == test_post_epoch_proc_func2
