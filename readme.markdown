Info
====

This application is a simple middleware and associated decorator that will add a ".mobile" attribute to your request objects, which, if True, means the requester is coming to you from a mobile phone (cellphone), PDA, or other device that should be considered small screened, or have an underpowered browser, such as games consoles.

This mostly works using a list of search strings, though there are a couple of other tricks, like detecting the presence of Opera Mini. The strings are in an easily-parseable text file, and thus can be used for other similar projects.

It also includes a pretty extensive list of user agents to test against.

Installation
============

Using microdetector is very simple. Simply place the microdetector package into your project's path, and then add:

	minidetector.Middleware

to your `MIDDLEWARE_CLASSES` tuple in your settings.py

Then in your view you can check `request.mobile` - if it's `True` then treat it like a small screen device. If it's `False` then it's probably a desktop browser, or a spider or something else.

If you only have certain views that need the distinction, you can choose not to search every request you receive. All you need to do is wrap the relevant views like this:

	from minidetectordetector import detect_mobile

	@detect_mobile
	def my_mobile_view(request):
		if request.mobile:
			#do something with mobile

"Special" Devices
=================

minidetector also adds some extra info for popular devices to the request object.

Extra Info
----------

for the iPad:

	request.browser_is_ipad = True
	request.mobile_device = 'ipad'

for the iPhone or iPod touch:

	request.browser_is_iphone = True
	request.mobile_device = 'iphone'

and for Android:

	request.browser_is_android = True
	request.mobile_device = 'android'

Override mobile treatment
-------------------------

By default the iPad is not treated as a mobile browser. If you want to reverse this, add the following to your settings.py:

	IPAD_IS_MOBILE = True

You can do the reverse for iphone and android (i.e. having them treat your site as non-mobile.)

	IPHONE_IS_MOBILE = False
	ANDROID_IS_MOBILE = False