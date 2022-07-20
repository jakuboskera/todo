# Contributing guide lines

Simple description on how to contribute and interact with this repository.

## Contributing

### Make changes

1. Create feature branch

    ```bash
    git checkout -b <feature-branch-name>
    ```

1. Make changes and commit them

    ```bash
    git add .
    git commit -m "feat: add some changes" # Convential commits
    ```

1. Push local branch into git repository

    ```bash
    git push origin -u <feature-branch-name>
    ```

1. In <https://gitlab.moravia.com/devops/k8s-dashboard-guidepost/-/merge_requests>
   create merge request for yor feature-branch to master.
1. Merge changes to master.

### Commit messages

Commits message must follow [**Conventional commits**](https://www.conventionalcommits.org/en/v1.0.0/).

Used verbs:

- `feat` - adding new features / functionality
- `fix` - fixing existing, but broken configuration
- `refactor` - refactoring existing configuration
- `docs` - changing README.md, CONTRIBUTING.md, TODO.md
- `ci` - changing `.gitlab-ci.yml` file
- `style` - changes not fixing bugs or adding new functionality, but making
  chages to files and styling, e.g. idententation, docstring, etc.
- `chore` - no changes, bumps, etc.

Commit messages should be in imperative.

Scopes are not strict, use what fits - for changing code of `src/guidepost`,
use scope `guidepost`, for nginx, `nginx`, etc.

If changing more things at once, consider splitting this commit into more or
use folder name as a scope.

### Pre commit hooks

When you are editing this repository, please setup pre-commit hooks.
We run our hooks on every commit to automatically point out issues in code
such as bad indentation, trailing whitespace, bad formatting inmarkdown files,
etc. List of all used hooks are in [`.pre-commit-config.yaml`](.pre-commit-config.yaml).

1. install [`pre-commit`](https://pre-commit.com/#installation)
1. once pre-cmomit is installed, install hooks

    ```bash
    make pre-commit-install
    ```

1. all done, now githooks will run before every commit and check if your
   changes follow repository rules.
