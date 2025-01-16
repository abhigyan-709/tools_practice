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

Let's continue with the Intermediate Level Questions (21-40):

INTERMEDIATE LEVEL QUESTIONS AND ANSWERS:

21. What is a detached HEAD state?
Answer: A detached HEAD state occurs when you checkout a specific commit instead of a branch. In this state, any new commits you make won't belong to any branch and could be lost when you switch to another branch.

22. What is git stash?
Answer: Git stash temporarily saves uncommitted changes (both staged and unstaged) to a stack of unfinished changes that can be reapplied later. Common commands:
- git stash save: Save changes
- git stash pop: Apply and remove stashed changes
- git stash apply: Apply but keep stashed changes
- git stash list: View stashed changes

23. How do you resolve merge conflicts in Git?
Answer: To resolve merge conflicts:
1. Identify conflicting files (marked with <<<<<<, =======, >>>>>>>)
2. Open files and decide which changes to keep
3. Remove conflict markers
4. Stage resolved files (git add)
5. Complete the merge with git commit

24. What is git cherry-pick?
Answer: Git cherry-pick is used to apply specific commits from one branch to another. Syntax: git cherry-pick <commit-hash>. It's useful when you want to pick specific changes rather than merging entire branches.

25. What is git reset?
Answer: Git reset is used to undo changes by moving both HEAD and branch refs to a specified commit. It can also modify the staging area and working directory depending on the mode used.

26. What's the difference between git reset --soft, --hard, and --mixed?
Answer:
- --soft: Moves HEAD to specified commit, keeps staging area and working directory unchanged
- --mixed (default): Moves HEAD and updates staging area, keeps working directory unchanged
- --hard: Moves HEAD, updates staging area and working directory (destructive)

27. What is git revert?
Answer: Git revert creates a new commit that undoes changes from a specified commit. It's a safe way to undo changes as it doesn't alter existing history.

28. What's the difference between git reset and git revert?
Answer:
- git reset modifies history by moving HEAD and branch pointer
- git revert creates new commits to undo changes while preserving history
- reset is typically used for local changes, revert for published changes

29. What is git remote?
Answer: Git remote manages the set of remote repositories that your local repository communicates with. Common commands:
- git remote add
- git remote remove
- git remote show
- git remote -v

30. How do you remove a file from git without removing it from your file system?
Answer: Use git rm --cached <file>. This removes the file from Git tracking while keeping it in your working directory.

31. What is git reflog?
Answer: Git reflog shows a log of all reference updates in the repository, including commits, branch changes, and resets. It's useful for recovering lost commits or branches.

32. What is git blame?
Answer: Git blame shows who last modified each line of a file, when it was modified, and the commit hash. Useful for tracking changes and understanding code history.

33. What are Git hooks?
Answer: Git hooks are scripts that run automatically before or after Git events like commit, push, and receive. They're useful for enforcing policies, automation, and continuous integration.

34. What is git bisect?
Answer: Git bisect is a debugging tool that uses binary search to find which commit introduced a bug. Process:
1. Start with git bisect start
2. Mark known good and bad commits
3. Git checks out commits for testing
4. Mark each tested commit as good/bad
5. Git identifies the problematic commit

35. What is git squash?
Answer: Squashing in Git combines multiple commits into a single commit, usually done during interactive rebase (git rebase -i). It helps maintain a clean commit history.

36. What is the purpose of git config?
Answer: Git config is used to set configuration variables that control Git's operation and appearance. Three levels:
- System level: --system
- User level: --global
- Repository level: --local

37. What is git tag and what are the different types of tags?
Answer: Git tags mark specific points in repository history. Two types:
- Lightweight: Just a pointer to a commit
- Annotated: Full objects containing tagger name, email, date, and message

38. How do you delete a branch locally and remotely?
Answer:
- Local: git branch -d <branch-name>
- Remote: git push origin --delete <branch-name>

39. What is the purpose of git clean?
Answer: Git clean removes untracked files from the working directory. Common options:
- -n: Dry run
- -f: Force removal
- -d: Include directories
- -x: Include ignored files

40. What is git archive?
Answer: Git archive creates an archive file of a specified format (zip, tar) containing a tree from a named commit, branch, or tag.

