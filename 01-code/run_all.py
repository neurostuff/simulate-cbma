import papermill as pm
from os.path import abspath, dirname, join


def run_notebooks(note0_params, note1_params):
    pm.execute_notebook(
        abspath(join(dirname(__file__), '00-derive-simulation-distributions.ipynb')),
        abspath(join(dirname(__file__), '../02-output/00-derive-simulation-distributions-output.ipynb')),
        parameters=note0_params
    )

    pm.execute_notebook(
        abspath(join(dirname(__file__), '01-compare-analytic-and-empirical-null-distributions.ipynb')),
        abspath(join(dirname(__file__), '../02-output/01-compare-analytic-and-empirical-null-distributions-output.ipynb')),
        parameters=note1_params
    )

if __name__ == "__main__":
    import sys
    run_type = sys.argv[1]
    print(run_type)
    note0_params = dict(
        data_dir=abspath(join(dirname(__file__), 'intermediate_data')),
        overwrite=False,
    )

    if run_type == "test":
        note1_params = {
            'DATA_DIR': abspath(join(dirname(__file__), 'intermediate_data')),
            'DSET_FILE': abspath(join(dirname(__file__), 'intermediate_data', 'test_dsets.pkl')),
            'OVERWRITE_DSETS': True,
            'N_DSET': 1,
            'N_ITERS': 2,
            'N_JOBS': None,
        }
    elif run_type == "small":
        n_jobs = sys.argv[2]
        note1_params = {
            'DATA_DIR': abspath(join(dirname(__file__), 'intermediate_data')),
            'DSET_FILE': abspath(join(dirname(__file__), 'intermediate_data', 'test_dsets.pkl')),
            'OVERWRITE_DSETS': True,
            'N_DSET': 100,
            'N_ITERS': 1000,
            'N_JOBS': n_jobs,
        }
    elif run_type == "large":
        n_jobs = sys.argv[2]
        note1_params = {
            'DATA_DIR': abspath(join(dirname(__file__), 'intermediate_data')),
            'DSET_FILE': abspath(join(dirname(__file__), 'intermediate_data', 'test_dsets.pkl')),
            'OVERWRITE_DSETS': True,
            'N_DSET': 100,
            'N_ITERS': 10000,
            'N_JOBS': n_jobs,
        }

    run_notebooks(note0_params, note1_params)