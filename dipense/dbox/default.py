# -*- coding: utf-8 -*-
from datetime import datetime
from django.contrib import messages


class Default:
	@staticmethod
	def default():
		"""It is mainly created so that it can be use (access) in any page,
		for example the year that will show in the footer
		it is not only for one page it is for all pages in the site
		
		so by using this class method we can access it in any page
		instead of creating `the_year` variable in each view
		
		like so the category list in the menu bar also it is not for one page
		and possibly for other variables ==> [the_year, category, comment, reply, search, message]
		
		Also for the notification of new recent comment, reply, search, or message
		that will show on the menu bar button (in the header)
		"""
		
		the_year = datetime.utcnow().year
		data = {
			'the_year': the_year,
		}
		return data
		
	# def flash_msg(request):
	# 	if request.user.is_authenticated:
	# 		pass
	# 	else:
	# 		messages.success(request, f'Login first!')

	sites_list = [
		'site:facebook.com',
		'site:twitter.com',
		'site:instagram.com',
		'site:tiktok.com',
		'site:youtube.com',
		'site:linkedin.com',
		'site:github.com',
	]

		
def default():
	"""This is the function (shortcut of `Default.default') that we will call in some of our site view, instead of calling the `Default.default' which will make our code so large
	"""
	return Default.default