ADVANCED LEVEL QUESTIONS AND ANSWERS (41-60):

41. Explain the Git branching strategies you've used?
Answer: Common strategies include:
- GitFlow: master, develop, feature, release, and hotfix branches
- Trunk-Based Development: Short-lived feature branches off main
- GitHub Flow: Simple workflow with feature branches and main
- Release Branching: Separate branches for different releases

42. What is GitFlow workflow?
Answer: GitFlow is a branching model with five types of branches:
- Master: Production-ready code
- Develop: Integration branch for features
- Feature: New feature development
- Release: Release preparation
- Hotfix: Emergency production fixes

43. What is Trunk-Based Development?
Answer: A branching strategy where developers merge small, frequent updates to a core "trunk" or main branch. Features are developed behind feature flags and integrated continuously.

44. How does Git handle large binary files?
Answer: Git isn't optimized for large binary files. Solutions include:
- Git LFS (Large File Storage)
- git-annex
- Using .gitignore for binary files
- External artifact repositories

45. What is Git LFS?
Answer: Git Large File Storage (LFS) replaces large files with text pointers in Git, while storing the file contents on a remote server. It's useful for managing large binary files.

46. How do you handle security in Git?
Answer:
- Use .gitignore for sensitive files
- Implement pre-commit hooks
- Use git-secrets for scanning
- Enable GPG signing
- Manage access controls
- Regular security audits

47. What is git submodule?
Answer: Git submodules allow you to keep a Git repository as a subdirectory of another Git repository. Useful for including external dependencies or shared components.

48. How do you modify a commit message after push?
Answer:
1. git rebase -i HEAD~n
2. Change 'pick' to 'reword'
3. Save and modify message
4. git push --force-with-lease

49. What is git rebase -i?
Answer: Interactive rebase allows you to modify commits in various ways:
- Reorder commits
- Edit commit messages
- Squash commits
- Split commits
- Drop commits

50. How do you recover a deleted branch?
Answer:
1. Find branch commit using git reflog
2. Create new branch at that commit:
   git checkout -b branch-name commit-hash

Let's continue with the remaining Advanced Level Questions and other sections:

ADVANCED LEVEL QUESTIONS (continued, 51-60):

51. What is git worktree?
Answer: Git worktree allows you to have multiple working directories from a single Git repository. Useful for:
- Working on multiple branches simultaneously
- Building different versions
- Testing changes in isolation

52. How do you handle merge conflicts in binary files?
Answer:
- Use 'ours' or 'theirs' strategy
- Implement custom merge drivers
- Use Git LFS
- Keep binary files in separate branches
- Use proper versioning for binary assets

53. What is git filter-branch?
Answer: A tool to rewrite Git repository history. Used for:
- Removing sensitive data
- Moving subdirectories to new repositories
- Changing author information
- Global modifications to commits

54. How do you optimize Git repository performance?
Answer:
- Regular garbage collection (git gc)
- Use shallow clones when possible
- Implement Git LFS for large files
- Prune unnecessary references
- Clean up old branches
- Optimize .gitignore

55. What is git gc?
Answer: Git Garbage Collection (gc) cleans up unnecessary files and optimizes local repository by:
- Removing unreachable objects
- Packing loose objects
- Pruning reflog entries
- Repacking packed objects

56. How do you handle Git repository corruption?
Answer:
1. Run git fsck to check repository integrity
2. Use git reflog to find lost commits
3. Create backup of repository
4. Try git gc --prune=now
5. Clone fresh repository if needed
6. Restore from backup if necessary

57. What is git rerere?
Answer: "Reuse Recorded Resolution" - Git feature that remembers how you resolved merge conflicts and automatically reapplies the resolution next time the same conflict occurs.

58. How do you set up Git hooks for team collaboration?
Answer:
1. Create hooks in .git/hooks directory
2. Make hooks executable
3. Share hooks via separate repository
4. Use pre-commit frameworks
5. Implement CI/CD integration

59. What is git bundle?
Answer: Git bundle creates a single file containing Git repository data, useful for:
- Transferring changes without network access
- Creating backups
- Sharing specific commits
- Offline collaboration

