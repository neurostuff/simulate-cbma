def _create_dsets(n_dsets, **kwargs):
    partial_ccd = partial(create_coordinate_dataset, **kwargs)
    # just return the dset output since there are no signal foci
    return [
        dset for foci, dset in Parallel(n_jobs=N_JOBS)(delayed(partial_ccd)(**{'seed': seed})
        for seed in range(n_dsets))
    ]


def parameterize_dsets(n_foci, n_participants, n_studies):
    if OVERWRITE_DSETS or not os.path.isfile(DSET_FILE):
        dset_params = product(peaks_per_exp_low_high, part_per_exp_low_high, num_of_exp_low_high)
        dset_dict = {}
        for foci, participants, studies in dset_params:
            key = f"foci-{foci}_participants-{participants}_studies-{studies}"
            dset_dict[key] = create_dsets(N_DSET, foci=0, n_noise_foci=foci, sample_size=participants, n_studies=studies)
        with open(DSET_FILE, "wb") as pkl_file:
            pickle.dump(dset_dict, pkl_file)
    else:
        with open(DSET_FILE, "rb") as pkl_file:
            dset_dict = pickle.load(pkl_file)