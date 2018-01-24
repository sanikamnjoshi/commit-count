import os
from os import path
import git
from git import Repo


clone_path = "C:/Users/sanika/code/sample0_clone"	# path to which I want to clone the repo
repo_url = "https://github.com/sanikamnjoshi/sample0.git"	# url of repo I want to clone

# if NOT cloned already, then clone
if not path.exists(clone_path):
	print("\nCloning repo.\n")
	repo = Repo.clone_from(repo_url, clone_path)
	print("\nRepository " + repo_url + " has been cloned to " + clone_path)

	
# if cloned already, then pull
else:
	print("\nRepo cloned already. Running pull.\n")
	repo = Repo(clone_path)
	
	# get no. of commits before pulling
	commit = repo.commit()
	old_num_commits = commit.count()
	print("\nNo. of commits in log before pulling: " , old_num_commits)
	
	# pull
	print("\nPulling now...\n")
	for remote in repo.remotes:
		remote.pull()
			
	# get no. of commits after pulling
	commit = repo.commit()
	new_num_commits = commit.count()
	print("\nNo. of commits in log after pulling: " , new_num_commits)
	
	# difference in the number of commits
	print("\nThere have been {0} new commits since the last pull.\n" .format(new_num_commits-old_num_commits))
		
print("\nProgram execution done.\n")