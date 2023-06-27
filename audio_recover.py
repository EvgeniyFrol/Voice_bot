import os
import soundfile as sf
import speech_recognition


def recognize_speach(file):
    new_file = file.replace('.oga', '.wav')
    data, samplerate = sf.read(file)
    sf.write(new_file, data, samplerate)

    recognizer = speech_recognition.Recognizer()

    with speech_recognition.WavFile(new_file) as source:
        wav_audio = recognizer.record(source)

    text = recognizer.recognize_google(wav_audio, language='ru')

    if os.path.exists(file):
        os.remove(file)

    if os.path.exists(new_file):
        os.remove(new_file)

    return text

def download_file(bot, file_id):
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    filename = file_id + file_info.file_path
    filename = filename.replace('/', '_')

    with open(filename, 'wb') as f:
        f.write(downloaded_file)

    return filename

