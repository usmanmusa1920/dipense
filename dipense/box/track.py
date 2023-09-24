import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from simtrack.models import NumPayloadRec
from .default import Default, default


class STRACK:
    @staticmethod
    # @login_required
    def simtrack(request):
        p_num = request.GET.get('num')
        amp="&amp;"
        
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
            
            # saving the payloaded phone into database
            history = NumPayloadRec(payload_num=p_num)
            history.save()
            
            context = {
                'amp': amp,
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
                'default': default(),
            }
        except:
            context = {
                'default': default(),
                'p_num': p_num,
            }
        return render(request, 'pages/simtrack.html', context)
