from TTS.api import TTS

model_name = TTS.list_models() [0]

tts = TTS(model_name)


wav = tts.tts("Testing this text to speech model", speaker=tts.speakers[0], language=tts.languages[0])


