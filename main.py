from BayesNet import *
from Dataset import *
from Input import *
from Learning import *

nodes = asia_net()
net = BayesNet(nodes)
dataset = Dataset(net, 150)
sum_dag = np.zeros((len(nodes), len(nodes)))
for i in range(1000):
    dataset = Dataset(net, 150)
    app = k2(dataset.dataset, dataset.ordered_array, 2)
    sum_dag = sum_dag + app

print(sum_dag)
