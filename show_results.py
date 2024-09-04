from functions_plotting import *


def show_results(file_dir):
    plt.close()
    with open(f'{file_dir}', 'r') as openfile:
        # Reading from json file
        logs_dict = json.load(openfile)
        expr_type = logs_dict['expr_type']

        if expr_type == 'MAPF':
            # logs_dict['alg_names'] = [
            #     # "LaCAM*",
            #     # "APF-LaCAM*",
            #     # "LaCAM",
            #     # "APF-LaCAM",
            #     # "PIBT",
            #     # "APF-PIBT",
            #     "k-LNS2-A*",
            #     "APF-k-LNS2-A*",
            #     "k-LNS2-SIPPS",
            #     "APF-k-LNS2-SIPPS",
            #     "k-PrP-A*",
            #     "APF-k-PrP-A*",
            #     "k-PrP-SIPPS",
            #     "APF-k-PrP-SIPPS",
            # ]

            fig, ax = plt.subplots(2, 2, figsize=(8, 8))
            # fig, ax = plt.subplots(1, 1, figsize=(8, 8))

            # plot_rsoc(ax, info=logs_dict)

            plot_sr(ax[0, 0], info=logs_dict)
            plot_time_metric(ax[0, 1], info=logs_dict)
            # plot_time_metric_cactus(ax[0, 1], info=logs_dict)
            # plot_makespan(ax[1, 0], info=logs_dict)
            plot_makespan_cactus(ax[1, 0], info=logs_dict)
            # plot_soc(ax[1, 1], info=logs_dict)
            plot_soc_cactus(ax[1, 1], info=logs_dict)
            # plot_sr(ax, info=logs_dict)
            # plot_time_metric_cactus(ax, info=logs_dict)

        if expr_type == 'LMAPF':
            # logs_dict['alg_names'] = [
            #     "L-LNS2-A*",
            #     "APF-L-LNS2-A*",
            #     "L-LNS2-SIPPS",
            #     "APF-L-LNS2-SIPPS",
            #     "L-PIBT",
            #     "L-PrP-A*",
            #     "APF-L-PrP-A*",
            #     "L-PrP-SIPPS",
            #     "APF-L-PrP-SIPPS",
            #     # "APF-L-PIBT",
            #     "L-LaCAM",
            #     'L-LaCAM*'
            # ]
            fig, ax = plt.subplots(1, 1, figsize=(8, 8))

            plot_throughput(ax, info=logs_dict)

        plt.tight_layout()
        plt.show()


def main():

    file_dir = 'MAPF_2024-09-04--19-12_ALGS-6_RUNS-3_MAP-maze-32-32-2.json'

    # LMAPF
    # file_dir = ''

    # MAPF
    # file_dir = ''

    # parameters
    # file_dir = ''

    show_results(file_dir=f'logs_for_experiments/{file_dir}')
    # show_results(file_dir=f'final_logs/{file_dir}')


if __name__ == '__main__':
    main()
