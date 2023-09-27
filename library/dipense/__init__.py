# -*- coding: utf-8 -*-
"""
    An OSINT tool for it ninjas
    
    _____________
    ICHECKP usage:
    from dipense.icheckp import ICHECKP
    --- OR ---
    from dipense import ICHECKP
    
    
    ICHECKP().icheckp('197.3.11.7')
    
    you can pass a kwargs of `autoOpenMap=True`
    into the ICHECKP class, this will automatically open a map in
    your webbrowser, e.g
        _______________________________________________
        ICHECKP(autoOpenMap=True).icheckp('197.3.11.7')

@@@@@@@   @@@  @@@@@@@   @@@@@@@@  @@@  @@@   @@@@@@   @@@@@@@@  
@@@@@@@@  @@@  @@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@@@@   @@@@@@@@  
@@!  @@@  @@!  @@!  @@@  @@!       @@!@!@@@  !@@       @@!       
!@!  @!@  !@!  !@!  @!@  !@!       !@!!@!@!  !@!       !@!       
@!@  !@!  !!@  @!@@!@!   @!!!:!    @!@ !!@!  !!@@!!    @!!!:!    
!@!  !!!  !!!  !!@!!!    !!!!!:    !@!  !!!   !!@!!!   !!!!!:    
!!:  !!!  !!:  !!:       !!:       !!:  !!!       !:!  !!:       
:!:  !:!  :!:  :!:       :!:       :!:  !:!      !:!   :!:       
 :::: ::   ::   ::        :: ::::   ::   ::  :::: ::    :: ::::  
:: :  :   :     :        : :: ::   ::    :   :: : :    : :: :: 

"""


import argparse
from datetime import datetime


__title__ = 'dipense'
__version__ = '0.1.5'
__author__ = 'Usman Musa'
__author_email__ = 'usmanmusa1920@gmail.com'
__author_website__ = 'https://usmanmusa1920.github.io'
__repository__ = 'https://github.com/usmanmusa1920/dipense'
__url__ = 'https://dipense.readthedocs.io'
__download_url__ = 'https://pypi.org/project/dipense'
__license__ = 'MIT'
__copyright__ = f'Copyright (C) 2022 - {datetime.today().year} Usman Musa'
__description__ = 'An OSINT tool for it ninjas.'


from .icheckp import ICHECKP
from .default import default
from .default import Default
from .cli_txt import getout
from .cli_txt import log_style


# def icheckp(ip, autoOpenMap=False):
#     print('The year is', default()['the_year'])


def ipLoad():
    # prog is the name of the program, default=sys.argv[0]
    parser = argparse.ArgumentParser(
        prog='scan an ip address', description='This scan an ip address!')
    # metavar make the -help to look cleaan
    parser.add_argument(
        '--ip', '-i', required=True, type=str, metavar='', help='What is the ip address?')
    parser.add_argument(
        '--open', '-o', default=False, required=False, type=str, metavar='', help='This will automatic open your map in web browser, it is a boolean of `True or False`')
    parser.add_argument(
        dest='payloadip', default='payloadip', type=str, metavar='', help='The payload is to find an ip address infomation')
    args = parser.parse_args()
    ICHECKP(autoOpenMap=args.open).icheckp(args.ip)
  
  
def payloads(helper):
    import sys
    import logging
    from .drone import whoLoad
    from .drone import numLoad
    # from .structure import helper
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    def run(args):
        return [args]

    dft = Default.payload
    lst_1 = Default.suffix_payload
    
    """
    this return a list of positional argument that
    can be use in the command line/terminal
    where we concatenate `dft` with each item in `lst_1`
    """
    lst_2 = [dft+i for i in lst_1]
  
    if len(sys.argv) == 1:
        log_style('\n Include a positional argument!', log='info')
        getout(helper())
    elif sys.argv[1] not in lst_2:
        getout(f'\n `{sys.argv[1]}` is not a valid positional argument!')
        getout(helper())
    else:
        for i in lst_1:
            if sys.argv[1] == f'{dft}{i}':
                # if __name__ == '__main__':
                logger.debug(run(eval(f'{i}Load()')))
                break
