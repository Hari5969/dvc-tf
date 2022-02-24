from distutils.file_util import copy_file
from threading import local
from src.utils.all_utils import read_yaml,create_directory
import argparse
import pandas as pd
import os
from tqdm import tqdm


def copy_file(source_download_dir, local_data_dir):
    list_of_files = os.listdir(source_download_dir)
    N = len(list_of_files)

    for file in list_of_files:
        src = os.path.join(source_download_dir,file)
        dest = os.path.join(local_data_dir,file)
        shutil.copy(src,dest)


def get_data(confg_path):
    config = read_yaml(config_path)

    remote_data_path = config["data_source"]
    df = pd.read_csv(remote_data_path, sep = ';')

    artifacts_dir = config["artifacts"]['artifacts_dir']
    raw_local_dir = config['artifacts']['raw_local_dir']
    raw_local_file = config["artifacts"]['raw_local_file']

    raw_local_dir_path = os.path.join(artifacts_dir,raw_local_dir)

    create_directory(dirs = [raw_local_dir_path])

    raw_local_file_path = os.path.join(raw_local_dir_path,raw_local_file)


def get_data(config_path):
    config = read_yaml(config_path)

    source_download_dirs = config["source_download_dirs"]
    local_data_dirs  = config["local_data_dirs"]

    for source_download_dir,local_data_dir in zip(source_download_dirs,local_data_dirs):
        create_directory(["local_data_dir"])
        copy_file(source_download_dir,local_data_dir)

if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config" , "-c", default = "config/config.yaml")

    parsed_args = args.parse_args()

    get_data(config_path = parsed_args.config)

