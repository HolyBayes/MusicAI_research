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
## MusicGen Large
Подход представляет из себя модифицированный VQVAE, в котором модифицирован процесс квантизации (вместо одного codebook'a делается residual vector quantization, где каждый остаток квантизируется и из него вычитается ближайший embeding из соответствующего codebook'a. Таким образом, выучивается последовательность codebook'ов, по одному для каждого шага, см. рис. ниже). Модель примечательная тем, что обучается на исходных waveform'ах, а не на mel-спектрограммах. Encoder представляет собой обычный каскад 1D-свёрток
![Residual vector quantization](assets/rvq.webp)

Тем не При квантизации используется три лосса - MSE между mel исходным и реконструированным, ошибка реконструкции исходной waveform'ы после квантизации (стандартный лосс VQVAE), и лосс критика (как в Adversarial autoencoder). См. ниже

![MusicGen](assets/encodec.webp)

На втором этапе обучения обучается декодер трансформера (GPT) на квантизованных аудиопредставлениях. Тут ничего примечательного, всё как с обычными LLM

## Stable Audio



## AudioLDM2 Music



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

* Попробововал 3 современных модели генерёжки музыки - Stable Audio, MusicGen Large (Facebook), AudioLDM2
* Попробовал 3 подхода к денойзингу полученного аудио. Получилось улучшить качество, сделав музыку более приятной слуху и естественной, избавив от шумов
* Написал скрипт инференса
* Расписал, как работают исследованные архитектуры под капотом
* Набросал дальнейший план работ

# План дальнейших улучшений

* Lumina-T2X - инференс не заработал из-за старой видеокарточки. На колабе запустить не успел
* Завести Lumina-Next - это продолжение Lumina-T2X
* 
