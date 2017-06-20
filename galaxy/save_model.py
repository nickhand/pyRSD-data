from pyRSD.rsd import GalaxySpectrum

config = {}
config['Pdv_model_type'] = 'jennings'
config['correct_mu2'] = False
config['correct_mu4'] = False
config['params'] = {'H0': 69.0, 'Ob0': 0.04620, 'Om0': 0.292, 'n_s': 0.965, 'sigma8': 0.82, 'flat':True}
config['fog_model'] = 'modified_lorentzian'
config['include_2loop'] = False
config['interpolate'] = True
config['max_mu'] = 4
config['transfer_fit'] = 'CLASS'
config['use_P00_model'] = True
config['use_P01_model'] = True
config['use_P11_model'] = True
config['use_Pdv_model'] = True
config['use_Phm_model'] = True
config['use_mean_bias'] = False
config['use_so_correction'] = False
config['use_tidal_bias'] = False
config['use_vlah_biasing'] = True
config['vel_disp_from_sims'] = False
config['z'] = 0.55

model = GalaxySpectrum(**config)
model.initialize()
model.to_npy('model.npy')
