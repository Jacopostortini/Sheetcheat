from PIL import Image, ImageDraw, ImageFont
import numpy

characters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z À È Ì Ò Ù 0 1 2 3 4 5 6 7 8 9 . , ; : ! ? _ - + * / = ^ ' < > ( ) [ ] { } £ $ % & @ # °".split(" ")
paper_width = 2100
paper_height = 2970
margin = 100
symbol_line_height = 75
horizontal_line_color = [0, 0, 0]
vertical_line_color = [0, 0, 0]
symbol_line_color = [0, 0, 0]
squares_in_height = 11
squares_in_width = 8
line_width = 8
squares_width = (paper_width-2*margin)/squares_in_width
squares_height = (paper_height-2*margin)/squares_in_height

paper = Image.new("RGB", (paper_width, paper_height), (255,255,255))
paper_arr = numpy.asarray(paper).copy()
for width in range(paper.width):
    for i in range(line_width):
        paper_arr[margin+i][width] = horizontal_line_color
for height in range(paper.height):
    for i in range(line_width):
        paper_arr[height][margin+i] = vertical_line_color

for height in range(margin, paper.height-margin, int(squares_height)):
    for width in range(paper.width):
        for i in range(line_width):
            paper_arr[height+i][width] = horizontal_line_color
        if(height>=margin and height<paper.height-margin-100):
            for i in range(line_width):
                paper_arr[height+symbol_line_height+i][width] = symbol_line_color
for height in range(paper.height):
    for width in range(margin, paper.width-margin, int(squares_width)):
        for i in range(line_width):
            paper_arr[height][width+i] = vertical_line_color
        

paper = Image.fromarray(paper_arr)
paper.save("griglia.png")
counter = 0
for height in range(margin+5, paper.height-margin, int(squares_height)):
    for width in range(int(margin+squares_width/2), int(paper.width-margin-squares_width/2+1), int(squares_width)):
        if height>=margin and height<paper.height-margin-100 and counter<len(characters):
            paper_arr[height+symbol_line_height][width] = symbol_line_color
            fnt = ImageFont.truetype('arial.ttf', symbol_line_height-15)
            d = ImageDraw.Draw(paper)
            d.text((width, height), characters[counter], font=fnt, fill=(0,0,0))
            counter+=1

paper.show()
paper.save("scheda.png")
