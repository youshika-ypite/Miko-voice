import time
import speech_recognition as sr

from threading import Thread

from configure__main import Configuration

from assistante_soundModule import Sound
from assistante_commandDispatcher import commandDispatcher

def listenTimer(stopFunc, getoldtime):
    while getoldtime() is not None:
        print(getoldtime())
        if time.time() - getoldtime() > 15:
            stopFunc()
        break

class Assistant:

    def __init__(self) -> None:

        self.listen = False
        self.blocker = False

        self.command = None
        self.response = "Скажи 'Готово!'"

        self.duration = 2

        self.oldtime = None
        self.timer = False

        self._import()
        self._init()
        
        self.speechR = sr.Recognizer()
        self.audioData = None

    def _import(self) -> None:
        if Configuration._CONFIG()['settings']['voiceActive']:
            print("Voice module init..")
            try:
                if not Configuration._import():
                    from assistante_voiceModule import Voice
                    from assistante_llama3_1 import Llama
                    self.voiceModule = Voice()
                    self.llamaModule = Llama()
                    Configuration.loadimport()
                else:
                    self.voiceModule.voice.load()
                print("Voice module init successfully.")
            except Exception as exc: print(exc)
    
    def _init(self) -> None:
        self.cdispatcher = commandDispatcher()
        self.soundModule = Sound()
        
    def __start__(self) -> None:
        print("--- Miko! Start! ---")
        print("Start loop -", time.strftime('%X'))
        print("@youshika--ecosys. ")

    def __close__(self) -> None:
        errorCounter, errors = 0, []
        if Configuration._CONFIG()['settings']['voiceActive']:
            print("Saving llama chat history..")
            try:
                self.llamaModule._SAVE()
                print("Llama chat history saved success")
            except Exception as exc:
                errorCounter += 1
                errors.append(exc)

        print("Save assistant configuration")
        try:
            Configuration.save()
            print("Assistant configuration saved success")
        except Exception as exc:
            errorCounter += 1
            errors.append(exc)
        
        print("--- Miko! Close! ---")
        print("Stop. loop -", time.strftime('%X'))
        if errorCounter == 0: print("Program was closed without errors")
        else: print(f"Program was closed with {errorCounter} errors\n", errors)
        print("@youshika--ecosys. ")

    def __play_trigger__(self, type: int) -> None: # subsequent
        """
        Start listen -> 1\n
        Stop listen  -> 0\n
        Notify       -> -1
        """
        {
             1 :self.soundModule._start_listen,
             0 :self.soundModule._stop_listen,
            -1 :self.soundModule._notify
        }.get(type, lambda : None)()

    def _llama_get_(self, prompt) -> str | None: # subsequent
        return self.llamaModule.getResponse(
            prompt
            ).replace("*", "")
    
    def _voice_speak(self, response) -> None: # subsequent
        self.voiceModule.generate(response)
        print("Speaking..")
        self.voiceModule.speak()

    def _start_listen(self) -> None: # subsequent
        self.__play_trigger__(1)
        self.duration += 2
        self.listen = True
        self.oldtime = time.time()

    def _stop_listen(self) -> None: # subsequent
        self.__play_trigger__(0)
        self.duration -= 2
        self.listen = False
        self.oldtime = None

    def __checkCommand(self, data) -> str | None:
        
        input_RESULT = self.cdispatcher.checkInput(data)    
        response = self.response

        if input_RESULT in [1, 2]:
            if input_RESULT == 2:
                response = self.cdispatcher.response
            self.command = True
        else:
            command_RESULT = self.cdispatcher.checkCommandAvailable(data)
            if command_RESULT: self.command = False
            else: print("None commands")

        return response

    def __recognizer(self, data=None) -> None: # check target-word
        if data is None: return
        self.data = data

        target = Configuration._TRIGGERS().intersection(self.data.split())
        if not target: return

        self._start_listen()

    def _recognize(self, data: str) -> None: # recognize command

        response = self.__checkCommand(data)
        if Configuration._CONFIG()['settings']['voiceActive']:
            if 'LLM ' in response:
                response = self._llama_get_(response.replace("LLM ", ""))
            else:
                if self.command is None:
                    response = self._llama_get_(data)
            self.command = None
            
            self._voice_speak(response)

        self._stop_listen()

    def _listen(self, audio):
        try:
            result = self.speechR.recognize_google(
                audio,
                language='ru_RU'
                ).lower()
            print(result)
            if not self.listen:
                self.__recognizer(result)
            else:
                if any(x in result for x in Configuration._STOPTRIGGERS()):
                    self._stop_listen()
                else: self._recognize(result)
        except Exception as exc:
            print(__name__, f"recognize ERROR\n{exc}")

    def getOldTime(self) -> any:
        return self.oldtime

    def _listener(self):
        self.__start__()
        timerThread = Thread(target=listenTimer, args=(self._stop_listen, self.getOldTime), daemon=False)
        while Configuration._CONFIG()['settings']['ATactive']:
            if not self.blocker and not Configuration._PAUSE():
                if Configuration._CONFIG()['settings']['loader']:
                    self._import()
                    Configuration.loaderOFF()
                try:
                    if self.timer is False and self.oldtime is not None:
                        timerThread.start()
                        self.timer = True
                except Exception as exc: print(__name__, f"timer ERROR\n{exc}")
                with sr.Microphone() as source:
                    audio = self.speechR.adjust_for_ambient_noise(source)
                    audio = self.speechR.listen(source)
                self._listen(audio)
        
        self.__close__()