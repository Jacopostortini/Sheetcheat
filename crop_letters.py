#coding=utf8
from PIL import Image, ImageFilter
import numpy
import pathlib
from remove_shadows import remove_shadows
characters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z À È Ì Ò Ù 0 1 2 3 4 5 6 7 8 9 punto virgola puntoevirgola duepunti puntoesclamativo puntointerrogativo trattinobasso meno più asterisco barra uguale apice apostrofo minore maggiore apertatonda chiusatonda apertquadra chiusaquadra apertagraffa chiusagraffa sterlina dollaro percentuale ecommerciale chiocciola cancelletto grado".split(" ")

#def crop_rgb_image(filename):
#    paper = Image.open(filename)
#    paper = paper.convert("RGB")
#    paper_arr = numpy.asarray(paper).copy()
#    vertical_lines = []
#    horizontal_lines = []
#    starting_point = 200
#    moduled_arr = paper_arr/255
#    print(paper.width, paper.height)
#
#    #Rendo davvero bianco ciò che è bianco
#    for w in range(paper.width):
#        for h in range(paper.height):
#            if moduled_arr[h][w][0]+moduled_arr[h][w][1]+moduled_arr[h][w][2]>2.4:
#                paper_arr[h][w] = [255,255,255]
#    Image.fromarray(paper_arr).show()
#    for width in range(paper.width):
#        if paper_arr[starting_point][width][0]<230 and paper_arr[starting_point][width][2]>200 and (len(vertical_lines)==0 or vertical_lines[-1]<width-5):
#            vertical_lines.append(width)
#    for height in range(paper.height):
#        if paper_arr[height][starting_point][0]>200 and paper_arr[height][starting_point][2]<200 and (len(horizontal_lines)==0 or horizontal_lines[-1]<height-5):
#            horizontal_lines.append(height)
#    print(vertical_lines, horizontal_lines)
#    counter = 0
#    for h in range(len(horizontal_lines)-1):
#        for v in range(len(vertical_lines)-1):
#            if counter<len(characters):
#                paper.crop((vertical_lines[v], horizontal_lines[h], vertical_lines[v+1], horizontal_lines[h+1])).save("cropped_letters/"+characters[counter]+".png")
#            else:
#                break
#            counter+=1

def black_and_white_image(im):
    im = im.convert('L')

    arr = numpy.asarray(im)
    arr = arr - arr.mean() *0.9 + 128

    return Image.fromarray(arr).convert('1', dither=Image.NONE)

def clean_image(im):
    im = im.convert('L').filter(ImageFilter.BoxBlur(1)).convert('1', dither=Image.NONE)
    return im

def crop_borders(im, border):
    return im.crop((border, border, im.width-border, im.height-border))

def crop_grey_scale_image(filename, ext):
    paper = Image.open(filename+ext)
    paper = paper.convert("L")
    paper = Image.fromarray(remove_shadows(remove_shadows(paper)))
    vertical_lines = []
    horizontal_lines = []

    paper = black_and_white_image(paper)

    paper_arr = numpy.asarray(paper).copy()
    starting_point = 0
    while len(vertical_lines) != 9:
        vertical_lines = []
        for width in range(paper.width):
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
    for h in range(1, len(horizontal_lines)-1, 2):
        for v in range(len(vertical_lines)-1):
            if counter<len(characters):
                #pathlib.Path(filename).mkdir(parents=True, exist_ok=True)
                letter  = paper.crop((vertical_lines[v], horizontal_lines[h], vertical_lines[v+1], horizontal_lines[h+1]))
                letter = clean_image(letter)
                letter = crop_borders(letter, 10)
                letter.save(filename+"/"+characters[counter]+".png")
            else:
                break
            counter+=1

crop_grey_scale_image("foto_jacobsen", ".jpeg")
