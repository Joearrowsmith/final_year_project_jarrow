import tensorflow as tf
from Auto_Augment.augmentation_funcs.augmentation_2d import \
    apply_random_brightness, apply_random_left_right_flip, \
    apply_random_up_down_flip, apply_random_shear, apply_random_zoom, \
    apply_random_contrast


class NoAugmentationPolicy(tf.keras.Model):
    def __init__(self, *args, **kwargs):
        super(NoAugmentationPolicy, self).__init__()

    def call(self, inputs, training=False):
        x, y = inputs
        return x, y


class RandomAugmentationPolicy(tf.keras.Model):
    def __init__(self, apply_to_y=False, image=True):
        super(RandomAugmentationPolicy, self).__init__()
        if image:
            self.augmentation_choices = [apply_random_brightness, apply_random_left_right_flip,
                                         apply_random_up_down_flip, apply_random_shear, apply_random_zoom, \
                                         apply_random_contrast]
        else:
            raise NotImplementedError()

    def call(self, inputs, training=False):
        x, y = inputs
        for aug in self.augmentation_choices:
            x, y = aug(x, y, do_prob=tf.random.uniform(()))
        return x, y


class FixAugmentationPolicy(tf.keras.Model):
    def __init__(self, aug_args, apply_to_y=False, image=True):
        super(FixAugmentationPolicy, self).__init__()
        self.aug_args = aug_args
        if image:
            self.augmentation_choices = [apply_random_brightness, apply_random_left_right_flip,
                                         apply_random_up_down_flip, apply_random_shear, apply_random_zoom, \
                                         apply_random_contrast]
        else:
            raise NotImplementedError()

    def call(self, inputs, training=False):
        # todo: final optimal static augmentation parameters
        x, y = inputs
        for aug, args in zip(self.augmentation_choices, self.aug_args):
            x, y = aug(x, y, *args)
        return x, y
