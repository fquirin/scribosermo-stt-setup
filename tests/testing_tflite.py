import json
import multiprocessing as mp
import random
import time

import numpy as np
import soundfile as sf
import tflite_runtime.interpreter as tflite

# If you want to improve the transcriptions with an additional language model, without using the
# training container, you can find a prebuilt pip-package in the published assets here:
# https://github.com/mozilla/DeepSpeech/releases/tag/v0.9.3
# or for use on a Raspberry Pi you can use the one from extras/misc directory
from ds_ctcdecoder import Alphabet, Scorer, ctc_beam_search_decoder

# ==================================================================================================

#checkpoint_file = "model/model_quantized.tflite"
checkpoint_file = "model/model_full.tflite"
alphabet_path = "data/de/alphabet.json"
ds_alphabet_path = "data/de/alphabet.txt"
ds_scorer_path = "model/kenlm_de_all.scorer"

test_wav_path = "data/test_de.wav"

beam_size = 256
labels_path = "data/labels.json"

with open(alphabet_path, "r", encoding="utf-8") as file:
    alphabet = json.load(file)

with open(labels_path, "r", encoding="utf-8") as file:
    labels = json.load(file)

ds_alphabet = Alphabet(ds_alphabet_path)
ds_scorer = Scorer(
    alpha=0.931289039105002,
    beta=1.1834137581510284,
    scorer_path=ds_scorer_path,
    alphabet=ds_alphabet,
)

# ==================================================================================================


def load_audio(wav_path):
    """Load wav file with the required format"""

    audio, _ = sf.read(wav_path, dtype="int16")
    audio = audio / np.iinfo(np.int16).max
    audio = np.expand_dims(audio, axis=0)
    audio = audio.astype(np.float32)
    return audio


# ==================================================================================================


def predict(interpreter, audio):
    """Feed an audio signal with shape [1, len_signal] into the network and get the predictions"""

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Enable dynamic shape inputs
    interpreter.resize_tensor_input(input_details[0]["index"], audio.shape)
    interpreter.allocate_tensors()

    # Feed audio
    interpreter.set_tensor(input_details[0]["index"], audio)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]["index"])
    return output_data


# ==================================================================================================


def print_prediction_scorer(prediction, print_text=True):
    """Decode the network's prediction with an additional language model"""
    global beam_size, ds_alphabet, ds_scorer

    ldecoded = ctc_beam_search_decoder(
        prediction.tolist(),
        alphabet=ds_alphabet,
        beam_size=beam_size,
        cutoff_prob=1.0,
        cutoff_top_n=512,
        scorer=ds_scorer,
        hot_words=dict(),
        num_results=1,
    )
    lm_text = ldecoded[0][1]

    if print_text:
        print("Prediction scorer: {}".format(lm_text))


# ==================================================================================================


def timed_transcription(interpreter, wav_path):
    """Transcribe an audio file and measure times for intermediate steps"""

    time_start = time.time()

    audio = load_audio(wav_path)
    time_audio = time.time()

    prediction = predict(interpreter, audio)
    time_model = time.time()

    print_prediction_scorer(prediction[0])
    time_scorer = time.time()

    dur_audio = time_audio - time_start
    dur_model = time_model - time_audio
    dur_scorer = time_scorer - time_model

    len_audio = float(sf.info(wav_path).duration)
    msg = "\nLength of audio was {:.3f}s, loading it took {:.3f}s."
    print(msg.format(len_audio, dur_audio))

    msg = "Calculating the predictions did take {:.3f}s "
    msg += "and decoding with a scorer {:.3f}s."
    print(msg.format(dur_model, dur_scorer))

    rtf_scorer = (dur_model + dur_scorer) / len_audio
    msg = "The Real-Time-Factor for scorer decoding is {:.3f}."
    print(msg.format(rtf_scorer))


# ==================================================================================================


def main():

    print("\nLoading model ...")
    interpreter = tflite.Interpreter(
        model_path=checkpoint_file, num_threads=mp.cpu_count()
    )
    print("Input details:", interpreter.get_input_details())

    print("\nRunning some initialization steps ...")
    # Run some random predictions to initialize the model
    for _ in range(5):
        st = time.time()
        length = random.randint(1234, 123456)
        data = np.random.uniform(-1, 1, [1, length]).astype(np.float32)
        _ = predict(interpreter, data)
        print("TM:", time.time() - st)

    # Run random decoding steps to initialize the scorer
    for _ in range(15):
        st = time.time()
        length = random.randint(123, 657)
        data = np.random.uniform(0, 1, [length, len(alphabet) + 1])
        print_prediction_scorer(data, print_text=False)
        print("TD:", time.time() - st)

    print("\nTranscribing the audio ...")

    # Print label if one of the test wavs is used
    if test_wav_path.startswith("/Scribosermo/extras/exporting/data/test_"):
        lang = test_wav_path[-6:-4]
        if lang in labels:
            print("Label:            ", labels[lang])

    # Now run the transcription
    timed_transcription(interpreter, test_wav_path)


# ==================================================================================================

if __name__ == "__main__":
    main()
    print("\nFINISHED")
