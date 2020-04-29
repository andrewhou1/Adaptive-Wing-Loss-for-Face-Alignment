"""
TRAIN LAUNCHER 

"""

import configparser
from inference import HourglassModel
from datagen import DataGenerator

def process_config(conf_file):
	"""
	"""
	params = {}
	config = configparser.ConfigParser()
	config.read(conf_file)
	for section in config.sections():
		if section == 'DataSetHG':
			for option in config.options(section):
				params[option] = eval(config.get(section, option))
		if section == 'Network':
			for option in config.options(section):
				params[option] = eval(config.get(section, option))
	return params


if __name__ == '__main__':
	print('--Parsing Config File')
	params = process_config('config_test.cfg')
	
	'''print('--Creating Dataset')
	dataset = DataGenerator(params['joint_list'], params['img_directory'], params['training_txt_file'], remove_joints=params['remove_joints'])
	dataset._create_train_table()
	dataset._randomize()
	dataset._create_sets()'''
	
	model = HourglassModel(nFeat=params['nfeats'], nStack=params['nstacks'], nModules=params['nmodules'], nLow=params['nlow'], outputDim=params['num_landmarks'], batch_size=params['batch_size'], attention = params['mcam'],training=False, drop_rate= params['dropout_rate'], name=params['name'], tiny= params['tiny'], modif=False)
	model.generate_model()
	model.restore('adaptive_wing_loss_checkpoint/hg_refined_200_38')
	model.testing_init()
	
