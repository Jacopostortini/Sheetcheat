#coding=utf8
from PIL import Image, ImageFilter
import numpy
#from remove_shadows import remove_shadows
import os
from os import listdir
from os.path import isfile, join
characters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z À È Ì Ò Ù 0 1 2 3 4 5 6 7 8 9 punto virgola puntoevirgola duepunti puntoesclamativo puntointerrogativo trattinobasso meno più asterisco barra uguale apice apostrofo minore maggiore apertatonda chiusatonda apertquadra chiusaquadra apertagraffa chiusagraffa sterlina dollaro percentuale ecommerciale chiocciola cancelletto grado".split(" ")

def black_and_white_image(im):
    arr = numpy.asarray(im)
    arr = arr - arr.mean() *0.9 + 128

    return Image.fromarray(arr).convert('1', dither=Image.NONE)

def clean_image(im):
    im = im.convert('L').filter(ImageFilter.BoxBlur(1)).convert('1', dither=Image.NONE)
    return im

def find_left(im):
    im_arr=numpy.array(im)
    for w in range(im.width):
        for h in range(im.height):
            if im_arr[h][w]==0:
                return w
    return None

def find_right(im):
    im_arr=numpy.array(im)
    for w in range(im.width-1, -1, -1):
        for h in range(im.height):
            if im_arr[h][w]==0:
                return w
    return None
def find_top(im):
    im_arr=numpy.array(im)
    for h in range(im.height):
        for w in range(im.width):
            if im_arr[h][w]==0:
                return h
    return None

def find_bottom(im):
    im_arr=numpy.array(im)
    for h in range(im.height-1, -1, -1):
        for w in range(im.width):
            if im_arr[h][w]==0:
                return h
    return None

def crop_grey_scale_image(file):
    filename, extension = file.split(".")[0], file.split(".")[1]
    path=os.path.splitext("raw_images/")[0]
    paper = Image.open(path+filename+"."+extension)

    paper = paper.convert("L")
    paper_arr = numpy.array(paper)
    paper = black_and_white_image(paper_arr)
    paper_arr = numpy.array(paper)

    #paper_arr = remove_shadows(paper_arr)

    vertical_lines = []
    horizontal_lines = []

    starting_point = 0
    while len(vertical_lines) != 9:
        vertical_lines = []
        for width in range(paper.width-1):
            if paper_arr[starting_point][width] == 0 and (len(vertical_lines)==0 or vertical_lines[-1]<width-20):
                vertical_lines.append(width)
        starting_point += 1

    starting_point = 0
    while len(horizontal_lines) != 23:
        horizontal_lines = []
        for height in range(paper.height):
            if paper_arr[height][starting_point] == 0 and (len(horizontal_lines)==0 or horizontal_lines[-1]<height-20):
                horizontal_lines.append(height)
        starting_point += 1
    counter = 0


    dirName = 'data/'+filename

    os.mkdir(dirName)
    dirName = 'data/'+filename+"/1"
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")
    paper.save(dirName+".png")
    for h in range(1, len(horizontal_lines)-1, 2):
        for v in range(len(vertical_lines)-1):
            if counter<len(characters):
                letter  = paper.crop((vertical_lines[v], horizontal_lines[h], vertical_lines[v+1], horizontal_lines[h+1]))
                letter = clean_image(letter)
                letter =letter.crop((20, 20, letter.width-20, letter.height-15))
                letter = letter.crop((find_left(letter), find_top(letter), find_right(letter), find_bottom(letter)))
                letter.save(dirName+"/"+characters[counter]+".png")
            else:
                break
            counter+=1

def crop_all():
    images=os.listdir("raw_images")

    onlyfiles = [f for f in listdir("raw_images") if isfile(join("raw_images", f))]

    for i in onlyfiles:




        #image = image.crop((0, 70, image.width, image.height-60))
        try:
            image=Image.open("raw_images/"+i)
            crop_grey_scale_image(i)
        except:
            pass





crop_all()
#crop_grey_scale_image("foto_jacobsen", ".jpeg")
