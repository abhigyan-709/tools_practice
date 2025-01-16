1. What is Version Control System (VCS)?
Answer: A Version Control System is a software tool that helps manage changes to source code over time. It tracks modifications to files, allows multiple people to work on the same codebase, and maintains a history of changes. This helps teams collaborate effectively and maintain different versions of their software.

2. What are the types of VCS?
Answer: There are three main types of VCS:
- Local Version Control Systems (LVCS): Maintains versions in local database
- Centralized Version Control Systems (CVCS): Like SVN, with a central server
- Distributed Version Control Systems (DVCS): Like Git, where every user has a complete copy of the repository

3. What is Git?
Answer: Git is a distributed version control system designed to handle projects of any size with speed and efficiency. It was created by Linus Torvalds for Linux kernel development. Git tracks changes in source code during software development and allows multiple developers to work together.

4. What is the difference between Git and SVN?
Answer: Key differences include:
- Git is distributed, SVN is centralized
- Git has better branching and merging capabilities
- Git stores snapshots, SVN stores differences
- Git provides better performance and works offline
- Git has a staging area, SVN doesn't

5. What is a repository in Git?
Answer: A Git repository is a storage location that contains all your project's files and maintains a history of all changes made to those files. It includes the complete history of versions and branches. Each repository has a .git directory that contains all the version control information.

6. What is the difference between local and remote repository?
Answer: 
- Local repository: Exists on your local machine, contains all project files and version history
- Remote repository: Hosted on a server (like GitHub), allows collaboration between team members, serves as a centralized location for sharing code

7. What is a commit in Git?
Answer: A commit is a snapshot of your repository at a specific point in time. It includes changes to files, a unique identifier (SHA-1 hash), commit message, author details, and timestamp. Commits form the project's history and can be used to track changes or revert to previous states.

8. What is the basic Git workflow?
Answer: The basic Git workflow consists of:
1. Modify files in working directory
2. Stage changes using git add
3. Commit changes using git commit
4. Push changes to remote repository using git push

9. What are the three states of Git?
Answer: The three states are:
- Working Directory: Where you modify files
- Staging Area (Index): Where you prepare changes for commit
- Git Repository: Where changes are permanently stored

10. How do you initialize a Git repository?
Answer: Use the command 'git init' in your project directory. This creates a new .git subdirectory with all necessary repository files.

11. What is git clone?
Answer: 'git clone' is a command used to create a copy of a remote repository on your local machine. Syntax: git clone <repository-url>

12. What is git push?
Answer: 'git push' is a command used to upload local repository content to a remote repository. Syntax: git push <remote> <branch>

13. What is git pull?
Answer: 'git pull' fetches changes from a remote repository and automatically merges them into your current branch. It's essentially a combination of 'git fetch' and 'git merge'.

14. What is git fetch?
Answer: 'git fetch' downloads changes from a remote repository but doesn't automatically merge them into your working files. It updates your remote-tracking branches.

15. What's the difference between git pull and git fetch?
Answer:
- git fetch only downloads new data but doesn't integrate it into your working files
- git pull downloads new data and automatically merges it into your current working branch

16. What is git status?
Answer: 'git status' shows the current state of your working directory and staging area. It shows which files are modified, staged, or untracked.

17. What is .gitignore file?
Answer: .gitignore is a configuration file that tells Git which files or directories to ignore in a project. Common examples include build directories, log files, and dependencies.

18. How do you create a new branch in Git?
Answer: Use either:
- git branch <branch-name>
- git checkout -b <branch-name> (creates and switches to the new branch)

19. What is git checkout?
Answer: 'git checkout' is used to:
- Switch between branches
- Create new branches (-b flag)
- Restore working tree files
- Switch to specific commits

20. What is the difference between git merge and git rebase?
Answer:
- git merge creates a new commit that combines changes from different branches
- git rebase moves or combines a sequence of commits to a new base commit, creating a linear history

This covers the basic section. Would you like me to continue with the Intermediate level questions next?