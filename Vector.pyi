from typing import Optional
from enum import Enum

class DimDataType(Enum):
    """
    Enumeration of supported data types for vector embeddings.
    
    Attributes:
        Text: Text/string data type
        Image: Image data type
        Audio: Audio data type
        Video: Video data type
    """
    Text = ...
    Image = ...
    Audio = ...
    Video = ...

class DimVector:
    """
    A vector class that can hold different types of data (text or image) and their embeddings.
    
    The vector can be initialized with either text data or image data, but not both.
    The corresponding data type will be automatically determined based on the input.
    """
    
    def __init__(self, string_data: Optional[str] = None, image_data: Optional[bytes] = None) -> None:
        """
        Initialize a DimVector with either text or image data.
        
        Args:
            string_data: Optional string input for text-based vectors
            image_data: Optional bytes input for image-based vectors
            
        Raises:
            Exception: If neither string_data nor image_data is provided, or if both are provided
        """
        ...