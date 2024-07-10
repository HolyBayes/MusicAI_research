# Установка

**Python 3.11**

```
conda install cuda transformers==4.37.1 pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 pytorch-cuda=12.1 -c pytorch -c nvidia -y
pip install flash-attn --no-build-isolation
pip install deepfilternet
```

Мог что-то пропустить

# Структура репозитория

[Research.ipynb](Research.ipynb) - ноутбук, где исследовал различные архитектуры и подходы
[scripts/](scripts/) - папка со скриптами. Сейчас там только скрипт по инференсу MusicGen Large и утилиты
[samples/](samples/) - папка с примерами различных песен от разных исследованных архитектур

# Инструкция по запуску кода

```
cd scripts/
python musicgen_large.py "An uplifting jazz song that makes your head shake" --output output.wav --durability_seconds 10
```

# Архитектуры

#TODO

# Примеры аудио
## MusicGen Large

* [80s pop track with bassy drums and synth](samples/MusicGen_Large/80s_pop_track_with_bassy_drums_and_synth.wav)
* [90s rock song with loud guitars and heavy drums](samples/MusicGen_Large/90s_rock_song_with_loud_guitars_and_heavy_drums.wav)
* [Techno music with a strong, upbeat tempo and high melodic riffs](samples/MusicGen_Large/Techno_music_with_a_strong,_upbeat_tempo_and_high_melodic_riffs.wav) 
* [Lo-fi funk](samples/MusicGen_Large/Lo-fi_funk.wav)
* [Country instrumental](samples/MusicGen_Large/Country_instrumental.wav)
* [An uplifting jazz song that makes your head shake](samples/MusicGen_Large/An_uplifting_jazz_song_that_makes_your_head_shake.wav)



## AudioLDM2 Music

* [80s pop track with bassy drums and synth](samples/AudioLDM2_Music/80s_pop_track_with_bassy_drums_and_synth.wav)
* [90s rock song with loud guitars and heavy drums](samples/AudioLDM2_Music/90s_rock_song_with_loud_guitars_and_heavy_drums.wav)
* [Techno music with a strong, upbeat tempo and high melodic riffs](samples/AudioLDM2_Music/Techno_music_with_a_strong,_upbeat_tempo_and_high_melodic_riffs.wav) 
* [Lo-fi funk](samples/AudioLDM2_Music/Lo-fi_funk.wav)
* [Country instrumental](samples/AudioLDM2_Music/Country_instrumental.wav)
* [An uplifting jazz song that makes your head shake](samples/AudioLDM2_Music/An_uplifting_jazz_song_that_makes_your_head_shake.wav)


## Stable Audio

* [80s pop track with bassy drums and synth](samples/Stable_Audio/80s_pop_track_with_bassy_drums_and_synth.wav)
* [90s rock song with loud guitars and heavy drums](samples/Stable_Audio/90s_rock_song_with_loud_guitars_and_heavy_drums.wav)
* [Techno music with a strong, upbeat tempo and high melodic riffs](samples/Stable_Audio/Techno_music_with_a_strong,_upbeat_tempo_and_high_melodic_riffs.wav) 
* [Lo-fi funk](samples/Stable_Audio/Lo-fi_funk.wav)
* [Country instrumental](samples/Stable_Audio/Country_instrumental.wav)
* [An uplifting jazz song that makes your head shake](samples/Stable_Audio/An_uplifting_jazz_song_that_makes_your_head_shake.wav)


# Резюме

#TODO

# План дальнейших улучшений

#TODO
