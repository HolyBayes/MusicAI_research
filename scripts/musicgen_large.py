from transformers import AutoProcessor, MusicgenForConditionalGeneration
import scipy
from utils import spectral_substraction, wiener_filtering, deepfilternet 
import argparse

parser = argparse.ArgumentParser(description='MusicGen inference script')
parser.add_argument('caption', type=str, help='Song caption')
parser.add_argument('--post_processing', choices=[None, 'ss', 'wiener', 'df'], default=None, help='ss - Spectral Substraction, wiener - Wiener Filtering, df - DeepFilterNet')
parser.add_argument('--output', default='output.wav')
parser.add_argument('--durability_seconds', default=10, type=int)
args = parser.parse_args()


processor = AutoProcessor.from_pretrained("facebook/musicgen-large")
model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-large")



def postprocess(wav, type):
    if type is None: return wav
    return {'ss': spectral_substraction, 'wiener': wiener_filtering, 'df': deepfilternet}[type](wav)

if __name__ == '__main__':
    inputs = processor(
        text=[args.caption],
        padding=True,
        return_tensors="pt",
    )

    max_new_tokens = int(256*args.durability_seconds/5) # 256 corresponds to a 5 seconds output sample
    
    wav = model.generate(**inputs, max_new_tokens=max_new_tokens)[0,0].numpy()
    wav = postprocess(wav, args.post_processing)
    scipy.io.wavfile.write(args.output, rate=model.config.audio_encoder.sampling_rate, data=wav)
