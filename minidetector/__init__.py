from django.conf import settings

from minidetector.useragents import search_strings
from django.utils.deprecation import MiddlewareMixin

class Middleware(object):
    @staticmethod
    def process_request(request):
        """ Adds a "mobile" attribute to the request which is True or False
            depending on whether the request should be considered to come from a
            small-screen device such as a phone or a PDA"""
        
        # defaults (we assume this is a desktop)
        request.is_simple_device = False
        request.is_touch_device = False
        request.is_wide_device = True

        if "HTTP_X_OPERAMINI_FEATURES" in request.META:
            #Then it's running opera mini. 'Nuff said.
            #Reference from:
            # http://dev.opera.com/articles/view/opera-mini-request-headers/
            
            request.is_simple_device = True
            
            return None

        if "HTTP_ACCEPT" in request.META:
            s = request.META["HTTP_ACCEPT"].lower()
            if 'application/vnd.wap.xhtml+xml' in s:
                # Then it's a wap browser
                
                request.is_simple_device = True
                
                return None

        if "HTTP_USER_AGENT" in request.META:
            # This takes the most processing. Surprisingly enough, when I
            # Experimented on my own machine, this was the most efficient
            # algorithm. Certainly more so than regexes.
            # Also, Caching didn't help much, with real-world caches.
            
            s = request.META["HTTP_USER_AGENT"].lower()
            
            if 'applewebkit' in s:
                request.is_webkit = True
            
            if 'ipad' in s:
                request.is_ios_device = True
                request.is_touch_device = True
                request.is_wide_device = True
                
                return None
            
            if 'iphone' in s or 'ipod' in s:
                request.is_ios_device = True
                request.is_touch_device = True
                request.is_wide_device = False
                
                return None
            
            if 'android' in s:
                request.is_android_device = True
                request.is_touch_device = True
                request.is_wide_device = False # TODO add support for andriod tablets
                
                return None
            
            if 'webos' in s:
                request.is_webos_device = True
                request.is_touch_device = True
                request.is_wide_device = False # TODO add support for webOS tablets
                
                return None
            
            if 'windows phone' in s:
                request.is_windows_phone_device = True
                request.is_touch_device = True
                request.is_wide_device = False
                
                return None
            
            for ua in search_strings:
                if ua in s:
                    request.is_simple_device = True
                    return None
        
        return None

def detect_mobile(view):
    """ View Decorator that adds a "mobile" attribute to the request which is
        True or False depending on whether the request should be considered
        to come from a small-screen device such as a phone or a PDA"""
    
    def detected(request, *args, **kwargs):
        Middleware.process_request(request)
        return view(request, *args, **kwargs)
    detected.__doc__ = "%s\n[Wrapped by detect_mobile which detects if the request is from a phone]" % view.__doc__
    return detected

class NewMiddleware(MiddlewareMixin, Middleware):
    pass

__all__ = ['NewMiddleware', 'Middleware', 'detect_mobile']
