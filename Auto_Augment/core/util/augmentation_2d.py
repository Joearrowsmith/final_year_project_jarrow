import tensorflow as tf


def apply_random_brightness(image_tensor, label_tensor, do_prob=1.0, magnitude=1.0):
    if tf.random.uniform(()) <= do_prob:
        image_tensor = tf.image.random_brightness(image_tensor, magnitude)
    return image_tensor, label_tensor


def apply_random_left_right_flip(image_tensor, label_tensor, do_prob=1.0, magnitude=None):
    if tf.random.uniform(()) <= do_prob:
        image_tensor = tf.image.random_flip_left_right(image_tensor, magnitude)
    return image_tensor, label_tensor


def apply_random_up_down_flip(image_tensor, label_tensor, do_prob=1.0, magnitude=None):
    if tf.random.uniform(()) <= do_prob:
        image_tensor = tf.image.random_flip_up_down(image_tensor, magnitude)
    return image_tensor, label_tensor


def apply_random_shear(image_tensor, label_tensor, do_prob=1.0, magnitude=20.0):
    if tf.random.uniform(()) <= do_prob:
        image_tensor = tf.keras.preprocessing.image.random_shear(image_tensor, magnitude),
    return image_tensor, label_tensor


def apply_random_zoom(image_tensor, label_tensor, do_prob=1.0, magnitude=None):
    if tf.random.uniform(()) <= do_prob:
        image_tensor = tf.image.random_crop(image_tensor, magnitude)
    return image_tensor, label_tensor


def apply_random_contrast(image_tensor, label_tensor, do_prob=1.0, magnitude=None):
    if tf.random.uniform(()) <= do_prob:
        image_tensor = tf.image.random_contrast(image_tensor, 0.0, 1.0)
    return image_tensor, label_tensor
