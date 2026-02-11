import os
import shutil
import warnings


def organize_files_by_team(source_dir, root_dir, team_suffix="_1D"):
    """
    Copies files from source_dir to team-specific subdirectories in root_dir.

    Parameters:
    - source_dir (str): Directory containing the original files.
    - root_dir (str): Directory containing the subdirectories for each team.
    - team_suffix (str): String suffix that indicates the end of the team name.
    """
    for filename in os.listdir(source_dir):
        if team_suffix in filename:
            team_name = filename.split(team_suffix)[0]
            team_dir = os.path.join(root_dir, team_name)

            if not os.path.isdir(team_dir):
                warnings.warn(f"Directory not found for team '{
                              team_name}': {team_dir}")
                continue

            src_file = os.path.join(source_dir, filename)
            dst_file = os.path.join(team_dir, filename)

            shutil.copy2(src_file, dst_file)
            print(f"Copied: {filename} → {team_dir}")


if __name__ == '__main__':
    # source_directory = "/Users/omkar.bait/work/SDC/sdc3b/submission_analysis/plots"
    source_directory = '/Users/omkar.bait/work/SDC/sdc3b/submission_analysis/submissions_processed/plots'

    destination_root = "/Users/omkar.bait/work/SDC/sdc3b/submission_analysis/final_submissions_copy/validated_submissions/PS1/team_folders/"
    # suffix_to_identify_team = "_1D"
    suffix_to_identify_team = "_PS"

    organize_files_by_team(
        source_directory, destination_root, suffix_to_identify_team)
