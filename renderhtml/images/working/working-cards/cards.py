import os
import subprocess


def crop_svg(path):
    filenames = os.listdir(path)
    for name in filenames:
        subprocess.call(['inkscape', '--verb=FitCanvasToDrawing',
                        '--verb=FileSave', '--verb=FileClose',
                        path + name])
        print path + name

def crop_all(paths):
    for path in paths:
        crop_svg(path)

def resize(path, to_path, width):
    filenames = os.listdir(path)
    for name in filenames:
        new_name = name.split('.')
        new_name = new_name[0] + '-' + str(width) + '.png'
        resize_arg = '%sx' % (width)
        print 'Creating %s' % (new_name)
        subprocess.call(['convert', '-background', 'none',
                         path + name, path + new_name])
        subprocess.call(['convert', path + new_name, '-resize',
                         resize_arg, path + new_name])
        subprocess.call(['mv', path + new_name, to_path + new_name])

        
def resize_all(paths, to_path, width):
    for path in paths:
        resize(path, to_path, width)

# widths: 70px and 150px
        
# paths = ['./Clubs/', './Diamonds/', './Hearts/', './Spades/']
paths = ['./backs/']
# move_all(paths, './cards/')
# resize_all(['./tmp/'], './tmp2/', 150)
# crop_all(paths)
resize_all(paths, './cards/', 150)
