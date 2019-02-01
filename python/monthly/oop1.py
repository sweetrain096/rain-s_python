'''
문제. 이름이 Dictfind인 클래스를 생성하시오.
------------------------------------------------------------
		  이름	 |	usage
------------------------------------------------------------
메소드 : getfemale | dict를 받아, 그 중에서female인 사람을 반환하시오
------------------------------------------------------------
'''
'''
프린트 하시오.
p1 = Dictfind()
p1.getfemale({'female':'지원', 'male':'창오', 'female':'민지', 'none':'하리보'})
'''




class Dictfind:

    def __init__(self):
        self.dict_hi = dict()

    def getfemale(self, *args):
        self.dict_hi = args

        self.dict_hi = self.dict_hi[0]



        for key, val in self.dict_hi.items():
            if key == 'female':
                print({key: val})


p1 = Dictfind()
p1.getfemale({'female':'지원', 'male':'창오', 'female':'민지', 'none':'하리보'})



'''
문제. 이름이 Dictfind2 인 클래스를 생성하시오.
--------------------------------------------------------
		  이름	 |	usage
--------------------------------------------------------
클래스 : Dictfind2 |
메소드 : 	init	| dict를 받기
메소드 : getfemale | 받은 dict에서 female인 사람을 반환하시오
--------------------------------------------------------
'''
'''
프린트 하시오.
p1 = Dictfind2(female='지원',male='민지',none='창오')
p1.getfemale()
'''


class Dictfind2:

    def __init__(self, **kwargs):
        self.my_dict = kwargs



    def getfemale(self):
        for key, val in self.my_dict.items():
            if key == 'female':
                print({key: val})


p2 = Dictfind2(female='지원',male='민지',none='창오')
p2.getfemale()