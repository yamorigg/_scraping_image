import time

def pngsaver(name, png):
    with open('../imgs/{}{}.png'.format(name, time.time()), 'wb') as f:
        f.write(png)