60. How do you implement CI/CD with Git?
Answer:
- Use branch protection rules
- Implement automated testing
- Set up deployment pipelines
- Use version tags
- Automate releases
- Implement code review processes

PRACTICAL SCENARIO QUESTIONS (61-80):

61. How would you revert multiple commits that have been pushed to remote?
Answer:
1. Use git revert for each commit:
   git revert HEAD~3..HEAD
2. Or use interactive rebase:
   git rebase -i HEAD~3
3. Create new commit reverting changes
4. Push to remote

62. How do you maintain different configurations for different environments?
Answer:
- Use git-crypt for sensitive configs
- Implement environment-specific branches
- Use configuration templates
- Store sensitive data in environment variables
- Use configuration management tools

63. How do you clean up local and remote tracking branches?
Answer:
Local cleanup:
```bash
git branch -d $(git branch --merged)
git remote prune origin
```
Remote cleanup:
```bash
git push origin --delete branch-name
```

64. How do you handle merge conflicts in package-lock.json?
Answer:
1. Remove package-lock.json
2. Run npm install
3. Commit regenerated package-lock.json
4. Consider using yarn.lock instead
5. Keep node_modules in .gitignore

65. How would you implement feature toggles with Git?
Answer:
- Use configuration files for toggles
- Implement feature flag service
- Use environment variables
- Maintain toggle states in database
- Use branching strategies with toggles

Let's continue with the remaining questions:

PRACTICAL SCENARIO QUESTIONS (continued, 66-70):

66. How do you manage large monorepo with Git?
Answer:
- Use Git LFS for large files
- Implement sparse checkout
- Use shallow clones for CI/CD
- Set up proper .gitignore
- Use Git submodules or subtrees
- Implement build caching
- Use monorepo-specific tools (like Bazel, Nx, or Lerna)

67. How do you handle database schema changes with Git?
Answer:
- Use database migration tools
- Version control migration scripts
- Follow naming conventions (timestamp_description)
- Maintain separate branches for schema changes
- Test migrations in isolation
- Document rollback procedures
- Use tools like Flyway or Liquibase

68. How would you implement Git workflow for microservices architecture?
Answer:
- Separate repository for each microservice
- Implement CI/CD pipelines per service
- Use semantic versioning
- Maintain service dependency documentation
- Use git submodules for shared components
- Implement contract testing
- Use feature branches per service

69. How do you handle sensitive data accidentally committed to Git?
Answer:
1. Immediately rotate compromised credentials
2. Use git filter-branch or BFG Repo Cleaner to remove sensitive data
3. Force push changes
4. Require all collaborators to rebase
5. Implement preventive measures (git-secrets, pre-commit hooks)
6. Update .gitignore

70. How would you migrate from SVN to Git?
Answer:
1. Use git-svn to clone SVN repository
2. Clean up SVN-specific metadata
3. Convert SVN ignore patterns to .gitignore
4. Map SVN users to Git authors
5. Verify repository integrity
6. Set up new Git remote
7. Update team workflows and documentation

BEST PRACTICES AND EXPERIENCE QUESTIONS (71-80):

71. What Git branching strategy do you prefer and why?
Answer: (Example answer)
I prefer trunk-based development because:
- Promotes continuous integration
- Reduces merge conflicts
- Faster feedback cycles
- Better suited for CI/CD
- Simpler workflow
- Easier to maintain
However, the choice depends on team size, project requirements, and release cycles.

72. How do you ensure code quality in Git workflow?
Answer:
- Implement pre-commit hooks
- Automated testing in CI pipeline
- Code review process
- Static code analysis
- Branch protection rules
- Automated formatting
- Regular security scanning
- Documentation requirements

73. How do you handle code reviews in Git?
Answer:
- Use Pull Request/Merge Request workflow
- Implement review templates
- Set up automated checks
- Use review tools (e.g., GitHub PR reviews)
- Follow review checklist
- Enforce branch policies
- Implement size limits for PRs
- Regular review sessions

74. What are your preferred Git tools and why?
Answer:
- CLI: For automation and full control
- GUI Tools: GitKraken/SourceTree for visualization
- IDE Integration: For everyday operations
- GitHub/GitLab: For collaboration
- Git-extras: For additional functionality
- Hub: For GitHub CLI integration

