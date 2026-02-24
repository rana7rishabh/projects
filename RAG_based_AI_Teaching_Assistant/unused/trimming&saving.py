import subprocess

command = [
    "ffmpeg",
    "-ss", "0",
    "-i", "audios/SEO and Core Web Vitals in HTML ｜ Sigma Web Development Course - Tutorial #6 [CyRlWlaJnTY].mp3",
    "-t", "10",
    "-acodec", "copy",
    "audios/sample.mp3"
]

subprocess.run(command)
