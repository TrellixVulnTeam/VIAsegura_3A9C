from pathlib import Path
import boto3
import os
import sys

viasegura_path = Path(__file__).parent

class Downloader:
	def __init__(self, models_path = viasegura_path / 'models'):
		"""
		This class allows to download de models and other model data from the Inter-American Development Bank repositories
		
		Parameters
		----------

		models_path: str (default instalation path of package)
			The route where is going to download and check the artifacts of the models
		"""
		self.models_path = models_path
	
	def check_artifacts(self):
		"""
		This function allows to check if the path for downloads exists
		"""
		if not Path(self.models_path).is_dir():
			raise ImportError('The route for the models is not present, it means that the models are not downloaded on this environment, use viasegura.download_models function to download them propertly')
	
	def check_files(self, filePath):

		"""
		This function allows to chec if an specific file exists

		Parameters
		----------

		filePath: str
			Route of the file to be checked

		"""
		if Path(filePath).is_file():
			return True
		else:
			return False
	
	def download(self, aws_access_key=None, aws_secret_key=None):
		"""
		This function allows to dowload the corresponding packages using the route already on the created instance

		Parameters
		----------

		aws_access_key: str
			The aws access key id provided by the interamerican development bank to have access to the models

		aws_secret_key: str
			The aws access secret key provided by the interamerican development bank to have access to the models			


		"""
		if not aws_access_key or not aws_secret_key:
			raise NameError('Must provide valid aws_access_key and aws_secret_key values')
		if not Path(self.models_path).is_dir():
			Path(self.models_path).mkdir(parents=True, exist_ok=True)
		sess = boto3.Session(aws_access_key_id = aws_access_key,
							aws_secret_access_key = aws_secret_key,
							region_name = 'us-east-1')
		s3 = sess.resource('s3')
		s3_client = sess.client('s3')
		my_bucket = s3.Bucket('via-segura-artifacts')
		for my_bucket_object in my_bucket.objects.all():
			elements = my_bucket_object.key.split('/')
			if elements[-1]=="":
				(self.models_path / my_bucket_object.key).mkdir(parents=True, exist_ok=True)
			else:
				my_file = self.models_path / Path(my_bucket_object.key)
				if not self.check_files(self.models_path / Path(my_bucket_object.key)):
					with open(self.models_path / Path(my_bucket_object.key), 'wb') as f:
						s3_client.download_fileobj('via-segura-artifacts', my_bucket_object.key, f)
					
		print('Elements Downloaded')