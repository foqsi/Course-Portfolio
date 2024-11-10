from images import Image

def grayscale(image):
    """Converts an image to grayscale."""
    width = image.getWidth()
    height = image.getHeight()
    for x in range(width):
        for y in range(height):
            (red, green, blue) = image.getPixel(x, y)
            gray = int(0.3 * red + 0.59 * green + 0.11 * blue)
            image.setPixel(x, y, (gray, gray, gray))
    return image

def sepia(image):
    image = grayscale(image)
    width = image.getWidth()
    height = image.getHeight()
    for x in range(width):
        for y in range(height):
            (red, green, blue) = image.getPixel(x, y)
            if red < 63:
                red = int(red * 1.1)
                blue = int(blue * 0.9)
            elif red < 192:
                red = int(red * 1.15)
                blue = int(blue * 0.85)
            else:
                red = min(int(red * 1.08), 255)
                blue = int(blue * 0.93)
            image.setPixel(x, y, (red, green, blue))
    return image

if __name__ == "__main__":
    image = Image("smokey.gif")
    
    sepia_image = sepia(image)
    
    sepia_image.draw()
    
    sepia_image.save("smokey_sepia.gif")
