import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

input_file = './all_textandidedit.csv'

# Create a graph object
graph = nx.Graph()

# Read the CSV file with pandas
df = pd.read_csv(input_file, encoding='utf-8', names=['authorChannelId', 'videoId'])

# Iterate through the DataFrame and add edges to the graph
for i in range(len(df)):
    user_id = df.at[i, 'authorChannelId']
    video_id = df.at[i, 'videoId']
    
    # Add the edge to the graph
    if graph.has_edge(user_id, video_id):
        graph[user_id][video_id]['weight'] += 1
    else:
        graph.add_edge(user_id, video_id, weight=1)

# Draw the graph
pos = nx.spring_layout(graph, seed=42)
nx.draw(graph, pos, with_labels=True, node_size=300, edge_color='gray', font_size=8, font_weight='bold')

# Draw edge labels
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size=6)

# Show the graph
plt.show()
