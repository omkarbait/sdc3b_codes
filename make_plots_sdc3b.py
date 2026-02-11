import plot_sdc3b_results as plot_sdc3b
import glob


submissions_dir = '/Users/omkar.bait/work/SDC/sdc3b/submission_analysis/submissions_processed'
ps1_npz_files = glob.glob(submissions_dir + '/*_PS1_2D_projections.npz')

plot_dir = submissions_dir + '/plots/'
print(ps1_npz_files)

for npz in ps1_npz_files:

    plot_sdc3b.plot_from_saved_projections(npz, xhi_marks=(0.699600, 0.401250, 0.125250), xhi_widths=(0.2558,0.3409,0.2111), contour_levels=(0.6827, 0.9545, 0.9973), save_dir=plot_dir, suffix='PS1')


ps2_npz_files = glob.glob(submissions_dir + '/*_PS2_2D_projections.npz')

plot_dir = submissions_dir + '/plots/'
print(ps2_npz_files)

for npz in ps2_npz_files:

    plot_sdc3b.plot_from_saved_projections(npz,xhi_marks=(0.911173, 0.811154, 0.647652), 
		                               xhi_widths=(0.0763450, 0.123693, 0.20331), contour_levels=(0.6827, 0.9545, 0.9973), save_dir=plot_dir, suffix='PS2')



ps3_npz_files = glob.glob(submissions_dir + '/*_PS3_2D_projections.npz')
plot_dir = submissions_dir + '/plots/'

print(ps3_npz_files)

for npz in ps3_npz_files:

    plot_sdc3b.plot_from_saved_projections(npz,xhi_marks=(0.770638, 0.524308, 0.244184), 
		                               xhi_widths=(0.208909, 0.283752, 0.276496), contour_levels=(0.6827, 0.9545, 0.9973), save_dir=plot_dir, suffix='PS3')


im1_npz_files = glob.glob(submissions_dir + '/*_IM1_2D_projections.npz')
plot_dir = submissions_dir + '/plots/'

print(im1_npz_files)

for npz in im1_npz_files:

    plot_sdc3b.plot_from_saved_projections(npz,xhi_marks=(0.770638, 0.524308, 0.244184), 
		                               xhi_widths=(0.208909, 0.283752, 0.276496), contour_levels=(0.6827, 0.9545, 0.9973), save_dir=plot_dir, suffix='IM1')