75. How do you handle versioning in your projects?
Answer:
- Use Semantic Versioning (MAJOR.MINOR.PATCH)
- Git tags for releases
- Automated version bumping
- Changelog maintenance
- Release branches
- Version in package files
- Documentation updates

TROUBLESHOOTING AND DEBUG QUESTIONS (81-90):

76. How do you debug Git issues?
Answer:
- Use git log for history analysis
- git reflog for reference history
- git bisect for finding issues
- git blame for code investigation
- Enable Git debugging (GIT_TRACE)
- Check .git directory structure
- Verify remote configurations

77. How do you recover from a bad merge?
Answer:
1. Identify the bad merge commit
2. Use git reset --hard to pre-merge state
3. Or git revert the merge commit
4. Re-apply necessary changes
5. Document the issue and solution
6. Update team procedures if needed

78. How do you fix a broken Git repository?
Answer:
1. Create backup
2. Run git fsck
3. Use git gc
4. Check for corruption
5. Repair or clone fresh
6. Restore necessary commits
7. Verify repository integrity

79. How do you handle large Git repositories?
Answer:
- Implement Git LFS
- Use shallow clones
- Regular maintenance (gc)
- Optimize .gitignore
- Archive old branches
- Use partial clones
- Implement submodules

80. How do you troubleshoot Git performance issues?
Answer:
- Profile operations
- Check large files
- Optimize hooks
- Clean unnecessary branches
- Pack references
- Use git gc
- Monitor disk usage

ADVANCED CONCEPTS AND INTEGRATION (91-100):

81. How do you integrate Git with Jenkins?
Answer:
- Configure Git plugin
- Set up webhooks
- Implement pipeline as code
- Use Jenkinsfile
- Configure credentials
- Set up build triggers
- Implement branch filtering

82. How do you implement Git-based deployment strategies?
Answer:
- GitOps workflow
- Feature flags
- Blue-green deployments
- Canary releases
- Automated rollbacks
- Environment branches
- Release tagging

Let's continue with the remaining Advanced Concepts and Integration questions (83-100):

83. How do you handle Git in containerized environments?
Answer:
- Use multi-stage Dockerfile builds
- Implement .dockerignore alongside .gitignore
- Store container configurations in Git
- Version container images with Git tags
- Use Git commits for image tags
- Implement CI/CD for container builds
- Store Docker Compose files in Git
- Handle secrets separately from Git

84. How do you implement Git-based rollback strategies?
Answer:
1. Tag-based rollbacks:
   - Use semantic versioning tags
   - Maintain deployment history
   - Automate rollback scripts
   - Test rollback procedures

2. Implementation steps:
   ```bash
   git tag -l # list available tags
   git checkout <previous-tag>
   git push --force origin HEAD:main # for immediate rollback
   ```

3. Additional considerations:
   - Database migrations
   - API version compatibility
   - Dependencies management
   - User session handling

85. How do you handle Git in distributed teams?
Answer:
1. Communication:
   - Clear branching strategy
   - Documentation requirements
   - Code review guidelines
   - Regular sync meetings

2. Technical setup:
   - Branch protection rules
   - Automated testing
   - Code style enforcement
   - Time zone considerations
   - Clear commit message standards

3. Workflow:
   - Pull request templates
   - Issue tracking integration
   - Documentation requirements
   - Code review assignments

86. How do you implement Git-based feature flags?
Answer:
1. Implementation:
   ```json
   // feature-flags.json
   {
     "features": {
       "newFeature": {
         "enabled": false,
         "users": ["beta-testers"],
         "percentage": 10
       }
     }
   }
   ```

2. Version control:
   - Store configurations in Git
   - Environment-specific settings
   - Feature flag service integration
   - Automated toggle updates

3. Management:
   - Feature flag cleanup
   - Documentation
   - Testing strategies
   - Gradual rollout

87. How do you handle Git in compliance-heavy environments?
Answer:
1. Security measures:
   - Signed commits (GPG)
   - Access controls
   - Audit logging
   - Code scanning

