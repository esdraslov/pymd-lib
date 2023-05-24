import os as software


def make_folder(folder_name: str):
  software.system(f'mkdir "{folder_name}"')

def make_file(file_name: str, file_extension: str):
  software.system(f'echo > "{file_name}.{file_extension}"')

def delete_file(file_complete_name: str):
  software.system(f'erase "{file_complete_name}"')

def delete_folder(folder_name: str):
  software.system(f'rmdir "{folder_name}"')

def read_file(file_name: str):
  return open(file_name)

def write_file(file_name: str, value):
  software.system(f'echo "{value}" >> "{file_name}"')

class commander:
  def __init__(self, cmder_name):
    self.cmder_name = cmder_name

  def setup(self, command):
    software.system(command)