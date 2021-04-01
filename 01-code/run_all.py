import papermill as pm
from os.path import abspath, dirname, join

pm.execute_notebook(
   abspath(join(dirname(__file__), '00-derive-simulation-distributions.ipynb')),
   abspath(join(dirname(__file__), '../02-output/00-derive-simulation-distributions-output.ipynb')),
   parameters=dict(data_dir=abspath(join(dirname(__file__), 'intermediate_data')))
)

pm.execute_notebook(
   abspath(join(dirname(__file__), '01-compare-analytic-and-empirical-null-distributions.ipynb')),
   abspath(join(dirname(__file__), '01-compare-analytic-and-empirical-null-distributions-output.ipynb')),
   parameters=dict(
       DATA_DIR=abspath(join(dirname(__file__), 'intermediate_data')),
       DSET_FILE=abspath(join(dirname(__file__), 'intermediate_data', 'test_dsets.pkl')),
       OVERWRITE_DSETS=True,
       N_DSET=3,
       N_JOBS=4)
)