import argparse

class HParams(object):
	def __init__(self):
		# Dataset Settings
		self.dataset_path = './data/gtzan'
		self.feature_path = './data/feature'
		self.genres = ['classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae']

		# Feature Parameters
		self.sample_rate = 22050
		self.fft_size = 1024
		self.win_size = 1024
		self.hop_size = 512
		self.num_mels = 128
		self.feature_length = 1024  # audio length = feature_length*hop_size/sample_rate (s)

		# Training Parameters
		self.device = 0  # 0: CPU, 1: GPU0, 2: GPU1, ...
		self.batch_size = 4
		self.num_epochs = 10
		self.learning_rate = 1e-2

	# Function for parsing argument and set hyper parameters
	def parse_argument(self, print_argument=True):
		parser = argparse.ArgumentParser()
		for var in vars(self):
			value = getattr(hparams, var)
			argument = '--' + var
			parser.add_argument(argument, type=type(value), default=value)

		args = parser.parse_args()
		for var in vars(self):
			setattr(hparams, var, getattr(args, var))

		if print_argument:
			print('-------------------------')
			print('Hyper Parameter Settings')
			print('-------------------------')
			for var in vars(self):
				value = getattr(hparams, var)
				print(var + ': ' + str(value))
			print('-------------------------')

hparams = HParams()
hparams.parse_argument()
