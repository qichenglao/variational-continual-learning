
export PYTHONPATH=$PYTHONPATH:~/variational-continual-learning

data_name='mnist'
method='onlinevi'

CUDA_VISIBLE_DEVICES=${device} python dgm/exp.py $data_name $method

