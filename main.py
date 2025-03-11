import subprocess
import sys

try:
    from faster_whisper import WhisperModel
except ImportError:
    # Install dependencies
    subprocess.check_call([sys.executable, "-m", "pip", "install", "faster-whisper"])


def transcribe_audio(model_size, audio_path):
    print(model_size, audio_path)
    model = WhisperModel(model_size, device="cpu")
    segments, info = model.transcribe(audio_path, beam_size=5)

    print(
        "Detected language '%s' with probability %f"
        % (info.language, info.language_probability)
    )

    result = ""

    for segment in segments:
        # print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
        result = result + "\n" + segment.text

    # # Afficher la transcription et les résultats
    print(result)

    # Sauvegarder la transcription dans un fichier texte
    txt_filename = "enregistrement.txt"
    with open(txt_filename, "w") as f:
        f.write(result)

    print(f"Transcription terminée et sauvegardée dans {txt_filename}")


# transcribe()

# model_size = "base"

# audio_path = "dataset_audio/Indila_derniere_danse.mp3"
# transcribe_audio(model_size, audio_path)
