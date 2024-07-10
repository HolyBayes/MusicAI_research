import librosa
import numpy as np
from df.enhance import enhance, init_df, load_audio
# Load default model
df_model, df_state, _ = init_df()


def spectral_substraction(wav, alpha=1.5):
    # alpha - Sealing factor for noise substraction
    audio = librosa.util.normalize(wav)
    noisy_spectrum = np.abs(librosa.stft(audio))
    noise_spectrum = np.expand_dims(np.mean(noisy_spectrum, axis=1), -1)
    clean_spectrum = np.maximum(noisy_spectrum - alpha*noise_spectrum, 0)
    enhanced_audio = librosa.istft(clean_spectrum)
    return enhanced_audio

def wiener_filtering(wav):
    raise NotImplemented
    audio = librosa.util.normalize(wav)
    noise_stft = np.abs(librosa.stft(audio))

    clean_stft = np.abs(librosa.stft(clean_audio))

    wiener_filter = clean_stft**2 / (clean_stft**2 + noise_stft**2)

    enhanced_stft = wiener_filter*noise_stft

    enhanced_audio = librosa.istft(enhanced_stft)

    return enhanced_audio

def deepfilternet(wav):
    # Denoise the audio
    audio = librosa.util.normalize(wav)
    enhanced_audio = enhance(df_model, df_state, audio)
    return enhanced_audio
