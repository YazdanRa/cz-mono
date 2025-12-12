# Contributing to cz-mono

Thanks for your interest in contributing to this project!

The project uses [uv](https://astral.sh/uv/) for managing development dependencies.
To set up your development environment, follow these steps:

1. Install uv if you haven't already:
2. Clone the repository
3. Navigate to the project directory
4. Run the following command to install development dependencies:
    ```shell
    uv sync --dev
    ```
5. Install pre-commit hooks:
    ```shell
    uvx pre-commit install
    ```
6. Make your changes and be sure to add tests if applicable.
7. Run tests to ensure everything is working:
    ```shell
    uv run pytest tests
    ```
8. Commit your changes following the [conventional commit](https://www.conventionalcommits.org/) guidelines.
9. Push your changes and create a pull request.
10. Thank you for contributing!

# Maintainers Publishing Guide

To publish a new version of the `cz-mono` package, follow these steps:

1. Ensure all tests pass and your changes are committed.
2. Bump the version using Commitizen:
    ```shell
    cz bump
    ```
3. Push the changes to the remote repository:
    ```shell
    git push origin master --tags
    ```

4. This will trigger the CI/CD pipeline to build and publish the new version to PyPI and add a new release on GitHub.
5. Verify that the new version is available on PyPI and that the GitHub release has been created successfully.
6. Celebrate your successful release! 🎉
