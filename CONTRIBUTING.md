# Contributing

**Working on your first Pull Request?** You can learn how from this *free* series [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github)

## Reporting issues and providing feedback

If you have interesting beginner projects that you would like to publish here, you are welcome to do so.

If you find any bugs, open up an issue.

## Development Dependencies

- Python 3 (versions 3.10+ are currently supported)
- `pip3 install flake8 black pytest`
        - `flake8` to check for errors and to enforce code style.
        - `black` to format the code.
        - `pytest` to run the tests (optional, you can contribute without writing tests).
- Install all requirements with the following command:

        pip3 install -r requirements.txt

## Development Process

- Select an issue to work on.
- Fork and clone the repository, create a **virtual environment** and install all the dependencies:

        $ pip3 install -r requirements.txt

- Work on the master branch for smaller patches or create a **separate branch for new features**.
- Make changes, `git add` and then commit. You can link to the issue number in the commit message (optional).
- (Optional) Run `flake8` and `pytest`.
- Use the GitHub website to create a Pull Request (PR) and wait for the maintainers to review it.
