import os
import subprocess
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import VideoUploadForm
from .models import Video

import subprocess

def extract_subtitles(video_path, output_path):
    command = [
        'ffmpeg', '-y',  # Add '-y' to overwrite existing files
        '-i', video_path,
        output_path
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Error extracting subtitles:", result.stderr.decode())
    else:
        print("Subtitles extracted successfully.")


def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()

            video_path = video.file.path
            subtitle_path = os.path.join(settings.MEDIA_ROOT, 'subtitles', f'{video.id}.srt')

            os.makedirs(os.path.dirname(subtitle_path), exist_ok=True)

            try:
                extract_subtitles(video_path, subtitle_path)
            except Exception as e:
                video.subtitles = None
                video.save()
                print(f'Error extracting subtitles: {e}')
                return redirect('upload_video')

            try:
                with open(subtitle_path, 'r', encoding='utf-8') as subtitle_file:
                    video.subtitles = subtitle_file.read()
                    video.save()
            except Exception as e:
                video.subtitles = None
                video.save()
                print(f'Error reading subtitles file: {e}')

            return redirect('video_list')
    else:
        form = VideoUploadForm()

    return render(request, 'upload_video.html', {'form': form})
import re
from django.shortcuts import render
from .models import Video
from .forms import SubtitleSearchForm

def video_list(request):
    videos = Video.objects.all()
    search_results = []
    query = None
    selected_video = None

    if request.method == 'GET':
        form = SubtitleSearchForm(request.GET)
        video_id = request.GET.get('video_id')
        if video_id:
            try:
                selected_video = Video.objects.get(id=video_id)
                if form.is_valid():
                    query = form.cleaned_data['query']
                    search_results = selected_video.search_subtitles(query)
            except Video.DoesNotExist:
                selected_video = None
                search_results = []
    else:
        form = SubtitleSearchForm()

    return render(request, 'video_list.html', {
        'videos': videos,
        'form': form,
        'query': query,
        'search_results': search_results,
        'selected_video': selected_video,
    })

def search_subtitles(self, query):
    if not self.subtitles:
        return []

    results = []
    pattern = re.compile(r"(\d{2}:\d{2}:\d{2},\d{3}) --> .*?\n(.*?)(?=\n\n|\Z)", re.DOTALL | re.IGNORECASE)
    for match in pattern.finditer(self.subtitles):
        timestamp = match.group(1)
        subtitle_text = match.group(2).strip()
        if query.lower() in subtitle_text.lower():
            results.append((timestamp, subtitle_text))
    return results
