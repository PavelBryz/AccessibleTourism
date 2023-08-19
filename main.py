import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.say("The Adelaide Botanic Garden is a breathtaking public garden located in the heart of Adelaide, South Australia. Spanning over 51 hectares, it is situated on the north-east corner of the Adelaide Park Lands, just a stone's throw away from the city center. The garden is a peaceful oasis, offering visitors a serene escape from the bustling city.")
engine.runAndWait()