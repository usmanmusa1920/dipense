from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import whois
from .default import default



class WH:
  
  @staticmethod
  # @login_required
  def site(request):
    domain = request.GET.get('domain')
    
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
      country = howis.country
      
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
        'default': default(),
      }
      
    except:
      context = {
        'domain': domain,
        'default': default(),
      }
    return render(request, 'pages/whois.html', context)