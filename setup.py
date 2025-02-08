from setuptools import setup, find_packages

setup(
    name='document_ai',
    version='0.1',
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    install_requires=[
        'streamlit',
        'langchain_community',
        'langchain_text_splitters',
        'langchain_core',
        'langchain_ollama',
        'pdfplumber'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'document-ai=app:main'
        ]
    },
)
