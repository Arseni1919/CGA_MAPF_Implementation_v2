# Multi-Agent Corridor Generating Algorithm (MACGA)

This repository contains the implementation of the **Multi-Agent Corridor Generating Algorithm (MACGA)**, published at IJCAI-25. MACGA is a novel approach for solving Multi-Agent Path Finding (MAPF) and Lifelong MAPF (LMAPF) problems by generating corridors to guide agent navigation in crowded environments.

## 📖 Paper Information

**Title:** Multi-Agent Corridor Generating Algorithm  
**Conference:** IJCAI-25  
**Algorithm Variants:**
- **MACGA** - Pure corridor-based algorithm
- **MACGA+PIBT** - Hybrid approach combining corridor generation with Priority-based Incremental Best-first Tree search

## 🏗️ Repository Structure

```
├── algs/                           # Algorithm implementations
│   ├── alg_mapf_cga_pure.py       # Pure MACGA implementation
│   ├── alg_mapf_cga.py            # MACGA+PIBT hybrid implementation
│   ├── alg_lifelong_cga*.py       # Lifelong MAPF variants
│   └── alg_functions_*.py          # Algorithm helper functions
├── maps/                           # Test maps and environments
│   ├── *.map                      # Map files in standard format
│   └── pngs/                      # Map visualizations
├── logs_for_heuristics/            # Precomputed heuristic data
├── logs_for_freedom_maps/          # Precomputed spatial data
├── final_logs_*/                   # Experimental results
├── run_single_MAPF_func.py        # Single instance execution
├── experiments_MAPF.py             # MAPF benchmark experiments
├── experiments_LMAPF.py            # Lifelong MAPF experiments
├── functions_general.py            # General utilities
├── functions_plotting.py           # Visualization functions
└── globals.py                      # Global imports and constants
```

## 🚀 Quick Start

### Prerequisites

Install the required Python packages:

```bash
pip install numpy matplotlib
```

### Initial Setup

1. **Extract precomputed data:**
   ```bash
   # Extract heuristic data
   unzip logs_for_heuristics.zip
   
   # Extract spatial data
   unzip logs_for_freedom_maps.zip
   ```

2. **Verify directory structure:**
   ```
   ├── logs_for_heuristics/
   │   └── h_dict_of_*.json
   └── logs_for_freedom_maps/
       └── *.npy
   ```

## 🎯 Usage Options

### Option 1: Run Single Instance

Execute MACGA on a predefined problem instance:

```bash
python alg_mapf_cga.py
```

**Customization:**
Edit `run_single_MAPF_func.py` to modify:
- Map selection (line 21): `img_dir = 'random-32-32-20.map'`
- Number of agents (line 34): `n_agents = 250`
- Algorithm selection: Choose from available algorithms

**Available Maps:**
- `empty-32-32.map` - Open grid environment
- `random-32-32-20.map` - 20% obstacle density
- `maze-32-32-4.map` - Maze environment
- `room-32-32-4.map` - Multi-room environment

### Option 2: Run Full Experiments

Execute comprehensive benchmark experiments comparing multiple algorithms:

#### MAPF Experiments
```bash
python experiments_MAPF.py
```

#### Lifelong MAPF Experiments
```bash
python experiments_LMAPF.py
```

**Experiment Configuration:**
- Modify algorithm list (line 102 in `experiments_MAPF.py`):
  ```python
  alg_list = alg_list_MACGA_paper_experiments
  ```
- Adjust parameters:
  - Map: `img_dir = 'maze-32-32-4.map'`
  - Agent counts: `n_agents_list = [250, 300]`
  - Problem instances: `i_problems = 30`
  - Time limit: `max_time = 60`

## 🔧 Algorithm Variants

### Available Algorithms

1. **MACGA** (`alg_mapf_cga_pure.py`)
   - Pure corridor-based approach
   - Optimal for structured environments

2. **MACGA+PIBT** (`alg_mapf_cga.py`)
   - Hybrid corridor generation + PIBT
   - Better performance in complex scenarios

3. **Comparison Algorithms:**
   - LaCAM* - State-of-the-art MAPF solver
   - PrP (Prioritized Planning)
   - LNS2 (Large Neighborhood Search)
   - PIBT (Priority-based Incremental Best-first Tree)

### Algorithm Selection

In experiment files, uncomment desired algorithms in the algorithm list:

```python
alg_list_MACGA_paper_experiments = [
    (run_lacam_star, {
        'alg_name': f'LaCAM*',
        'flag_star': False,
        'to_render': False,
    }),
    (run_cga_mapf, {
        'alg_name': f'MACGA+PIBT',
        'alt_goal_flag': 'first',
        'alt_goal_num': 1,
        'to_render': False,
    }),
]
```

## 📊 Results and Visualization

### Metrics Tracked

**MAPF Metrics:**
- Success Rate (SR)
- Sum of Costs (SoC)
- Makespan
- Runtime

**LMAPF Metrics:**
- Throughput (agents reaching goals per timestep)

### Visualization

View results using:
```bash
python show_results.py
```

## 🗺️ Map Formats

Maps use the standard `.map` format:
- `@` - Obstacle
- `.` - Free space
- Grid-based representation

**Example Map Categories:**
- **Empty:** Open environments
- **Random:** Randomly distributed obstacles
- **Maze:** Structured maze layouts
- **Room:** Multi-room environments

## ⚙️ Advanced Configuration

### Custom Problem Generation

Modify problem generation in experiment files:
```python
# Random start/goal positions
start_nodes: List[Node] = random.sample(nodes, n_agents)
goal_nodes: List[Node] = random.sample(nodes, n_agents)

# Fixed positions (for debugging)
start_nodes: List[Node] = [nodes_dict['4_8'], nodes_dict['4_4']]
goal_nodes: List[Node] = [nodes_dict['4_2'], nodes_dict['4_4']]
```

### Performance Profiling

Algorithm performance is automatically profiled and saved to `stats/` directory.

### Rendering Options

Enable visualization during execution:
```python
params = {
    'to_render': True,  # Enable real-time visualization
    'final_render': True,  # Show final path animation
}
```

## 🐛 Troubleshooting

### Common Issues

1. **Missing precomputed data:**
   ```bash
   # Regenerate heuristics (if needed)
   python build_heuristic_map.py
   
   # Regenerate spatial data (if needed)
   python create_non_sv_tables.py
   ```

2. **Import errors:**
   - Ensure all Python dependencies are installed
   - Check that you're running from the repository root

3. **Memory issues:**
   - Reduce `n_agents` for large instances
   - Use smaller maps for testing

### Performance Tips

- Use precomputed heuristics for better performance
- Reduce visualization frequency for faster experiments
- Consider algorithm time limits for difficult instances

## 📄 Citation

If you use this implementation in your research, please cite:

```bibtex
@misc{pertzovsky2025multiagentcorridorgeneratingalgorithm,
      title={Multi-Agent Corridor Generating Algorithm}, 
      author={Arseniy Pertzovsky and Roni Stern and Roie Zivan and Ariel Felner},
      year={2025},
      eprint={2410.12397},
      archivePrefix={arXiv},
      primaryClass={cs.MA},
      url={https://arxiv.org/abs/2410.12397}, 
}
```

## 📬 Contact

For questions, issues, or collaboration opportunities, please:
- Open an issue in the GitHub repository
- Contact the authors directly

## 📝 License

This project is available for research and educational purposes. Please refer to the license file for detailed terms.

---

**Note:** This implementation was developed for research purposes. While functional, the code structure may be optimized further for production use. Contributions and improvements are welcome!