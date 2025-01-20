use pyo3::prelude::*;
use dim_rs::prelude::*;
use image::DynamicImage;

#[pyclass(eq, eq_int)]
#[derive(PartialEq)]
pub enum DimDataType {
    Text,
    Image,
    Audio,
    Video
}

#[pyclass]
pub struct DimVector {
    vector: Vec<f32>,
    data_type: DimDataType,
    string: Option<String>,
    image: Option<DynamicImage>,
}

#[pymethods]
impl DimVector {
    #[new]
    #[pyo3(signature = (string_data=None, image_data=None))]
    pub fn new(string_data: Option<String>, image_data: Option<Vec<u8>>) -> Self {
        let data_type: DimDataType = if string_data.is_some() {
            DimDataType::Text
        } else if image_data.is_some() {
            DimDataType::Image
        } else {
            panic!("Data type not supported")
        };
        
        if let DimDataType::Text = data_type {
            return Self {
                vector: Vec::new(),
                data_type,
                string: string_data,
                image: None,
            }
        }
        
        if let DimDataType::Image = data_type {
            return Self {
                vector: Vec::new(),
                data_type,
                string: None,
                image: image_data.map(|data| image::load_from_memory(&data).unwrap()),
            }
        }
        
        panic!("Data type not supported")
    }
}

impl Into<Vector<String>> for DimVector {
    fn into(self) -> Vector<String> {
        match self.data_type {
            DimDataType::Text => Vector::from_text(self.string.unwrap()),
            _ => panic!("Data type not supported")
        }
    }
}

impl Into<Vector<DynamicImage>> for DimVector {
    fn into(self) -> Vector<DynamicImage> {
        match self.data_type {
            DimDataType::Image => Vector::from_image(self.image.unwrap()),
            _ => panic!("Data type not supported")
        }
    }
}