import os.path
from django import template
from django.conf import settings
register = template.Library()
import re

@register.filter(name='youtube_embed_url')
def youtube_embed_url(value):
    iframe1 = '<iframe class="embed-responsive-item" src="'
    iframe2 = '" allowfullscreen="allowfullscreen" mozallowfullscreen="mozallowfullscreen" msallowfullscreen="msallowfullscreen" oallowfullscreen="oallowfullscreen" webkitallowfullscreen="webkitallowfullscreen"></iframe>'
    match = re.search(r'^(?:https?:\/\/)?(?:www\.|m\.)?youtu\.?be(?:\.com)?\/?.*(?:watch|embed)?(?:.*v=|v\/|\/)([\w\-_]+)?(\?t=\d+s)?(&feature=related)?$', value)
    match2 = re.search(r'^(http|https)?:\/\/(www\.)?vimeo.com\/(?:channels\/(?:\w+\/)?|groups\/([^\/]*)\/videos\/|)(\d+)(?:|\/\?)$', value)
    match3 = re.search(r'^(^http(s)?://)?((www|en-es|en-gb|secure|beta|ro|www-origin|en-ca|fr-ca|lt|zh-tw|he|id|ca|mk|lv|ma|tl|hi|ar|bg|vi|th)\.)?twitch.tv/(?!directory|p|user/legal|admin|login|signup|jobs)(?P<channel>\w+)$', value)
    match4 = re.search(r'^(http|https)?:\/\/(www|clips)?.twitch.tv\/(\w+)$', value)
    match5 = re.search(r'^(http|https):\/\/(i\.|media\.|www\.)?(giphy.com)\/(media|gifs)\/([a-zA-Z0-9_.-]*)$', value)
    if match:
        embed_url = 'https://www.youtube.com/embed/%s?rel=0' %(match.group(1))
        res = iframe1 + embed_url + iframe2
        return res
    elif match2:
        embed_url = 'https://player.vimeo.com/video/%s' %(match2.group(4))
        res = iframe1 + embed_url + iframe2
        return res
    elif match3:
        embed_url = 'https://player.twitch.tv/?channel=%s&autoplay=false' %(match3.group('channel'))
        res = iframe1 + embed_url + iframe2
        return res
    elif match4:
        embed_url = 'https://clips.twitch.tv/embed?clip=%s&autoplay=false' %(match4.group(3))
        res = iframe1 + embed_url + iframe2
        return res
    elif match5:
        embed_url = 'https://giphy.com/embed/%s' %(match5.group(5))
        res = iframe1 + embed_url + iframe2
        return res
    else:
        embed_url = '<div class="jumbotron"><h1>Whoops!</h1><p>We found an error with the link that you sent us, the developers were notified. We will solve it soon.</p></div>'
        res = embed_url
        return res
    return ''

youtube_embed_url.is_safe = True