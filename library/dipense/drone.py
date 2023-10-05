# -*- coding: utf-8 -*-
import argparse
from .default import Default
from . import getout

import whois
import phonenumbers
from termcolor import colored
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone


def numLoad():
    # prog is the name of the program, default=sys.argv[0]
    parser = argparse.ArgumentParser(
        prog='scan phone number', description='This scan a phone number!')
    
    # metavar make the -help to look cleaan
    parser.add_argument(
        '--number', '-n', required=True, type=str, metavar='', help='What is the phone number? it should start with country code e.g +2348123456789')
    parser.add_argument(
        dest='payloadnum', default='payloadnum', type=str, metavar='', help='The payload is to find phone number infomation')
    
    args = parser.parse_args()
    p_num = args.number
    try:
        num_parse = phonenumbers.parse(p_num, None)
        num_valid = phonenumbers.is_valid_number(num_parse)
        p_nation = phonenumbers.format_number(num_parse, phonenumbers.PhoneNumberFormat.NATIONAL)
        inter_nation = phonenumbers.format_number(
            num_parse, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        p_e164 = phonenumbers.format_number(num_parse, phonenumbers.PhoneNumberFormat.E164)
        p_geo = geocoder.description_for_number(num_parse, 'en')
        p_carr = carrier.name_for_number(num_parse, 'en')
        time_zone_1 = timezone.time_zones_for_number(num_parse)
        time_zone_2 = timezone.time_zones_for_geographical_number(num_parse)
        
        """
        >>> p_num = '+2349083513047'
        >>> num_parse = phonenumbers.parse(p_num, None)
        >>> num_parse
        PhoneNumber(country_code=234, national_number=9083513047, extension=None, italian_leading_zero=None, number_of_leading_zeros=None, country_code_source=0, preferred_domestic_carrier_code=None)
        >>> num_valid = phonenumbers.is_valid_number(num_parse)
        >>> num_valid
        True
        >>> p_nation = phonenumbers.format_number(num_parse, phonenumbers.PhoneNumberFormat.NATIONAL)
        >>> p_nation
        '0908 351 3047'
        >>> inter_nation = phonenumbers.format_number(num_parse, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        >>> inter_nation
        '+234 908 351 3047'
        >>> p_e164 = phonenumbers.format_number(num_parse, phonenumbers.PhoneNumberFormat.E164)
        >>> p_e164
        '+2349083513047'
        >>> p_geo = geocoder.description_for_number(num_parse, 'en')
        >>> p_geo
        'Nigeria'
        >>> p_carr = carrier.name_for_number(num_parse, 'en')
        >>> p_carr
        '9mobile'
        >>> time_zone_1 = timezone.time_zones_for_number(num_parse)
        >>> time_zone_1
        ('Africa/Lagos',)
        >>> time_zone_2 = timezone.time_zones_for_geographical_number(num_parse)
        >>> time_zone_2
        ('Africa/Lagos',)
        """

        context = {
            'num_parse': num_parse,
            'num_valid': num_valid,
            'p_nation': p_nation,
            'inter_nation': inter_nation,
            'p_e164': p_e164,
            'p_geo': p_geo,
            'p_carr': p_carr,
            'time_zone_1': time_zone_1,
            'time_zone_2': time_zone_2,
            'sites_list': Default.sites_list,
        }
        
        getout(colored(r"""
          _..._
        .'     '.
       /  _   _  \
       | (o)_(o) |
        \(     ) /
        //'._.'\ \
       //   .   \ \
      ||   .     \ \
      |\   :     / |
      \ `) '   (`  /_
    _)``".____,.'"` (_
    )     )'--'(     (
     '---`      `---`
""", 'cyan', attrs=['blink']))
        
        # q1 = f'{site} intext: '{p_e164}' OR intex: '{inter_nation}' OR intex: '{p_nation}''
        # q2 = q1.replace(' ', '+')
        # for site in context['sites_list']:
        #     # q1 = f'{site} intext: '{p_e164}' OR intex: '{inter_nation}' OR intex: '{p_nation}''
        #     # q2 = q1.replace(' ', '+')
        #     url_g = '[+] ' + f'https://www.google.com/search?q={site}+intext%3A{p_e164}'+OR+intext'{inter_nation}'+OR +ntext:'{p_nation}''
        #     getout(colored(url_g, 'magenta'))
        
    except:
        context = {
            'p_num': p_num,
        }

    for k, v in context.items():
        if k == 'sites_list':
            pass
        else:
            r = k + ': '
            getout(colored(' =>', 'magenta'), colored(r, 'green'), v)
    # if args.kind == 'nmap':
    #     n_cmd = 'nmap -v -A -sV ' + args.ip
    #     n = sp.run(shlex.split(n_cmd))
    #     getout('This', n.args)
    #     return [args, n]
    return args


def whoLoad():
    # prog is the name of the program, default=sys.argv[0]
    parser = argparse.ArgumentParser(
        prog='who is', description='This scan and find info of a domain!')
    
    # metavar make the -help to look cleaan
    parser.add_argument(
        '--domain', '-d', required=True, type=str, metavar='', help='What is the domain name? probably it gives infoof most TLD, while others like ().tk, .io, .org) it capture less')
    parser.add_argument(
        dest='payloadwho', default='payloadwho', type=str, metavar='', help='The payload is to find domain name infomation')
    
    args = parser.parse_args()
    domain = args.domain

    try:
        howis = whois.whois(domain)
        """
        >>> import whois
        >>> howis = whois.whois('google.com')
        >>> howis
        {'domain_name': ['GOOGLE.COM', 'google.com'], 'registrar': 'MarkMonitor, Inc.', 'whois_server': 'whois.markmonitor.com', 'referral_url': None, 'updated_date': [datetime.datetime(2019, 9, 9, 15, 39, 4), datetime.datetime(2019, 9, 9, 15, 39, 4, tzinfo=datetime.timezone.utc)], 'creation_date': [datetime.datetime(1997, 9, 15, 4, 0), datetime.datetime(1997, 9, 15, 7, 0, tzinfo=datetime.timezone.utc)], 'expiration_date': [datetime.datetime(2028, 9, 14, 4, 0), datetime.datetime(2028, 9, 13, 7, 0, tzinfo=datetime.timezone.utc)], 'name_servers': ['NS1.GOOGLE.COM', 'NS2.GOOGLE.COM', 'NS3.GOOGLE.COM', 'NS4.GOOGLE.COM', 'ns3.google.com', 'ns1.google.com', 'ns4.google.com', 'ns2.google.com'], 'status': ['clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited', 'clientTransferProhibited https://icann.org/epp#clientTransferProhibited', 'clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited', 'serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited', 'serverTransferProhibited https://icann.org/epp#serverTransferProhibited', 'serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited', 'clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)', 'clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)', 'clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)', 'serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)', 'serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)', 'serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)'], 'emails': ['abusecomplaints@markmonitor.com', 'whoisrequest@markmonitor.com'], 'dnssec': 'unsigned', 'name': None, 'org': 'Google LLC', 'address': None, 'city': None, 'state': 'CA', 'registrant_postal_code': None, 'country': 'US'}
        """
        
        domain_name = howis.domain_name
        registrar = howis.registrar
        whois_server = howis.whois_server
        referral_url = howis.referral_url
        updated_date = howis.updated_date
        creation_date = howis.creation_date
        expiration_date = howis.expiration_date
        name_servers = howis.name_servers
        status = howis.status
        emails = howis.emails
        dnssec = howis.dnssec
        name = howis.name
        org = howis.org
        address = howis.address
        city = howis.city
        state = howis.state
        registrant_postal_code = howis.registrant_postal_code
        country = howis.countr
        
        context = {
            'howis': howis,
            'domain': domain,
            'domain_name': domain_name,
            'registrar': registrar,
            'whois_server': whois_server,
            'referral_url': referral_url,
            'updated_date': updated_date,
            'creation_date': creation_date,
            'expiration_date': expiration_date,
            'name_servers': name_servers,
            'status': status,
            'emails': emails,
            'dnssec': dnssec,
            'name': name,
            'org': org,
            'address': address,
            'city': city,
            'state': state,
            'registrant_postal_code': registrant_postal_code,
            'country': country,
        }
    except:
        context = {
            'domain': domain,
        }

    if domain_name == None:
        getout(colored(' => ', 'cyan'), colored('domain:', 'green'), domain)
        getout(
            colored(' => ', 'cyan', attrs=['blink']), colored('status:', 'green'), colored('unauthorized', 'red', attrs=['blink']))
    else:
        for k, v in context.items():
            # if the value of the result is None the color should be red
            if v == None:
                r = k + ':'
                getout(colored(
                    ' => ', 'cyan'), colored(r, 'green'), colored(v, 'red', attrs=['blink']))
            else:
                # if the key is status, it will print different and do for loof over the result list
                if k == 'status':
                    getout('\n', colored('=> ', 'cyan'), colored('status', 'yellow'), ':')
                    for s in v:
                        getout('\t\t', colored(' --- ', 'green'), colored(s, 'yellow'))
                    getout()
                # else if the key is howis, it will look different
                elif k == 'howis':
                    r = k + ':'
                    getout(colored(
                        ' => ', 'cyan'), colored(r, 'blue'), colored(v, 'blue', attrs=['blink']))
                else:
                    r = k + ':'
                    getout(colored(' => ', 'cyan'), colored(r, 'green'), v)
    return args
