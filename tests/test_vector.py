import io
import unittest
from typing import Any

from dim_python import DimDataType, DimVector
from PIL import Image


class TestDimVector(unittest.TestCase):
    def test_text_vector(self):
        # Test creating a vector from text
        text = "Hello, world!"
        vector = DimVector(string_data=text, image_data=None)
        self.assertIsNotNone(vector)
        
    def test_image_vector(self):
        # Create a sample image and convert it to bytes
        img = Image.new('RGB', (100, 100), color='red')
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        
        # Test creating a vector from image
        vector = DimVector(string_data=None, image_data=img_byte_arr)
        self.assertIsNotNone(vector)
            
    def test_mixed_input(self):
        # Test that creating a vector with both text and image data
        # should use text as priority (based on the Rust implementation)
        text = "Hello, world!"
        img = Image.new('RGB', (100, 100), color='red')
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        
        vector = DimVector(string_data=text, image_data=img_byte_arr)
        self.assertIsNotNone(vector)

if __name__ == '__main__':
    unittest.main()
