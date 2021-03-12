from PIL import Image, ImageDraw
import numpy
import random
import time
import os, sys

random.seed(time.time())

#qua ci sara' la funzione di max
from PIL import Image
import os
import numpy as np

class LetterImage:
    def __init__(self, path, image_name, height, color):
        self.path = path
        self.image_name = image_name
        image = Image.open(path + "/" + image_name)
        new_width = height * image.width / image.height
        image = image.resize((int(new_width), int(height)), Image.ANTIALIAS)
        self.image = image
        self.height = image.height
        self.width = image.width
        self.color = color

    def get_image(self):
        return {
            "image_name": self.image_name,
            "image_height": self.height,
            "image_width": self.width,
            "image": self.image
        }

    def change_color(self):
        image=Image.new("RGBA", (20, 20))
        print(np.asarray(image))
        arr = np.logical_not(np.asarray(self.image))
        new_arr = np.zeros((self.height, self.width, 4), dtype=np.uint8)
        for i in range(4):
            temp_arr = np.zeros((self.height, self.width), dtype=np.uint8)
            temp_arr.fill(self.color[i])
            temp_arr = temp_arr*arr
            new_arr[:,:,i] = temp_arr
        print(new_arr)
        image=Image.fromarray(new_arr).convert("RGBA")
        return image



folder_path = "/Users/matteo/Desktop/letters/data/rubbiani/1"
all_images = os.listdir(folder_path)
images_array = []
for image in all_images:
    real_image = LetterImage(folder_path, image, 45, (128, 128, 0, 200))
    images_array.append(real_image)
    real_image.change_color().resize((200, 200)).show()
    break
def remove_background(img):
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] > 253 and item[1] > 253 and item[2] > 253:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    return img


def resize_and_remove_background_all():
    path = "/Users/Matteo/PycharmProjects/handwrite/styles/"
    dirs = os.listdir(path)
    print(dirs)

    def resize():
        for item in dirs:
            try:
                im = Image.open(path + item)
            except:
                pass
            f, e = os.path.splitext(path + item)
            # imResize = im.resize((28, 28), Image.ANTIALIAS)
            imResize = color_letters(im, (255, 255, 255), )
            imResize = remove_background(imResize)

            imResize.save("styles/" + str(item), "png")

    resize()


def color_letters(im, letter_color):
    im = im.convert('RGBA')
    data = numpy.array(im)  # "data" is a height x width x 4 numpy array
    red, green, blue, alpha = data.T  # Temporarily unpack the bands for readability
    black_areas = (red < 2) & (blue < 2) & (green < 2)
    data[..., :-1][black_areas.T] = letter_color
    imResize = Image.fromarray(data)
    imResize = remove_background(imResize)
    return imResize


def prepare_string(string):
    for i in range(len(string)):
        number_of_spaces_in_a_row = 0
        if string[i] == " ":
            number_of_spaces_in_a_row = number_of_spaces_in_a_row + 1
        else:
            if number_of_spaces_in_a_row > 1:
                for k in range(i - number_of_spaces_in_a_row, i - 2):
                    string[i] = ""
                string[i - 1] = "£"
                number_of_spaces_in_a_row = 0

    return string


