import re
from matplotlib.lines import Line2D
import os
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

def compute_and_save_2d_projections(fits_file, output_file=None, save_dir=None):
    """
    Computes 2D projections from a normalized 3D FITS datacube and saves them to a .npz file.

    Parameters:
        fits_file (str): Path to the 3D FITS file
        output_file (str, optional): File name for .npz file. If None, uses fits_file name.
        save_dir (str, optional): Directory to save the output file. Defaults to current directory.

    Returns:
        str: Path to the saved .npz file
    """

    # Ensure save_dir is a Path object and exists
    if save_dir is None:
        save_dir = Path.cwd()
    else:
        save_dir = Path(save_dir)
        save_dir.mkdir(parents=True, exist_ok=True)

    # Generate default output file name if not provided
    if output_file is None:
        base_name = os.path.splitext(os.path.basename(fits_file))[0]
        output_file = f"{base_name}_2D_projections.npz"

    output_path = save_dir / output_file

    # Load and normalize FITS data
    with fits.open(fits_file) as hdul:
        data = hdul[0].data
        header = hdul[0].header

        if data is None or len(data.shape) != 3:
            raise ValueError("Data is not a 3D datacube.")

        data_sum = np.sum(data)

        if data_sum == 0:
            raise ValueError("Cannot normalize; sum of all pixels is 0.")
        elif not np.isclose(data_sum, 1.0, atol=1e-6):
            data = data / data_sum
            print("Data cube normalized.")
        else:
            print("Cube is already normalized.")

    # Helper function to compute axis coordinates
    def get_axis_values(axis_num):
        crval = header.get(f'CRVAL{axis_num}', 0)
        crpix = header.get(f'CRPIX{axis_num}', 1)
        cdelt = header.get(f'CDELT{axis_num}', 1)
        naxis = header.get(f'NAXIS{axis_num}', data.shape[3-axis_num])
        return np.linspace(
            crval + (1-crpix)*cdelt,
            crval + (naxis-crpix)*cdelt,
            naxis
        )

    x_values = get_axis_values(1)
    y_values = get_axis_values(2)
    z_values = get_axis_values(3)

    # Collapse the data along each axis
    print(base_name)
    if base_name in ['LoreliB_PS1', 'EoR-PIE-MC_PS1', 'EoR-PIE_PS1', 'LoreliB_PS2', 'EoR-PIE-MC_PS2', 'EoR-PIE_PS2']:
        print(base_name)
        
        collapsed_z = np.sum(data, axis=0) #np.sum(data, axis=0)
        collapsed_y = np.sum(data, axis=1)
        collapsed_x = np.sum(data, axis=2)

    else:

        collapsed_z = np.sum(data, axis=2)
        collapsed_y = np.sum(data, axis=1)
        collapsed_x = np.sum(data, axis=0)

    # Axis labels
    axis_labels = {
        'x': header.get('AXIS1-FREQ', 'xHI (151-166 MHz)'),
        'y': header.get('AXIS2-FREQ', 'xHI (166-181 MHz)'),
        'z': header.get('AXIS3-FREQ', 'xHI (181-196 MHz)')
    }

    axis_labels = {
        k: re.sub(r'xHI (\d+-\d+ MHz)', r'$x_{\\mathrm{HI}}$ (\1)', v)
        for k, v in axis_labels.items()
    }

    # Save to .npz file
    np.savez(output_path,
             collapsed_x=collapsed_x,
             collapsed_y=collapsed_y,
             collapsed_z=collapsed_z,
             x_values=x_values,
             y_values=y_values,
             z_values=z_values,
             axis_labels=np.array([axis_labels['x'], axis_labels['y'], axis_labels['z']])
    )

    return str(output_path)

