from django.shortcuts import HttpResponse
from django.http import JsonResponse
import yt_dlp

def get_m3u8_url(request):  
    
    url = 'https://www.youtube.com/@neda_radio/live'  
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])
            for format in formats:
                    return JsonResponse({"title" : info_dict["title"], "url" : format['manifest_url'] }, json_dumps_params={'indent': 4, "ensure_ascii" : False})      #['url']
            return JsonResponse({"title" : info_dict["title"], "url" : None }, json_dumps_params={'indent': 4, "ensure_ascii" : False} )     
        
        except Exception as e:
            print("An error occurred during the download:")
            return HttpResponse("")