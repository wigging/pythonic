"""Streamlit app."""

import streamlit as st
from stpkg.adder import add


def main():
    """Create content for the streamlit app."""

    st.markdown("""
    # Streamlit app

    Hello there!
    """)

    total = add(12, 5.5)
    st.markdown(f"Total is {total}")


if __name__ == "__main__":
    main()
