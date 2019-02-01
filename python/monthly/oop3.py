'''
문제. 이름이 Listfind2 인 클래스를 생성하시오.
--------------------------------------------------------
		  이름	 |	usage
--------------------------------------------------------
클래스 : Listfind  |
메소드 : 	init	| list를 받기
메소드 : getfemale | 받은 dict에서 female인 사람을 반환하시오
--------------------------------------------------------
'''
'''
프린트 하시오.
p1 = Listfind2('female', 'male', 'none')
p1.getfemale()
'''



class Listfind2:
    def __init__(self, *args):
        self.find_list = []
        for arg in args:
            self.find_list.append(arg)
