
DiPense - lib
=============

An OSINT tool for IT ninjas

Release v\ |version|


.. image:: https://static.pepy.tech/badge/dipense/month
    :target: https://pepy.tech/project/dipense
    :alt: DiPense Downloads Per Month Badge

.. image:: https://static.pepy.tech/badge/dipense/week
    :target: https://pepy.tech/project/dipense
    :alt: DiPense Downloads Per Week Badge
    
.. image:: https://img.shields.io/pypi/l/dipense.svg
    :target: https://pypi.org/project/dipense/
    :alt: License Badge

.. image:: https://img.shields.io/pypi/wheel/dipense.svg
    :target: https://pypi.org/project/dipense/
    :alt: Wheel Support Badge

.. image:: https://img.shields.io/pypi/pyversions/dipense.svg
    :target: https://pypi.org/project/dipense/
    :alt: Python Version Support Badge

.. image:: https://img.shields.io/github/contributors/usmanmusa1920/dipense.svg
    :target: https://github.com/usmanmusa1920/dipense/graphs/contributors
    :alt: Contributors Badge
    
-------------------

How to use the library
======================

First we recommend creating a virtual environment **python -m venv venv** and then activate it **source venv/bin/activate**

Once that finish now install the library using **pip install dipense** and wait for the installation basically the library was uploaded using **sdist** (Source Distribution)

After that create a new file let call it **route.py** in the file put the below code

.. code-block:: python

    from dipense import payloads
    from dipense.structure import helper


    if __name__ == '__main__':
      payloads(helper)

save the file and navigate to where the file is located in terminal and your are ready to go

To find information about a domain name run the file like::

    python route.py payloadwho -d google.com
    
    or

    python route.py payloadwho --domain google.com


To find information about an ip address run the file like so below, and the command require root previlage (super user)::

    python route.py payloadip -i 198.3.11.7
    
    or

    python route.py payloadip --ip 198.3.11.7

You can also specify a flag of **-o** or **--open** to **True** this will automatically open a webbrowser showing you where that ip address is located, like::

    python route.py payloadip -i 198.3.11.7 -o True
    
    or

    python route.py payloadip -i 198.3.11.7 --open True


To find information about a phone number run the file like you see below, be sure to start with the country code of that phone number::

    python route.py payloadnum -n +2349083513047

    or
     
    python route.py payloadnum --number +2349083513047


To see positional argument and flags available run the file without any flag or positional argument like::

    python route.py

Useful links:
=============

- `Repository <https://github.com/usmanmusa1920/dipense-lib>`_

- `PYPI Release <https://pypi.org/project/dipense>`_

- `Docker-hub Release <https://hub.docker.com/r/usmanmusa/dipense>`_

Version Status
==============

- version 0.1.5

DiPense at a glance (docker)
============================

.. image:: https://raw.githubusercontent.com/usmanmusa1920/dipense/master/docs/_static/screen-shot.png
  :width: 400
  :alt: DiPense at a glance (docker)

DiPense at a glance (pypi)
==========================

.. image:: https://raw.githubusercontent.com/usmanmusa1920/dipense/master/docs/_static/dipense-terminal.png
  :width: 400
  :alt: DiPense at a glance (pypi)
