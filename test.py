from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction
from rouge import Rouge

DATA_OUT_PATH = './data_out/'

# Req. 1-5-1. bleu score 계산 함수
def bleu_compute(ture, val):
    smooth = SmoothingFunction().method2
    score = sentence_bleu(
            [ture.split()],
            val.split(),
            weights=(0.25, 0.25, 0.25, 0.25),
            smoothing_function=smooth)

    return score

# Req. 1-5-2. rouge score 계산 함수
def rouge_compute(answer, pred):
   rouge = Rouge()
   scores = rouge.get_scores(answer, pred)
   score1 = scores[0]['rouge-1']
   return score1['r'], score1['p'], score1['f']


print(bleu_compute("그 사람도 그럴 거예요", "이 사람도 그럴 거예요"))
print(rouge_compute("그 사람도 그럴 거예요", "그 사람도 그럴 거예요"))