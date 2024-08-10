import heapq

from algs.alg_functions_cga import *
from algs.alg_functions_pibt import run_procedure_pibt
from run_single_MAPF_func import run_mapf_alg


def run_cga_mapf(
        start_nodes: List[Node],
        goal_nodes: List[Node],
        nodes: List[Node],
        nodes_dict: Dict[str, Node],
        h_dict: Dict[str, np.ndarray],
        map_dim: Tuple[int, int],
        params: Dict
) -> Tuple[None, Dict] | Tuple[Dict[str, List[Node]], Dict]:

    max_time: int | float = params['max_time']
    alg_name: str = params['alg_name']
    to_render: bool = params['to_render']
    img_np: np.ndarray = params['img_np']
    blocked_sv_map: np.ndarray = params['blocked_sv_map']

    if to_render:
        fig, ax = plt.subplots(1, 2, figsize=(14, 7))

    start_time = time.time()

    # create agents
    agents, agents_dict = create_agents(start_nodes, goal_nodes)
    n_agents = len(agents_dict)
    agents.sort(key=lambda a: a.priority, reverse=True)

    iteration = 0
    finished = False
    while not finished:

        config_from: Dict[str, Node] = {a.name: a.path[iteration] for a in agents}
        occupied_from: Dict[str, AgentAlg] = {a.path[iteration].xy_name: a for a in agents}
        config_to: Dict[str, Node] = {}
        occupied_to: Dict[str, AgentAlg] = {}
        blocked_nodes: List[Node] = []

        # Update config_to with agents that have planned future steps
        for agent in agents:
            if len(agent.path) - 1 >= iteration + 1:
                next_node: Node = agent.path[iteration + 1]
                config_to[agent.name] = next_node
                occupied_to[next_node.xy_name] = agent
                for n in agent.path[iteration + 1:]:
                    if n not in blocked_nodes:
                        heapq.heappush(blocked_nodes, n)

        # calc the step
        for agent in agents:
            # if planned, continue
            if agent.name in config_to:
                continue
            # if at its original goal, continue
            if config_from[agent.name] == agent.goal_node:
                stay(agent, config_from[agent.name], config_to, occupied_to)
                continue
            # if at its alt goal, switch to the original goal
            if agent.alt_goal_node is not None and config_from[agent.name] == agent.alt_goal_node:
                agent.alt_goal_node = None
            goal_node = agent.get_goal_node()
            next_node = get_min_h_nei_node(config_from[agent.name], goal_node, h_dict)
            non_sv_nodes_np = blocked_sv_map[goal_node.x, goal_node.y]
            if non_sv_nodes_np[next_node.x, next_node.y]:
                run_procedure_pibt(
                    agent,
                    config_from, occupied_from,
                    config_to, occupied_to,
                    agents_dict, nodes_dict, h_dict, blocked_nodes)
                continue
            else:
                calc_cga_step(
                    agent, iteration,
                    config_from, occupied_from,
                    config_to, occupied_to,
                    agents, agents_dict, nodes, nodes_dict, h_dict, non_sv_nodes_np, blocked_nodes)
                continue

        # execute the step + check the termination condition
        finished = True
        agents_finished = []
        for agent in agents:
            if len(agent.path) - 1 == iteration:
                next_node = config_to[agent.name]
                agent.path.append(next_node)
            else:
                next_node = agent.path[iteration + 1]
            agent.prev_node = agent.curr_node
            agent.curr_node = next_node
            if agent.curr_node != agent.goal_node:
                finished = False
                agent.priority += 1
            else:
                agent.priority = agent.init_priority
                agents_finished.append(agent)

        # unfinished first
        agents.sort(key=lambda a: a.priority, reverse=True)

        # print + render
        runtime = time.time() - start_time
        print(
            f'\r{'*' * 10} | [{alg_name}] {iteration=: <3} | finished: {len(agents_finished)}/{n_agents: <3} | runtime: {runtime: .2f} seconds | {'*' * 10}',
            end='')
        if to_render and iteration >= 0:
            # update curr nodes
            for a in agents:
                a.curr_node = config_to[a.name]
            # plot the iteration
            # i_agent = agents_dict['agent_0']
            i_agent = agents[0]
            plot_info = {
                'img_np': img_np,
                'agents': agents,
                'i_agent': i_agent,
            }
            plot_step_in_env(ax[0], plot_info)
            plt.pause(0.001)
            # plt.pause(1)
        iteration += 1

        if runtime > max_time:
            return None, {}

    # checks
    # for i in range(len(agents[0].path)):
    #     check_vc_ec_neic_iter(agents, i, to_count=False)
    runtime = time.time() - start_time
    return {a.name: a.path for a in agents}, {'agents': agents, 'time': runtime, 'makespan': iteration}


@use_profiler(save_dir='../stats/alg_cga_mapf.pstat')
def main():

    to_render = True
    # to_render = False

    params = {
        'max_time': 100,
        'alg_name': 'CGA-MAPF',
        'to_render': to_render,
    }
    run_mapf_alg(alg=run_cga_mapf, params=params)


if __name__ == '__main__':
    main()

