"""
Setup script for AIOS Hub de Arbitragem
"""
from setuptools import setup, find_packages

setup(
    name="aios-arbitragem",
    version="1.0.0",
    description="Sistema inteligente de análise financeira para arbitragem",
    author="Sergio Farias",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.28.0",
        "pandas>=2.0.0",
        "google-generativeai>=0.3.0",
        "python-dotenv>=1.0.0",
    ],
)
