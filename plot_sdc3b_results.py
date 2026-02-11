import re
from matplotlib.lines import Line2D
import os
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def plot_from_saved_projections(npz_file, xhi_marks=(0.5, 0.5, 0.5), xhi_widths=(0.1, 0.1, 0.1), bins=100, contour_levels=(0.6827, 0.9545, 0.9973), save_dir=None, suffix=''):
    """
    Plots corner-style projections from a saved .npz file with crosses marking specific xHI values.

    Parameters:
        npz_file (str): Path to the .npz file containing the projections
        xhi_marks (tuple): Three xHI values to mark on x, y, z axes respectively
        bins (int): Number of bins for the 2D histograms (can be int or tuple)
        contour_levels (tuple): Confidence levels for 1, 2, 3 sigma (default: 68.27%, 95.45%, 99.73%)
        save_dir (str or Path): Directory to save the output plot
    """
    # Load the saved data
    data = np.load(npz_file)
    base_name = os.path.splitext(os.path.basename(npz_file))[0]
    if suffix == 'PS1':
        base_name = base_name.replace('_PS1_2D_projections', '')
        print(base_name)
    elif suffix == 'PS2':
        base_name = base_name.replace('_PS2_2D_projections', '')

    elif suffix == 'PS3':
        base_name = base_name.replace('_PS3_2D_projections', '')

    elif suffix == 'IM1':
        base_name = base_name.replace('_IM1_2D_projections', '')


    # Create a figure with three subplots
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    projections = [data['collapsed_x'],
                   data['collapsed_y'], data['collapsed_z']]
    coords = [
        (data['y_values'], data['z_values']),  # for x projection (y-z plane)
        (data['z_values'], data['x_values']),  # for y projection (z-x plane)
        (data['x_values'], data['y_values'])   # for z projection (x-y plane)
    ]
    labels = data['axis_labels']
    label_pairs = [
        (labels[1], labels[2]),  # y-z labels for x projection
        (labels[2], labels[0]),  # z-x labels for y projection
        (labels[0], labels[1])   # x-y labels for z projection
    ]
    titles = ['Collapsed along x', 'Collapsed along y', 'Collapsed along z']
    mark_coords = [
        (xhi_marks[1], xhi_marks[2]),  # y-z coordinates for x projection
        (xhi_marks[2], xhi_marks[0]),  # z-x coordinates for y projection
        (xhi_marks[0], xhi_marks[1])   # x-y coordinates for z projection
    ]

    rect_widths = [
        (xhi_widths[1], xhi_widths[2]),  # width in y-z
        (xhi_widths[2], xhi_widths[0]),  # width in z-x
        (xhi_widths[0], xhi_widths[1])   # width in x-y
    ]

    for i, (ax, proj, (x_coords, y_coords), (x_lab, y_lab), title, marks, rect) in enumerate(
        zip(axes, projections, coords, label_pairs,
            titles, mark_coords, rect_widths)
    ):
        X, Y = np.meshgrid(x_coords, y_coords)
        # Flatten for histogram
        values = proj if i != 1 else proj.T
        values = values.flatten()

        if base_name in ['LoreliB', 'EoR-PIE-MC', 'EoR-PIE']:
        #if base_name in ['LoreliB_PS1', 'EoR-PIE-MC_PS1', 'EoR-PIE_PS1', 'LoreliB_PS2', 'EoR-PIE-MC_PS2', 'EoR-PIE_PS2']:
            print(base_name)

            H, xedges, yedges = np.histogram2d(
                Y.flatten(), X.flatten(), bins=bins, weights=values, density=True)

        else:

            H, xedges, yedges = np.histogram2d(
                X.flatten(), Y.flatten(), bins=bins, weights=values, density=True)

        # Compute contour levels for 1, 2, 3 sigma
        H_flat = H.flatten()
        H_sorted = np.sort(H_flat)[::-1]
        cumsum = np.cumsum(H_sorted)
        cumsum /= cumsum[-1]
        contour_vals = []
        for cl in contour_levels:
            idx = np.searchsorted(cumsum, cl)
            contour_vals.append(H_sorted[idx])
        contour_vals = sorted(contour_vals)  # Ensure increasing order

        # Plot histogram

        if base_name in ['LoreliB_PS1', 'EoR-PIE-MC_PS1', 'EoR-PIE_PS1', 'LoreliB_PS2', 'EoR-PIE-MC_PS2', 'EoR-PIE_PS2']:
            print(base_name)

            im = ax.imshow(H, origin='lower', aspect='auto',
                           extent=[xedges[0], xedges[-1],
                                   yedges[0], yedges[-1]],
                           cmap='Greys')
            # Plot contours
            CS = ax.contour(
                0.5 * (xedges[1:] + xedges[:-1]),
                0.5 * (yedges[1:] + yedges[:-1]),
                H,
                levels=contour_vals,
                colors=['C1', 'C2', 'C3'],
                linewidths=1.5,
                label=base_name
            )
        else:

            im = ax.imshow(H, origin='lower', aspect='auto',
                           extent=[xedges[0], xedges[-1],
                                   yedges[0], yedges[-1]],
                           cmap='Greys')
            # Plot contours
            CS = ax.contour(
                0.5 * (xedges[1:] + xedges[:-1]),
                0.5 * (yedges[1:] + yedges[:-1]),
                H,
                levels=contour_vals,
                colors=['C1', 'C2', 'C3'],
                linewidths=1.5,
                label=base_name
            )

            im = ax.imshow(H, origin='lower', aspect='auto',
                           extent=[xedges[0], xedges[-1],
                                   yedges[0], yedges[-1]],
                           cmap='Greys')
            # Plot contours
            CS = ax.contour(
                0.5 * (xedges[1:] + xedges[:-1]),
                0.5 * (yedges[1:] + yedges[:-1]),
                H,
                levels=contour_vals,
                colors=['C1', 'C2', 'C3'],
                linewidths=1.5,
                label=base_name
            )

        contour_proxy = Line2D([0], [0], color='C1',
                               linewidth=1.5, label='1,2,3$\sigma$ contours')

        ax.plot(marks[0], marks[1], 'rx', markersize=10, markeredgewidth=2,
                label=f'Input xHI=({marks[0]:.2f}, {marks[1]:.2f})')

       # Draw the rectangle
        rect_patch = Rectangle(
            (marks[0] - rect[0] / 2, marks[1] -
             rect[1] / 2),  # bottom-left corner
            rect[0], rect[1],                                 # width, height
            edgecolor='black',
            facecolor='none',
            linestyle='--',
            linewidth=2,
            alpha=0.8
        )
        ax.add_patch(rect_patch)

        ax.set_xlabel(x_lab, fontsize=20)
        ax.set_ylabel(y_lab, fontsize=20)
        ax.set_title(title, fontsize=18)

        handles, labels_ = ax.get_legend_handles_labels()
        handles.append(contour_proxy)
        if suffix == 'PS1':
            ax.legend(handles=handles, loc='upper right', fontsize=15)
        elif suffix == 'PS2':
            ax.legend(handles=handles, loc='lower left', fontsize=15)

        ax.set_xlim(-0.05, 1.05)
        ax.set_ylim(-0.05, 1.05)
        ax.set_xticks(np.linspace(0, 1, 6))
        ax.set_yticks(np.linspace(0, 1, 6))

    plt.tight_layout()

    if save_dir is None:
        save_dir = Path.cwd()
    else:
        save_dir = Path(save_dir)

    plt.savefig(str(save_dir) + '/'+str(base_name) +
                '_'+suffix + '_2Dproj.jpg', dpi=300)
    plt.close(fig)

    return None


