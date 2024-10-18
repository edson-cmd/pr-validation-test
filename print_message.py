import os 

with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
    print('message=Hello, world!', file=fh)