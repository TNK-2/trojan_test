# save_file.py
def run(**args):
  with open('test.txt', 'r') as f:
      results = f.read()

  return results