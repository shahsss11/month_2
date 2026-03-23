class Streamer:    
    def live(self):       
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"
    
    def earn(self):       
        return "Заработал 500 донатов за 2 часа"


class TikToker:    
    def live(self):        
        return "Снимаю трендовый тикток под песню месяца!"
    
    def viral(self):        
        return "Набрал 3 миллиона просмотров за сутки!"


class Mutant:    
    def live(self):        
        return "Я... я свечусь в темноте... это мой вайб..."
    
    def superpower(self):       
        return "Летаю и стреляю лазерами из глаз"


class GlowStreamer(Streamer, Mutant):
    def ultimate_content(self):
        return f"{self.live()} + {self.superpower()}"


class ViralCyborg(TikToker, Mutant):
    def ultimate_content(self):
        return f"{self.live()} + {self.superpower()} + {self.viral()}"


class DonateMage(Streamer, TikToker):
    def ultimate_content(self):
        return f"{self.live()} + {self.earn()} + {self.viral()}"


g = GlowStreamer()
v = ViralCyborg()
d = DonateMage()

print(GlowStreamer.mro())
print(ViralCyborg.mro())
print(DonateMage.mro())

print(g.live())
print(v.live())
print(d.live())

print(g.ultimate_content())
print(v.ultimate_content())
print(d.ultimate_content())