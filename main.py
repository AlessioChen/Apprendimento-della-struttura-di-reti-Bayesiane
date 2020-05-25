from BayesNet import *
from Dataset import *
from Input import *
from Learning import *

dataset_dim = 150
nodes = asia_net()
net = BayesNet(nodes)
dataset = Dataset(net, dataset_dim)
sum_dag = np.zeros((len(nodes), len(nodes)))

for i in range(1000):
    dataset = Dataset(net, dataset_dim)
    app = k2(dataset.dataset, dataset.ordered_array, 2)
    sum_dag = sum_dag + app

print(sum_dag)
