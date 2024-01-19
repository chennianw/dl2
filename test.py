import pm4py

net, im, fm = pm4py.read_pnml('data/normal_heuristics_0.95_0.95_0.95.pnml')
pm4py.view_petri_net(net, im, fm)
