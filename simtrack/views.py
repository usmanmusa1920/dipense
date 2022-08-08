from datetime import datetime
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from django.shortcuts import render
from account.models import SiteToGet, Message
from . models import NumPayloadRec


def home(request):
  the_year = datetime.today().year
  msg = Message.objects.filter(is_read=False)
  context = {
    'msg': msg,
    'the_year': the_year
  }
  return render(request, 'home.html', context)


def simtrack(request):
  the_year = datetime.today().year
  p_num = request.GET.get('num')
  msg = Message.objects.filter(is_read=False)
  sites_list = SiteToGet.objects.all()
  # sites_list = [
  #   'site:facebook.com',
  #   'site:twitter.com',
  #   'site:instagram.com',
  #   'site:youtube.com',
  #   'site:linkedin.com',
  #   'site:github.com',
  # ]
  try:
    num_parse = phonenumbers.parse(p_num, None)
    num_valid = phonenumbers.is_valid_number(num_parse)
    p_nation = phonenumbers.format_number(num_parse, phonenumbers.PhoneNumberFormat.NATIONAL)
    inter_nation = phonenumbers.format_number(num_parse, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    p_e164 = phonenumbers.format_number(num_parse, phonenumbers.PhoneNumberFormat.E164)
    p_geo = geocoder.description_for_number(num_parse, 'en')
    p_carr = carrier.name_for_number(num_parse, 'en')
    time_zone_1 = timezone.time_zones_for_number(num_parse)
    time_zone_2 = timezone.time_zones_for_geographical_number(num_parse)
    
    history = NumPayloadRec(payload_num=p_num)
    history.save()
    
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
      'the_year': the_year,
      'msg': msg,
      'sites_list': sites_list,
    }
  except:
    context = {
      'msg': msg,
      'the_year': the_year
    }
  return render(request, 'simtrack.html', context)


def about(request):
  the_year = datetime.today().year
  msg = Message.objects.filter(is_read=False)
  context = {
    'msg': msg,
    'the_year': the_year
  }
  return render(request, 'about.html', context)


def contactUs(request):
  the_year = datetime.today().year
  msg = Message.objects.filter(is_read=False)
  payloads = NumPayloadRec.objects.all()
  context = {
    'msg': msg,
    'payloads': payloads,
    'the_year': the_year
  }
  return render(request, 'contact.html', context)
