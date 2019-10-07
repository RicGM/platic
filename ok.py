from PIL import Image

if __name__ == '__main__':
    im = Image.open('IMG_6091.jpg')

    width, height = im.size

    for y in range(height):
        total_r = 0
        total_g = 0
        total_b = 0
        total = 0

        for x in range(width):
            r, g, b = im.getpixel((x, y))

            if not (133 < r < 173 and 176 < g < 216 and 96 < b < 156):
                total_r = total_r + r
                total_g = total_g + g
                total_b = total_b + b

                total += 1

        avg_r = total_r / total
        avg_g = total_g / total
        avg_b = total_b / total

        print(avg_r,avg_g,avg_b)




    # im.show()