def plot_from_saved_1d_projections(npz_file, xhi_marks=(0.5, 0.5, 0.5)):
    """
    Plots 1D projections from a saved .npz file with vertical lines at specified xHI values.

    Parameters:
        npz_file (str): Path to the .npz file containing the 1D projections
        xhi_marks (tuple): Three xHI values to mark on x, y, z axes respectively
    """
    # Load the saved data
    data = np.load(npz_file)
    base_name = os.path.splitext(os.path.basename(npz_file))[0]
    base_name = base_name.replace(
        '_PS1_1D_projections', ' ')  # Remove the suffix
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Define the plotting parameters
    projections = [data['proj_x'], data['proj_y'], data['proj_z']]
    coordinates = [data['x_values'], data['y_values'], data['z_values']]
    labels = data['axis_labels']
    titles = ['Projection along x', 'Projection along y', 'Projection along z']

    for ax, proj, coords, label, title, xhi in zip(axes, projections, coordinates, labels, titles, xhi_marks):
        # Plot the 1D projection
        ax.plot(coords, proj, '-', linewidth=2, label=base_name)

        # Add vertical line at xHI value
        ax.axvline(x=xhi, color='black', linestyle='--',
                   label=f'Input $x_{{\\mathrm{{HI}}}}$={xhi:.2f}')

        ax.set_xlabel(label, fontsize=20)
        ax.set_ylabel('Marginalized Posterior', fontsize=20)
        ax.grid(False)

        # Set x-axis limits and ticks
        ax.set_xlim(-0.05, 1.05)
        ax.set_xticks(np.linspace(0, 1, 6))
        ax.xaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))

        # Add legend
        ax.legend(fontsize=15)
    return ax
