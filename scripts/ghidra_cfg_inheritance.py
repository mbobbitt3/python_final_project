from collections import OrderedDict
import json
from ghidra.program.model.block import SimpleBlockModel
from ghidra.util.task import ConsoleTaskMonitor

# Base class for program setup and function operations
class ProgramBase:
	"""utiity functions and intiializations to be inherited from in the CFG class"""
	def __init__(self, offset):
		self.prog = getCurrentProgram() 
		self.monitor = ConsoleTaskMonitor()
		self._func = self.func_conv(offset)

	def func_conv(self, offset):
		"""Convert a raw hex address into a Ghidra function object"""
		f_addr = self.prog.getAddressFactory().getDefaultAddressSpace().getAddress(offset)
		return self.prog.getFunctionManager().getFunctionContaining(f_addr)

	@property
	def func(self):
		"""Getter for the current function"""
		return self._func

	@func.setter
	def func(self, offset):
		"""Setter to change the current function"""
		self._func = self.func_conv(offset)


# Derived class for control flow graph operations
class CFG(ProgramBase):
	"""class to create the contorl flow graph and save it to json file"""
	def __init__(self):
		self.model = SimpleBlockModel(self.prog)
		self.block_iter = self.model.getCodeBlocksContaining(self._func.getBody(), self.monitor)
		self.edge_map = OrderedDict()

	def gen_cfg_dict(self):
		"""Generate a control flow graph dictionary by iterating through basic blocks and grabbing their respecitve
		destinations and flow type. Hey are then able to be stored into a json file"""
		f_name = self._func.getName()
		self.edge_map[f_name] = []
		entry_node = False

		# Iterate over basic blocks and find their destinations
		while self.block_iter.hasNext():
			bb = self.block_iter.next()
			bb_name = bb.getName().strip("LAB_")

			# Get the basic block's destinations
			bb_dests = bb.getDestinations(self.monitor)
			while bb_dests.hasNext():
				bb_succ = bb_dests.next()
				bb_succ_name = str(bb_succ).split("> ")[-1]
				flow_type = bb.getFlowType().toString()

				# Add the block and its successor to the edge map
				self.edge_map[f_name].append((bb_name, bb_succ_name, flow_type))

				if not entry_node:
					entry_node = True
					self.edge_map["entry_node"] = bb_name

				self.edge_map["exit_node"] = bb_succ_name

		return self.edge_map

	def save_cfg(self, cfg_dict):
		"""Save the control flow graph to a JSON file"""
		kwords = [self.prog.getName().replace(".", "_"), self._func.getName()]
		out_name = "_".join(kwords)
		with open("cfg_json_files/" + out_name + ".json", "w+") as fd:
			json.dump(cfg_dict, fd)


# Testing the refactored code
if __name__ == "__main__":
	cfg = CFG(0x0010146b)
	cfg_dict = cfg.gen_cfg_dict()
	cfg.save_cfg(cfg_dict)