class Sheet:

    def __init__(self, type, line_color, line_thickness, background_color, size, has_holes, letter_color, text):
        self.type = type  # 0 for blank, 1 for lines, 2 for squares
        self.line_color = line_color
        self.line_thickness = line_thickness
        self.background_color = background_color
        self.width = size[0]
        self.height = size[1]
        self.has_holes = has_holes
        self.letter_color = letter_color
        self.images = []
        self.line_distance = 80
        self.square_dimension = 40
        self.letter_dimension = 30
        self.text = text
        self.margin = 4
        self.distance_between_letters = self.letter_dimension // 4
        self.squares_to_be_left_between_lines = 1
        self.current_image = None
        self.down_margin = 200
        self.letter_folder = "/Users/matteo/Desktop/letters/data/rubbiani/1"


    def create_image(self):
        if self.type == 0:
            paper_image = Image.new('RGB', (self.width, self.height), color=self.background_color)
        elif self.type == 1:
            paper_image = Image.new('RGB', (2050, 2950), color=self.background_color)
            line_image = Image.new('RGB', (2050, self.line_thickness), color=self.line_color)
            starting_line = 310
            space_between_lines = 80
            for i in range(0, 31):
                current_position = starting_line + (i * space_between_lines)
                paper_image.paste(line_image, (0, current_position))
        elif self.type == 2:
            paper_image = Image.new('RGB', (2050, 2950), color=self.background_color)
            line_image = Image.new('RGB', (2050, self.line_thickness), color=self.line_color)
            vertical_line_image = Image.new('RGB', (self.line_thickness, 2950), color=self.line_color)
            starting_line = 10
            vertical_starting_line = 20
            space_between_lines = self.square_dimension
            # create orizontal lines
            for i in range(100):
                current_position = starting_line + (i * space_between_lines)
                if current_position > 2950:
                    break
                paper_image.paste(line_image, (0, current_position))
            # create vertical lines
            for i in range(100):
                current_position = vertical_starting_line + (i * space_between_lines)
                if current_position > 2050:
                    break
                paper_image.paste(vertical_line_image, (current_position, 0))
        self.images.append(paper_image)
        self.current_image = paper_image
        if self.has_holes:
            self.add_holes()

    def add_holes(self):
        first_y = 280
        x = 60
        distance_between_holes = 800
        draw = ImageDraw.Draw(self.images[-1])
        r = 30
        for i in range(4):
            y = first_y + (i * distance_between_holes)
            draw.ellipse((x - r, y - r, x + r, y + r), fill=(255, 255, 255, 255), outline=(0, 0, 0, 0))

    def write(self):

        self.create_image()
        if self.type == 0:
            edge = 0
            starting_y_point = 100
            space_between_lines = int(self.letter_dimension * 1.5)
            max_number_of_rows = (self.height - (starting_y_point)) // (space_between_lines + self.letter_dimension)
        elif self.type == 1:
            starting_y_point = 228 - self.letter_dimension
            space_between_lines = 80
            #se non ci sono i buchi non fare...
            edge = 130
            max_number_of_rows = (self.images[0] - starting_y_point) // (space_between_lines + self.letter_dimension)
        elif self.type == 2:
            starting_y_point = 10 + 3 * self.square_dimension - self.letter_dimension
            space_between_lines = self.square_dimension * (self.squares_to_be_left_between_lines + 1)
            edge = 130
            max_number_of_rows = (self.images[0].height - starting_y_point - self.down_margin) // (
                space_between_lines)  # +self.letter_dimension)

        string = self.text
        counter = -1
        row = 0

        try:
            x_ratio = (self.images[0].width - edge) // (self.letter_dimension - self.distance_between_letters)
        except:
            print("can't make letters completely overlap")
            return 0
        a = 0
        while a < len(string):
            paper_image = self.images[-1]
            if row > max_number_of_rows:
                row = 0
                self.create_image()

                continue
            counter = (counter + 1) % x_ratio
            if False:  # string[a] == "£":
                row = row + 1
                counter = -1
            else:
                try:
                    try:
                        name = self.letter_folder + "/" + string[a] + ".png"
                        print(string[a])
                        im = Image.open(name)
                    except:
                        name = "letters2/" + string[a] + ".jpeg"
                        im = Image.open(name)
                except:
                    name = "letters2/.jpeg"
                    im = Image.open(name)
                height = self.letter_dimension * im.height
                new_width = int(im.width * self.letter_dimension / im.height)

                raw_im = im.resize((new_width, self.letter_dimension), Image.ANTIALIAS)
                blank_image = Image.new("RGBA", (self.letter_dimension, self.letter_dimension), (255, 255, 255, 255))

                blank_image.paste(raw_im, (0, 0), raw_im)
                im = color_letters(im, self.letter_color)


                # predict if the word will fit
                if string[a] != " ":
                    letter_count = 0
                    for k in range(a, len(string)):
                        if string[k] != " ":
                            letter_count = letter_count + 1
                        else:
                            break
                    if letter_count * self.letter_dimension > paper_image.width - edge - (
                            counter * (-self.distance_between_letters + self.letter_dimension)):
                        counter = 0

                # decide to start a new line
                if counter == 0:
                    # so a line does not start with a blank space
                    if string[a] == " ":
                        counter = counter - 1
                        a = a + 1
                        continue
                    row = row + 1
                    a = a - 1
                    continue
                # paste image
                x = random.randint(-2, 2)
                y = random.randint(-2, 2)
                x_pos = edge + counter * (self.letter_dimension - self.distance_between_letters) + x
                y_pos = starting_y_point + row * space_between_lines + y
                # im = color_letters(im, background_color, letter_color)
                self.images[-1].paste(im, (x_pos, y_pos), im)
            a = a + 1


paper = Sheet(2, (0, 0, 0), 3, (255, 255, 255), (2050, 2950), True, (0, 0, 0), """CIAO COME STAI """)
paper.letter_color = (0, 0, 0)
paper.write()

for i in range(len(paper.images)):
    paper.images[i].show()
    paper.images[i].save("testo" + str(i) + ".png", "PNG")

resize_and_remove_background_all()
