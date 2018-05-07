import os.path
from django import template
from django.conf import settings
register = template.Library()
import re

@register.filter(name='youtube_embed_url')
def youtube_embed_url(value):
    # Starting a Div Bootstrap 4 responsive.
    div_responsive_start = '<div class="embed-responsive embed-responsive-16by9">'
    div_responsive_end = '</div>'
    iframe1 = '<iframe class="embed-responsive-item rounded-top" src="'
    iframe2 = '" allowfullscreen="allowfullscreen" mozallowfullscreen="mozallowfullscreen" msallowfullscreen="msallowfullscreen" oallowfullscreen="oallowfullscreen" webkitallowfullscreen="webkitallowfullscreen"></iframe>'
    nosupp = '<div class="jumbotron bg-black-t">'
    orted = '</div>'
    match = re.search(r'^(?:https?:\/\/)?(?:www\.|m\.)?youtu\.?be(?:\.com)?\/?.*(?:watch|embed)?(?:.*v=|v\/|\/)([\w\-_]+)?(\?t=\d+s)?(&feature=related)?$', value)
    match2 = re.search(r'^(http|https)?:\/\/(www\.)?vimeo.com\/(?:channels\/(?:\w+\/)?|groups\/([^\/]*)\/videos\/|)(\d+)(?:|\/\?)$', value)
    match3 = re.search(r'^(^http(s)?://)?((www|en-es|en-gb|secure|beta|ro|www-origin|en-ca|fr-ca|lt|zh-tw|he|id|ca|mk|lv|ma|tl|hi|ar|bg|vi|th)\.)?twitch.tv/(?!directory|p|user/legal|admin|login|signup|jobs)(?P<channel>\w+)$', value)
    match4 = re.search(r'^(http|https)?:\/\/(www|clips)?.twitch.tv\/(\w+)$', value)
    match5 = re.search(r'^(http|https):\/\/(media|giphy).(com|giphy.com)\/(media|gifs)\/([a-zA-Z0-9_.-]*)\/([a-zA-Z0-9_.-]*)$', value)
    if match:
        embed_url = 'https://www.youtube.com/embed/%s?rel=0' %(match.group(1))
        res = div_responsive_start + iframe1 + embed_url + iframe2 + div_responsive_end
        return res
    elif match2:
        embed_url = 'https://player.vimeo.com/video/%s' %(match2.group(4))
        res = div_responsive_start + iframe1 + embed_url + iframe2 + div_responsive_end
        return res
    elif match3:
        embed_url = 'https://player.twitch.tv/?channel=%s&autoplay=false' %(match3.group('channel'))
        res = div_responsive_start + iframe1 + embed_url + iframe2 + div_responsive_end
        return res
    elif match4:
        embed_url = 'https://clips.twitch.tv/embed?clip=%s&autoplay=false' %(match4.group(3))
        res = div_responsive_start + iframe1 + embed_url + iframe2 + div_responsive_end
        return res
    elif match5:        
        embed_url = 'https://media.giphy.com/media/%s/giphy.mp4' %(match5.group(5))
        res = div_responsive_start + '<video class="embed-responsive-item rounded-top" autoplay loop><source src="' + embed_url + '" type="video/mp4"></video>' + div_responsive_end
        return res
    else:
        embed_url = '<h2 class="lead text-center">Link format not supported.</h2> <p class="text-center text-info">The developers have been notified of this error.</p>'
        res = nosupp + embed_url + orted
        return res
    return ''

youtube_embed_url.is_safe = True