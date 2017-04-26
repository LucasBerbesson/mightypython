Set up your environment
-----------------------

To run the notebook and the examples you should have python 3 and pip installed
on your computer.
To check that is it the case, run in your terminal :

.. code-block:: console

    python --version
    pip --version

Create a virtualenv
-------------------
A Virtual Environment (commonly referred to as a 'virtualenv') is a tool to keep
the dependencies required by different projects in separate places, by creating
virtual Python environments for them.

This project depends on a lot of libraries so if you don't want to destroy your
other projects you'd better use one.

.. note::
    I personnaly recommand ``pew`` or ``virtualenvwrapper``

Install required python packages
--------------------------------
As I said there are a lot of them but if you use a virtualenv you'll be able to
delete all files installed in one simple command !
Libraries are stores in requirements.txt.

To install them run :

.. code-block:: console

    pip install -r requirements.txt

Launch the notebook
--------------------------------
All examples are in the jupyter notebook (n open-source web application that
allows you to create and share documents that contain live code, equations,
visualizations and explanatory text).

To launch the notebook simply run :

.. code-block:: console

    jupyter notebook
