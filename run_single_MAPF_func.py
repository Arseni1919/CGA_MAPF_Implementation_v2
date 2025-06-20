from globals import *
from functions_general import *
from functions_plotting import *


def run_mapf_alg(alg, params, final_render: bool = True):
    # set_seed(random_seed_bool=False, seed=5)
    # set_seed(random_seed_bool=False, seed=123)
    # set_seed(random_seed_bool=False, seed=2953)
    set_seed(random_seed_bool=True)

    # img_dir = '10_10_my_rand.map'
    # img_dir = '15-15-two-rooms.map'
    # img_dir = '15-15-four-rooms.map'
    # img_dir = '15-15-six-rooms.map'
    # img_dir = '15-15-eight-rooms.map'

    # img_dir = '10_10_my_corridor.map'
    # img_dir = 'empty-32-32.map'
    # img_dir = 'random-32-32-10.map'
    img_dir = 'random-32-32-20.map'
    # img_dir = 'maze-32-32-4.map'
    # img_dir = 'maze-32-32-2.map'
    # img_dir = 'room-32-32-4.map'

    # n_agents = 700
    # n_agents = 600
    # n_agents = 550
    # n_agents = 500
    # n_agents = 450
    # n_agents = 400
    # n_agents = 350
    # n_agents = 300
    n_agents = 250
    # n_agents = 200
    # n_agents = 170
    # n_agents = 150
    # n_agents = 100
    # n_agents = 80
    # n_agents = 70
    # n_agents = 50
    # n_agents = 40
    # n_agents = 15
    # n_agents = 10
    # n_agents = 3

    path_to_maps: str = '../maps'
    path_to_heuristics: str = '../logs_for_heuristics'
    path_to_sv_maps: str = '../logs_for_freedom_maps'

    img_np, (height, width) = get_np_from_dot_map(img_dir, path_to_maps)
    map_dim = (height, width)
    nodes, nodes_dict = build_graph_from_np(img_np, show_map=False)
    h_dict: Dict[str, np.ndarray] = exctract_h_dict(img_dir, path_to_heuristics)
    blocked_sv_map: np.ndarray = get_blocked_sv_map(img_dir, folder_dir=path_to_sv_maps)
    # sv_map: np.ndarray = get_sv_map(img_dir, folder_dir=path_to_sv_maps)

    start_nodes: List[Node] = random.sample(nodes, n_agents)
    goal_nodes: List[Node] = random.sample(nodes, n_agents)
    # start_nodes: List[Node] = [nodes_dict['4_8'], nodes_dict['4_4'], nodes_dict['8_8']]
    # goal_nodes: List[Node] = [nodes_dict['4_2'], nodes_dict['4_4'], nodes_dict['8_8']]
    # start_nodes: List[Node] = [nodes_dict['4_8'], nodes_dict['4_4']]
    # goal_nodes: List[Node] = [nodes_dict['4_2'], nodes_dict['4_4']]
    # goal_nodes: List[Node] = [nodes_dict['4_1'], nodes_dict['4_0']]
    # start_nodes: List[Node] = [nodes_dict['4_0'], nodes_dict['4_1'], nodes_dict['4_2']]
    # goal_nodes: List[Node] = [nodes_dict['4_1'], nodes_dict['4_0'], nodes_dict['4_2']]

    # start_nodes: List[Node] = [nodes_dict['4_0'], nodes_dict['4_1'], nodes_dict['4_2'], nodes_dict['4_3']]
    # goal_nodes: List[Node] = [nodes_dict['4_1'], nodes_dict['4_0'], nodes_dict['4_2'], nodes_dict['4_3']]

    params['img_np'] = img_np
    # params['sv_map'] = sv_map
    params['blocked_sv_map'] = blocked_sv_map
    paths_dict, info = alg(
        start_nodes, goal_nodes, nodes, nodes_dict, h_dict, map_dim, params
    )

    # plot
    if final_render and paths_dict is not None:
        agents: List = info['agents']
        plt.close()
        fig, ax = plt.subplots(1, 2, figsize=(14, 7))
        plot_rate = 0.001
        # plot_rate = 0.5
        # plot_rate = 1
        max_path_len = max([len(a.path) for a in agents])
        soc = sum([len(a.path) for a in agents])

        print(f'\n{max_path_len=}')
        print(f'{soc=}')
        for i in range(max_path_len):
            # update curr nodes
            for a in agents:
                a.update_curr_node(i)
            # plot the iteration
            i_agent = agents[0]
            plot_info = {
                'img_np': img_np,
                'agents': agents,
                'i_agent': i_agent,
                'iteration': i,
            }
            plot_step_in_env(ax[0], plot_info)
            plt.pause(plot_rate)
        plt.show()







