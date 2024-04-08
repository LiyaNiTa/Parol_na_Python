функции менеджера паролей
=========================

.. image:: /_static/logo.gif
   :alt: Гифка
   :width: 100

.. code-block:: console

   (.venv) $ pip install cryptography

.. code-block:: python

   import json, hashlib, getpass, os, pyperclip, sys
   from cryptography.fernet import Fernet

.. autosummary::
   :toctree: generated

   lumache
