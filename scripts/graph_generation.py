import networkx as nx
import json
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
import random
class Cfg_Graph:

	def __init__(self):
		with open("cfg_json_files/sample_out_main.json", 'r') as fd:
			self.dict = json.load(fd)
		self.cfg = self.dict[next(iter(self.dict))]
		self.graph = nx.DiGraph()
		self.entry_node = self.dict['entry_node']
		self.exit_node = self.dict['exit_node']
		self.flow_types = [
			"CALL_OVERRIDE_UNCONDITIONAL",
			"CALL_TERMINATOR",
			"CALLOTHER_OVERRIDE_CALL",
			"CALLOTHER_OVERRIDE_JUMP",
			"COMPUTED_CALL",
			"COMPUTED_CALL_TERMINATOR",
			"COMPUTED_JUMP",
			"CONDITIONAL_CALL",
			"CONDITIONAL_CALL_TERMINATOR",
			"CONDITIONAL_COMPUTED_CALL",
			"CONDITIONAL_COMPUTED_JUMP",
			"CONDITIONAL_JUMP",
			"CONDITIONAL_TERMINATOR",
			"DATA",
			"DATA_IND",
			"EXTERNAL_REF",
			"FALL_THROUGH",
			"FLOW",
			"INDIRECTION",
			"INVALID",
			"JUMP_OVERRIDE_UNCONDITIONAL",
			"JUMP_TERMINATOR",
			"PARAM",
			"READ",
			"READ_IND",
			"READ_WRITE",
			"READ_WRITE_IND",
			"TERMINATOR",
			"THUNK",
			"UNCONDITIONAL_CALL",
			"UNCONDITIONAL_JUMP",
			"WRITE",
			"WRITE_IND"
		]
		self.colors = sns.color_palette('husl', len(self.flow_types))
		self.colors = [self.rgb_to_hex(color) for color in self.colors]
		self.type_to_color = {flow_type: self.colors[i] for i, flow_type in enumerate(self.flow_types)}


	def rgb_to_hex(self, rgb_tuple):
		# Ensure RGB tuple values are in the range [0, 1]
		if not all(0 <= v <= 1 for v in rgb_tuple):
			raise ValueError("RGB values should be between 0 and 1")
		
		# Convert to hexadecimal
		return mcolors.to_hex(rgb_tuple)

	def create_graph(self):
		# Loop through each key-value pair in the dictionary
		for source, target, flow_type in self.cfg:
			print(source, target, flow_type)
			self.graph.add_edge(source, target, color = self.type_to_color[flow_type])	# Add edge from source to target
		return self.graph
	
	def visualize_graph(self, graph):
		# Generate the visualization
		plt.figure(figsize=(100, 60))
		pos = nx.nx_agraph.graphviz_layout(self.graph, prog='dot')	# Positions for all nodes
		nx.draw(self.graph, pos, with_labels=True, node_size=700, node_color='lightblue', edge_color='gray', font_size=7)
		#edge_labels = nx.get_edge_attributes(self.graph, 'label')
		edge_colors = [self.graph.edges[edge]['color'] for edge in self.graph.edges]
		nx.draw_networkx_edges(self.graph, pos, edge_color = edge_colors)
		nx.draw_networkx_nodes(self.graph, pos, nodelist = [self.entry_node], node_color = 'green', node_size = 800)
		nx.draw_networkx_nodes(self.graph, pos, nodelist = [self.exit_node], node_color = 'red', node_size = 800)
		used_types = set(edge_colors)
		legend_elements = [
			plt.Line2D([0], [0], color=self.type_to_color[flow_type], lw=4, label=flow_type)
			for flow_type in self.type_to_color 
			if self.type_to_color[flow_type] in used_types
		]
		plt.legend(handles = legend_elements, title = 'edge flow types', loc = 'upper left')
		plt.title("Control Flow Graph")
		plt.show()	# Display the graph
	
cfg = Cfg_Graph()
cfg_obj = cfg.create_graph()
cfg.visualize_graph(cfg_obj)
