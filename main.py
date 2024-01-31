import pandas as pd
import holoviews as hv
from bokeh.plotting import show

hv.extension('bokeh')
raw = pd.read_csv('data/result.csv')
edges = raw.sort_values(['source', 'value'])
dim = hv.Dimension('value', value_format=lambda x: f'{x} %')
sankey = hv.Sankey(edges, label='Personal Finance Planning as Percentage (%)',
                   vdims=dim)
sankey.opts(label_position='left', edge_color='target',
            node_color='index', cmap='viridis')

show(hv.render(sankey))
