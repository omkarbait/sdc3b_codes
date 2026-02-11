import os
import read_submissions as rs
import compute_2dprojections as proj2d
import compute_1dprojections as proj1d

'''
#  read submissions to get a list of team names

#ps1_submissions_dir = "/Users/omkar.bait/work/SDC/sdc3b/submission_analysis/submissions_28may/validated_submissions/PS1/team_folders"
#ps2_submissions_dir = "/Users/omkar.bait/work/SDC/sdc3b/submission_analysis/submissions_28may/validated_submissions/PS2/team_folders"

ps1_submissions_dir = "/Users/omkar.bait/work/SDC/sdc3b/submission_analysis/final_submissions/validated_submissions/PS1/team_folders"
ps2_submissions_dir = "/Users/omkar.bait/work/SDC/sdc3b/submission_analysis/final_submissions/validated_submissions/PS2/team_folders"


ps1_teams = rs.get_nonempty_subdirs(ps1_submissions_dir)

# process PS1  files
for team_name in ps1_teams:
    ps1_file_name = team_name + '_PS1.fits'
    ps1_full_path = os.path.join(ps1_submissions_dir, team_name, ps1_file_name)

    print('Processing PS1 data for', team_name)
    try:
        npz_file = proj2d.compute_and_save_2d_projections(
            ps1_full_path, save_dir='/Users/omkar.bait/work/SDC/sdc3b/submission_analysis/submissions_processed')
        npz_file_1D = proj1d.compute_and_save_1d_projections(
            ps1_full_path, save_dir='/Users/omkar.bait/work/SDC/sdc3b/submission_analysis/submissions_processed')
        print('Done.')
    except:
        print('Processing failed.')

ps2_teams = rs.get_nonempty_subdirs(ps2_submissions_dir)

# process PS2 files
for team_name in ps2_teams:
    ps2_file_name = team_name + '_PS2.fits'

    ps2_full_path = os.path.join(ps2_submissions_dir, team_name, ps2_file_name)

    print('Processing PS2 data for', team_name)
    try:
        npz_file = proj2d.compute_and_save_2d_projections(
            ps2_full_path, save_dir='/Users/omkar.bait/work/SDC/sdc3b/submission_analysis/submissions_processed')

        npz_file_1D = proj1d.compute_and_save_1d_projections(
            ps2_full_path, save_dir='/Users/omkar.bait/work/SDC/sdc3b/submission_analysis/submissions_processed')
        print('Done.')
    except:
        print('Processing failed.')


'''
#ps3_teams = rs.get_nonempty_subdirs(ps3_submissions_dir)


ps3_submissions_dir = "/Users/omkar.bait/work/SDC/sdc3b/submission_analysis/PS3_IM1_analysis/team_folders"


ps3_teams = ['HIMALAYA', 'YEYE', 'Traditional_SEarCH', 'Modern_SEarCH' ]

# process PS3 files
for team_name in ps3_teams:
    ps3_file_name = team_name + '_PS3.fits'

    ps3_full_path = os.path.join(ps3_submissions_dir, team_name, ps3_file_name)
    print(ps3_full_path)
    print('Processing PS3 data for', team_name)
    try:
        npz_file = proj2d.compute_and_save_2d_projections(
            ps3_full_path, save_dir='/Users/omkar.bait/work/SDC/sdc3b/submission_analysis/submissions_processed')

        npz_file_1D = proj1d.compute_and_save_1d_projections(
            ps3_full_path, save_dir='/Users/omkar.bait/work/SDC/sdc3b/submission_analysis/submissions_processed')
        print('Done.')
    except:
        print('Processing failed.')


# process IM1 files
for team_name in ps3_teams:
    im1_file_name = team_name + '_IM1.fits'

    im1_full_path = os.path.join(ps3_submissions_dir, team_name, im1_file_name)
    print(im1_full_path)

    print('Processing IM1 data for', team_name)
    try:
        npz_file = proj2d.compute_and_save_2d_projections(
            im1_full_path, save_dir='/Users/omkar.bait/work/SDC/sdc3b/submission_analysis/submissions_processed')

        npz_file_1D = proj1d.compute_and_save_1d_projections(
            im1_full_path, save_dir='/Users/omkar.bait/work/SDC/sdc3b/submission_analysis/submissions_processed')
        print('Done.')
    except:
        print('Processing failed.')
