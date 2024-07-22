import unittest
from PIL import Image
import src.main as ascii_art_tool

class TestASCIIArtTool(unittest.TestCase):

    def test_load_image(self):
        image = ascii_art_tool.load_image("test_image.png")
        self.assertIsInstance(image, Image.Image)

    def test_convert_to_grayscale(self):
        image = Image.new('RGB', (10, 10), color = 'white')
        grayscale_image = ascii_art_tool.convert_to_grayscale(image)
        self.assertEqual(grayscale_image.mode, 'L')

    def test_map_pixels_to_ascii(self):
        image = Image.new('L', (10, 10), color = 255)
        ascii_str = ascii_art_tool.map_pixels_to_ascii(image)
        self.assertIsInstance(ascii_str, str)
        self.assertGreater(len(ascii_str), 0)

    def test_generate_ascii_art(self):
        image = Image.new('RGB', (10, 10), color = 'white')
        ascii_art = ascii_art_tool.generate_ascii_art(image, new_width=10)
        self.assertIsInstance(ascii_art, str)
        self.assertGreater(len(ascii_art), 0)

if __name__ == '__main__':
    unittest.main()
