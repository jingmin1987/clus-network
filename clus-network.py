# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 21:35:59 2017

Visualize SAS Proc Varclus and where LexisNexis variables fit in
the existing cluster structure

@author: Jingmin
"""

import plotly.plotly as py
import plotly.graph_objs as go
import networkx as nx
import pandas as pd

# Empty graph
G = nx.Graph()

# Import cluster structure data
fmcc = pd.read_csv(
   r'C:\Users\Jingmin\Documents\GitHub\clus-network\VC1.csv'
)

ln = pd.read_csv(
   r'C:\Users\Jingmin\Documents\GitHub\clus-network\VC2.csv'
)

# Some clean up of var_name
fmcc['var_name'] = fmcc['var_name'].apply(lambda x: x.replace('WOE_', ''))
ln['var_name'] = ln['var_name'].apply(lambda x: x.replace('WOE_', ''))

# Add nodes and edges
for row in fmcc.itertuples():
    _, clus, var, rsq, rsq_n, clus_n, _ = tuple(row)
    G.add_node(clus, type='clus', cluster=clus)
    G.add_node(var, type='fmcc var', cluster=clus)     
    G.add_node(clus_n, type='clus', cluster=clus_n)
    if rsq > 0.36:
        G.add_edge(clus, var, rsq=rsq)
        if rsq_n > 0.36:
            G.add_edge(clus_n, var, rsq=rsq_n)     

    
for row in ln.itertuples():
    _, clus, var, rsq, rsq_n, clus_n, _ = tuple(row)
    G.add_node(clus, type='clus', cluster=clus)
    G.add_node(var, type='ln var', cluster=clus)     
    G.add_node(clus_n, type='clus', cluster=clus_n)
    if rsq > 0.36:
        G.add_edge(clus, var, rsq=rsq)
        if rsq_n > 0.36:
            G.add_edge(clus_n, var, rsq=rsq_n)
            
# Customize the plot
pos = nx.spring_layout(G)

edge_trace = go.Scatter(
    x=[],                     
    y=[],
    line=go.Line(
        width=[],
        color='#888'           
    ),
    hoverinfo=None,
    mode='line'
)

for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_trace['x'] += [x0, x1, None]
    edge_trace['y'] += [y0, y1, None]
    edge_trace['line']['width'].append(G[edge[0]][edge[1]]['rsq'] / 2)
    
node_trace = go.Scatter(
    x=[], 
    y=[], 
    text=[],
    marker=go.Marker(
        showscale=True,
        colorscale='YIGnBu',
        color=[], 
        size=[],
        symbol=[],       
        colorbar=dict(
            thickness=15,
            title='Cluster',
            xanchor='left',
            titleside='right'
        ),
        line=dict(width=1)
    ),
    mode='markers', 
    hoverinfo='text',
)
        
for node in G.nodes():
    x, y = pos[node]
    node_trace['x'].append(x)
    node_trace['y'].append(y)
    
    if G.node[node]['type'].find('var') > -1:
        node_trace['marker']['size'].append(5)
        
        if G.node[node]['type'] == 'fmcc var':
            node_trace['marker']['symbol'].append('circle')
        else:
            node_trace['marker']['symbol'].append('diamond')
        
    else:
        node_trace['marker']['size'].append(10)
        node_trace['marker']['symbol'].append('circle')
        
    node_trace['marker']['color'].append(int(G.node[node]['cluster'][-2:]))
    node_trace['text'].append(node)
    