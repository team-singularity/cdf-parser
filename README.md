# CDF Python Test Parser

## Requirements

* CDF Software Distribution
  * [Windows](https://spdf.gsfc.nasa.gov/pub/software/cdf/dist/cdf38_1/windows/cdf3.8.1_64bit_MS_Installer.msi)
  * [MacOS](https://spdf.gsfc.nasa.gov/pub/software/cdf/dist/cdf38_1/macosx/CDF3_8_1-binary_signed.pkg)

## Usage

1. Download specific CDF from Parker Solar Probe harvard website [here](http://sweap.cfa.harvard.edu/pub/data/sci/sweap/spc/).
2. Copy file to root directory of this project.
3. Install dependencies.
    ```bash
    pip install -r requirements.txt
    ```
4. Set environment variable `CDF_BASE` to the directory of the CDF installation.

    Linux/MacOS:
    ```bash
    export CDF_BASE=/path/to/cdf38_1-dist
    ```
   
    Windows:
    ```bash
    set CDF_BASE=F:\Programming\singularity\cdf38_1-dist
    ```
   Intellij Idea users can set this in the run configuration.
5. Run Flask server.
    ```bash
    python app.py
   ```
6. Navigate to `localhost:5000` in your browser. There is one available endpoint: `/data`.
   
## Useful Links

* [Sweap Data User Guide](http://sweap.cfa.harvard.edu/sweap_data_user_guide.pdf)