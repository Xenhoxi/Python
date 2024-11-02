import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.array:
	"""Invert colors of the image"""
	full = np.copy(array)
	full[:, :, :] = 255
	array = full - array
	return array


def ft_red(array) -> np.array:
	"""Apply red filter on the image"""
	img = np.copy(array)
	img[:, :, 1] = 0
	img[:, :, 2] = 0
	return img


def ft_green(array) -> np.array:
	"""Apply green filter on the image"""
	img = np.copy(array)
	img[:, :, 0] = 0
	img[:, :, 2] = 0
	return img


def ft_blue(array) -> np.array:
	"""Apply blue filter on the image"""
	img = np.copy(array)
	img[:, :, 0] = 0
	img[:, :, 1] = 0
	return img


def ft_grey(array) -> np.array:
	"""Tranform color image to grayscale image"""
	return array