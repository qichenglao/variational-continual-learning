import numpy as np

def config(data_name, n_channel):
    if data_name == 'mnist':
        labels = [[i] for i in range(10)]
        n_iter = 200
        dimX = 28**2
        shape_high = (28, 28)
        ll = 'bernoulli'
    if data_name == 'notmnist':
        labels = [[i] for i in range(10)]
        n_iter = 400
        dimX = 28**2
        shape_high = (28, 28)
        ll = 'bernoulli'

    if data_name == 'cifar10':
        labels = [[i] for i in range(10)]
        n_iter = 200
        dimX = 32**2*3
        shape_high = (32, 32, 3)
        ll = 'bernoulli'

    if data_name == 'coco':
        labels = ['bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe']
        n_iter = 200
        dimX = 28**2
        shape_high = (28, 28)
        ll = 'bernoulli'

    return labels, n_iter, dimX, shape_high, ll