2. Process requirements:
   - Documentation
   - Review procedures
   - Change management
   - Approval workflows

3. Implementation:
   - Branch protection
   - Automated compliance checks
   - Regular audits
   - Security scanning

88. How do you implement Git-based release management?
Answer:
1. Release process:
   - Version bumping
   - Changelog generation
   - Release branch creation
   - Tag management

2. Automation:
   ```bash
   # Example release script
   git checkout -b release/v1.2.0
   npm version minor
   git push origin release/v1.2.0 --tags
   ```

3. Documentation:
   - Release notes
   - Migration guides
   - API changes
   - Breaking changes

89. How do you handle Git in cloud-native applications?
Answer:
1. Infrastructure as Code:
   - Store Terraform/CloudFormation in Git
   - Version control for cloud configs
   - Environment separation

2. CI/CD integration:
   - Cloud provider integration
   - Automated deployments
   - Environment promotion
   - Configuration management

3. Security:
   - Secrets management
   - Access controls
   - Compliance checks
   - Audit trails

90. How do you implement Git-based configuration management?
Answer:
1. Structure:
   ```
   config/
   ├── development/
   ├── staging/
   ├── production/
   └── default.yaml
   ```

2. Implementation:
   - Environment-specific configs
   - Secret management
   - Version control
   - Change tracking

3. Management:
   - Configuration validation
   - Automated updates
   - Access controls
   - Audit logging

91. How do you handle Git with microservices dependencies?
Answer:
1. Dependency management:
   - Service versioning
   - API contracts
   - Shared libraries
   - Version compatibility

2. Implementation:
   - Monorepo vs multi-repo
   - Service discovery
   - Contract testing
   - Version control

92. How do you implement Git-based disaster recovery?
Answer:
1. Backup strategy:
   - Regular backups
   - Multiple remotes
   - Backup verification
   - Recovery testing

2. Recovery procedures:
   - Repository restoration
   - History preservation
   - Access recovery
   - Documentation

93. How do you handle Git with database changes?
Answer:
1. Migration management:
   ```sql
   -- migrations/V1__initial_schema.sql
   CREATE TABLE users (
     id SERIAL PRIMARY KEY,
     name VARCHAR(255)
   );
   ```

2. Version control:
   - Migration scripts
   - Rollback procedures
   - Data preservation
   - Schema versioning

94. How do you implement Git-based security scanning?
Answer:
1. Implementation:
   - Pre-commit hooks
   - Automated scanning
   - Vulnerability checks
   - Secret detection

2. Tools integration:
   - SonarQube
   - GitGuardian
   - Snyk
   - Dependencies scanning

95. How do you handle Git with large scale refactoring?
Answer:
1. Strategy:
   - Incremental changes
   - Feature toggles
   - Parallel implementations
   - Gradual migration

2. Implementation:
   - Branch management
   - Testing strategy
   - Documentation
   - Review process

96. How do you implement Git-based monitoring?
Answer:
1. Metrics:
   - Repository size
   - Commit frequency
   - Branch lifetime
   - Build status

2. Implementation:
   - Monitoring tools
   - Alerts setup
   - Performance tracking
   - Health checks

97. How do you handle Git with legacy systems?
Answer:
1. Integration:
   - Bridge patterns
   - Compatibility layers
   - Migration strategy
   - Version control

2. Management:
   - Documentation
   - Knowledge transfer
   - Gradual updates
   - Risk management

98. How do you implement Git-based automation?
Answer:
1. Tools:
   - GitHub Actions
   - GitLab CI
   - Jenkins
   - Custom scripts

2. Implementation:
   - Automated testing
   - Deployment automation
   - Documentation generation
   - Version management

99. How do you handle Git with multiple product versions?
Answer:
1. Branch strategy:
   - Long-term support branches
   - Version-specific fixes
   - Feature backporting
   - Release management

2. Implementation:
   - Version tagging
   - Cherry-picking
   - Documentation
   - Testing strategy

100. How do you implement Git-based knowledge sharing?
Answer:
1. Documentation:
   - Wiki integration
   - Code comments
   - Architecture decisions
   - Process documentation

2. Implementation:
   - Documentation as code
   - Automated updates
   - Review process
   - Knowledge base
