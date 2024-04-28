#!/bin/bash
analyzeHeadless $HOME/ghidra_projects/ final_python -import sample/sample.out -postScript scripts/ghidra_cfg_inheritance.py 
python scripts/graph_generation.py
