mod vector;

use pyo3::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
fn dim_python(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<vector::DimVector>()?;
    m.add_class::<vector::DimDataType>()?;
    Ok(())
}
