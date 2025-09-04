import argparse
import importlib.resources
from streamlit.web import cli


def main():
    """Command line entrypoint for the package."""

    parser = argparse.ArgumentParser(description="CLI package with Streamlit app")
    parser.add_argument("run", help="enter 'go' to run streamlit app")
    args = parser.parse_args()

    if args.run == "go":
        print("Run the Streamlit app ...")

        with importlib.resources.path("stpkg", "app.py") as app_file:
            cli.main_run([str(app_file)])
